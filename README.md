# 🎓 Simulador de Exámenes Escolares

Simulador web interactivo, rápido y ligero desarrollado con **Python (FastAPI + Jinja2 + Tailwind CSS)**. Diseñado específicamente para practicar evaluaciones escolares por temas y talleres.

🌐 **Enlace de Producción (AWS):** [https://test-estudio.servigest.online](https://test-estudio.servigest.online)  
📦 **Repositorio GitHub:** [https://github.com/osdavene/Test-Estudio](https://github.com/osdavene/Test-Estudio)

---

## 🚀 Características Principales

- **Sin inicios de sesión ni registros**: Acceso inmediato con 1 clic.
- **Exámenes de 15 preguntas aleatorias**: Cada vez que inicias un test se extrae un subconjunto aleatorio de preguntas del banco de la materia.
- **Opciones en orden aleatorio**: Las alternativas (A, B, C, D) se mezclan en diferente orden en cada intento para evitar la memorización por posición.
- **Navegador interactivo de preguntas**: Cuadrícula de 1 a 15 con estados visuales (Respondida, Sin responder, Pregunta actual).
- **Temporizador pedagógico configurable**: 30 minutos por defecto (2 min/pregunta, ideal para primaria), 20 min, 15 min o modo *Práctica Libre* sin límite de tiempo.
- **Calificación y Retroalimentación Inmediata**:
  - Porcentaje de acierto y escala de desempeño.
  - Métricas de correctas, incorrectas y tiempo empleado.
  - Desglose de rendimiento por tema/taller.
  - Revisión pregunta por pregunta con **explicación pedagógica detallada**.
- **100% Extensible para Nuevas Materias**: Añadir materias futuras (Matemáticas, Ciencias, Sociales, Lenguaje) requiere únicamente agregar un archivo `.json` en `app/subjects/`.

---

## 📚 Materia Actual: Estadística (Pensamiento Aleatorio) - Grado 3°
**Institución Educativa Cecilia de Lleras**

Cubre los 3 talleres y ejes temáticos de los documentos oficiales:
1. **Taller 1: Recolección y tabulación de datos (Semana 15)**:
   - Actividad *"El Tesoro de los Datos"*.
   - Estudio de preferencia de sabor de helado (Chocolate, Vainilla, Fresa).
   - Tabla de Frecuencias de Deportes (Fútbol, Baloncesto, Natación).
   - Conceptos estadísticos: Variable, Cualitativa Nominal, Cualitativa Ordinal, Población, Frecuencia Absoluta, Tabla, Datos, Encuesta y Conteo.
2. **Taller 4: Comparación de datos y formulación de preguntas a partir de tablas (Semana 21)**:
   - Torneo intercursos y meriendas tradicionales en descansos de 3°A y 3°B (Bollo de Mazorca, Carimañola, Arepa de Huevo).
   - Identificación de modas por salón (Moda 3°A: Bollo 12; Moda 3°B: Carimañola 15).
   - Comparaciones directas y cálculos de diferencias por unidades.
   - Formulación de preguntas de investigación conjuntas y lenguaje formal para cooperativa escolar.
3. **Taller 5: Redacción de conclusiones estadísticas apoyadas en la interpretación de datos (Semana 23)**:
   - Encuesta sobre Refrescos Tradicionales en la Ronda del Sinú, Montería (Chicha de Maíz, Agua de Coco, Jugo de Níspero, Guarapo con Limón).
   - Población total (70 personas).
   - Categoría de menor preferencia (Níspero, 10) y Moda (Agua de Coco, 25).
   - Criterios de escritura científica: formulación con rigor técnico sin apreciaciones subjetivas o infantiles.

---

## 🏃 Cómo Iniciar el Simulador

### Opción 1 (Directa en Windows):
Haz doble clic en el archivo:
```bash
iniciar.bat
```

### Opción 2 (Desde terminal PowerShell o CMD):
```bash
cd C:\Proyectos\Test-Estudio
python main.py
```
O con Uvicorn:
```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Abre tu navegador en:  
👉 **http://127.0.0.1:8000**

---

## ➕ Cómo Agregar Nuevas Materias en el Futuro

Para agregar cualquier otra materia (por ejemplo: Ciencias Naturales, Matemáticas, Historia):

1. Crea un archivo JSON dentro de `app/subjects/`, por ejemplo: `ciencias.json`.
2. Sigue esta estructura básica:

```json
{
  "id": "ciencias",
  "name": "Ciencias Naturales",
  "grade": "Grado Tercero",
  "institution": "I.E. Cecilia de Lleras",
  "description": "Evaluación sobre seres vivos, ecosistemas y recursos naturales.",
  "badge": "Periodo 2",
  "icon": "fa-seedling",
  "color": "emerald",
  "default_question_count": 20,
  "questions": [
    {
      "id": 1,
      "category": "Ecosistemas",
      "question": "¿Cuál es un factor abiótico de un ecosistema?",
      "context": "Recuerda la clasificación de factores bióticos y abióticos.",
      "options": [
        "El agua y la luz solar",
        "Los peces y las plantas",
        "Las bacterias del suelo",
        "Los animales herbívoros"
      ],
      "correct_answer": "El agua y la luz solar",
      "explanation": "Los factores abióticos son los elementos no vivos del ambiente, como la luz solar, el agua, la temperatura y el suelo."
    }
  ]
}
```

¡El simulador lo detectará automáticamente en la pantalla de inicio sin necesidad de reiniciar el servidor ni configurar bases de datos!
