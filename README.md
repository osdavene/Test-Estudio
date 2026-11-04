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
- **Gráficos e Ilustraciones Creados para Niños:** Todas las preguntas de cada materia cuentan con **gráficos e infografías diseñados a medida en alta resolución** (esquemas de barras, cuadrículas de perímetro, geoplanos con bandas elásticas, reglas graduadas con punto cero, conteos técnicos y diagramas geométricos) para facilitar el aprendizaje visual en niños de primaria.
- **Calificación y Retroalimentación Pedagógica:** Puntaje porcentual, nivel de desempeño, análisis por taller y revisión pregunta por pregunta con **explicación de la solución**.
- **Arquitectura Modular Multimateria:** Selector inicial interactivo para elegir entre las materias disponibles. Agregar una nueva materia requiere únicamente incluir su archivo `.json` en `app/subjects/`.

---

## 📚 Materias Disponibles — Grado 3° (I.E. Cecilia de Lleras)

### 1. 📊 Estadística (Pensamiento Aleatorio)
Banco de **42 preguntas** basadas en los talleres oficiales de Segundo Periodo:

| Taller / Eje Temático | Contenidos Evaluados |
| :--- | :--- |
| **Taller 1: Recolección y Tabulación (Sem. 15)** | Conteo técnico con palotes, helado preferido, tabla de deportes, conceptos de sopa de letras (*variable, cualitativa nominal/ordinal, población, frecuencia absoluta, tabla, encuesta, datos*). |
| **Taller 4: Comparación de Tablas (Sem. 21)** | Torneo intercursos, meriendas en 3°A y 3°B, cálculo de modas por salón, diferencias numéricas entre categorías y redacción técnica escolar. |
| **Taller 5: Redacción de Conclusiones (Sem. 23)** | Refrescos tradicionales de la Ronda del Sinú, moda, menor frecuencia, población total y criterios de escritura científica sin apreciaciones subjetivas. |

### 2. 📐 Geometría (Pensamiento Espacial y Métrico)
Banco de **40 preguntas** basadas en los talleres y guías técnicas de Segundo Periodo:

| Taller / Eje Temático | Contenidos Evaluados (DBA 4 y DBA 5) |
| :--- | :--- |
| **Taller 1: Herramientas no estandarizadas (Sem. 15)** | Longitud como atributo medible, Rally de la Cuarta (técnica consecutiva), medición con pasos en el patio escolar, precisión con el pulgar (hojas y ramitas), situación Saber de Juan y María en la puerta del aula, patrones arbitrarios y dispersión. |
| **Taller 2: Instrumentos estandarizados y precisión (Sem. 17)** | Uso de la regla graduada, regla de oro del punto cero (0), situación Saber del sacapuntas (1 a 4 cm), centímetro (cm) y metro (1 m = 100 cm), criterio de selección (regla rígida vs cinta métrica flexible para curvas), estimación, cálculo de error y líneas perpendiculares (90°). |
| **Taller 3: Perímetro en cuadrícula (Sem. 21)** | Concepto de perímetro como contorno exterior, regla técnica de omitir líneas internas, puesto rectangular del Mercado del Sur (3x2), situación Saber del planchón del Río Sinú (4x3), letra "M" de Montería en cuadrícula, identificación de vértices y fórmula del perímetro. |
| **Taller 4: Polígonos en el geoplano (Sem. 23)** | Construcción con pines y bandas elásticas, unidad lineal entre pines consecutivos, condición de figura cerrada para ser polígono, planchón en geoplano (3x2), carpas triangulares (lados y vértices), situación Saber del cuadrado de 3x3 del Proyecto Centro de Interés. |

### 3. 🌍 Ciencias Sociales (Geografía, Historia y Economía)
Banco de **40 preguntas** basadas en la Guía de Estudio Oficial de Tercer Periodo (8 Temas):

| Unidad / Eje Temático | Contenidos Evaluados |
| :--- | :--- |
| **Tema 1: Recursos Naturales de Colombia** | Satisfacción de necesidades humanas, factores de la riqueza natural (relieve y posición astronómica), selvas del Pacífico y Amazonia, sabanas ganaderas del Caribe y Orinoquia, riqueza minera (carbón, petróleo, oro, esmeraldas). |
| **Tema 2: El Planeta Tierra y Océanos** | La Tierra vista desde el espacio como "el planeta azul", distribución (70% agua y 30% continentes), los 5 grandes océanos (Pacífico, Atlántico, Índico, Ártico, Antártico), continente helado antártico deshabitado, ubicación de Colombia en el noroccidente de Suramérica con dos océanos. |
| **Tema 3: Fronteras y Límites de Colombia** | Superficie territorial (1 141 748 km²) y marítima (928 660 km²), límites con 5 países (Venezuela, Brasil, Perú, Ecuador y Panamá), frontera más larga (Venezuela con 2219 km), tratados internacionales limítrofes y zonas de frontera para la integración y la paz. |
| **Tema 4: Periodos Históricos e Indígenas** | 4 grandes periodos (Indígena, Hispánico, Independencia, República), poblamiento aborigen de +20 000 años, 3 familias lingüísticas (Chibcha, Caribe, Arawac), fin del periodo indígena en el año 1500 con la llegada de expediciones españolas. |
| **Tema 5: Periodo Hispánico y Mestizaje** | Etapas de Descubrimiento, Conquista y Colonia; primeras ciudades fundadas (Santa Marta 1525, Cartagena 1533, Bogotá 1538); 300 años de régimen colonial virreinal; mestizaje triétnico (indígenas, españoles y africanos); aportes hispánicos (idioma español, religión católica, animales domésticos, arquitectura). |
| **Tema 6: Periodo de la República** | Inicio en 1810 con Acta de Independencia; Batalla de Boyacá del 7 de agosto de 1819 con Simón Bolívar; evolución constitucional de nombres (Gran Colombia, Rep. Neogranadina, Conf. Granadina, EE.UU. de Colombia y República de Colombia desde 1886); exportaciones de café, banano, flores, carbón y petróleo. |
| **Tema 7: Los Tres Sectores de la Economía** | Sector Primario (extracción natural: café, banano, flores, caña, minería), Sector Secundario (transformación industrial y manufactura en fábricas), Sector Terciario (servicios: comercio, transporte, banca, salud, educación); superación de desigualdades sociales. |
| **Tema 8: Diversidad Cultural y Exponentes** | Plurietnicidad e identidad regional (habla, trajes, platos típicos, música y danzas folclóricas); exponentes mundiales: Gabriel García Márquez (Premio Nobel 1982), Fernando Botero (arte y esculturas con volumen "Boterismo"), Shakira y Juanes (embajadores de la música colombiana). |

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
