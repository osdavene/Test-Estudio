import os
import sys
import json

sys.path.insert(0, os.path.abspath("."))

from fastapi.testclient import TestClient
from app.main import app
from app.questions_loader import get_subjects_list, get_subject_data, create_exam_session

def verify_all():
    print("=== 1. VERIFICACIÓN DE MATERIAS ===")
    subjects = get_subjects_list()
    print(f"Total materias encontradas: {len(subjects)}")
    for sub in subjects:
        print(f" - [{sub['id']}] {sub['name']} ({sub['total_questions']} preguntas, icon={sub['icon']}, color={sub['color']})")

    assert len(subjects) == 3, f"Esperaba 3 materias, pero encontré {len(subjects)}"

    print("\n=== 2. VERIFICACIÓN DE IMÁGENES DE CIENCIAS SOCIALES ===")
    soc_data = get_subject_data("sociales")
    assert soc_data is not None, "No se pudo cargar 'sociales.json'"
    assert len(soc_data["questions"]) == 40, f"Esperaba 40 preguntas en sociales, hay {len(soc_data['questions'])}"

    missing = []
    for q in soc_data["questions"]:
        img_rel = q["image"].lstrip("/")
        app_path = os.path.join("app", img_rel)
        if not os.path.exists(app_path):
            missing.append((q["id"], app_path))
    if missing:
        print(f"ERROR: Imágenes faltantes: {missing}")
        raise FileNotFoundError(f"Faltan {len(missing)} imágenes")
    print(f"¡Las 40 imágenes de Ciencias Sociales existen en app/static/img/questions_soc/!")

    print("\n=== 3. PRUEBA DE ENDPOINTS FASTAPI (TESTCLIENT) ===")
    client = TestClient(app)

    # Home
    res_home = client.get("/")
    assert res_home.status_code == 200, f"Error en GET /: {res_home.status_code}"
    assert "Ciencias Sociales" in res_home.text
    assert "Estadística" in res_home.text
    assert "Geometría" in res_home.text
    print("[OK] GET / retornó 200 y contiene las 3 materias.")

    # Exam Ciencias Sociales
    res_soc = client.get("/exam/sociales?count=15&timer=30")
    assert res_soc.status_code == 200, f"Error en GET /exam/sociales: {res_soc.status_code}"
    assert "Ciencias Sociales" in res_soc.text
    print("[OK] GET /exam/sociales retornó 200.")

    # Static image
    res_img = client.get("/static/img/questions_soc/q01.png")
    assert res_img.status_code == 200, f"Error en GET static img: {res_img.status_code}"
    print("[OK] GET /static/img/questions_soc/q01.png retornó 200.")

    print("\n=== ¡TODO VERIFICADO EXITOSAMENTE! ===")

if __name__ == "__main__":
    verify_all()
