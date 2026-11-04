"""
Generador automático de gráficos e ilustraciones para Ciencias Sociales (Grado 3°).
Crea 40 imágenes de alta resolución (q01.png a q40.png) para la materia de Ciencias Sociales.
Basado en las 8 páginas de la guía: Recursos Naturales, Océanos y Continentes, Fronteras,
Periodos Históricos, Periodo Hispánico y Mestizaje, República, Sectores Económicos y Cultura.
Compatible 100% con Windows y Linux (AWS).
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
    os.path.abspath('app/static/img/questions_soc'),
    os.path.abspath('static/img/questions_soc')
]
for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

def create_soc_canvas(title, category, foot_title, foot_sub="", badge_color='#10b981', foot_color='#10b981'):
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

def save_soc_fig(fig, qid):
    """Guarda la figura en todas las carpetas destino."""
    filename = f"q{qid:02d}.png"
    plt.tight_layout()
    for d in OUT_DIRS:
        target = os.path.join(d, filename)
        plt.savefig(target, facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
    print(f"[OK] Guardado Sociales: {filename}")


# ==============================================================================
# TEMA 1: RECURSOS NATURALES DE COLOMBIA (Q01 a Q05)
# ==============================================================================

def gen_soc_01():
    fig, ax = create_soc_canvas("¿QUÉ SON LOS RECURSOS NATURALES?", "CIENCIAS SOCIALES: RECURSOS",
                                "RECURSOS NATURALES: Elementos de la naturaleza que satisfacen necesidades humanas.",
                                "Ejemplos: Agua, suelos, sol, aire, flora, fauna, minerales y bosques.",
                                badge_color='#10b981', foot_color='#10b981')
    items = [
        ("AGUA Y MARES", "Ríos, lagunas, ciénagas\ny riqueza de peces", 18, "#06b6d4"),
        ("SUELOS Y BOSQUES", "Valles montañosos,\nselvas y agricultura", 50, "#10b981"),
        ("MINERALES Y ENERGÍA", "Oro, esmeraldas, carbón,\nsol y petróleo", 82, "#f59e0b")
    ]
    for title, desc, cx, col in items:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, title, color=col, fontsize=10, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9.5, ha='center', va='center')
        ax.text(cx, 31, "SATISFACEN NECESIDADES", color='#94a3b8', fontsize=7.5, fontweight='bold', ha='center')
    save_soc_fig(fig, 1)

def gen_soc_02():
    fig, ax = create_soc_canvas("¿POR QUÉ COLOMBIA ES TAN RICA EN RECURSOS?", "CIENCIAS SOCIALES: RECURSOS",
                                "Colombia posee gran riqueza por dos factores: el origen de sus relieves y su posición astronómica.",
                                "Permite contar con todos los pisos térmicos, lluvias y gran biodiversidad.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    b1 = patches.FancyBboxPatch((8, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    b2 = patches.FancyBboxPatch((52, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 66, "DIVERSIDAD DE RELIEVES", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 52, "CORDILLERAS Y VALLES", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 38, "Montañas, llanuras y costas\ncon todos los pisos térmicos", color='#cbd5e1', fontsize=9, ha='center')
    
    ax.text(72, 66, "POSICIÓN ASTRONÓMICA", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 52, "ZONA TROPICAL", color='#ffffff', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 38, "Luz solar constante todo el año\ny abundantes fuentes de agua", color='#cbd5e1', fontsize=9, ha='center')
    save_soc_fig(fig, 2)

def gen_soc_03():
    fig, ax = create_soc_canvas("BOSQUES Y SELVAS: PACÍFICO Y AMAZONIA", "CIENCIAS SOCIALES: RECURSOS",
                                "Los grandes pulmones de selvas y bosques húmedos están en el Pacífico y la Amazonia.",
                                "Albergan la mayor variedad de fauna, flora y árboles maderables.",
                                badge_color='#10b981', foot_color='#10b981')
    p1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    p2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#059669', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(28, 65, "REGIÓN PACÍFICA", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "Selvas Húmedas Tropicales", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(28, 35, "Zona de altísima lluvia y ríos caudalosos", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "REGIÓN AMAZÓNICA", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "Gran Selva Amazónica", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(72, 35, "Mayor reserva forestal y de oxígeno", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 3)

def gen_soc_04():
    fig, ax = create_soc_canvas("PASTOS Y SABANAS: CARIBE Y ORINOQUIA", "CIENCIAS SOCIALES: RECURSOS",
                                "Las amplias sabanas y pastos naturales se extienden en el Caribe y los Llanos de la Orinoquia.",
                                "Son zonas ideales para el desarrollo de la ganadería extensiva y la agricultura.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    p1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    p2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#d97706', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(28, 65, "REGIÓN CARIBE", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "Sabanas y Llanuras Costeras", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(28, 35, "Ganadería de carne y leche,\ncultivos de maíz y algodón", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "REGIÓN ORINOQUIA", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "Llanos Orientales", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(72, 35, "Grandes llanuras de pastoreo,\narroz y palma de aceite", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 4)

def gen_soc_05():
    fig, ax = create_soc_canvas("MINERALES DE COLOMBIA: ORO, CARBÓN Y PETRÓLEO", "CIENCIAS SOCIALES: RECURSOS",
                                "Riqueza minera: Carbón en La Guajira, petróleo en los Llanos, esmeraldas y oro en Antioquia y Chocó.",
                                "Permiten el desarrollo de la minería, la energía y la exportación internacional.",
                                badge_color='#ec4899', foot_color='#ec4899')
    cards = [
        ("CARBÓN", "La Guajira (Cerrejón)\ny Cesar", 18, "#64748b"),
        ("PETRÓLEO", "Llanos Orientales,\nSantander y Putumayo", 50, "#38bdf8"),
        ("ORO Y ESMERALDAS", "Antioquia, Chocó,\nBoyacá y Santander", 82, "#eab308")
    ]
    for title, desc, cx, col in cards:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, title, color=col, fontsize=9.5, fontweight='bold', ha='center')
        ax.text(cx, 46, desc, color='#ffffff', fontsize=9.5, ha='center', va='center')
        ax.text(cx, 31, "MINERAL VALIOSO", color='#94a3b8', fontsize=7.5, fontweight='bold', ha='center')
    save_soc_fig(fig, 5)


# ==============================================================================
# TEMA 2: EL PLANETA TIERRA, OCÉANOS Y CONTINENTES (Q06 a Q10)
# ==============================================================================

def gen_soc_06():
    fig, ax = create_soc_canvas("LA TIERRA: 'EL PLANETA AZUL'", "CIENCIAS SOCIALES: LA TIERRA",
                                "La Tierra vista desde el espacio se observa como un globo azulado.",
                                "La atmósfera que la envuelve y las nubes son iluminadas por el Sol reflejando el agua de los mares.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    # Globo azulado
    earth = patches.Circle((50, 52), 22, facecolor='#0284c7', edgecolor='#38bdf8', linewidth=2.5)
    ax.add_patch(earth)
    # Manchas de continentes
    c1 = patches.Circle((43, 56), 7, facecolor='#15803d', alpha=0.8)
    c2 = patches.Circle((56, 45), 9, facecolor='#15803d', alpha=0.8)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.text(50, 52, "70% AGUA\n30% TIERRA", color='#ffffff', fontsize=10, fontweight='bold', ha='center', va='center')
    save_soc_fig(fig, 6)

def gen_soc_07():
    fig, ax = create_soc_canvas("DISTRIBUCIÓN: 70% AGUA Y 30% CONTINENTES", "CIENCIAS SOCIALES: LA TIERRA",
                                "Aproximadamente el 70% de la superficie terrestre son aguas y nubes.",
                                "Solo el 30% restante corresponde a las masas de tierra firme (continentes).",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    b1 = patches.FancyBboxPatch((12, 28), 34, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#0369a1', edgecolor='#38bdf8', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 28), 34, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#15803d', edgecolor='#22c55e', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(29, 61, "MASAS DE AGUA", color='#bae6fd', fontsize=10, fontweight='bold', ha='center')
    ax.text(29, 46, "70%", color='#ffffff', fontsize=26, fontweight='bold', ha='center')
    ax.text(29, 34, "Océanos, mares y nubes", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(71, 61, "TIERRA FIRME", color='#bbf7d0', fontsize=10, fontweight='bold', ha='center')
    ax.text(71, 46, "30%", color='#ffffff', fontsize=26, fontweight='bold', ha='center')
    ax.text(71, 34, "Los 6 continentes", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 7)

def gen_soc_08():
    fig, ax = create_soc_canvas("LOS 5 GRANDES OCÉANOS DE LA TIERRA", "CIENCIAS SOCIALES: LA TIERRA",
                                "Océanos: Pacífico (el más grande), Atlántico, Índico, Ártico y Antártico.",
                                "Son extensas masas de agua salada que rodean los continentes.",
                                badge_color='#06b6d4', foot_color='#06b6d4')
    oceans = [
        ("PACÍFICO", "El más grande y profundo", 11),
        ("ATLÁNTICO", "Baña las costas del Caribe", 29),
        ("ÍNDICO", "Entre África y Asia", 48),
        ("ÁRTICO", "Polo Norte glacial", 67),
        ("ANTÁRTICO", "Rodea el polo sur helado", 86)
    ]
    for name, desc, cx in oceans:
        bx = patches.FancyBboxPatch((cx-8, 25), 16, 50, boxstyle="round,pad=0.3,rounding_size=1.5",
                                    facecolor='#1e293b', edgecolor='#06b6d4', linewidth=1.5)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color='#67e8f9', fontsize=8, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=7.5, ha='center', va='center')
    save_soc_fig(fig, 8)

def gen_soc_09():
    fig, ax = create_soc_canvas("LOS CONTINENTES Y EL CONTINENTE HELADO", "CIENCIAS SOCIALES: LA TIERRA",
                                "Continentes: Asia, América, Europa, África, Oceanía y Antártico.",
                                "El Antártico está cubierto de hielo en la zona polar del sur y se encuentra deshabitado.",
                                badge_color='#8b5cf6', foot_color='#8b5cf6')
    b1 = patches.FancyBboxPatch((8, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
    b2 = patches.FancyBboxPatch((52, 25), 40, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#a855f7', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 66, "CONTINENTES HABITADOS", color='#93c5fd', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(28, 48, "• América (donde vivimos)\n• Asia (el más poblado)\n• Europa y África\n• Oceanía (islas)", color='#ffffff', fontsize=9, ha='center')
    
    ax.text(72, 66, "CONTINENTE HELADO", color='#d8b4fe', fontsize=10.5, fontweight='bold', ha='center')
    ax.text(72, 52, "EL ANTÁRTICO", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(72, 38, "Cubierto de hielo en el Polo Sur.\n¡Se encuentra deshabitado!", color='#cbd5e1', fontsize=9, ha='center')
    save_soc_fig(fig, 9)

def gen_soc_10():
    fig, ax = create_soc_canvas("UBICACIÓN DE COLOMBIA EN AMÉRICA", "CIENCIAS SOCIALES: GEOGRAFÍA",
                                "Colombia está ubicada en el noroccidente de América del Sur, en el límite con América Central.",
                                "Es el único país de América del Sur con costas sobre los dos grandes océanos: Caribe y Pacífico.",
                                badge_color='#10b981', foot_color='#10b981')
    card = patches.FancyBboxPatch((15, 26), 70, 48, boxstyle="round,pad=0.5,rounding_size=2",
                                  facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(card)
    ax.text(50, 65, "COLOMBIA: ESQUINA NOROCCIDENTAL", color='#34d399', fontsize=12, fontweight='bold', ha='center')
    ax.text(50, 50, "Punto de unión entre América Central y América del Sur", color='#ffffff', fontsize=10, ha='center')
    ax.text(50, 36, "Mar Caribe al Norte  |  Océano Pacífico al Occidente", color='#facc15', fontsize=10.5, fontweight='bold', ha='center')
    save_soc_fig(fig, 10)


# ==============================================================================
# TEMA 3: POSICIÓN GEOGRÁFICA Y FRONTERAS (Q11 a Q15)
# ==============================================================================

def gen_soc_11():
    fig, ax = create_soc_canvas("SUPERFICIE TERRITORIAL Y MARÍTIMA", "CIENCIAS SOCIALES: FRONTERAS",
                                "Superficie territorial: 1 141 748 km² | Área marítima: 928 660 km² en Caribe y Pacífico.",
                                "Menos 93 000 km² perdidos frente a Nicaragua en el fallo de La Haya (2012).",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    b1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#0284c7', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 65, "ÁREA TERRESTRE", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "1 141 748 km²", color='#ffffff', fontsize=14, fontweight='bold', ha='center')
    ax.text(28, 35, "Tierra firme colombiana", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "ÁREA MARÍTIMA", color='#7dd3fc', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "928 660 km²", color='#ffffff', fontsize=14, fontweight='bold', ha='center')
    ax.text(72, 35, "Mar Caribe y Océano Pacífico", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 11)

def gen_soc_12():
    fig, ax = create_soc_canvas("PAÍSES LIMÍTROFES TERRESTRES DE COLOMBIA", "CIENCIAS SOCIALES: FRONTERAS",
                                "Colombia limita con 5 países en su territorio continental.",
                                "Venezuela (2219 km), Brasil (1645 km), Perú (1626 km), Ecuador (586 km) y Panamá (266 km).",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    borders = [
        ("VENEZUELA", "2219 km (La más larga)", 11, '#ef4444'),
        ("BRASIL", "1645 km (Selva amazónica)", 29, '#10b981'),
        ("PERÚ", "1626 km (Río Putumayo)", 48, '#f59e0b'),
        ("ECUADOR", "586 km (Sur andino)", 67, '#38bdf8'),
        ("PANAMÁ", "266 km (Tapón del Darién)", 86, '#8b5cf6')
    ]
    for name, desc, cx, col in borders:
        bx = patches.FancyBboxPatch((cx-8, 25), 16, 50, boxstyle="round,pad=0.3,rounding_size=1.5",
                                    facecolor='#1e293b', edgecolor=col, linewidth=1.8)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=8, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=7.5, ha='center', va='center')
    save_soc_fig(fig, 12)

def gen_soc_13():
    fig, ax = create_soc_canvas("FRONTERA MÁS EXTENSA: VENEZUELA (2219 km)", "CIENCIAS SOCIALES: FRONTERAS",
                                "La línea fronteriza con Venezuela es la más extensa con 2219 km de longitud.",
                                "Abarca desde La Guajira hasta las llanuras de la Orinoquia y la Amazonia.",
                                badge_color='#ef4444', foot_color='#ef4444')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "FRONTERA TERRESTRE MÁS LARGA", color='#fca5a5', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "COLOMBIA ↔ VENEZUELA", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(50, 38, "2219 kilómetros de frontera compartida", color='#facc15', fontsize=11, fontweight='bold', ha='center')
    save_soc_fig(fig, 13)

def gen_soc_14():
    fig, ax = create_soc_canvas("¿QUÉ SON LOS TRATADOS INTERNACIONALES DE LÍMITES?", "CIENCIAS SOCIALES: FRONTERAS",
                                "TRATADOS DE LÍMITES: Acuerdos oficiales firmados entre países vecinos.",
                                "Establecen con precisión hasta dónde llega el territorio de cada nación para convivir en paz.",
                                badge_color='#10b981', foot_color='#10b981')
    p1 = patches.FancyBboxPatch((12, 28), 34, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    p2 = patches.FancyBboxPatch((54, 28), 34, 46, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(29, 61, "ACUERDOS DE PAZ", color='#86efac', fontsize=10, fontweight='bold', ha='center')
    ax.text(29, 46, "FIRMA DE\nTRATADOS", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(29, 33, "Fijan las fronteras", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(71, 61, "BENEFICIO MUTUO", color='#93c5fd', fontsize=10, fontweight='bold', ha='center')
    ax.text(71, 46, "BUENA\nCONVIVENCIA", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(71, 33, "Evitan conflictos", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 14)

def gen_soc_15():
    fig, ax = create_soc_canvas("IMPORTANCIA DE LAS ZONAS FRONTERIZAS", "CIENCIAS SOCIALES: FRONTERAS",
                                "Las zonas fronterizas impulsan el comercio, el turismo, la cultura y la integración internacional.",
                                "Es necesario el respeto mutuo entre países vecinos para asegurar la paz.",
                                badge_color='#ec4899', foot_color='#ec4899')
    items = [
        ("COMERCIO Y EMPLEO", "Intercambio de bienes,\nalimentos y productos", 18, "#38bdf8"),
        ("INTEGRACIÓN CULTURAL", "Hermandad de pueblos,\nfamilias y tradiciones", 50, "#10b981"),
        ("PAZ Y RESPETO", "Convivencia pacífica\nentre gobiernos vecinos", 82, "#f59e0b")
    ]
    for title, desc, cx, col in items:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, title, color=col, fontsize=9, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9.5, ha='center', va='center')
    save_soc_fig(fig, 15)


# ==============================================================================
# TEMA 4: PERIODOS HISTÓRICOS Y PERIODO INDÍGENA (Q16 a Q20)
# ==============================================================================

def gen_soc_16():
    fig, ax = create_soc_canvas("LOS 4 GRANDES PERIODOS HISTÓRICOS DE COLOMBIA", "CIENCIAS SOCIALES: HISTORIA",
                                "La historia de Colombia se divide en 4 grandes épocas de transformación social.",
                                "1. Periodo Indígena | 2. Periodo Hispánico | 3. Independencia | 4. República.",
                                badge_color='#eab308', foot_color='#eab308')
    periods = [
        ("1. INDÍGENA", "Más de 20 000 años\nhasta el año 1500", 11, '#10b981'),
        ("2. HISPÁNICO", "Descubrimiento,\nConquista y Colonia", 29, '#f59e0b'),
        ("3. INDEPENDENCIA", "1810 a 1819\nLucha por libertad", 48, '#ef4444'),
        ("4. REPÚBLICA", "1819 hasta hoy\nNación democrática", 70, '#38bdf8')
    ]
    for name, desc, cx, col in periods:
        bx = patches.FancyBboxPatch((cx-8, 25), 18, 50, boxstyle="round,pad=0.3,rounding_size=1.5",
                                    facecolor='#1e293b', edgecolor=col, linewidth=1.8)
        ax.add_patch(bx)
        ax.text(cx+1, 66, name, color=col, fontsize=8.5, fontweight='bold', ha='center')
        ax.text(cx+1, 44, desc, color='#ffffff', fontsize=8, ha='center', va='center')
    save_soc_fig(fig, 16)

def gen_soc_17():
    fig, ax = create_soc_canvas("EL PERIODO INDÍGENA EN COLOMBIA", "CIENCIAS SOCIALES: HISTORIA",
                                "Durante la mayor parte de la historia, el territorio estuvo habitado únicamente por indígenas.",
                                "Llegaron hace más de 20 000 años. Actualmente sobreviven más de 100 grupos indígenas.",
                                badge_color='#10b981', foot_color='#10b981')
    b1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 65, "POBLADORES ORIGINALES", color='#86efac', fontsize=10, fontweight='bold', ha='center')
    ax.text(28, 48, "+ 20 000 AÑOS", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(28, 35, "Llegada por diversas rutas", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "POBLACIÓN ACTUAL", color='#fde047', fontsize=10, fontweight='bold', ha='center')
    ax.text(72, 48, "+ 100 GRUPOS", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(72, 35, "Comunidades vivas en el país", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 17)

def gen_soc_18():
    fig, ax = create_soc_canvas("TRES FAMILIAS LINGÜÍSTICAS PREHISPÁNICAS", "CIENCIAS SOCIALES: HISTORIA",
                                "Tres grandes familias lingüísticas poblaron el territorio colombiano: Chibcha, Caribe y Arawac.",
                                "Desarrollaron la orfebrería, la cerámica, el tejido y la agricultura.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    families = [
        ("CHIBCHA", "Muiscas y Taironas\n(Andes y Sierra Nevada)\nOrfebrería y agricultura", 18, '#f59e0b'),
        ("CARIBE", "Costas y ríos\nGuerreros, navegantes\ny recolectores", 50, '#ef4444'),
        ("ARAWAC", "Llanos y selvas\nAgricultores y tejedores\nde hamacas", 82, '#10b981')
    ]
    for name, desc, cx, col in families:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=11, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 18)

def gen_soc_19():
    fig, ax = create_soc_canvas("LLEGADA DE LOS ESPAÑOLES EN EL AÑO 1500", "CIENCIAS SOCIALES: HISTORIA",
                                "El periodo indígena terminó con la llegada de los españoles en 1500.",
                                "Inició la etapa de dominación, sometimiento y choque de culturas.",
                                badge_color='#ef4444', foot_color='#ef4444')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "CAMBIO DE ERA HISTÓRICA", color='#fca5a5', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "AÑO 1500", color='#ffffff', fontsize=22, fontweight='bold', ha='center')
    ax.text(50, 38, "Fin del periodo indígena y comienzo del periodo hispánico", color='#cbd5e1', fontsize=9.5, ha='center')
    save_geo_fig = save_soc_fig
    save_soc_fig(fig, 19)

def gen_soc_20():
    fig, ax = create_soc_canvas("¿QUÉ ES UN PERIODO HISTÓRICO?", "CIENCIAS SOCIALES: HISTORIA",
                                "PERIODO HISTÓRICO: Época delimitada por hechos y cambios profundos que transforman la sociedad.",
                                "Permite organizar y comprender el pasado paso a paso.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    p1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    p2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(p1)
    ax.add_patch(p2)
    ax.text(28, 65, "HECHOS CLAVE", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "ACONTECIMIENTOS", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(28, 35, "Guerras, fundaciones y leyes", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "TRANSFORMACIÓN", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "CAMBIO SOCIAL", color='#ffffff', fontsize=10, fontweight='bold', ha='center')
    ax.text(72, 35, "Nueva forma de vida y cultura", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 20)


# ==============================================================================
# TEMA 5: EL PERIODO HISPÁNICO Y EL MESTIZAJE (Q21 a Q25)
# ==============================================================================

def gen_soc_21():
    fig, ax = create_soc_canvas("EL PERIODO HISPÁNICO: 1500 A 1810", "CIENCIAS SOCIALES: COLONIA",
                                "Inició en 1500 con el Descubrimiento de la Costa Caribe y culminó en 1810 con la Independencia.",
                                "Abarca tres etapas fundamentales: Descubrimiento, Conquista y Colonia.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    stages = [
        ("DESCUBRIMIENTO", "1500\nLlegada a costas\ndel Caribe", 18, '#38bdf8'),
        ("CONQUISTA", "Exploración,\nsometimiento militar\ny fundaciones", 50, '#ef4444'),
        ("COLONIA", "300 años de gobierno\nvirreinal español\n(1550 - 1810)", 82, '#10b981')
    ]
    for name, desc, cx, col in stages:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=9.5, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 21)

def gen_soc_22():
    fig, ax = create_soc_canvas("FUNDACIÓN DE CIUDADES EN LA CONQUISTA", "CIENCIAS SOCIALES: COLONIA",
                                "Los conquistadores fundaron villas y ciudades clave como Santa Marta, Cartagena y Bogotá.",
                                "Se convirtieron en centros de administración, comercio y religión colonial.",
                                badge_color='#8b5cf6', foot_color='#8b5cf6')
    cities = [
        ("SANTA MARTA", "Fundada en 1525\npor Rodrigo de Bastidas", 18, '#3b82f6'),
        ("CARTAGENA", "Fundada en 1533\npor Pedro de Heredia", 50, '#f59e0b'),
        ("SANTAFÉ DE BOGOTÁ", "Fundada en 1538\npor Gonzalo Jiménez de Quesada", 82, '#10b981')
    ]
    for name, desc, cx, col in cities:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=9, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=8.5, ha='center', va='center')
    save_soc_fig(fig, 22)

def gen_soc_23():
    fig, ax = create_soc_canvas("LA COLONIA: 300 AÑOS DE DOMINIO", "CIENCIAS SOCIALES: COLONIA",
                                "La época colonial se extendió durante tres siglos (aproximadamente de 1550 a 1810).",
                                "Finalizó con el grito de Independencia el 20 de julio de 1810.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "DURACIÓN DE LA COLONIA", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "300 AÑOS", color='#ffffff', fontsize=24, fontweight='bold', ha='center')
    ax.text(50, 38, "Desde las primeras fundaciones hasta el grito de 1810", color='#cbd5e1', fontsize=9.5, ha='center')
    save_soc_fig(fig, 23)

def gen_soc_24():
    fig, ax = create_soc_canvas("EL MESTIZAJE: FUSIÓN DE TRES CULTURAS", "CIENCIAS SOCIALES: COLONIA",
                                "Mestizaje: Mezcla entre indígenas nativos, blancos españoles y negros africanos.",
                                "Dio origen a la identidad multiétnica del pueblo colombiano.",
                                badge_color='#ec4899', foot_color='#ec4899')
    races = [
        ("INDÍGENAS", "Pobladores nativos\noriginarios de América", 18, '#10b981'),
        ("BLANCOS", "Españoles europeos\ncolonizadores", 50, '#38bdf8'),
        ("AFRICANOS", "Llegados de África\ncon su rica cultura", 82, '#f59e0b')
    ]
    for name, desc, cx, col in races:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=10, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 24)

def gen_soc_25():
    fig, ax = create_soc_canvas("APORTES CULTURALES DE LOS ESPAÑOLES", "CIENCIAS SOCIALES: COLONIA",
                                "La cultura española trajo el idioma castellano, la religión católica, animales domésticos y nuevas leyes.",
                                "Transformó las técnicas de cultivo, la arquitectura y los medios de transporte.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    items = [
        ("LENGUA Y CULTURA", "Idioma español\ny religión católica", 18, '#38bdf8'),
        ("ANIMALES NUEVOS", "Caballos, vacas,\ncerdos y gallinas", 50, '#10b981'),
        ("ARQUITECTURA", "Casas de teja, plazas,\niglesias y caminos", 82, '#f59e0b')
    ]
    for name, desc, cx, col in items:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=9.5, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 25)


# ==============================================================================
# TEMA 6: PERIODO DE LA REPÚBLICA Y NOMBRES HISTÓRICOS (Q26 a Q30)
# ==============================================================================

def gen_soc_26():
    fig, ax = create_soc_canvas("EL PERIODO DE LA REPÚBLICA: 1810 HASTA HOY", "CIENCIAS SOCIALES: REPÚBLICA",
                                "Se inició en 1810 con el Acta de proclamación de la Independencia y continúa en la actualidad.",
                                "Colombia se organizó como una república libre, soberana y democrática.",
                                badge_color='#10b981', foot_color='#10b981')
    b1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 65, "NACIMIENTO", color='#fca5a5', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "AÑO 1810", color='#ffffff', fontsize=16, fontweight='bold', ha='center')
    ax.text(28, 35, "Proclamación de la Independencia", color='#cbd5e1', fontsize=8, ha='center')
    
    ax.text(72, 65, "PRESENTE", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "ACTUALIDAD", color='#ffffff', fontsize=16, fontweight='bold', ha='center')
    ax.text(72, 35, "Vigente hasta nuestros días", color='#cbd5e1', fontsize=8, ha='center')
    save_soc_fig(fig, 26)

def gen_soc_27():
    fig, ax = create_soc_canvas("BATALLA DE BOYACÁ: 7 DE AGOSTO DE 1819", "CIENCIAS SOCIALES: REPÚBLICA",
                                "La Independencia definitiva se selló con la Campaña Libertadora en la Batalla de Boyacá.",
                                "Liderada por Simón Bolívar y el ejército libertador en el Puente de Boyacá.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "TRIUNFO DE LA CAMPAÑA LIBERTADORA", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "7 DE AGOSTO DE 1819", color='#ffffff', fontsize=16, fontweight='bold', ha='center')
    ax.text(50, 38, "Sellamiento definitivo de la libertad de la Nueva Granada", color='#cbd5e1', fontsize=9.5, ha='center')
    save_soc_fig(fig, 27)

def gen_soc_28():
    fig, ax = create_soc_canvas("EVOLUCIÓN DE NOMBRES DE COLOMBIA (SIGLO XIX)", "CIENCIAS SOCIALES: REPÚBLICA",
                                "1. La Gran Colombia | 2. Rep. Neogranadina | 3. Conf. Granadina | 4. EE.UU. de Colombia | 5. Rep. de Colombia.",
                                "Diversas constituciones cambiaron el nombre hasta fijar el actual en 1886.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    names = [
        ("Gran Colombia", "1819", 11),
        ("R. Neogranadina", "1831", 29),
        ("C. Granadina", "1858", 48),
        ("EE.UU. Colombia", "1863", 67),
        ("R. de Colombia", "1886", 86)
    ]
    for title, yr, cx in names:
        bx = patches.FancyBboxPatch((cx-8, 25), 16, 50, boxstyle="round,pad=0.3,rounding_size=1.5",
                                    facecolor='#1e293b', edgecolor='#38bdf8', linewidth=1.5)
        ax.add_patch(bx)
        ax.text(cx, 66, yr, color='#facc15', fontsize=9, fontweight='bold', ha='center')
        ax.text(cx, 44, title, color='#ffffff', fontsize=8, fontweight='bold', ha='center', va='center')
    save_soc_fig(fig, 28)

def gen_soc_29():
    fig, ax = create_soc_canvas("DESDE 1886: 'REPÚBLICA DE COLOMBIA'", "CIENCIAS SOCIALES: REPÚBLICA",
                                "La Constitución de 1886 estableció el nombre oficial y definitivo: República de Colombia.",
                                "Consolidó un estado centralizado, unificado y soberano.",
                                badge_color='#10b981', foot_color='#10b981')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "NOMBRE OFICIAL DEFINITIVO", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "REPÚBLICA DE COLOMBIA", color='#ffffff', fontsize=16, fontweight='bold', ha='center')
    ax.text(50, 38, "Adoptado desde 1886 hasta la actualidad", color='#facc15', fontsize=10.5, fontweight='bold', ha='center')
    save_soc_fig(fig, 29)

def gen_soc_30():
    fig, ax = create_soc_canvas("PRODUCTOS CLAVE DE EXPORTACIÓN", "CIENCIAS SOCIALES: REPÚBLICA",
                                "La economía republicana creció exportando café, banano, flores, carbón, petróleo y oro.",
                                "Conectó a Colombia con los grandes mercados del mundo.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    products = [
        ("CAFÉ Y FLORES", "Reconocimiento mundial\npor su aroma y calidad", 18, '#f59e0b'),
        ("PETRÓLEO Y CARBÓN", "Fuentes energéticas de\ngran valor comercial", 50, '#38bdf8'),
        ("BANANO Y ORO", "Cultivos costeños y\nminería tradicional", 82, '#10b981')
    ]
    for name, desc, cx, col in products:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=9.5, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 30)


# ==============================================================================
# TEMA 7: LOS TRES SECTORES DE LA ECONOMÍA (Q31 a Q35)
# ==============================================================================

def gen_soc_31():
    fig, ax = create_soc_canvas("LOS 3 SECTORES DE LA ECONOMÍA", "CIENCIAS SOCIALES: ECONOMÍA",
                                "1. Primario (Extracción natural) | 2. Secundario (Fábricas e industria) | 3. Terciario (Servicios).",
                                "Juntos generan el trabajo, los productos y los ingresos de la sociedad.",
                                badge_color='#10b981', foot_color='#10b981')
    sectors = [
        ("1. PRIMARIO", "Extracción de la naturaleza:\nagricultura, minería,\nganadería y pesca", 18, '#10b981'),
        ("2. SECUNDARIO", "Transformación en fábricas:\ntextiles, alimentos\ne industrias", 50, '#38bdf8'),
        ("3. TERCIARIO", "Servicios a la comunidad:\ncomercio, transporte,\nbancos y salud", 82, '#f59e0b')
    ]
    for name, desc, cx, col in sectors:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=10, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=8.5, ha='center', va='center')
    save_soc_fig(fig, 31)

def gen_soc_32():
    fig, ax = create_soc_canvas("EL SECTOR PRIMARIO: RECURSOS DE LA NATURALEZA", "CIENCIAS SOCIALES: ECONOMÍA",
                                "SECTOR PRIMARIO: Actividades de extracción directa de los recursos naturales.",
                                "Incluye el cultivo de café, flores, caña de azúcar y la extracción de petróleo y carbón.",
                                badge_color='#10b981', foot_color='#10b981')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "EXTRACCIÓN DIRECTA DE LA TIERRA", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "AGRICULTURA Y MINERÍA", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(50, 38, "Café, banano, flores, azúcar, oro, carbón y petróleo", color='#facc15', fontsize=9.5, fontweight='bold', ha='center')
    save_soc_fig(fig, 32)

def gen_soc_33():
    fig, ax = create_soc_canvas("EL SECTOR SECUNDARIO: FÁBRICAS E INDUSTRIAS", "CIENCIAS SOCIALES: ECONOMÍA",
                                "SECTOR SECUNDARIO: Procesa y transforma las materias primas en productos elaborados.",
                                "Ejemplo: Convertir el algodón en ropa o la leche en queso y mantequilla.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "TRANSFORMACIÓN EN FÁBRICAS", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "INDUSTRIA Y MANUFACTURA", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(50, 38, "Materias primas  ->  Productos terminados para el uso", color='#facc15', fontsize=9.5, fontweight='bold', ha='center')
    save_soc_fig(fig, 33)

def gen_soc_34():
    fig, ax = create_soc_canvas("EL SECTOR TERCIARIO: PRESTACIÓN DE SERVICIOS", "CIENCIAS SOCIALES: ECONOMÍA",
                                "SECTOR TERCIARIO: No produce objetos materiales, sino que brinda servicios esenciales.",
                                "Comercio en almacenes, bancos, colegios, hospitales y empresas de transporte.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    services = [
        ("COMERCIO", "Venta de alimentos,\nropa y medicamentos", 18, '#f59e0b'),
        ("TRANSPORTE", "Buses, taxis, aviones\ny planchones del río", 50, '#38bdf8'),
        ("BANCOS Y SALUD", "Servicios financieros,\nhospitales y escuelas", 82, '#10b981')
    ]
    for name, desc, cx, col in services:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=10, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 34)

def gen_soc_35():
    fig, ax = create_soc_canvas("SUPERAR LAS DESIGUALDADES SOCIOECONÓMICAS", "CIENCIAS SOCIALES: ECONOMÍA",
                                "El desarrollo económico debe garantizar una mejor distribución de bienes y servicios.",
                                "Permite alcanzar el bienestar, la educación y la salud de todas las familias colombianas.",
                                badge_color='#ec4899', foot_color='#ec4899')
    b1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 65, "CRECIMIENTO", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 48, "PRODUCCIÓN", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(28, 35, "Mayor trabajo y riquezas", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "BIENESTAR SOCIAL", color='#86efac', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 48, "DISTRIBUCIÓN JUSTA", color='#ffffff', fontsize=12, fontweight='bold', ha='center')
    ax.text(72, 35, "Salud y educación para todos", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 35)


# ==============================================================================
# TEMA 8: DIVERSIDAD CULTURAL Y EXPONENTES (Q36 a Q40)
# ==============================================================================

def gen_soc_36():
    fig, ax = create_soc_canvas("DIVERSIDAD REGIONAL Y COSTUMBRES", "CIENCIAS SOCIALES: CULTURA",
                                "Los grupos culturales regionales se diferencian por el habla, vestir, comida, danzas y fiestas.",
                                "Costeños, paisas, llaneros, santandereanos, vallunos y pastusos enriquecen a Colombia.",
                                badge_color='#ec4899', foot_color='#ec4899')
    items = [
        ("FORMA DE HABLAR", "Acentos y dichos típicos\nde cada región", 18, '#38bdf8'),
        ("COMIDAS TÍPICAS", "Sancocho, arepas, bandeja\npaisa y mote de queso", 50, '#f59e0b'),
        ("MÚSICA Y FIESTAS", "Cumbia, vallenato, joropo,\nbambuco y carnavales", 82, '#10b981')
    ]
    for name, desc, cx, col in items:
        bx = patches.FancyBboxPatch((cx-14, 25), 28, 50, boxstyle="round,pad=0.5,rounding_size=2",
                                    facecolor='#1e293b', edgecolor=col, linewidth=2)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=9.5, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=9, ha='center', va='center')
    save_soc_fig(fig, 36)

def gen_soc_37():
    fig, ax = create_soc_canvas("EXPONENTES DE LA CULTURA COLOMBIANA", "CIENCIAS SOCIALES: CULTURA",
                                "Artistas colombianos de fama internacional reconocidos en todo el mundo.",
                                "Gabriel García Márquez, Fernando Botero, Shakira y Juanes.",
                                badge_color='#f59e0b', foot_color='#f59e0b')
    artists = [
        ("GARCÍA MÁRQUEZ", "Literatura\nPremio Nobel", 11, '#f59e0b'),
        ("FERNANDO BOTERO", "Pintura y Escultura\nFormas volumétricas", 36, '#38bdf8'),
        ("SHAKIRA", "Música pop y danza\nEmbajadora mundial", 63, '#ec4899'),
        ("JUANES", "Música rock y pop\nGanador de Grammys", 89, '#10b981')
    ]
    for name, desc, cx, col in artists:
        bx = patches.FancyBboxPatch((cx-10, 25), 20, 50, boxstyle="round,pad=0.3,rounding_size=1.5",
                                    facecolor='#1e293b', edgecolor=col, linewidth=1.8)
        ax.add_patch(bx)
        ax.text(cx, 66, name, color=col, fontsize=8, fontweight='bold', ha='center')
        ax.text(cx, 44, desc, color='#ffffff', fontsize=7.5, ha='center', va='center')
    save_soc_fig(fig, 37)

def gen_soc_38():
    fig, ax = create_soc_canvas("GABRIEL GARCÍA MÁRQUEZ: PREMIO NOBEL", "CIENCIAS SOCIALES: CULTURA",
                                "Gran maestro de la literatura mundial, autor de 'Cien años de soledad'.",
                                "Nacido en Aracataca, llevó el realismo mágico y la cultura caribe a todo el planeta.",
                                badge_color='#eab308', foot_color='#eab308')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#eab308', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "LITERATURA UNIVERSAL", color='#fde047', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "GABRIEL GARCÍA MÁRQUEZ", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(50, 38, "Premio Nobel de Literatura (1982) &bull; 'Gabo'", color='#cbd5e1', fontsize=10, ha='center')
    save_soc_fig(fig, 38)

def gen_soc_39():
    fig, ax = create_soc_canvas("FERNANDO BOTERO: PINTURA Y ESCULTURA", "CIENCIAS SOCIALES: CULTURA",
                                "Reconocido mundialmente por su estilo único de figuras y formas voluminosas.",
                                "Sus monumentales esculturas se exhiben en museos y plazas de las principales capitales.",
                                badge_color='#38bdf8', foot_color='#38bdf8')
    tag = patches.FancyBboxPatch((15, 30), 70, 44, boxstyle="round,pad=0.5,rounding_size=2",
                                 facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
    ax.add_patch(tag)
    ax.text(50, 64, "ARTE, PINTURA Y ESCULTURA", color='#93c5fd', fontsize=11, fontweight='bold', ha='center')
    ax.text(50, 50, "MAESTRO FERNANDO BOTERO", color='#ffffff', fontsize=15, fontweight='bold', ha='center')
    ax.text(50, 38, "Creador del estilo 'Boterismo' con grandes volúmenes", color='#facc15', fontsize=10, fontweight='bold', ha='center')
    save_soc_fig(fig, 39)

def gen_soc_40():
    fig, ax = create_soc_canvas("SHAKIRA Y JUANES: EMBAJADORES MUSICALES", "CIENCIAS SOCIALES: CULTURA",
                                "Llevaron los ritmos colombianos, el pop, rock y folclor a los escenarios de todo el mundo.",
                                "Orgullo nacional y símbolos del talento contemporáneo de Colombia.",
                                badge_color='#10b981', foot_color='#10b981')
    b1 = patches.FancyBboxPatch((10, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#ec4899', linewidth=2)
    b2 = patches.FancyBboxPatch((54, 26), 36, 48, boxstyle="round,pad=0.4,rounding_size=2",
                                facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.text(28, 65, "SHAKIRA", color='#fbcfe8', fontsize=12, fontweight='bold', ha='center')
    ax.text(28, 48, "BARRANQUILLA", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(28, 35, "Pop, danza y folclor caribe", color='#cbd5e1', fontsize=8.5, ha='center')
    
    ax.text(72, 65, "JUANES", color='#86efac', fontsize=12, fontweight='bold', ha='center')
    ax.text(72, 48, "ANTIOQUIA", color='#ffffff', fontsize=11, fontweight='bold', ha='center')
    ax.text(72, 35, "Rock, pop y música social", color='#cbd5e1', fontsize=8.5, ha='center')
    save_soc_fig(fig, 40)


# ==============================================================================
# EJECUCIÓN PRINCIPAL: GENERAR LAS 40 IMÁGENES
# ==============================================================================
def main():
    print("Iniciando generación de 40 imágenes de Ciencias Sociales (q01.png a q40.png)...")
    generators = [
        gen_soc_01, gen_soc_02, gen_soc_03, gen_soc_04, gen_soc_05,
        gen_soc_06, gen_soc_07, gen_soc_08, gen_soc_09, gen_soc_10,
        gen_soc_11, gen_soc_12, gen_soc_13, gen_soc_14, gen_soc_15,
        gen_soc_16, gen_soc_17, gen_soc_18, gen_soc_19, gen_soc_20,
        gen_soc_21, gen_soc_22, gen_soc_23, gen_soc_24, gen_soc_25,
        gen_soc_26, gen_soc_27, gen_soc_28, gen_soc_29, gen_soc_30,
        gen_soc_31, gen_soc_32, gen_soc_33, gen_soc_34, gen_soc_35,
        gen_soc_36, gen_soc_37, gen_soc_38, gen_soc_39, gen_soc_40
    ]
    for fn in generators:
        fn()
    print("¡Todas las 40 imágenes de Ciencias Sociales han sido generadas exitosamente!")

if __name__ == '__main__':
    main()
