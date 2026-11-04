"""
Generador automático de gráficos e ilustraciones geométricas para niños de 3° de primaria.
Crea 40 imágenes de alta resolución (q01.png a q40.png) para la materia de Geometría.
Compatible 100% con Windows y Linux (AWS).
"""

import os
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Rutas de salida
OUT_DIRS = [
    os.path.abspath('app/static/img/questions_geo'),
    os.path.abspath('static/img/questions_geo')
]
for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

def create_geo_canvas(title, category, foot_title, foot_sub="", badge_color='#3b82f6', foot_color='#38bdf8'):
    """Crea la base de la tarjeta geométrica con estilo oscuro y bordes redondeados."""
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

def save_geo_fig(fig, qid):
    """Guarda la figura en todas las carpetas destino."""
    filename = f"q{qid:02d}.png"
    plt.tight_layout()
    for d in OUT_DIRS:
        target = os.path.join(d, filename)
        plt.savefig(target, facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
    print(f"[OK] Guardado Geometria: {filename}")


# ==============================================================================
# TALLER 1: HERRAMIENTAS NO ESTANDARIZADAS Y LONGITUD (Q01 a Q10)
# ==============================================================================

def gen_geo_01():
    fig, ax = create_geo_canvas("¿QUÉ ES LA LONGITUD EN GEOMETRÍA?", "TALLER 1: SEMANA 15",
                                "LONGITUD: Magnitud física que expresa la distancia recta entre dos puntos.",
                                "Permite saber qué tan largo, ancho o alto es un objeto o recorrido.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    # Dos puntos con flecha de distancia
    ax.plot([20, 80], [50, 50], color='#38bdf8', linewidth=4, zorder=2)
    p1 = patches.Circle((20, 50), 3.5, facecolor='#ef4444', edgecolor='#ffffff', linewidth=2, zorder=3)
    p2 = patches.Circle((80, 50), 3.5, facecolor='#10b981', edgecolor='#ffffff', linewidth=2, zorder=3)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(20, 40, "PUNTO A\n(Inicio)", color='#fca5a5', fontsize=10, fontweight='bold', ha='center')
    ax.text(80, 40, "PUNTO B\n(Final)", color='#86efac', fontsize=10, fontweight='bold', ha='center')
    
    # Cartel central
    tag = patches.FancyBboxPatch((35, 57), 30, 15, boxstyle="round,pad=0.4,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 66, "DISTANCIA ENTRE A Y B", color='#93c5fd', fontsize=9, fontweight='bold', ha='center')
    ax.text(50, 59.5, "= LONGITUD", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    save_geo_fig(fig, 1)

def gen_geo_02():
    fig, ax = create_geo_canvas("PATRÓN DE MEDIDA: LA CUARTA", "TALLER 1: SEMANA 15",
                                "LA CUARTA: Medida de la mano extendida desde la punta del pulgar al meñique.",
                                "Es un patrón no estandarizado porque el tamaño de la mano varía entre personas.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    # Dibujo esquemático de mano extendida
    card = patches.FancyBboxPatch((15, 23), 70, 53, boxstyle="round,pad=0.5,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(card)
    ax.text(50, 68, "MANO EXTENDIDA AL MÁXIMO", color='#fef08a', fontsize=12, fontweight='bold', ha='center')
    
    # Flecha de cuarta
    ax.annotate("", xy=(75, 45), xytext=(25, 45),
                arrowprops=dict(arrowstyle="<->", color='#f59e0b', lw=3.5))
    ax.text(25, 34, "DEDO PULGAR\n(Punto inicial)", color='#fde047', fontsize=10, fontweight='bold', ha='center')
    ax.text(75, 34, "DEDO MEÑIQUE\n(Punto final)", color='#fde047', fontsize=10, fontweight='bold', ha='center')
    ax.text(50, 49, "1 CUARTA COMPLETA", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    save_geo_fig(fig, 2)

def gen_geo_03():
    fig, ax = create_geo_canvas("TÉCNICA CONSECUTIVA: RALLY DE LA CUARTA", "TALLER 1: SEMANA 15",
                                "TÉCNICA CORRECTA: Unir el meñique con el pulgar siguiente sin dejar espacios.",
                                "Así se evita la dispersión y se garantiza una medición continua y ordenada.",
                                badge_color='#10b981', foot_color='#10b981')
    # 3 Cuartas consecutivas
    colors = ['#3b82f6', '#10b981', '#f59e0b']
    for i in range(3):
        x = 10 + i * 27
        bx = patches.FancyBboxPatch((x, 30), 24, 38, boxstyle="round,pad=0.4,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=colors[i], linewidth=2)
        ax.add_patch(bx)
        ax.text(x+12, 59, f"CUARTA {i+1}", color=colors[i], fontsize=11, fontweight='bold', ha='center')
        ax.text(x+4, 46, "Pulgar", color='#cbd5e1', fontsize=8.5, ha='center')
        ax.text(x+20, 46, "Meñique", color='#cbd5e1', fontsize=8.5, ha='center')
        ax.annotate("", xy=(x+20, 38), xytext=(x+4, 38), arrowprops=dict(arrowstyle="->", color=colors[i], lw=2))
        
        if i < 2:
            ax.text(x+25.5, 48, "=", color='#ffffff', fontsize=14, fontweight='bold', ha='center')
            ax.text(x+25.5, 25, "Unión exacta\nsin huecos", color='#a7f3d0', fontsize=7.5, ha='center')
    save_geo_fig(fig, 3)

def gen_geo_04():
    fig, ax = create_geo_canvas("SITUACIÓN SABER: JUAN Y MARÍA (LA PUERTA)", "TALLER 1: SEMANA 15",
                                "Juan = 6 cuartas | María = 8 cuartas en la MISMA puerta del aula.",
                                "Razón: La cuarta varía con el tamaño de la mano de cada persona (patrón arbitrario).",
                                badge_color='#ec4899', foot_color='#ec4899')
    # Puerta al centro
    door = patches.Rectangle((40, 24), 20, 52, facecolor='#334155', edgecolor='#f8fafc', linewidth=2)
    ax.add_patch(door)
    ax.text(50, 66, "PUERTA\nDEL AULA", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.plot([43, 43], [48, 52], color='#facc15', linewidth=3) # picaporte
    
    # Juan a la izquierda
    b_juan = patches.FancyBboxPatch((6, 26), 28, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                    facecolor='#1e3a8a', edgecolor='#3b82f6', linewidth=2)
    ax.add_patch(b_juan)
    ax.text(20, 63, "JUAN", color='#93c5fd', fontsize=12, fontweight='bold', ha='center')
    ax.text(20, 48, "6 cuartas", color='#ffffff', fontsize=16, fontweight='bold', ha='center')
    ax.text(20, 35, "Mano más grande\n(necesita menos)", color='#bfdbfe', fontsize=8.5, ha='center')
    
    # María a la derecha
    b_maria = patches.FancyBboxPatch((66, 26), 28, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#831843', edgecolor='#ec4899', linewidth=2)
    ax.add_patch(b_maria)
    ax.text(80, 63, "MARÍA", color='#fbcfe8', fontsize=12, fontweight='bold', ha='center')
    ax.text(80, 48, "8 cuartas", color='#ffffff', fontsize=16, fontweight='bold', ha='center')
    ax.text(80, 35, "Mano más pequeña\n(necesita más)", color='#fce7f3', fontsize=8.5, ha='center')
    save_geo_fig(fig, 4)

def gen_geo_05():
    fig, ax = create_geo_canvas("PATRONES ARBITRARIOS (NO ESTANDARIZADOS)", "TALLER 1: SEMANA 15",
                                "PATRÓN ARBITRARIO: Unidad que varía entre personas o no tiene medida fija.",
                                "Ejemplos corporales: Pasos, Cuartas, Pulgares, Brazadas.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    items = [
        ("✋ LA CUARTA", "Mano extendida\n(Varía con la mano)", 18, "#3b82f6"),
        ("👣 LOS PASOS", "Pisadas al caminar\n(Varía con la zancada)", 50, "#10b981"),
        ("👍 EL PULGAR", "Ancho del dedo\n(Varía con la edad)", 82, "#f59e0b")
    ]
    for title, desc, cx, col in items:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, title, color=col, fontsize=10.5, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=10, ha='center', va='center')
        ax.text(cx, 31, "UNIDAD NO FIJA", color='#94a3b8', fontsize=8, fontweight='bold', ha='center')
    save_geo_fig(fig, 5)

def gen_geo_06():
    fig, ax = create_geo_canvas("RELACIÓN INVERSA: TAMAÑO DE MANO Y CUARTAS", "TALLER 1: SEMANA 15",
                                "A mayor tamaño del patrón (mano grande), MENOR número de cuartas se necesitan.",
                                "Juan (mano grande) = 6 cuartas. María (mano pequeña) = 8 cuartas.",
                                badge_color='#8b5cf6', foot_color='#8b5cf6')
    b1 = patches.FancyBboxPatch((8, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
    b2 = patches.FancyBboxPatch((52, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#ec4899', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 66, "MANO DE JUAN", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 52, "🖐️ MÁS GRANDE", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(28, 38, "Ocupa más espacio,\npor eso solo cuenta 6 cuartas", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(72, 66, "MANO DE MARÍA", color='#fbcfe8', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 52, "🖐️ MÁS PEQUEÑA", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(72, 38, "Ocupa menos espacio,\npor eso necesita 8 cuartas", color='#cbd5e1', fontsize=9, ha='center')
    save_geo_fig(fig, 6)

def gen_geo_07():
    fig, ax = create_geo_canvas("MEDICIÓN CON PASOS: PATIO ESCOLAR", "TALLER 1: SEMANA 15",
                                "PASOS FIRMES Y RECTOS: Se camina en línea recta sin saltos para mantener la medida.",
                                "Adecuado para distancias grandes en el entorno escolar.",
                                badge_color='#10b981', foot_color='#10b981')
    # Ruta de pasos
    for i in range(6):
        x = 10 + i * 14
        foot = patches.FancyBboxPatch((x, 42), 9, 18, boxstyle="round,pad=0.2,rounding_size=1",
                                      facecolor='#059669', edgecolor='#34d399', linewidth=1.5)
        ax.add_patch(foot)
        ax.text(x+4.5, 51, f"{i+1}", color='#ffffff', fontsize=11, fontweight='bold', ha='center', va='center')
    
    ax.text(12, 68, "PUERTA DEL AULA", color='#93c5fd', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(88, 68, "PATIO ESCOLAR", color='#fde047', fontsize=9.5, fontweight='bold', ha='center')
    ax.annotate("", xy=(90, 51), xytext=(5, 51), arrowprops=dict(arrowstyle="->", color='#ffffff', lw=2))
    save_geo_fig(fig, 7)

def gen_geo_08():
    fig, ax = create_geo_canvas("DIAGRAMA DE CONTEO: PUERTA AL TABLERO", "TALLER 1: SEMANA 15",
                                "Del salón a la pizarra = 8 pasos lineales exactos.",
                                "Cada pisada firme representa una unidad lineal en el recorrido.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    # 8 pisadas numeradas
    for i in range(8):
        x = 6 + i * 11
        bx = patches.FancyBboxPatch((x, 38), 8.5, 22, boxstyle="round,pad=0.2,rounding_size=1",
                                    facecolor='#1e293b', edgecolor='#38bdf8', linewidth=1.5)
        ax.add_patch(bx)
        ax.text(x+4.25, 49, f"Paso\n{i+1}", color='#f8fafc', fontsize=8.5, fontweight='bold', ha='center', va='center')
    
    ax.text(10, 68, "🚪 PUERTA", color='#cbd5e1', fontsize=10, fontweight='bold', ha='center')
    ax.text(88, 68, "📋 TABLERO", color='#a7f3d0', fontsize=10, fontweight='bold', ha='center')
    save_geo_fig(fig, 8)

def gen_geo_09():
    fig, ax = create_geo_canvas("PRECISIÓN CON EL PULGAR: ELEMENTOS PEQUEÑOS", "TALLER 1: SEMANA 15",
                                "EL PULGAR: Patrón arbitrario adecuado para objetos cortos del entorno.",
                                "Ejemplos del taller: ramitas secas y hojas de roble recolectadas.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    # Ramita con pulgares
    r_box = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                   facecolor='#1e293b', edgecolor='#854d0e', linewidth=2)
    h_box = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                   facecolor='#1e293b', edgecolor='#15803d', linewidth=2)
    ax.add_patch(r_box)
    ax.add_patch(h_box)
    ax.text(28, 65, "OBJETO A: RAMITA", color='#fed7aa', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 48, "Medida: 5 pulgares", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 35, "Largo medido de punta a punta", color='#cbd5e1', fontsize=8, ha='center')
    
    ax.text(72, 65, "OBJETO B: HOJA", color='#bbf7d0', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 48, "Medida: 3 pulgares", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 35, "Ancho medido de lado a lado", color='#cbd5e1', fontsize=8, ha='center')
    save_geo_fig(fig, 9)

def gen_geo_10():
    fig, ax = create_geo_canvas("¿QUÉ ES LA DISPERSIÓN EN LA MEDICIÓN?", "TALLER 1: SEMANA 15",
                                "DISPERSIÓN: Variación o diferencias en los resultados al usar patrones corporales.",
                                "Para evitar la dispersión se crearon los instrumentos estandarizados como la regla.",
                                badge_color='#ec4899', foot_color='#ec4899')
    c1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
    c2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(28, 65, "CON DISPERSIÓN", color='#fca5a5', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 48, "6 cuartas vs 8 cuartas", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 35, "Resultados distintos para\nel mismo objeto (Varía)", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "SIN DISPERSIÓN", color='#86efac', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 48, "80 cm = 80 cm", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 35, "Con regla graduada,\ntodos obtienen lo mismo", color='#cbd5e1', fontsize=8.5, ha='center')
    save_geo_fig(fig, 10)


# ==============================================================================
# TALLER 2: INSTRUMENTOS ESTANDARIZADOS Y PRECISIÓN (Q11 a Q20)
# ==============================================================================

def draw_ruler(ax, x_start=15, y_start=35, length_cm=10, highlight_start=0, highlight_end=None, obj_name=""):
    """Dibuja una regla escolar graduada en centímetros."""
    w = length_cm * 6.5
    h = 16
    ruler = patches.Rectangle((x_start, y_start), w, h, facecolor='#fef08a', edgecolor='#ca8a04', linewidth=2)
    ax.add_patch(ruler)
    
    for cm in range(length_cm + 1):
        x = x_start + cm * 6.5
        # Marca de cm
        ax.plot([x, x], [y_start + h - 6, y_start + h], color='#000000', linewidth=1.8)
        ax.text(x, y_start + 3, str(cm), color='#000000', fontsize=9, fontweight='bold', ha='center')
        # Milímetros
        if cm < length_cm:
            for mm in range(1, 10):
                x_mm = x + mm * 0.65
                h_mm = 4 if mm == 5 else 2.5
                ax.plot([x_mm, x_mm], [y_start + h - h_mm, y_start + h], color='#713f12', linewidth=0.8)
    
    # Dibujar objeto encima si se especifica
    if highlight_end is not None:
        x_obj_start = x_start + highlight_start * 6.5
        x_obj_end = x_start + highlight_end * 6.5
        w_obj = x_obj_end - x_obj_start
        obj = patches.FancyBboxPatch((x_obj_start, y_start + h + 4), w_obj, 10,
                                     boxstyle="round,pad=0.2,rounding_size=1",
                                     facecolor='#3b82f6', edgecolor='#ffffff', linewidth=1.5)
        ax.add_patch(obj)
        ax.text(x_obj_start + w_obj/2, y_start + h + 9, obj_name, color='#ffffff', fontsize=9, fontweight='bold', ha='center')

def gen_geo_11():
    fig, ax = create_geo_canvas("LA REGLA DE ORO: EL PUNTO CERO (0)", "TALLER 2: SEMANA 17",
                                "REGLA DE ORO: Ubicar siempre el inicio del objeto exactamente en el número 0.",
                                "Si inicias en el 0, el número final donde termina el objeto indica su medida exacta.",
                                badge_color='#10b981', foot_color='#10b981')
    draw_ruler(ax, x_start=18, y_start=30, length_cm=9, highlight_start=0, highlight_end=6, obj_name="LÁPIZ (6 cm)")
    
    # Destacar punto cero con círculo y flecha
    c_zero = patches.Circle((18, 54), 3, facecolor='#ef4444', edgecolor='#ffffff', linewidth=2)
    ax.add_patch(c_zero)
    ax.annotate("¡INICIAR AQUÍ EN EL 0!", xy=(18, 50), xytext=(18, 68),
                arrowprops=dict(arrowstyle="->", color='#f87171', lw=2.5),
                color='#fca5a5', fontsize=9.5, fontweight='bold', ha='center')
    save_geo_fig(fig, 11)

def gen_geo_12():
    fig, ax = create_geo_canvas("SITUACIÓN SABER: EL SACAPUNTAS DE 1 A 4", "TALLER 2: SEMANA 17",
                                "Inició en el 1 y terminó en el 4  ->  Medida real = 4 - 1 = 3 cm.",
                                "¡No mide 4 cm porque no comenzó desde la marca del cero (0)!",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    draw_ruler(ax, x_start=20, y_start=28, length_cm=8, highlight_start=1, highlight_end=4, obj_name="SACAPUNTAS")
    
    # Cartel de resta
    tag = patches.FancyBboxPatch((28, 66), 44, 13, boxstyle="round,pad=0.4,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 74, "CÁLCULO: 4 cm (final) - 1 cm (inicio) = 3 cm", color='#fef08a', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(50, 68.5, "Longitud real = 3 centímetros", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    save_geo_fig(fig, 12)

def gen_geo_13():
    fig, ax = create_geo_canvas("UNIDAD ESTANDARIZADA: EL CENTÍMETRO (cm)", "TALLER 2: SEMANA 17",
                                "CENTÍMETRO (cm): Unidad de medida estándar marcada en la regla escolar.",
                                "Mide exactamente lo mismo en cualquier lugar del mundo.",
                                badge_color='#06b6d4', foot_color='#06b6d4')
    draw_ruler(ax, x_start=20, y_start=34, length_cm=8)
    # Resaltar 1 cm de 0 a 1
    ax.plot([20, 26.5], [56, 56], color='#06b6d4', linewidth=3)
    ax.text(23.25, 62, "1 cm exacto", color='#67e8f9', fontsize=10, fontweight='bold', ha='center')
    save_geo_fig(fig, 13)

def gen_geo_14():
    fig, ax = create_geo_canvas("EQUIVALENCIA FUNDAMENTAL: METRO Y CENTÍMETROS", "TALLER 2: SEMANA 17",
                                "1 METRO (m) = 100 CENTÍMETROS (cm).",
                                "El metro se usa para distancias grandes y el centímetro para objetos cortos.",
                                badge_color='#10b981', foot_color='#10b981')
    b1 = patches.FancyBboxPatch((12, 28), 34, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e3a8a', edgecolor='#3b82f6', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 28), 34, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#064e3b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(29, 61, "UNIDAD UNIVERSAL", color='#93c5fd', fontsize=10, fontweight='bold', ha='center')
    ax.text(29, 46, "1 m", color='#ffffff', fontsize=26, fontweight='bold', ha='center')
    ax.text(29, 34, "1 metro completo", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(71, 61, "EQUIVALENCIA", color='#6ee7b7', fontsize=10, fontweight='bold', ha='center')
    ax.text(71, 46, "100 cm", color='#ffffff', fontsize=26, fontweight='bold', ha='center')
    ax.text(71, 34, "100 centímetros", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(49, 51, "=", color='#facc15', fontsize=28, fontweight='bold', ha='center', va='center')
    save_geo_fig(fig, 14)

def gen_geo_15():
    fig, ax = create_geo_canvas("CRITERIO DE SELECCIÓN: REGLA VS CINTA MÉTRICA", "TALLER 2: SEMANA 17",
                                "REGLA: Instrumento rígido para líneas rectas | CINTA MÉTRICA: Flexible para curvas.",
                                "Para medir la cintura o el tronco de un árbol se elige siempre la cinta métrica.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    p1 = patches.FancyBboxPatch((8, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    p2 = patches.FancyBboxPatch((52, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(28, 66, "REGLA GRADUADA", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 52, "RÍGIDA Y DERECHA", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 36, "• Cuaderno de geometría\n• Lápices y borradores\n• Trazar líneas rectas", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(72, 66, "CINTA MÉTRICA", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 52, "FLEXIBLE (CURVAS)", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 36, "• Cintura de personas\n• Tronco de un árbol\n• Superficies curvas", color='#cbd5e1', fontsize=9, ha='center')
    save_geo_fig(fig, 15)

def gen_geo_16():
    fig, ax = create_geo_canvas("RETO DE TRAZO: LÍNEAS CON MEDIDAS EXACTAS", "TALLER 2: SEMANA 17",
                                "Uso de la regla y lápiz bien tajado para construir bordes y trazos rectos.",
                                "Ejemplos del taller escolar: líneas de 5 cm, 8 cm y 12 cm de longitud.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    lines = [
        ("Línea corta (5 cm)", 5, 62, '#38bdf8'),
        ("Línea mediana (8 cm)", 8, 46, '#10b981'),
        ("Línea larga (12 cm)", 12, 30, '#f59e0b')
    ]
    for lbl, length, y, col in lines:
        ax.plot([15, 15 + length * 5], [y, y], color=col, linewidth=4)
        ax.text(78, y, f"{lbl}  =  {length} cm", color=col, fontsize=10, fontweight='bold', va='center')
    save_geo_fig(fig, 16)

def gen_geo_17():
    fig, ax = create_geo_canvas("LA ESTIMACIÓN: CALCULAR A SIMPLE VISTA", "TALLER 2: SEMANA 17",
                                "ESTIMACIÓN: Proceso mental de proyectar un valor cercano antes de medir.",
                                "Permite anticipar la longitud comparando con referentes conocidos.",
                                badge_color='#8b5cf6', foot_color='#8b5cf6')
    b1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#a855f7', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 65, "1. ESTIMACIÓN", color='#c084fc', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "'Parece de 10 cm'", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 35, "Cálculo mental previo\na simple vista", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "2. MEDIDA REAL", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "'Mide 9 cm'", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 35, "Verificación con regla\n(Medición exacta)", color='#cbd5e1', fontsize=8.5, ha='center')
    save_geo_fig(fig, 17)

def gen_geo_18():
    fig, ax = create_geo_canvas("ERROR DE ESTIMACIÓN: DIFERENCIA NUMÉRICA", "TALLER 2: SEMANA 17",
                                "ERROR DE ESTIMACIÓN = Medida Estimada - Medida Real Verificada.",
                                "Ejemplo: Si estimaste 10 cm y medía 9 cm, el error fue de 1 cm.",
                                badge_color='#ef4444', foot_color='#ef4444')
    tag = patches.FancyBboxPatch((15, 32), 70, 42, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "FÓRMULA DEL ERROR DE ESTIMACIÓN", color='#fca5a5', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "10 cm (Estimado) - 9 cm (Real) = 1 cm", color='#ffffff', fontsize=13, fontweight='bold', ha='center')
    ax.text(50, 39, "Diferencia numérica obtenida al verificar con la regla", color='#cbd5e1', fontsize=9, ha='center')
    save_geo_fig(fig, 18)

def gen_geo_19():
    fig, ax = create_geo_canvas("LÍNEAS PERPENDICULARES: ÁNGULO RECTO (90°)", "TALLER 2: SEMANA 17",
                                "PERPENDICULARES: Dos líneas rectas que se cortan formando una esquina recta (90°).",
                                "Como los bordes de la hoja de tu cuaderno o las esquinas del aula.",
                                badge_color='#10b981', foot_color='#10b981')
    # Trazar dos líneas perpendiculares
    ax.plot([30, 75], [35, 35], color='#38bdf8', linewidth=4)
    ax.plot([45, 45], [25, 75], color='#10b981', linewidth=4)
    # Cuadrito de 90°
    sq = patches.Rectangle((45, 35), 6, 6, facecolor='none', edgecolor='#facc15', linewidth=2)
    ax.add_patch(sq)
    ax.text(58, 48, "ÁNGULO RECTO\n(90°)", color='#fde047', fontsize=10, fontweight='bold')
    save_geo_fig(fig, 19)

def gen_geo_20():
    fig, ax = create_geo_canvas("DIFERENCIA: MARCADOR (12 cm) VS BORRADOR (5 cm)", "TALLER 2: SEMANA 17",
                                "Marcador (12 cm) supera al Borrador (5 cm) por 7 centímetros.",
                                "Resta de longitudes: 12 cm - 5 cm = 7 cm de diferencia.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    # Barra borrador
    b_borrador = patches.FancyBboxPatch((15, 50), 25, 12, boxstyle="round,pad=0.2,rounding_size=1",
                                        facecolor='#ec4899', edgecolor='#f472b6', linewidth=1.5)
    ax.add_patch(b_borrador)
    ax.text(27.5, 56, "Borrador (5 cm)", color='#ffffff', fontsize=9.5, fontweight='bold', ha='center', va='center')
    
    # Barra marcador
    b_marcador = patches.FancyBboxPatch((15, 32), 60, 12, boxstyle="round,pad=0.2,rounding_size=1",
                                        facecolor='#3b82f6', edgecolor='#60a5fa', linewidth=1.5)
    ax.add_patch(b_marcador)
    ax.text(45, 38, "Marcador de Tablero (12 cm)", color='#ffffff', fontsize=9.5, fontweight='bold', ha='center', va='center')
    
    # Diferencia
    ax.plot([40, 75], [56, 56], color='#fde047', linewidth=2, linestyle='--')
    ax.text(57.5, 61, "Diferencia: 12 - 5 = 7 cm", color='#fde047', fontsize=10, fontweight='bold', ha='center')
    save_geo_fig(fig, 20)


# ==============================================================================
# TALLER 3: PERÍMETRO EN CUADRÍCULA (Q21 a Q30)
# ==============================================================================

def draw_grid_shape(ax, x0, y0, cols, rows, cell_size=7, highlight_border=True, show_labels=True):
    """Dibuja una cuadrícula de base y resalta el contorno exterior."""
    # Cuadrícula base tenue
    for r in range(rows + 2):
        for c in range(cols + 2):
            sq = patches.Rectangle((x0 - cell_size + c*cell_size, y0 - cell_size + r*cell_size),
                                   cell_size, cell_size, facecolor='#0f172a', edgecolor='#1e293b', linewidth=0.8)
            ax.add_patch(sq)
            
    # Área de la figura
    fig_w = cols * cell_size
    fig_h = rows * cell_size
    shape = patches.Rectangle((x0, y0), fig_w, fig_h, facecolor='#1e3a8a', edgecolor='none')
    ax.add_patch(shape)
    
    # Líneas internas de la figura en tono suave
    for r in range(1, rows):
        ax.plot([x0, x0 + fig_w], [y0 + r*cell_size, y0 + r*cell_size], color='#3b82f6', linewidth=1, linestyle=':')
    for c in range(1, cols):
        ax.plot([x0 + c*cell_size, x0 + c*cell_size], [y0, y0 + fig_h], color='#3b82f6', linewidth=1, linestyle=':')
        
    # Borde exterior resaltado
    if highlight_border:
        border = patches.Rectangle((x0, y0), fig_w, fig_h, facecolor='none', edgecolor='#10b981', linewidth=3.5)
        ax.add_patch(border)
        
    if show_labels:
        ax.text(x0 + fig_w/2, y0 + fig_h + 3, f"{cols} unidades", color='#86efac', fontsize=10, fontweight='bold', ha='center')
        ax.text(x0 + fig_w/2, y0 - 4, f"{cols} unidades", color='#86efac', fontsize=10, fontweight='bold', ha='center')
        ax.text(x0 - 3, y0 + fig_h/2, f"{rows} u", color='#86efac', fontsize=10, fontweight='bold', ha='right', va='center')
        ax.text(x0 + fig_w + 3, y0 + fig_h/2, f"{rows} u", color='#86efac', fontsize=10, fontweight='bold', ha='left', va='center')

def gen_geo_21():
    fig, ax = create_geo_canvas("¿QUÉ ES EL PERÍMETRO EN GEOMETRÍA?", "TALLER 3: SEMANA 21",
                                "PERÍMETRO: Es la medida de la longitud de todo el contorno exterior de una figura.",
                                "Para calcularlo sumamos la longitud de todos sus lados exteriores.",
                                badge_color='#10b981', foot_color='#10b981')
    draw_grid_shape(ax, x0=32, y0=28, cols=5, rows=4, cell_size=7)
    tag = patches.FancyBboxPatch((70, 40), 24, 25, boxstyle="round,pad=0.3,rounding_size=1.5",
                                 facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(tag)
    ax.text(82, 57, "BORDE EXTERIOR", color='#34d399', fontsize=9, fontweight='bold', ha='center')
    ax.text(82, 46, "Suma de los\n4 lados exteriores", color='#ffffff', fontsize=8.5, ha='center')
    save_geo_fig(fig, 21)

def gen_geo_22():
    fig, ax = create_geo_canvas("CÁLCULO DE PERÍMETRO EN CUADRÍCULA", "TALLER 3: SEMANA 21",
                                "Cada lado de un cuadrito = 1 unidad de longitud lineal.",
                                "Se cuenta segmento por segmento alrededor de toda la figura.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    draw_grid_shape(ax, x0=35, y0=30, cols=4, rows=3, cell_size=8)
    save_geo_fig(fig, 22)

def gen_geo_23():
    fig, ax = create_geo_canvas("¡REGLA TÉCNICA: NO CONTAR LÍNEAS INTERNAS!", "TALLER 3: SEMANA 21",
                                "OJO: Contar únicamente los bordes del contorno exterior.",
                                "Las líneas internas de los cuadritos NO forman parte del perímetro.",
                                badge_color='#ef4444', foot_color='#ef4444')
    draw_grid_shape(ax, x0=18, y0=28, cols=3, rows=2, cell_size=10, show_labels=False)
    
    # Flecha a líneas internas con X
    ax.text(68, 62, "✅ CONTORNO EXTERIOR (VERDE)", color='#34d399', fontsize=9.5, fontweight='bold')
    ax.text(68, 54, "-> Se suman todos los bordes", color='#cbd5e1', fontsize=8.5)
    
    ax.text(68, 42, "❌ LÍNEAS INTERNAS (PUNTADAS)", color='#f87171', fontsize=9.5, fontweight='bold')
    ax.text(68, 34, "-> ¡QUEDA PROHIBIDO CONTARLAS!", color='#fca5a5', fontsize=8.5)
    save_geo_fig(fig, 23)

def gen_geo_24():
    fig, ax = create_geo_canvas("LOCAL DEL MERCADO DEL SUR (3 x 2 CUADRITOS)", "TALLER 3: SEMANA 21",
                                "Perímetro del local rectangular = 3 + 2 + 3 + 2 = 10 unidades lineales.",
                                "3 cuadritos de largo arriba y abajo, y 2 cuadritos de ancho a los lados.",
                                badge_color='#10b981', foot_color='#10b981')
    draw_grid_shape(ax, x0=16, y0=26, cols=3, rows=2, cell_size=11, show_labels=True)
    
    # Tarjeta de suma a la derecha
    calc = patches.FancyBboxPatch((58, 26), 36, 50, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(calc)
    ax.text(76, 68, "PERÍMETRO TOTAL", color='#34d399', fontsize=11, fontweight='bold', ha='center')
    ax.text(76, 54, "Lado 1 (Largo): 3\nLado 2 (Ancho): 2\nLado 3 (Largo): 3\nLado 4 (Ancho): 2", color='#ffffff', fontsize=9.5, ha='center')
    ax.text(76, 35, "= 10 UNIDADES", color='#facc15', fontsize=13, fontweight='bold', ha='center')
    save_geo_fig(fig, 24)

def gen_geo_25():
    fig, ax = create_geo_canvas("SITUACIÓN SABER: PLANCHÓN DEL RÍO SINÚ (4 x 3)", "TALLER 3: SEMANA 21",
                                "Tira de madera en el contorno exterior = Perímetro total.",
                                "Cálculo: 4 + 3 + 4 + 3 = 14 unidades lineales.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    draw_grid_shape(ax, x0=15, y0=25, cols=4, rows=3, cell_size=9, show_labels=True)
    
    calc = patches.FancyBboxPatch((60, 25), 34, 52, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(calc)
    ax.text(77, 68, "PLANCHÓN DEL SINÚ", color='#fde047', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(77, 54, "4 (arriba) + 3 (der)\n+ 4 (abajo) + 3 (izq)", color='#ffffff', fontsize=9.5, ha='center')
    ax.text(77, 36, "= 14 UNIDADES", color='#facc15', fontsize=13, fontweight='bold', ha='center')
    save_geo_fig(fig, 25)

def gen_geo_26():
    fig, ax = create_geo_canvas("FÓRMULA DEL PERÍMETRO DEL RECTÁNGULO", "TALLER 3: SEMANA 21",
                                "PERÍMETRO = Largo + Ancho + Largo + Ancho  (o 2×Largo + 2×Ancho).",
                                "Para el planchón: 4 + 3 + 4 + 3 = 14 unidades lineales.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "FÓRMULA MATEMÁTICA FORMAL", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "P = Lado + Lado + Lado + Lado", color='#ffffff', fontsize=14, fontweight='bold', ha='center')
    ax.text(50, 38, "P = 4 + 3 + 4 + 3 = 14 unidades lineales", color='#facc15', fontsize=12, fontweight='bold', ha='center')
    save_geo_fig(fig, 26)

def gen_geo_27():
    fig, ax = create_geo_canvas("LA LETRA 'M' DE MONTERÍA EN CUADRÍCULA", "TALLER 3: SEMANA 21",
                                "Vértice: Punto o esquina donde se unen dos segmentos de la figura.",
                                "Se recorre el contorno de la letra M contando cada unidad exterior.",
                                badge_color='#ec4899', foot_color='#ec4899')
    # Dibujar la letra M en bloques
    m_pts = [
        (25, 25), (25, 70), (33, 70), (45, 45), (55, 45), (67, 70), (75, 70), (75, 25),
        (67, 25), (67, 52), (58, 35), (42, 35), (33, 52), (33, 25)
    ]
    poly = patches.Polygon(m_pts, closed=True, facecolor='#831843', edgecolor='#f43f5e', linewidth=2.5)
    ax.add_patch(poly)
    
    # Destacar algunos vértices en rojo
    v1 = patches.Circle((25, 70), 2, facecolor='#ef4444', edgecolor='#ffffff')
    v2 = patches.Circle((50, 40), 2, facecolor='#ef4444', edgecolor='#ffffff')
    v3 = patches.Circle((75, 70), 2, facecolor='#ef4444', edgecolor='#ffffff')
    for v in [v1, v2, v3]: ax.add_patch(v)
    ax.text(50, 29, "Vértices (Puntos Rojos)", color='#fca5a5', fontsize=10, fontweight='bold', ha='center')
    save_geo_fig(fig, 27)

def gen_geo_28():
    fig, ax = create_geo_canvas("FIGURA CON LADOS: 2, 4, 2, 4 UNIDADES", "TALLER 3: SEMANA 21",
                                "Perímetro total = 2 + 4 + 2 + 4 = 12 unidades lineales.",
                                "Suma ordenada de los cuatro segmentos que forman el contorno exterior.",
                                badge_color='#8b5cf6', foot_color='#8b5cf6')
    draw_grid_shape(ax, x0=22, y0=28, cols=4, rows=2, cell_size=10, show_labels=True)
    tag = patches.FancyBboxPatch((70, 35), 24, 34, boxstyle="round,pad=0.3,rounding_size=1.5",
                                 facecolor='#1e293b', edgecolor='#a855f7', linewidth=2)
    ax.add_patch(tag)
    ax.text(82, 60, "SUMA TOTAL", color='#c084fc', fontsize=10, fontweight='bold', ha='center')
    ax.text(82, 48, "2 + 4 + 2 + 4", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(82, 39, "= 12 u", color='#facc15', fontsize=12, fontweight='bold', ha='center')
    save_geo_fig(fig, 28)

def gen_geo_29():
    fig, ax = create_geo_canvas("DIFERENCIA ENTRE LONGITUD Y PERÍMETRO", "TALLER 3: SEMANA 21",
                                "LONGITUD: Distancia de UN solo lado | PERÍMETRO: Longitud de TODO el contorno.",
                                "El perímetro es la suma de las longitudes de todos los lados de la figura.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    p1 = patches.FancyBboxPatch((8, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    p2 = patches.FancyBboxPatch((52, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(28, 66, "LONGITUD", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 52, "UN SOLO SEGMENTO", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 38, "Mide qué tan largo es\nun solo lado (ej. 3 u)", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(72, 66, "PERÍMETRO", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 52, "TODO EL CONTORNO", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 38, "Suma las longitudes de\ntodos los lados (ej. 10 u)", color='#cbd5e1', fontsize=9, ha='center')
    save_geo_fig(fig, 29)

def gen_geo_30():
    fig, ax = create_geo_canvas("AMPLIACIÓN DEL LOCAL: 5 x 2 CUADRITOS", "TALLER 3: SEMANA 21",
                                "Nuevo perímetro = 5 (largo) + 2 (ancho) + 5 (largo) + 2 (ancho) = 14 unidades.",
                                "Al aumentar el largo a 5, el contorno exterior aumenta a 14 unidades lineales.",
                                badge_color='#10b981', foot_color='#10b981')
    draw_grid_shape(ax, x0=12, y0=26, cols=5, rows=2, cell_size=9, show_labels=True)
    calc = patches.FancyBboxPatch((66, 26), 28, 50, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(calc)
    ax.text(80, 67, "NUEVO LOCAL", color='#34d399', fontsize=10, fontweight='bold', ha='center')
    ax.text(80, 52, "5 + 2\n+ 5 + 2", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(80, 36, "= 14 u", color='#facc15', fontsize=14, fontweight='bold', ha='center')
    save_geo_fig(fig, 30)


# ==============================================================================
# TALLER 4: POLÍGONOS EN EL GEOPLANO (Q31 a Q40)
# ==============================================================================

def draw_geoplano(ax, x0=20, y0=24, grid_n=5, pin_dist=10, shape_points=None, shape_color='#10b981'):
    """Dibuja un geoplano con pines y bandas elásticas."""
    # Pines del geoplano
    for r in range(grid_n):
        for c in range(grid_n):
            px = x0 + c * pin_dist
            py = y0 + r * pin_dist
            pin = patches.Circle((px, py), 1.2, facecolor='#94a3b8', edgecolor='#ffffff', linewidth=0.5, zorder=3)
            ax.add_patch(pin)
            
    # Si hay figura con banda elástica
    if shape_points:
        pts = [(x0 + c * pin_dist, y0 + r * pin_dist) for (c, r) in shape_points]
        poly = patches.Polygon(pts, closed=True, facecolor=shape_color, alpha=0.35, edgecolor=shape_color, linewidth=3.5, zorder=4)
        ax.add_patch(poly)
        # Resaltar vértices (pines de esquina)
        for pt in pts:
            v = patches.Circle(pt, 2, facecolor='#facc15', edgecolor='#000000', linewidth=1, zorder=5)
            ax.add_patch(v)

def gen_geo_31():
    fig, ax = create_geo_canvas("EL GEOPLANO Y LAS BANDAS ELÁSTICAS", "TALLER 4: SEMANA 23",
                                "GEOPLANO: Tablero de pines o clavos para construir figuras geométricas.",
                                "Las bandas elásticas se estiran entre pines para crear polígonos.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    draw_geoplano(ax, x0=30, y0=25, grid_n=5, pin_dist=10)
    tag = patches.FancyBboxPatch((74, 40), 20, 24, boxstyle="round,pad=0.3,rounding_size=1.5",
                                 facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(tag)
    ax.text(84, 56, "TABLERO DE PINES", color='#93c5fd', fontsize=8.5, fontweight='bold', ha='center')
    ax.text(84, 46, "Construcción de\npolígonos planos", color='#ffffff', fontsize=8, ha='center')
    save_geo_fig(fig, 31)

def gen_geo_32():
    fig, ax = create_geo_canvas("UNIDAD DE LONGITUD EN EL GEOPLANO", "TALLER 4: SEMANA 23",
                                "1 UNIDAD = El espacio recto entre dos pines o clavos consecutivos.",
                                "Contamos cuántos espacios de clavo a clavo recorre la banda elástica.",
                                badge_color='#10b981', foot_color='#10b981')
    draw_geoplano(ax, x0=25, y0=25, grid_n=4, pin_dist=12)
    # Flecha resaltando 1 unidad entre pin (0,2) y (1,2)
    ax.plot([25, 37], [49, 49], color='#10b981', linewidth=4, zorder=6)
    ax.text(31, 53, "1 unidad lineal", color='#34d399', fontsize=9.5, fontweight='bold', ha='center')
    save_geo_fig(fig, 32)

def gen_geo_33():
    fig, ax = create_geo_canvas("CONDICIÓN OBLIGATORIA: POLÍGONO CERRADO", "TALLER 4: SEMANA 23",
                                "POLÍGONO: Debe ser una figura COMPLETAMENTE CERRADA por la banda elástica.",
                                "Si queda abierta o con extremos sueltos, NO es un polígono geométrico.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    # Figura cerrada izquierda
    draw_geoplano(ax, x0=10, y0=26, grid_n=3, pin_dist=12, shape_points=[(0,0), (2,0), (1,2)], shape_color='#10b981')
    ax.text(22, 65, "✅ POLÍGONO CERRADO", color='#34d399', fontsize=9.5, fontweight='bold', ha='center')
    
    # Figura abierta derecha (solo 2 líneas)
    draw_geoplano(ax, x0=56, y0=26, grid_n=3, pin_dist=12)
    ax.plot([56, 80], [26, 26], color='#ef4444', linewidth=3)
    ax.plot([80, 68], [26, 50], color='#ef4444', linewidth=3)
    ax.text(68, 65, "❌ FIGURA ABIERTA", color='#f87171', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(68, 19, "(No es polígono)", color='#fca5a5', fontsize=8.5, ha='center')
    save_geo_fig(fig, 33)

def gen_geo_34():
    fig, ax = create_geo_canvas("PLANCHÓN EN EL GEOPLANO (3 x 2 UNIDADES)", "TALLER 4: SEMANA 23",
                                "Perímetro del planchón en geoplano = 3 + 2 + 3 + 2 = 10 unidades lineales.",
                                "Banda elástica rectangular uniendo pines consecutivos en el Río Sinú.",
                                badge_color='#10b981', foot_color='#10b981')
    draw_geoplano(ax, x0=12, y0=25, grid_n=5, pin_dist=9,
                  shape_points=[(0,1), (3,1), (3,3), (0,3)], shape_color='#10b981')
    
    calc = patches.FancyBboxPatch((60, 26), 34, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(calc)
    ax.text(77, 66, "PLANCHÓN 3 x 2", color='#34d399', fontsize=11, fontweight='bold', ha='center')
    ax.text(77, 52, "3 u (abajo) + 2 u (der)\n+ 3 u (arriba) + 2 u (izq)", color='#ffffff', fontsize=9, ha='center')
    ax.text(77, 36, "Perímetro = 10 u", color='#facc15', fontsize=12, fontweight='bold', ha='center')
    save_geo_fig(fig, 34)

def gen_geo_35():
    fig, ax = create_geo_canvas("CARPA TRIANGULAR: LADOS Y VÉRTICES", "TALLER 4: SEMANA 23",
                                "TRIÁNGULO: Polígono de 3 lados rectos y 3 vértices (pines de esquina).",
                                "Carpa de ventas inspirada en los puestos del Mercado del Sur.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    draw_geoplano(ax, x0=12, y0=24, grid_n=5, pin_dist=9,
                  shape_points=[(0,1), (4,1), (2,4)], shape_color='#f59e0b')
    
    info = patches.FancyBboxPatch((60, 25), 34, 50, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(info)
    ax.text(77, 67, "PROPIEDADES", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(77, 52, "• Número de lados: 3\n• Vértices (esquinas): 3\n• Figura cerrada", color='#ffffff', fontsize=9.5, ha='center')
    ax.text(77, 35, "VÉRTICES EN AMARILLO", color='#facc15', fontsize=8, fontweight='bold', ha='center')
    save_geo_fig(fig, 35)

def gen_geo_36():
    fig, ax = create_geo_canvas("SITUACIÓN SABER: CUADRADO DE 3 x 3 EN GEOPLANO", "TALLER 4: SEMANA 23",
                                "Longitud total de la banda elástica (Perímetro) = 3 + 3 + 3 + 3 = 12 unidades.",
                                "Base para el tablero de juegos del Proyecto Centro de Interés.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    draw_geoplano(ax, x0=12, y0=24, grid_n=5, pin_dist=9,
                  shape_points=[(1,1), (4,1), (4,4), (1,4)], shape_color='#38bdf8')
    
    calc = patches.FancyBboxPatch((60, 25), 34, 50, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(calc)
    ax.text(77, 67, "TABLERO CUADRADO", color='#93c5fd', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(77, 53, "4 lados iguales de 3 u\n3 + 3 + 3 + 3", color='#ffffff', fontsize=10, ha='center')
    ax.text(77, 36, "P = 12 UNIDADES", color='#facc15', fontsize=13, fontweight='bold', ha='center')
    save_geo_fig(fig, 36)

def gen_geo_37():
    fig, ax = create_geo_canvas("PERÍMETRO DE TRIÁNGULO: LADOS 3, 4 Y 5 UNIDADES", "TALLER 4: SEMANA 23",
                                "Perímetro del triángulo = 3 + 4 + 5 = 12 unidades lineales.",
                                "Sumamos la longitud de cada uno de los 3 lados formados entre los pines.",
                                badge_color='#8b5cf6', foot_color='#8b5cf6')
    draw_geoplano(ax, x0=12, y0=24, grid_n=5, pin_dist=9,
                  shape_points=[(0,1), (4,1), (0,4)], shape_color='#8b5cf6')
    
    calc = patches.FancyBboxPatch((60, 25), 34, 50, boxstyle="round,pad=0.4,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#8b5cf6', linewidth=2)
    ax.add_patch(calc)
    ax.text(77, 67, "TRIÁNGULO RECTO", color='#c084fc', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(77, 53, "Base: 4 u | Altura: 3 u\nDiagonal: 5 u", color='#ffffff', fontsize=9.5, ha='center')
    ax.text(77, 36, "3 + 4 + 5 = 12 u", color='#facc15', fontsize=13, fontweight='bold', ha='center')
    save_geo_fig(fig, 37)

def gen_geo_38():
    fig, ax = create_geo_canvas("¿QUÉ SON LOS VÉRTICES EN EL GEOPLANO?", "TALLER 4: SEMANA 23",
                                "VÉRTICES: Son los pines de esquina donde la banda elástica cambia de dirección.",
                                "Cada esquina del polígono cerrado corresponde a un vértice.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    draw_geoplano(ax, x0=25, y0=24, grid_n=5, pin_dist=10,
                  shape_points=[(1,1), (4,1), (4,3), (1,3)], shape_color='#f59e0b')
    ax.text(50, 68, "Pines de esquina en amarillo = 4 VÉRTICES", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    save_geo_fig(fig, 38)

def gen_geo_39():
    fig, ax = create_geo_canvas("POR QUÉ UNA FIGURA ABIERTA NO ES POLÍGONO", "TALLER 4: SEMANA 23",
                                "Un polígono delimita una región interior cerrada.",
                                "Si la banda no regresa al pin de partida, el contorno no está cerrado.",
                                badge_color='#ef4444', foot_color='#ef4444')
    # Abierta
    draw_geoplano(ax, x0=10, y0=25, grid_n=4, pin_dist=10)
    ax.plot([10, 40], [25, 25], color='#ef4444', linewidth=3)
    ax.plot([40, 40], [25, 55], color='#ef4444', linewidth=3)
    ax.text(25, 63, "EXTREMO ABIERTO", color='#f87171', fontsize=9.5, fontweight='bold', ha='center')
    
    # Cerrada
    draw_geoplano(ax, x0=55, y0=25, grid_n=4, pin_dist=10,
                  shape_points=[(0,0), (3,0), (3,3), (0,3)], shape_color='#10b981')
    ax.text(70, 63, "REGIÓN CERRADA", color='#34d399', fontsize=9.5, fontweight='bold', ha='center')
    save_geo_fig(fig, 39)

def gen_geo_40():
    fig, ax = create_geo_canvas("VENTAJAS DEL GEOPLANO: APRENDIZAJE VISUAL", "TALLER 4: SEMANA 23",
                                "Permite tocar, construir y contar directamente cada segmento del perímetro.",
                                "Facilita comprender las propiedades geométricas antes de usar fórmulas abstractas.",
                                badge_color='#10b981', foot_color='#10b981')
    p1 = patches.FancyBboxPatch((8, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    p2 = patches.FancyBboxPatch((52, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(28, 66, "MANIPULACIÓN REAL", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 52, "CONSTRUIR Y TOCAR", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 38, "• Estirar bandas elásticas\n• Contar pines de esquina\n• Comprobar contornos", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(72, 66, "CÁLCULO EXACTO", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 52, "CONTEO DIRECTO", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 38, "• Contar unidades lineales\n• Comprobar perímetros\n• Evitar errores de memoria", color='#cbd5e1', fontsize=9, ha='center')
    save_geo_fig(fig, 40)


# ==============================================================================
# EJECUCIÓN PRINCIPAL: GENERAR LAS 40 IMÁGENES DE GEOMETRÍA
# ==============================================================================
def main():
    print("Iniciando generación de 40 imágenes de Geometría (q01.png a q40.png)...")
    generators = [
        gen_geo_01, gen_geo_02, gen_geo_03, gen_geo_04, gen_geo_05,
        gen_geo_06, gen_geo_07, gen_geo_08, gen_geo_09, gen_geo_10,
        gen_geo_11, gen_geo_12, gen_geo_13, gen_geo_14, gen_geo_15,
        gen_geo_16, gen_geo_17, gen_geo_18, gen_geo_19, gen_geo_20,
        gen_geo_21, gen_geo_22, gen_geo_23, gen_geo_24, gen_geo_25,
        gen_geo_26, gen_geo_27, gen_geo_28, gen_geo_29, gen_geo_30,
        gen_geo_31, gen_geo_32, gen_geo_33, gen_geo_34, gen_geo_35,
        gen_geo_36, gen_geo_37, gen_geo_38, gen_geo_39, gen_geo_40
    ]
    for fn in generators:
        fn()
    print("¡Todas las 40 imágenes de Geometría han sido generadas exitosamente!")

if __name__ == '__main__':
    main()
