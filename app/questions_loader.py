import json
import os
import random
import uuid
from typing import Dict, List, Optional

SUBJECTS_DIR = os.path.join(os.path.dirname(__file__), "subjects")

# In-memory store for active exam sessions (lightweight, zero database needed)
EXAM_SESSIONS: Dict[str, dict] = {}

def get_subjects_list() -> List[dict]:
    """Scans the subjects directory and returns metadata for each available subject."""
    subjects = []
    if not os.path.exists(SUBJECTS_DIR):
        os.makedirs(SUBJECTS_DIR, exist_ok=True)
        return subjects

    for filename in sorted(os.listdir(SUBJECTS_DIR)):
        if filename.endswith(".json"):
            filepath = os.path.join(SUBJECTS_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    subjects.append({
                        "id": data.get("id", os.path.splitext(filename)[0]),
                        "name": data.get("name", "Materia sin nombre"),
                        "grade": data.get("grade", "Grado no especificado"),
                        "institution": data.get("institution", ""),
                        "description": data.get("description", ""),
                        "badge": data.get("badge", ""),
                        "icon": data.get("icon", "fa-book-open"),
                        "color": data.get("color", "emerald"),
                        "total_questions": len(data.get("questions", [])),
                        "default_question_count": min(data.get("default_question_count", 15), len(data.get("questions", []))),
                    })
            except Exception as e:
                print(f"Error loading subject from {filename}: {e}")
    return subjects

def get_subject_data(subject_id: str) -> Optional[dict]:
    """Loads complete subject data from JSON file."""
    filepath = os.path.join(SUBJECTS_DIR, f"{subject_id}.json")
    if not os.path.exists(filepath):
        # Fallback check by scanning id attribute
        for filename in os.listdir(SUBJECTS_DIR):
            if filename.endswith(".json"):
                candidate = os.path.join(SUBJECTS_DIR, filename)
                try:
                    with open(candidate, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if data.get("id") == subject_id:
                            return data
                except Exception:
                    continue
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def create_exam_session(subject_id: str, question_count: int = 15, time_limit_minutes: int = 15) -> dict:
    """
    Creates a new exam session:
    - Randomly picks `question_count` questions from the pool.
    - Shuffles the answer options for EACH question independently.
    - Stores the session in memory.
    """
    subject_data = get_subject_data(subject_id)
    if not subject_data:
        raise ValueError(f"Materia con id '{subject_id}' no encontrada.")

    all_questions = subject_data.get("questions", [])
    if not all_questions:
        raise ValueError(f"La materia '{subject_data.get('name')}' no tiene preguntas registradas.")

    # Select random questions
    count = min(question_count, len(all_questions))
    selected = random.sample(all_questions, count)

    session_id = uuid.uuid4().hex
    exam_questions = []

    for idx, q in enumerate(selected, start=1):
        # Copy and randomize options
        original_options = list(q.get("options", []))
        shuffled_options = random.sample(original_options, len(original_options))

        exam_questions.append({
            "order": idx,
            "id": q.get("id"),
            "category": q.get("category", "General"),
            "question": q.get("question"),
            "context": q.get("context"),
            "options": shuffled_options,
            "correct_answer": q.get("correct_answer"),
            "explanation": q.get("explanation", "")
        })

    session_record = {
        "exam_id": session_id,
        "subject_id": subject_id,
        "subject_name": subject_data.get("name"),
        "grade": subject_data.get("grade"),
        "institution": subject_data.get("institution"),
        "total_questions": len(exam_questions),
        "time_limit_minutes": time_limit_minutes,
        "questions": exam_questions,
        "submitted": False,
        "results": None
    }

    EXAM_SESSIONS[session_id] = session_record
    return session_record

def evaluate_exam(exam_id: str, user_answers: Dict[str, str], time_spent_seconds: int = 0) -> dict:
    """
    Evaluates submitted answers against the stored session questions.
    Returns detailed score and review data.
    """
    session = EXAM_SESSIONS.get(exam_id)
    if not session:
        raise ValueError("Sesión de examen no encontrada o expirada.")

    questions = session["questions"]
    total = len(questions)
    correct_count = 0
    incorrect_count = 0
    unanswered_count = 0

    category_stats: Dict[str, dict] = {}
    review_items = []

    for q in questions:
        q_order = str(q["order"])
        selected_option = user_answers.get(q_order, "").strip()
        correct_option = q["correct_answer"].strip()
        category = q.get("category", "General")

        if category not in category_stats:
            category_stats[category] = {"total": 0, "correct": 0}
        category_stats[category]["total"] += 1

        is_correct = False
        is_unanswered = False

        if not selected_option:
            is_unanswered = True
            unanswered_count += 1
        elif selected_option == correct_option:
            is_correct = True
            correct_count += 1
            category_stats[category]["correct"] += 1
        else:
            incorrect_count += 1

        review_items.append({
            "order": q["order"],
            "id": q["id"],
            "category": category,
            "question": q["question"],
            "context": q["context"],
            "options": q["options"],
            "selected_option": selected_option if not is_unanswered else None,
            "correct_option": correct_option,
            "is_correct": is_correct,
            "is_unanswered": is_unanswered,
            "explanation": q["explanation"]
        })

    percentage = round((correct_count / total * 100), 1) if total > 0 else 0

    # Assessment feedback message
    if percentage >= 90:
        performance_label = "Excelente Desempeño Superior"
        performance_badge = "bg-emerald-500"
        feedback_message = "¡Felicitaciones! Has demostrado un dominio sobresaliente de los conceptos estadísticos, tabulación y redacción formal."
    elif percentage >= 75:
        performance_label = "Buen Desempeño Alto"
        performance_badge = "bg-blue-500"
        feedback_message = "¡Muy bien! Comprendes con solidez la mayoría de los temas estadísticos y comparación de tablas."
    elif percentage >= 60:
        performance_label = "Desempeño Básico"
        performance_badge = "bg-amber-500"
        feedback_message = "Aprobado. Tienes las nociones básicas, pero te recomendamos repasar las diferencias entre frecuencias y modas."
    else:
        performance_label = "Necesita Refuerzo"
        performance_badge = "bg-rose-500"
        feedback_message = "Te invitamos a repasar las tablas de los talleres 1, 4 y 5 y volver a presentar una nueva prueba."

    minutes = time_spent_seconds // 60
    seconds = time_spent_seconds % 60
    time_formatted = f"{minutes:02d}:{seconds:02d}"

    results = {
        "exam_id": exam_id,
        "subject_name": session["subject_name"],
        "grade": session["grade"],
        "institution": session["institution"],
        "total_questions": total,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "unanswered_count": unanswered_count,
        "percentage": percentage,
        "performance_label": performance_label,
        "performance_badge": performance_badge,
        "feedback_message": feedback_message,
        "time_spent_seconds": time_spent_seconds,
        "time_formatted": time_formatted,
        "category_stats": category_stats,
        "review": review_items
    }

    session["submitted"] = True
    session["results"] = results
    return results
