import os
from typing import Dict, Any
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.questions_loader import (
    get_subjects_list,
    get_subject_data,
    create_exam_session,
    evaluate_exam,
    EXAM_SESSIONS
)

app = FastAPI(title="Simulador de Exámenes Escolares", version="1.0.0")

BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, exist_ok=True)
if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

css_dir = os.path.join(STATIC_DIR, "css")
if os.path.exists(css_dir):
    app.mount("/css", StaticFiles(directory=css_dir), name="css")

js_dir = os.path.join(STATIC_DIR, "js")
if os.path.exists(js_dir):
    app.mount("/js", StaticFiles(directory=js_dir), name="js")

webfonts_dir = os.path.join(STATIC_DIR, "webfonts")
if os.path.exists(webfonts_dir):
    app.mount("/webfonts", StaticFiles(directory=webfonts_dir), name="webfonts")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home view listing all available subjects and quick start configuration."""
    subjects = get_subjects_list()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"subjects": subjects}
    )

@app.get("/exam/{subject_id}", response_class=HTMLResponse)
async def start_exam(request: Request, subject_id: str, count: int = 15, timer: int = 15):
    """
    Starts an exam session:
    - Generates 15 random questions from the subject pool
    - Shuffles the answer choices
    - Presents the test interface
    """
    try:
        session = create_exam_session(
            subject_id=subject_id,
            question_count=count,
            time_limit_minutes=timer
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return templates.TemplateResponse(
        request=request,
        name="exam.html",
        context={
            "session": session,
            "questions": session["questions"],
            "timer_minutes": timer,
            "total_questions": session["total_questions"]
        }
    )

@app.post("/exam/{exam_id}/submit", response_class=HTMLResponse)
async def submit_exam(
    request: Request,
    exam_id: str,
    time_spent: int = Form(0)
):
    """
    Receives submitted answers from the exam form,
    evaluates them, and renders the results page.
    """
    session = EXAM_SESSIONS.get(exam_id)
    if not session:
        raise HTTPException(status_code=404, detail="Sesión de examen no encontrada o expirada.")

    # Read all form data to capture user answers
    form_data = await request.form()
    user_answers = {}

    for key, value in form_data.items():
        if key.startswith("q_"):
            order_str = key.replace("q_", "")
            user_answers[order_str] = str(value)

    # Evaluate results
    results = evaluate_exam(
        exam_id=exam_id,
        user_answers=user_answers,
        time_spent_seconds=time_spent
    )

    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "results": results,
            "session": session
        }
    )

@app.get("/exam/{exam_id}/results", response_class=HTMLResponse)
async def view_results(request: Request, exam_id: str):
    """View results for an already evaluated exam."""
    session = EXAM_SESSIONS.get(exam_id)
    if not session or not session.get("results"):
        return RedirectResponse(url="/")

    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "results": session["results"],
            "session": session
        }
    )
