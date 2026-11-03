# 🎓 Simulador de Exámenes Escolares (Test-Estudio)

Plataforma web ágil, interactiva y ligera desarrollada con **Python (FastAPI + Jinja2 + Tailwind CSS)** en **Tema Oscuro**, diseñada para presentar evaluaciones formativas con preguntas y respuestas aleatorias sin barreras de registro.

🌐 **Enlace de Producción (AWS):** [https://test-estudio.servigest.online](https://test-estudio.servigest.online)  
📦 **Repositorio GitHub:** [https://github.com/osdavene/Test-Estudio](https://github.com/osdavene/Test-Estudio)

---

## ⚡ Características Principales

- **Acceso Inmediato:** Sin usuario, contraseña ni configuración de base de datos.
- **Exámenes de 15 Preguntas Aleatorias:** Seleccionadas al azar del banco temático en cada nuevo intento.
- **Opciones Barajadas:** Las alternativas (A, B, C, D) se ordenan de forma aleatoria para evitar la memorización mecánica.
- **Tiempo Pedagógico Adaptado:** **30 minutos** predeterminados (2 min por pregunta, pensado para niños de primaria) o modo *Práctica Libre*.
- **Diseño Oscuro Ergonómico:** Paleta oscura (`slate-950` / `slate-900`) con acentos esmeralda inspirada en *Dian2676Py*.
- **100% Optimizado para Móviles:** Barra superior compacta, barra inferior flotante accesible con el pulgar y hoja óptica modal emergente.
- **Gráficos e Ilustraciones Creados para Niños:** Las 42 preguntas cuentan con **gráficos e infografías diseñados a medida en alta resolución**, con esquemas de barras, conteos técnicos con palotes, tablas comparativas y diagramas claros para facilitar el aprendizaje visual en niños de primaria.
- **Calificación y Retroalimentación Pedagógica:** Puntaje porcentual, nivel de desempeño, análisis por taller y revisión pregunta por pregunta con **explicación de la solución**.
- **Arquitectura Modular:** Agregar una nueva materia requiere únicamente incluir su archivo `.json` en `app/subjects/`.

---

## 📚 Materia Activa: Estadística (Pensamiento Aleatorio) — Grado 3°
**Institución Educativa Cecilia de Lleras** &bull; Banco de 42 preguntas basadas en los talleres oficiales:

| Taller / Eje Temático | Contenidos Evaluados |
| :--- | :--- |
| **Taller 1: Recolección y Tabulación (Sem. 15)** | Conteo técnico, helado preferido, tabla de deportes, conceptos de sopa de letras (*variable, cualitativa nominal/ordinal, población, frecuencia absoluta, tabla, encuesta, datos*). |
| **Taller 4: Comparación de Tablas (Sem. 21)** | Torneo intercursos, meriendas en 3°A y 3°B, cálculo de modas por salón, diferencias numéricas entre categorías y redacción técnica escolar. |
| **Taller 5: Redacción de Conclusiones (Sem. 23)** | Refrescos tradicionales de la Ronda del Sinú, moda, menor frecuencia, población total y criterios de escritura científica sin apreciaciones subjetivas. |

---

## 🚀 Inicio Rápido (Local)

### En Windows (1 Clic)
Haz doble clic en:
```bat
iniciar.bat
```

### Desde Terminal
```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
Abre en tu navegador: **http://127.0.0.1:8000**

---

## ☁️ Despliegue en Servidor AWS (Producción)

- **Dominio:** `https://test-estudio.servigest.online` (con SSL Let's Encrypt).
- **Ruta en Servidor:** `/home/testestudio/htdocs/test-estudio.servigest.online`
- **Servicio:** `test-estudio.service` (Systemd + Uvicorn en puerto interno `8006`).
- **CI/CD:** Despliegue automático vía GitHub Actions ([.github/workflows/deploy.yml](.github/workflows/deploy.yml)) en cada push a `main`.

---

## ➕ Cómo Agregar Nuevas Materias

Para sumar materias como *Ciencias Naturales*, *Matemáticas* o *Lenguaje*:

1. Crea un archivo JSON en `app/subjects/<materia>.json`:
```json
{
  "id": "ciencias",
  "name": "Ciencias Naturales",
  "grade": "Grado Tercero",
  "institution": "I.E. Cecilia de Lleras",
  "description": "Evaluación de seres vivos, ecosistemas y recursos.",
  "badge": "Periodo 2",
  "icon": "fa-seedling",
  "default_question_count": 15,
  "questions": [
    {
      "id": 1,
      "category": "Ecosistemas",
      "question": "¿Cuál es un factor abiótico de un ecosistema?",
      "context": "Factores bióticos y abióticos.",
      "options": [
        "El agua y la luz solar",
        "Los peces y las plantas",
        "Las bacterias del suelo",
        "Los animales herbívoros"
      ],
      "correct_answer": "El agua y la luz solar",
      "explanation": "Los factores abióticos son los elementos no vivos, como el agua, la luz solar y la temperatura."
    }
  ]
}
```
2. El sistema la detecta y lista automáticamente en la pantalla de inicio sin reiniciar servidores ni configurar bases de datos.
