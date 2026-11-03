"""
Generador automático de gráficos e ilustraciones estadísticas para niños de 3° de primaria.
Crea 42 imágenes de alta resolución (q01.png a q42.png) personalizadas para cada pregunta.
Compatible al 100% con Windows y Linux (AWS).
"""

import os
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Rutas de salida
OUT_DIRS = [
    os.path.abspath('app/static/img/questions'),
    os.path.abspath('static/img/questions')
]
for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

def create_canvas(title, category, foot_title, foot_sub="", badge_color='#10b981', foot_color='#38bdf8'):
    """Crea la base de la tarjeta con estilo oscuro elegante y bordes redondeados."""
    fig, ax = plt.subplots(figsize=(8.8, 4.8), dpi=140)
    fig.patch.set_facecolor('#090d16')
    ax.set_facecolor('#090d16')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Contenedor exterior
    outer = patches.FancyBboxPatch((1.2, 1.2), 97.6, 97.6, boxstyle="round,pad=0.5,rounding_size=3",
                                   facecolor='#111827', edgecolor='#1f2937', linewidth=1.5)
    ax.add_patch(outer)
    
    # Barra superior (Header)
    header_box = patches.FancyBboxPatch((3.5, 83), 93, 12, boxstyle="round,pad=0.4,rounding_size=2",
                                        facecolor='#1e293b', edgecolor=badge_color, linewidth=1.6)
    ax.add_patch(header_box)
    ax.text(6, 90.5, category.upper(), color=badge_color, fontsize=8, fontweight='bold', va='center')
    ax.text(50, 87.5, title, color='#ffffff', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Barra inferior (Footer con mensaje pedagógico)
    foot_box = patches.FancyBboxPatch((3.5, 3.5), 93, 14, boxstyle="round,pad=0.4,rounding_size=2",
                                      facecolor='#0f172a', edgecolor=foot_color, linewidth=1.4)
    ax.add_patch(foot_box)
    if foot_sub:
        ax.text(50, 12.2, foot_title, color='#ffffff', fontsize=9.5, fontweight='bold', ha='center', va='center')
        ax.text(50, 7.2, foot_sub, color='#94a3b8', fontsize=8.5, ha='center', va='center')
    else:
        ax.text(50, 10.5, foot_title, color='#ffffff', fontsize=9.5, fontweight='bold', ha='center', va='center')
        
    return fig, ax

def save_fig(fig, qid):
    """Guarda la figura en todas las carpetas destino."""
    filename = f"q{qid:02d}.png"
    plt.tight_layout()
    for d in OUT_DIRS:
        target = os.path.join(d, filename)
        plt.savefig(target, facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
    print(f"[OK] Guardado: {filename}")

# ==============================================================================
# 1. GENERADORES DE CONCEPTOS (Q01 a Q08, Q14, Q41)
# ==============================================================================

def gen_q01():
    fig, ax = create_canvas("¿QUÉ ES UNA VARIABLE EN ESTADÍSTICA?", "CONCEPTOS ESTADÍSTICOS",
                           "IDEA CLAVE: La Variable es la cualidad o característica que se investiga en el grupo.",
                           "Ejemplos: color, deporte, estatura, comida preferida...",
                           badge_color='#10b981', foot_color='#10b981')
    cards = [
        ("Color Favorito", "Rojo, Azul, Verde\n(Cualidad o gusto)", "#3b82f6"),
        ("Deporte Preferido", "Fútbol, Baloncesto\n(Actividad física)", "#10b981"),
        ("Estatura de Niños", "1.20 m, 1.25 m\n(Medida numérica)", "#f59e0b")
    ]
    for i, (title, desc, col) in enumerate(cards):
        x = 5.5 + i * 30.5
        box = patches.FancyBboxPatch((x, 23), 27.5, 54, boxstyle="round,pad=0.5,rounding_size=2",
                                     facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(box)
        tag = patches.FancyBboxPatch((x+2, 68), 23.5, 7, boxstyle="round,pad=0.2,rounding_size=1",
                                     facecolor=col, edgecolor='none')
        ax.add_patch(tag)
        ax.text(x+13.75, 71.5, f"EJEMPLO {i+1}", color='#ffffff', fontsize=8.5, fontweight='bold', ha='center', va='center')
        ax.text(x+13.75, 54, title, color='#f8fafc', fontsize=11, fontweight='bold', ha='center', va='center')
        ax.text(x+13.75, 38, desc, color='#cbd5e1', fontsize=9, ha='center', va='center')
    save_fig(fig, 1)

def gen_q02():
    fig, ax = create_canvas("VARIABLE CUALITATIVA NOMINAL", "CONCEPTOS ESTADÍSTICOS",
                           "NOMINAL: Nombres o cualidades que NO tienen un orden obligatorio.",
                           "Cualquiera puede mencionarse primero sin alterar el resultado.",
                           badge_color='#38bdf8', foot_color='#38bdf8')
    items = [
        ("Mascotas", "Perro, Gato, Loro\n(Sin orden específico)", "#ec4899"),
        ("Sabores Helado", "Vainilla, Fresa, Coco\n(Todos valen igual)", "#8b5cf6"),
        ("Colores", "Amarillo, Azul, Rojo\n(Sin jerarquía)", "#06b6d4")
    ]
    for i, (title, desc, col) in enumerate(items):
        x = 5.5 + i * 30.5
        box = patches.FancyBboxPatch((x, 23), 27.5, 54, boxstyle="round,pad=0.5,rounding_size=2",
                                     facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(box)
        tag = patches.FancyBboxPatch((x+2, 68), 23.5, 7, boxstyle="round,pad=0.2,rounding_size=1",
                                     facecolor=col, edgecolor='none')
        ax.add_patch(tag)
        ax.text(x+13.75, 71.5, "NO TIENE ORDEN", color='#ffffff', fontsize=8, fontweight='bold', ha='center', va='center')
        ax.text(x+13.75, 54, title, color='#f8fafc', fontsize=11, fontweight='bold', ha='center', va='center')
        ax.text(x+13.75, 38, desc, color='#cbd5e1', fontsize=9, ha='center', va='center')
    save_fig(fig, 2)

def gen_q03():
    fig, ax = create_canvas("VARIABLE CUALITATIVA ORDINAL", "CONCEPTOS ESTADÍSTICOS",
                           "ORDINAL: Cualidades que SÍ tienen un orden o jerarquía obligatoria.",
                           "Ejemplo: El puesto ocupado en una competencia (1.º, 2.º o 3.er puesto).",
                           badge_color='#f59e0b', foot_color='#f59e0b')
    # Podio
    # 2do puesto (Plata)
    p2 = patches.FancyBboxPatch((15, 23), 20, 32, boxstyle="round,pad=0.3,rounding_size=1.5",
                                facecolor='#334155', edgecolor='#94a3b8', linewidth=2)
    ax.add_patch(p2)
    ax.text(25, 45, "2.º PUESTO", color='#f1f5f9', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(25, 32, "(PLATA)", color='#cbd5e1', fontsize=10, fontweight='bold', ha='center', va='center')
    
    # 1er puesto (Oro)
    p1 = patches.FancyBboxPatch((40, 23), 20, 48, boxstyle="round,pad=0.3,rounding_size=1.5",
                                facecolor='#854d0e', edgecolor='#facc15', linewidth=2.5)
    ax.add_patch(p1)
    ax.text(50, 61, "1.º PUESTO", color='#fef08a', fontsize=14, fontweight='bold', ha='center', va='center')
    ax.text(50, 44, "GANADOR\n(ORO)", color='#fef9c3', fontsize=10, fontweight='bold', ha='center', va='center')
    
    # 3er puesto (Bronce)
    p3 = patches.FancyBboxPatch((65, 23), 20, 22, boxstyle="round,pad=0.3,rounding_size=1.5",
                                facecolor='#451a03', edgecolor='#d97706', linewidth=2)
    ax.add_patch(p3)
    ax.text(75, 37, "3.º PUESTO", color='#fed7aa', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(75, 28, "(BRONCE)", color='#fdba74', fontsize=9, fontweight='bold', ha='center', va='center')
    save_fig(fig, 3)

def gen_q04():
    fig, ax = create_canvas("LA POBLACIÓN EN UN ESTUDIO ESTADÍSTICO", "CONCEPTOS ESTADÍSTICOS",
                           "POBLACIÓN: El conjunto TOTAL de personas o elementos que se investigan.",
                           "No es solo un grupo pequeño: son todos los que participan en el estudio.",
                           badge_color='#8b5cf6', foot_color='#8b5cf6')
    # Círculo contenedor grande de población
    big_box = patches.FancyBboxPatch((10, 23), 80, 55, boxstyle="round,pad=0.8,rounding_size=3",
                                     facecolor='#1e293b', edgecolor='#a855f7', linewidth=2.5)
    ax.add_patch(big_box)
    ax.text(50, 70, "INSTITUCIÓN EDUCATIVA CECILIA DE LLERAS", color='#c084fc', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 63, "POBLACIÓN COMPLETA INVESTIGADA (100% DE ALUMNOS)", color='#f8fafc', fontsize=12, fontweight='bold', ha='center')
    
    # Iconos y badges dentro
    badges = [
        ("Niños de 3°A", "26 alumnos", 22, "#3b82f6"),
        ("Niños de 3°B", "30 alumnos", 50, "#10b981"),
        ("Total del Grado", "56 alumnos", 78, "#f59e0b")
    ]
    for name, qty, x_pos, col in badges:
        bx = patches.FancyBboxPatch((x_pos-12, 30), 24, 25, boxstyle="round,pad=0.4,rounding_size=2",
                                    facecolor='#0f172a', edgecolor=col, linewidth=1.8)
        ax.add_patch(bx)
        ax.text(x_pos, 47, name, color='#f1f5f9', fontsize=9.5, fontweight='bold', ha='center')
        ax.text(x_pos, 37, qty, color=col, fontsize=12, fontweight='bold', ha='center')
    save_fig(fig, 4)

def gen_q05():
    fig, ax = create_canvas("¿QUÉ ES LA FRECUENCIA ABSOLUTA?", "CONCEPTOS ESTADÍSTICOS",
                           "FRECUENCIA ABSOLUTA: El número de veces exacto que se repite un dato.",
                           "Ejemplo: Si 5 niños eligen Manzana, su frecuencia absoluta es 5.",
                           badge_color='#06b6d4', foot_color='#06b6d4')
    # 3 Pasos
    steps = [
        ("1. DATO OBSERVADO", "Manzana\n(5 veces elegida)", 18, "#3b82f6"),
        ("2. CONTEO TÉCNICO", "||||  (con barra)\n(Bloque cerrado)", 50, "#f59e0b"),
        ("3. FRECUENCIA ABSOLUTA", "f = 5\n(Repeticiones exactas)", 82, "#10b981")
    ]
    for title, desc, cx, col in steps:
        bx = patches.FancyBboxPatch((cx-14, 24), 28, 52, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 68, title, color=col, fontsize=9, fontweight='bold', ha='center')
        ax.text(cx, 46, desc, color='#ffffff', fontsize=11, fontweight='bold', ha='center', va='center')
    
    # Flechas conectoras
    ax.annotate("", xy=(34, 50), xytext=(32, 50), arrowprops=dict(arrowstyle="->", color='#94a3b8', lw=2.5))
    ax.annotate("", xy=(66, 50), xytext=(64, 50), arrowprops=dict(arrowstyle="->", color='#94a3b8', lw=2.5))
    save_fig(fig, 5)

def gen_q06():
    fig, ax = create_canvas("ESTRUCTURA DE UNA TABLA DE FRECUENCIAS", "CONCEPTOS ESTADÍSTICOS",
                           "Función principal: Organizar y resumir los datos en filas y columnas claras.",
                           "Permite saber rápidamente los conteos y frecuencias de cada opción.",
                           badge_color='#10b981', foot_color='#10b981')
    # Tabla dibujada
    # Cabecera
    headers = [("VARIABLE (DATO)", 7, 30), ("CONTEO TÉCNICO", 40, 27), ("FRECUENCIA ABSOLUTA", 70, 24)]
    for text, x, w in headers:
        bx = patches.FancyBboxPatch((x, 62), w, 12, boxstyle="round,pad=0.2,rounding_size=1",
                                    facecolor='#0f766e', edgecolor='#14b8a6', linewidth=1.5)
        ax.add_patch(bx)
        ax.text(x + w/2, 68, text, color='#ffffff', fontsize=9, fontweight='bold', ha='center', va='center')
    
    # Filas
    rows = [
        ("Helado de Fresa", "|||| |", "6 personas", 47, '#1e293b'),
        ("Helado de Vainilla", "|||| |||", "8 personas", 32, '#0f172a'),
        ("Helado de Chocolate", "|||| ||||", "10 personas", 17, '#1e293b')
    ]
    for cat, marks, freq, y, bg in rows:
        bx1 = patches.Rectangle((7, y), 30, 12, facecolor=bg, edgecolor='#334155')
        bx2 = patches.Rectangle((40, y), 27, 12, facecolor=bg, edgecolor='#334155')
        bx3 = patches.Rectangle((70, y), 24, 12, facecolor=bg, edgecolor='#334155')
        for b in [bx1, bx2, bx3]: ax.add_patch(b)
        ax.text(22, y+6, cat, color='#f1f5f9', fontsize=9.5, fontweight='bold', ha='center', va='center')
        ax.text(53.5, y+6, marks, color='#38bdf8', fontsize=11, fontweight='bold', ha='center', va='center')
        ax.text(82, y+6, freq, color='#10b981', fontsize=9.5, fontweight='bold', ha='center', va='center')
    save_fig(fig, 6)

def gen_q07():
    fig, ax = create_canvas("MÉTODO DE RECOLECCIÓN: LA ENCUESTA", "CONCEPTOS ESTADÍSTICOS",
                           "La Encuesta es el método para formular preguntas y recolectar datos directamente.",
                           "Se utiliza para conocer opiniones, gustos y preferencias de una población.",
                           badge_color='#f59e0b', foot_color='#f59e0b')
    # Dibujo de hoja de encuesta
    sheet = patches.FancyBboxPatch((20, 22), 60, 56, boxstyle="round,pad=0.5,rounding_size=2",
                                   facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(sheet)
    
    # Título encuesta
    ax.text(50, 71, "FORMULARIO DE ENCUESTA ESCOLAR", color='#fef08a', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 63, "¿Cuál es tu merienda favorita en el recreo?", color='#f8fafc', fontsize=10, ha='center')
    
    # Casillas de verificación
    options = [
        ("[X] Bollo de Mazorca", "#10b981", 52),
        ("[ ] Carimañola", "#94a3b8", 43),
        ("[ ] Arepa de Huevo", "#94a3b8", 34),
        ("Entrevistador registra la respuesta directa ->", "#38bdf8", 25)
    ]
    for opt, col, y in options:
        ax.text(26, y, opt, color=col, fontsize=9.5, fontweight='bold')
    save_fig(fig, 7)

def gen_q08():
    fig, ax = create_canvas("EL CONTEO TÉCNICO (MARCAS / PALOTES)", "CONCEPTOS ESTADÍSTICOS",
                           "Registrar marcas por cada respuesta y agrupar en bloques cerrados de 5.",
                           "4 palitos verticales y 1 diagonal cruzado = Grupo cerrado de 5 marcas.",
                           badge_color='#10b981', foot_color='#10b981')
    cards = [
        ("|", "1 marca", 13, "#64748b"),
        ("||", "2 marcas", 31, "#64748b"),
        ("|||", "3 marcas", 49, "#64748b"),
        ("||||", "4 marcas", 67, "#64748b"),
        ("||||", "5 MARCAS\n(Cerrado con diagonal)", 86, "#10b981")
    ]
    for marks, desc, cx, col in cards:
        bx = patches.FancyBboxPatch((cx-8, 26), 16, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 58, marks, color=col, fontsize=20, fontweight='bold', ha='center', va='center')
        ax.text(cx, 38, desc, color='#f1f5f9', fontsize=8, fontweight='bold', ha='center', va='center')
    
    # Línea diagonal sobre el último grupo para ilustrar el cierre
    ax.plot([80, 92], [52, 64], color='#ef4444', linewidth=3)
    save_fig(fig, 8)

def gen_q14():
    fig, ax = create_canvas("ACTIVIDAD: EL TESORO DE LOS DATOS", "TALLER 1: RECOLECCIÓN",
                           "Objetivo: Registrar los datos y realizar un conteo para hallar la mayor frecuencia.",
                           "Los estudiantes extraen útiles escolares sin mirar y registran cuántos salen de cada uno.",
                           badge_color='#8b5cf6', foot_color='#8b5cf6')
    # Bolsa de útiles
    bag = patches.FancyBboxPatch((10, 24), 35, 52, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#a855f7', linewidth=2)
    ax.add_patch(bag)
    ax.text(27.5, 68, "BOLSA DE ÚTILES", color='#c084fc', fontsize=11, fontweight='bold', ha='center')
    ax.text(27.5, 54, "Lápices (7)", color='#f8fafc', fontsize=11, ha='center')
    ax.text(27.5, 42, "Borradores (5)", color='#f8fafc', fontsize=11, ha='center')
    ax.text(27.5, 30, "Sacapuntas (4)", color='#f8fafc', fontsize=11, ha='center')
    
    # Hoja de Conteo al lado
    sheet = patches.FancyBboxPatch((52, 24), 38, 52, boxstyle="round,pad=0.5,rounding_size=2",
                                   facecolor='#0f172a', edgecolor='#10b981', linewidth=2)
    ax.add_patch(sheet)
    ax.text(71, 68, "REGISTRO DE CONTEO", color='#34d399', fontsize=11, fontweight='bold', ha='center')
    ax.text(71, 54, "Lápices: |||| ||  (7)", color='#38bdf8', fontsize=10, ha='center')
    ax.text(71, 42, "Borradores: ||||  (5)", color='#cbd5e1', fontsize=10, ha='center')
    ax.text(71, 30, "Sacapuntas: ||||  (4)", color='#cbd5e1', fontsize=10, ha='center')
    save_fig(fig, 14)

def gen_q41():
    fig, ax = create_canvas("VARIABLE CUALITATIVA VS CUANTITATIVA", "CONCEPTOS ESTADÍSTICOS",
                           "Cualitativa = Expresa cualidades o palabras (color, deporte, fruta).",
                           "Cuantitativa = Expresa cantidades numéricas o medidas (edad, peso, estatura).",
                           badge_color='#ec4899', foot_color='#ec4899')
    # Panel Izquierdo: Cualitativa
    p_left = patches.FancyBboxPatch((6, 23), 41, 54, boxstyle="round,pad=0.5,rounding_size=2",
                                   facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(p_left)
    ax.text(26.5, 70, "CUALITATIVA", color='#38bdf8', fontsize=13, fontweight='bold', ha='center')
    ax.text(26.5, 62, "Cualidades y Características", color='#94a3b8', fontsize=9, ha='center')
    ax.text(26.5, 48, "• Sabor de helado preferido\n• Deporte que más practicas\n• Color de ojos o cabello", color='#ffffff', fontsize=10, ha='center')
    ax.text(26.5, 29, "SE RESPONDE CON PALABRAS", color='#38bdf8', fontsize=8.5, fontweight='bold', ha='center')
    
    # Panel Derecho: Cuantitativa
    p_right = patches.FancyBboxPatch((53, 23), 41, 54, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(p_right)
    ax.text(73.5, 70, "CUANTITATIVA", color='#34d399', fontsize=13, fontweight='bold', ha='center')
    ax.text(73.5, 62, "Cantidades y Medidas", color='#94a3b8', fontsize=9, ha='center')
    ax.text(73.5, 48, "• Edad de los estudiantes (8 años)\n• Estatura en centímetros (125 cm)\n• Número de hermanos (2)", color='#ffffff', fontsize=10, ha='center')
    ax.text(73.5, 29, "SE RESPONDE CON NÚMEROS", color='#34d399', fontsize=8.5, fontweight='bold', ha='center')
    save_fig(fig, 41)


# ==============================================================================
# 2. GENERADORES TALLER 1: HELADOS (Q09 a Q13)
# ==============================================================================

def draw_icecream_bars(ax, highlight_mode=False, highlight_diff=False, show_sum=False):
    """Dibuja las barras de helados: Chocolate=10, Vainilla=8, Fresa=5."""
    data = [
        ("Chocolate", 10, "#eab308" if highlight_mode else "#a855f7", "10 votos"),
        ("Vainilla", 8, "#38bdf8", "8 votos"),
        ("Fresa", 5, "#f43f5e", "5 votos")
    ]
    for i, (name, val, col, lbl) in enumerate(data):
        x = 18 + i * 24
        w = 16
        h = val * 4.2
        bar = patches.FancyBboxPatch((x, 24), w, h, boxstyle="round,pad=0.3,rounding_size=2",
                                     facecolor=col, edgecolor='#ffffff' if (highlight_mode and i==0) else 'none',
                                     linewidth=2.5 if (highlight_mode and i==0) else 0)
        ax.add_patch(bar)
        ax.text(x + w/2, 24 + h + 2.5, lbl, color='#ffffff', fontsize=10, fontweight='bold', ha='center')
        ax.text(x + w/2, 19, name, color='#cbd5e1', fontsize=10, fontweight='bold', ha='center')

def gen_q09():
    fig, ax = create_canvas("ENCUESTA DE HELADOS: LA VARIABLE", "TALLER 1: TABULACIÓN",
                           "La variable estudiada es: 'Sabor de helado preferido'.",
                           "Es la pregunta central realizada a los niños del salón de clase.",
                           badge_color='#38bdf8', foot_color='#38bdf8')
    draw_icecream_bars(ax)
    callout = patches.FancyBboxPatch((15, 67), 70, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#0f766e', edgecolor='#14b8a6', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 72.5, "¿QUÉ SE LE PREGUNTÓ A CADA NIÑO?  ->  Sabor de helado preferido", color='#ffffff', fontsize=9.5, fontweight='bold', ha='center')
    save_fig(fig, 9)

def gen_q10():
    fig, ax = create_canvas("ENCUESTA DE HELADOS: TIPO DE VARIABLE", "TALLER 1: TABULACIÓN",
                           "Tipo de variable: CUALITATIVA NOMINAL.",
                           "Chocolate, Vainilla y Fresa son palabras (cualidades) sin ningún orden numérico.",
                           badge_color='#f59e0b', foot_color='#f59e0b')
    draw_icecream_bars(ax)
    callout = patches.FancyBboxPatch((12, 67), 76, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 72.5, "Los sabores no se ordenan de 1.º o 2.º  ->  ¡Son CUALITATIVOS NOMINALES!", color='#fef08a', fontsize=9.5, fontweight='bold', ha='center')
    save_fig(fig, 10)

def gen_q11():
    fig, ax = create_canvas("ENCUESTA DE HELADOS: POBLACIÓN TOTAL", "TALLER 1: TABULACIÓN",
                           "Población total encuestada = Suma de todas las frecuencias absolutas.",
                           "Operación matemática: 10 (Chocolate) + 8 (Vainilla) + 5 (Fresa) = 23 estudiantes.",
                           badge_color='#10b981', foot_color='#10b981')
    draw_icecream_bars(ax)
    callout = patches.FancyBboxPatch((10, 66), 80, 12, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#064e3b', edgecolor='#34d399', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 72, "SUMA DE FRECUENCIAS: 10 + 8 + 5 = 23 ESTUDIANTES EN TOTAL", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    save_fig(fig, 11)

def gen_q12():
    fig, ax = create_canvas("ENCUESTA DE HELADOS: ¿CUÁL ES LA MODA?", "TALLER 1: TABULACIÓN",
                           "LA MODA es Chocolate con 10 preferencias.",
                           "La moda es siempre el dato que tiene la MAYOR frecuencia absoluta (barra más alta).",
                           badge_color='#eab308', foot_color='#eab308')
    draw_icecream_bars(ax, highlight_mode=True)
    ax.text(26, 72, "MODA (MÁXIMO)", color='#facc15', fontsize=13, fontweight='bold', ha='center')
    save_fig(fig, 12)

def gen_q13():
    fig, ax = create_canvas("DIFERENCIA: CHOCOLATE VS VAINILLA", "TALLER 1: TABULACIÓN",
                           "Chocolate (10) supera a Vainilla (8) por 2 votos de diferencia.",
                           "Cálculo matemático: 10 - 8 = 2 preferencias de ventaja a favor de Chocolate.",
                           badge_color='#ec4899', foot_color='#ec4899')
    draw_icecream_bars(ax, highlight_diff=True)
    callout = patches.FancyBboxPatch((16, 67), 68, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#831843', edgecolor='#f43f5e', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 72.5, "RESTA DE FRECUENCIAS: 10 (Chocolate) - 8 (Vainilla) = 2 VOTOS", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 13)


# ==============================================================================
# 3. GENERADORES TALLER 1: TABLA DE DEPORTES (Q15 a Q18)
# ==============================================================================

def draw_sports_bars(ax, highlight_idx=-1):
    """Dibuja gráfico de deportes: Fútbol=12, Baloncesto=8, Natación=10."""
    sports = [
        ("Fútbol", 12, "#10b981", "12 votos"),
        ("Baloncesto", 8, "#f59e0b", "8 votos"),
        ("Natación", 10, "#06b6d4", "10 votos")
    ]
    for i, (name, val, col, lbl) in enumerate(sports):
        x = 18 + i * 24
        w = 16
        h = val * 3.6
        is_hl = (highlight_idx == i)
        bar = patches.FancyBboxPatch((x, 24), w, h, boxstyle="round,pad=0.3,rounding_size=2",
                                     facecolor=col, edgecolor='#ffffff' if is_hl else 'none',
                                     linewidth=2.5 if is_hl else 0)
        ax.add_patch(bar)
        ax.text(x + w/2, 24 + h + 2.5, lbl, color='#ffffff', fontsize=10, fontweight='bold', ha='center')
        ax.text(x + w/2, 19, name, color='#cbd5e1', fontsize=10, fontweight='bold', ha='center')

def gen_q15():
    fig, ax = create_canvas("PREFERENCIA DE DEPORTES: TOTAL POBLACIÓN", "TALLER 1: DEPORTES",
                           "Población encuestada = 30 personas en total.",
                           "Suma de frecuencias absolutas: 12 (Fútbol) + 8 (Baloncesto) + 10 (Natación) = 30.",
                           badge_color='#10b981', foot_color='#10b981')
    draw_sports_bars(ax)
    callout = patches.FancyBboxPatch((12, 68), 76, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#064e3b', edgecolor='#34d399', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 73.5, "POBLACIÓN TOTAL = 12 + 8 + 10 = 30 PERSONAS ENCUESTADAS", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 15)

def gen_q16():
    fig, ax = create_canvas("DEPORTES: MENOR FRECUENCIA ABSOLUTA", "TALLER 1: DEPORTES",
                           "Baloncesto tiene la MENOR frecuencia absoluta con 8 preferencias.",
                           "Es la barra más baja de la gráfica comparada con Fútbol (12) y Natación (10).",
                           badge_color='#f59e0b', foot_color='#f59e0b')
    draw_sports_bars(ax, highlight_idx=1)
    ax.text(50, 68, "MENOR FRECUENCIA (8)", color='#fcd34d', fontsize=11, fontweight='bold', ha='center')
    save_fig(fig, 16)

def gen_q17():
    fig, ax = create_canvas("CONTEO TÉCNICO: 12 VOTOS DE FÚTBOL", "TALLER 1: DEPORTES",
                           "12 personas en marcas = Dos grupos cerrados de 5 y 2 marcas sueltas.",
                           "Cálculo por bloques: (5 marcas) + (5 marcas) + (2 sueltas) = 12 marcas en total.",
                           badge_color='#10b981', foot_color='#10b981')
    blocks = [
        ("||||", "GRUPO 1\n(5 marcas)", 25, '#10b981'),
        ("||||", "GRUPO 2\n(5 marcas)", 50, '#10b981'),
        ("||", "SUELTOS\n(2 marcas)", 75, '#38bdf8')
    ]
    for marks, sub, cx, col in blocks:
        bx = patches.FancyBboxPatch((cx-10, 28), 20, 44, boxstyle="round,pad=0.4,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 56, marks, color=col, fontsize=20, fontweight='bold', ha='center', va='center')
        ax.text(cx, 38, sub, color='#f1f5f9', fontsize=9, fontweight='bold', ha='center', va='center')
    ax.plot([17, 33], [50, 62], color='#ef4444', linewidth=2.5)
    ax.plot([42, 58], [50, 62], color='#ef4444', linewidth=2.5)
    save_fig(fig, 17)

def gen_q18():
    fig, ax = create_canvas("DIFERENCIA: FÚTBOL VS NATACIÓN", "TALLER 1: DEPORTES",
                           "Fútbol (12) supera a Natación (10) por 2 unidades de diferencia.",
                           "Resta de frecuencias: 12 - 10 = 2 personas más prefieren Fútbol.",
                           badge_color='#06b6d4', foot_color='#06b6d4')
    draw_sports_bars(ax)
    callout = patches.FancyBboxPatch((15, 68), 70, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#155e75', edgecolor='#22d3ee', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 73.5, "RESTA: 12 (Fútbol) - 10 (Natación) = 2 UNIDADES DE DIFERENCIA", color='#ffffff', fontsize=9.5, fontweight='bold', ha='center')
    save_fig(fig, 18)


# ==============================================================================
# 4. GENERADORES TALLER 4: MERIENDAS 3°A Y 3°B (Q19 a Q30, Q42)
# ==============================================================================

def draw_dual_classroom_chart(ax, highlight_item=None, highlight_salon=None):
    """
    Dibuja gráfico comparativo de meriendas:
    3°A: Bollo=12, Carimañola=6, Arepa=8 (Total=26)
    3°B: Bollo=5, Carimañola=15, Arepa=10 (Total=30)
    """
    snacks = ["Bollo Mazorca", "Carimañola", "Arepa Huevo"]
    vals_a = [12, 6, 8]
    vals_b = [5, 15, 10]
    
    # Leyenda salones arriba
    leg_a = patches.FancyBboxPatch((24, 73), 22, 6.5, boxstyle="round,pad=0.2,rounding_size=1",
                                   facecolor='#1e3a8a', edgecolor='#3b82f6', linewidth=1.5)
    leg_b = patches.FancyBboxPatch((54, 73), 22, 6.5, boxstyle="round,pad=0.2,rounding_size=1",
                                   facecolor='#064e3b', edgecolor='#10b981', linewidth=1.5)
    ax.add_patch(leg_a)
    ax.add_patch(leg_b)
    ax.text(35, 76.2, "SALÓN 3°A (Total: 26)", color='#93c5fd', fontsize=8.5, fontweight='bold', ha='center', va='center')
    ax.text(65, 76.2, "SALÓN 3°B (Total: 30)", color='#6ee7b7', fontsize=8.5, fontweight='bold', ha='center', va='center')
    
    for i in range(3):
        x_base = 14 + i * 28
        # Barra 3°A
        h_a = vals_a[i] * 2.8
        is_hl_a = (highlight_item == i and (highlight_salon in ['A', 'BOTH']))
        b_a = patches.FancyBboxPatch((x_base, 24), 10, h_a, boxstyle="round,pad=0.2,rounding_size=1",
                                     facecolor='#2563eb', edgecolor='#facc15' if is_hl_a else 'none',
                                     linewidth=2.5 if is_hl_a else 0)
        ax.add_patch(b_a)
        ax.text(x_base + 5, 24 + h_a + 2, str(vals_a[i]), color='#93c5fd', fontsize=9.5, fontweight='bold', ha='center')
        
        # Barra 3°B
        h_b = vals_b[i] * 2.8
        is_hl_b = (highlight_item == i and (highlight_salon in ['B', 'BOTH']))
        b_b = patches.FancyBboxPatch((x_base + 11, 24), 10, h_b, boxstyle="round,pad=0.2,rounding_size=1",
                                     facecolor='#059669', edgecolor='#facc15' if is_hl_b else 'none',
                                     linewidth=2.5 if is_hl_b else 0)
        ax.add_patch(b_b)
        ax.text(x_base + 16, 24 + h_b + 2, str(vals_b[i]), color='#6ee7b7', fontsize=9.5, fontweight='bold', ha='center')
        
        # Etiqueta snack
        ax.text(x_base + 10.5, 19, snacks[i], color='#cbd5e1', fontsize=9, fontweight='bold', ha='center')

def gen_q19():
    fig, ax = create_canvas("MERIENDAS 3°A: POBLACIÓN TOTAL", "TALLER 4: COMPARACIÓN",
                           "Grado 3°A: Población total = 26 estudiantes encuestados.",
                           "Suma de frecuencias de 3°A: 12 (Bollo) + 6 (Carimañola) + 8 (Arepa) = 26.",
                           badge_color='#3b82f6', foot_color='#3b82f6')
    draw_dual_classroom_chart(ax, highlight_salon='A')
    save_fig(fig, 19)

def gen_q20():
    fig, ax = create_canvas("MERIENDAS 3°B: POBLACIÓN TOTAL", "TALLER 4: COMPARACIÓN",
                           "Grado 3°B: Población total = 30 estudiantes encuestados.",
                           "Suma de frecuencias de 3°B: 5 (Bollo) + 15 (Carimañola) + 10 (Arepa) = 30.",
                           badge_color='#10b981', foot_color='#10b981')
    draw_dual_classroom_chart(ax, highlight_salon='B')
    save_fig(fig, 20)

def gen_q21():
    fig, ax = create_canvas("MODA DE MERIENDA EN GRADO 3°A", "TALLER 4: COMPARACIÓN",
                           "La MODA en 3°A es el Bollo de Mazorca con 12 preferencias.",
                           "Es el dato con mayor frecuencia absoluta dentro del salón 3°A.",
                           badge_color='#f59e0b', foot_color='#f59e0b')
    draw_dual_classroom_chart(ax, highlight_item=0, highlight_salon='A')
    ax.text(19, 65, "MODA 3°A (12)", color='#fde047', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 21)

def gen_q22():
    fig, ax = create_canvas("MODA DE MERIENDA EN GRADO 3°B", "TALLER 4: COMPARACIÓN",
                           "La MODA en 3°B es la Carimañola con 15 preferencias.",
                           "Es el dato con mayor frecuencia absoluta dentro del salón 3°B.",
                           badge_color='#10b981', foot_color='#10b981')
    draw_dual_classroom_chart(ax, highlight_item=1, highlight_salon='B')
    ax.text(58, 71, "MODA 3°B (15)", color='#fde047', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 22)

def gen_q23():
    fig, ax = create_canvas("COMPARACIÓN: AREPA DE HUEVO (3°A vs 3°B)", "TALLER 4: COMPARACIÓN",
                           "Arepa de Huevo: Mayor preferencia en 3°B con 10 votos frente a 8 en 3°A.",
                           "Diferencia de frecuencias: 10 - 8 = 2 unidades de ventaja a favor de 3°B.",
                           badge_color='#f59e0b', foot_color='#f59e0b')
    draw_dual_classroom_chart(ax, highlight_item=2, highlight_salon='BOTH')
    ax.text(79, 60, "10 - 8 = 2 VOTOS\nA FAVOR DE 3°B", color='#fde047', fontsize=9, fontweight='bold', ha='center')
    save_fig(fig, 23)

def gen_q24():
    fig, ax = create_canvas("COMPARACIÓN: BOLLO DE MAZORCA (3°A vs 3°B)", "TALLER 4: COMPARACIÓN",
                           "Bollo de Mazorca: Mayor preferencia en 3°A con 12 votos frente a 5 en 3°B.",
                           "Diferencia de frecuencias: 12 - 5 = 7 unidades de ventaja a favor de 3°A.",
                           badge_color='#3b82f6', foot_color='#3b82f6')
    draw_dual_classroom_chart(ax, highlight_item=0, highlight_salon='BOTH')
    ax.text(25, 64, "12 - 5 = 7 VOTOS\nA FAVOR DE 3°A", color='#93c5fd', fontsize=9, fontweight='bold', ha='center')
    save_fig(fig, 24)

def gen_q25():
    fig, ax = create_canvas("COMPARACIÓN: CARIMAÑOLA (3°A vs 3°B)", "TALLER 4: COMPARACIÓN",
                           "Carimañola: 3°B tiene 15 votos y 3°A tiene 6 votos.",
                           "Diferencia de frecuencias: 15 - 6 = 9 unidades a favor de 3°B.",
                           badge_color='#10b981', foot_color='#10b981')
    draw_dual_classroom_chart(ax, highlight_item=1, highlight_salon='BOTH')
    ax.text(53, 71, "15 - 6 = 9 VOTOS\nA FAVOR DE 3°B", color='#6ee7b7', fontsize=9, fontweight='bold', ha='center')
    save_fig(fig, 25)

def gen_q26():
    fig, ax = create_canvas("POBLACIÓN TOTAL COMBINADA (3°A + 3°B)", "TALLER 4: COMPARACIÓN",
                           "Población total combinada = 56 estudiantes en total.",
                           "Suma técnica: 26 (alumnos de 3°A) + 30 (alumnos de 3°B) = 56 estudiantes.",
                           badge_color='#8b5cf6', foot_color='#8b5cf6')
    b1 = patches.FancyBboxPatch((12, 28), 34, 46, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e3a8a', edgecolor='#3b82f6', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 28), 34, 46, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#064e3b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(29, 60, "SALÓN 3°A", color='#93c5fd', fontsize=12, fontweight='bold', ha='center')
    ax.text(29, 42, "26", color='#ffffff', fontsize=26, fontweight='bold', ha='center')
    ax.text(29, 33, "estudiantes", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(71, 60, "SALÓN 3°B", color='#6ee7b7', fontsize=12, fontweight='bold', ha='center')
    ax.text(71, 42, "30", color='#ffffff', fontsize=26, fontweight='bold', ha='center')
    ax.text(71, 33, "estudiantes", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(49, 51, "+", color='#facc15', fontsize=24, fontweight='bold', ha='center', va='center')
    save_fig(fig, 26)

def gen_q27():
    fig, ax = create_canvas("TOTAL COMBINADO DE CARIMAÑOLA", "TALLER 4: COMPARACIÓN",
                           "Total de Carimañola = 21 estudiantes en ambos salones.",
                           "Suma de frecuencias: 6 (votos de 3°A) + 15 (votos de 3°B) = 21 estudiantes.",
                           badge_color='#10b981', foot_color='#10b981')
    b1 = patches.FancyBboxPatch((15, 28), 30, 44, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
    b2 = patches.FancyBboxPatch((55, 28), 30, 44, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(30, 58, "Carimañola 3°A", color='#93c5fd', fontsize=10, fontweight='bold', ha='center')
    ax.text(30, 42, "6", color='#ffffff', fontsize=24, fontweight='bold', ha='center')
    ax.text(70, 58, "Carimañola 3°B", color='#6ee7b7', fontsize=10, fontweight='bold', ha='center')
    ax.text(70, 42, "15", color='#ffffff', fontsize=24, fontweight='bold', ha='center')
    ax.text(50, 48, "+", color='#facc15', fontsize=22, fontweight='bold', ha='center')
    save_fig(fig, 27)

def gen_q28():
    fig, ax = create_canvas("MERIENDA GANADORA EN AMBOS SALONES", "TALLER 4: COMPARACIÓN",
                           "Merienda con más votos acumulados: Carimañola con 21 votos.",
                           "Consolidado general: Carimañola (21) > Arepa de Huevo (18) > Bollo de Mazorca (17).",
                           badge_color='#eab308', foot_color='#eab308')
    totals = [
        ("Carimañola", 21, "#eab308", True, "21 VOTOS (GANADORA)"),
        ("Arepa Huevo", 18, "#38bdf8", False, "18 votos"),
        ("Bollo Mazorca", 17, "#f59e0b", False, "17 votos")
    ]
    for i, (name, val, col, is_win, lbl) in enumerate(totals):
        x = 16 + i * 26
        w = 18
        h = val * 2.2
        b = patches.FancyBboxPatch((x, 24), w, h, boxstyle="round,pad=0.3,rounding_size=2",
                                   facecolor=col, edgecolor='#ffffff' if is_win else 'none',
                                   linewidth=2.5 if is_win else 0)
        ax.add_patch(b)
        ax.text(x + w/2, 24 + h + 2.5, lbl, color='#ffffff' if not is_win else '#fef08a', fontsize=9.5, fontweight='bold', ha='center')
        ax.text(x + w/2, 19, name, color='#cbd5e1', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 28)

def gen_q29():
    fig, ax = create_canvas("¿POR QUÉ ANALIZAR DOS TABLAS A LA VEZ?", "TALLER 4: COMPARACIÓN",
                           "Comparar salones exige consultar ambas tablas simultáneamente.",
                           "Ejemplo: Para saber en cuál de los dos salones gustó más la Arepa de Huevo.",
                           badge_color='#38bdf8', foot_color='#38bdf8')
    t1 = patches.FancyBboxPatch((8, 25), 38, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
    t2 = patches.FancyBboxPatch((54, 25), 38, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(t1)
    ax.add_patch(t2)
    ax.text(27, 65, "TABLA 1: GRADO 3°A", color='#93c5fd', fontsize=10, fontweight='bold', ha='center')
    ax.text(27, 45, "Arepa de Huevo = 8\nBollo = 12\nCarimañola = 6", color='#f8fafc', fontsize=9.5, ha='center')
    
    ax.text(73, 65, "TABLA 2: GRADO 3°B", color='#6ee7b7', fontsize=10, fontweight='bold', ha='center')
    ax.text(73, 45, "Arepa de Huevo = 10\nBollo = 5\nCarimañola = 15", color='#f8fafc', fontsize=9.5, ha='center')
    
    ax.annotate("", xy=(52, 49), xytext=(48, 49), arrowprops=dict(arrowstyle="<->", color='#facc15', lw=3))
    save_fig(fig, 29)

def gen_q30():
    fig, ax = create_canvas("RECOMENDACIÓN TÉCNICA PARA LA COOPERATIVA", "TALLER 4: COMPARACIÓN",
                           "Sugerencia basada en la MODA y FRECUENCIA ABSOLUTA de cada salón.",
                           "Para 3°A priorizar Bollo de Mazorca (12) y para 3°B Carimañola (15).",
                           badge_color='#10b981', foot_color='#10b981')
    c1 = patches.FancyBboxPatch((8, 24), 40, 52, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e3a8a', edgecolor='#60a5fa', linewidth=2)
    c2 = patches.FancyBboxPatch((52, 24), 40, 52, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#064e3b', edgecolor='#34d399', linewidth=2)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(28, 67, "RECOMENDACIÓN 3°A", color='#bfdbfe', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 52, "BOLLO DE MAZORCA", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 38, "Moda del salón\ncon 12 votos (46.1%)", color='#93c5fd', fontsize=9, ha='center')
    
    ax.text(72, 67, "RECOMENDACIÓN 3°B", color='#bbf7d0', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 52, "CARIMAÑOLA", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 38, "Moda del salón\ncon 15 votos (50.0%)", color='#86efac', fontsize=9, ha='center')
    save_fig(fig, 30)

def gen_q42():
    fig, ax = create_canvas("COMPARACIÓN DE PARTICIPANTES (3°A vs 3°B)", "TALLER 4: COMPARACIÓN",
                           "Grado 3°B tuvo mayor cantidad de participantes en la encuesta.",
                           "Diferencia: 30 (estudiantes 3°B) - 26 (estudiantes 3°A) = 4 estudiantes más.",
                           badge_color='#06b6d4', foot_color='#06b6d4')
    b1 = patches.FancyBboxPatch((15, 26), 30, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e3a8a', edgecolor='#3b82f6', linewidth=2)
    b2 = patches.FancyBboxPatch((55, 26), 30, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#064e3b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(30, 64, "GRADO 3°A", color='#93c5fd', fontsize=12, fontweight='bold', ha='center')
    ax.text(30, 44, "26", color='#ffffff', fontsize=28, fontweight='bold', ha='center')
    ax.text(30, 32, "participantes", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(70, 64, "GRADO 3°B", color='#6ee7b7', fontsize=12, fontweight='bold', ha='center')
    ax.text(70, 44, "30", color='#ffffff', fontsize=28, fontweight='bold', ha='center')
    ax.text(70, 32, "MAYOR PARTICIPACIÓN", color='#fef08a', fontsize=9, fontweight='bold', ha='center')
    save_fig(fig, 42)


# ==============================================================================
# 5. GENERADORES TALLER 5: BEBIDAS RONDA DEL SINÚ (Q31 a Q40)
# ==============================================================================

def draw_beverages_bars(ax, highlight_item=None):
    """
    Dibuja gráfico de bebidas de la Ronda del Sinú:
    Agua de Coco=25, Guarapo con Limón=20, Chicha de Maíz=15, Jugo de Níspero=10.
    Total = 70.
    """
    drinks = [
        ("Agua de Coco", 25, "#10b981", "25 votos"),
        ("Guarapo Limón", 20, "#eab308", "20 votos"),
        ("Chicha Maíz", 15, "#f97316", "15 votos"),
        ("Jugo Níspero", 10, "#8b5cf6", "10 votos")
    ]
    for i, (name, val, col, lbl) in enumerate(drinks):
        x = 9 + i * 22
        w = 16
        h = val * 1.9
        is_hl = (highlight_item == i)
        b = patches.FancyBboxPatch((x, 24), w, h, boxstyle="round,pad=0.3,rounding_size=2",
                                   facecolor=col, edgecolor='#ffffff' if is_hl else 'none',
                                   linewidth=2.5 if is_hl else 0)
        ax.add_patch(b)
        ax.text(x + w/2, 24 + h + 2.5, lbl, color='#ffffff', fontsize=9.5, fontweight='bold', ha='center')
        ax.text(x + w/2, 19, name, color='#cbd5e1', fontsize=9, fontweight='bold', ha='center')

def gen_q31():
    fig, ax = create_canvas("BEBIDAS RONDA DEL SINÚ: TOTAL POBLACIÓN", "TALLER 5: CONCLUSIONES",
                           "Población total estudiada = 70 personas encuestadas.",
                           "Suma de frecuencias: 25 (Coco) + 20 (Guarapo) + 15 (Chicha) + 10 (Níspero) = 70.",
                           badge_color='#10b981', foot_color='#10b981')
    draw_beverages_bars(ax)
    callout = patches.FancyBboxPatch((10, 68), 80, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#064e3b', edgecolor='#34d399', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 73.5, "TOTAL ENCUESTADOS: 25 + 20 + 15 + 10 = 70 PERSONAS", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 31)

def gen_q32():
    fig, ax = create_canvas("BEBIDAS RONDA DEL SINÚ: LA VARIABLE", "TALLER 5: CONCLUSIONES",
                           "Variable cualitativa nominal: 'Bebida refrescante tradicional preferida'.",
                           "Agua de Coco, Guarapo, Chicha y Níspero son categorías cualitativas sin orden.",
                           badge_color='#38bdf8', foot_color='#38bdf8')
    draw_beverages_bars(ax)
    callout = patches.FancyBboxPatch((10, 68), 80, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 73.5, "VARIABLE NOMINAL: Bebida refrescante tradicional preferida", color='#f8fafc', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 32)

def gen_q33():
    fig, ax = create_canvas("BEBIDAS: MENOR PREFERENCIA (MÍNIMO)", "TALLER 5: CONCLUSIONES",
                           "Jugo de Níspero tiene la MENOR preferencia con 10 personas.",
                           "Registró la frecuencia absoluta más baja de todo el estudio.",
                           badge_color='#8b5cf6', foot_color='#8b5cf6')
    draw_beverages_bars(ax, highlight_item=3)
    ax.text(83, 52, "MENOR (10)", color='#c084fc', fontsize=11, fontweight='bold', ha='center')
    save_fig(fig, 33)

def gen_q34():
    fig, ax = create_canvas("BEBIDAS: LA MODA ESTADÍSTICA", "TALLER 5: CONCLUSIONES",
                           "LA MODA es Agua de Coco con 25 votos de preferencia.",
                           "Es la bebida tradicional con la MÁXIMA frecuencia absoluta (barra más alta).",
                           badge_color='#eab308', foot_color='#eab308')
    draw_beverages_bars(ax, highlight_item=0)
    ax.text(17, 76, "MODA (25)", color='#facc15', fontsize=12, fontweight='bold', ha='center')
    save_fig(fig, 34)

def gen_q35():
    fig, ax = create_canvas("DIFERENCIA: AGUA DE COCO VS NÍSPERO", "TALLER 5: CONCLUSIONES",
                           "Agua de Coco (25) supera a Jugo de Níspero (10) por 15 personas.",
                           "Resta matemática: 25 - 10 = 15 personas de diferencia.",
                           badge_color='#ec4899', foot_color='#ec4899')
    draw_beverages_bars(ax)
    callout = patches.FancyBboxPatch((12, 68), 76, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#831843', edgecolor='#f43f5e', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 73.5, "RESTA: 25 (Agua de Coco) - 10 (Jugo Níspero) = 15 PERSONAS", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 35)

def gen_q36():
    fig, ax = create_canvas("FRECUENCIA DE GUARAPO CON LIMÓN", "TALLER 5: CONCLUSIONES",
                           "Frecuencia absoluta de Guarapo con Limón = 20 personas.",
                           "20 personas de las 70 encuestadas eligieron esta refrescante bebida tradicional.",
                           badge_color='#eab308', foot_color='#eab308')
    draw_beverages_bars(ax, highlight_item=1)
    ax.text(39, 68, "f = 20 PERSONAS", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    save_fig(fig, 36)

def gen_q37():
    fig, ax = create_canvas("SUMA: CHICHA DE MAÍZ + GUARAPO CON LIMÓN", "TALLER 5: CONCLUSIONES",
                           "Chicha de Maíz (15) + Guarapo con Limón (20) = 35 personas en total.",
                           "Suma combinada: 15 + 20 = 35 personas prefieren alguna de estas dos bebidas.",
                           badge_color='#f97316', foot_color='#f97316')
    draw_beverages_bars(ax, highlight_item=1)
    callout = patches.FancyBboxPatch((12, 68), 76, 11, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#431407', edgecolor='#f97316', linewidth=2)
    ax.add_patch(callout)
    ax.text(50, 73.5, "SUMA COMBINADA: 15 (Chicha) + 20 (Guarapo) = 35 PERSONAS", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    save_fig(fig, 37)

def gen_q38():
    fig, ax = create_canvas("ESTRUCTURA DE UNA CONCLUSIÓN CIENTÍFICA", "TALLER 5: CONCLUSIONES",
                           "Redacción formal: Sustentada con conceptos técnicos y datos numéricos.",
                           "Ejemplo: 'La moda de la muestra corresponde al Agua de Coco al alcanzar 25 preferencias'.",
                           badge_color='#10b981', foot_color='#10b981')
    parts = [
        ("1. CONCEPTO TÉCNICO", "La moda de la muestra...", 18, "#3b82f6"),
        ("2. CATEGORÍA GANADORA", "...corresponde al Agua de Coco...", 50, "#10b981"),
        ("3. SUSTENTO NUMÉRICO", "...con 25 preferencias (máxima frecuencia).", 82, "#f59e0b")
    ]
    for title, desc, cx, col in parts:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 67, title, color=col, fontsize=8.5, fontweight='bold', ha='center')
        ax.text(cx, 46, desc, color='#f8fafc', fontsize=10, fontweight='bold', ha='center', va='center')
    save_fig(fig, 38)

def gen_q39():
    fig, ax = create_canvas("RIGOR CIENTÍFICO EN ESTADÍSTICA", "TALLER 5: CONCLUSIONES",
                           "El taller prohíbe el lenguaje subjetivo o infantil en los informes.",
                           "Se deben utilizar términos estadísticos objetivos fundamentados en frecuencias.",
                           badge_color='#ef4444', foot_color='#ef4444')
    # Lado Izquierdo: Incorrecto
    p_bad = patches.FancyBboxPatch((6, 23), 42, 54, boxstyle="round,pad=0.5,rounding_size=2",
                                   facecolor='#2a1215', edgecolor='#ef4444', linewidth=2)
    ax.add_patch(p_bad)
    ax.text(27, 70, "EXPRESIONES NO VÁLIDAS", color='#ef4444', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(27, 62, "Apreciaciones Subjetivas", color='#fca5a5', fontsize=8.5, ha='center')
    ax.text(27, 46, "• 'El coco es muy rico'\n• 'Ganó el agua porque me gusta'\n• 'El níspero es feo'", color='#ffffff', fontsize=9.5, ha='center')
    ax.text(27, 28, "Carecen de rigor numérico", color='#ef4444', fontsize=8, fontweight='bold', ha='center')
    
    # Lado Derecho: Correcto
    p_good = patches.FancyBboxPatch((52, 23), 42, 54, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#09231b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(p_good)
    ax.text(73, 70, "EXPRESIÓN FORMAL VÁLIDA", color='#34d399', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(73, 62, "Sustento Técnico Formal", color='#a7f3d0', fontsize=8.5, ha='center')
    ax.text(73, 46, "• 'El Agua de Coco representa la\nmoda al obtener la mayor frecuencia\nabsoluta con 25 votos'", color='#ffffff', fontsize=9.5, ha='center')
    ax.text(73, 28, "Basado en datos y conceptos", color='#34d399', fontsize=8, fontweight='bold', ha='center')
    save_fig(fig, 39)

def gen_q40():
    fig, ax = create_canvas("DECISIÓN COMERCIAL CON DATOS", "TALLER 5: CONCLUSIONES",
                           "Decisión: Abastecer principalmente Agua de Coco (25) y Guarapo (20).",
                           "Los vendedores usan la moda y frecuencias para asegurar los refrescos más demandados.",
                           badge_color='#10b981', foot_color='#10b981')
    p1 = patches.FancyBboxPatch((10, 24), 38, 52, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    p2 = patches.FancyBboxPatch((52, 24), 38, 52, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#eab308', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(29, 67, "PRIORIDAD #1: MODA", color='#34d399', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(29, 52, "AGUA DE COCO", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(29, 36, "Frecuencia: 25 personas\n(Mayor demanda asegurada)", color='#93c5fd', fontsize=9, ha='center')
    
    ax.text(71, 67, "PRIORIDAD #2: SEGUNDO LUGAR", color='#fde047', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(71, 52, "GUARAPO CON LIMÓN", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(71, 36, "Frecuencia: 20 personas\n(Segunda bebida más pedida)", color='#fef08a', fontsize=9, ha='center')
    save_fig(fig, 40)

# ==============================================================================
# EJECUCIÓN PRINCIPAL: GENERAR LAS 42 IMÁGENES
# ==============================================================================
def main():
    print("Iniciando generación de 42 imágenes estadísticas personalizadas...")
    generators = [
        gen_q01, gen_q02, gen_q03, gen_q04, gen_q05, gen_q06, gen_q07, gen_q08,
        gen_q09, gen_q10, gen_q11, gen_q12, gen_q13, gen_q14,
        gen_q15, gen_q16, gen_q17, gen_q18,
        gen_q19, gen_q20, gen_q21, gen_q22, gen_q23, gen_q24, gen_q25, gen_q26, gen_q27, gen_q28, gen_q29, gen_q30,
        gen_q31, gen_q32, gen_q33, gen_q34, gen_q35, gen_q36, gen_q37, gen_q38, gen_q39, gen_q40,
        gen_q41, gen_q42
    ]
    for idx, fn in enumerate(generators, 1):
        fn()
    print("¡Todas las 42 imágenes han sido generadas exitosamente!")

if __name__ == '__main__':
    main()
