import json
import os

sociales_data = {
  "id": "sociales",
  "name": "Ciencias Sociales (Geografía, Historia y Economía)",
  "grade": "Grado Tercero",
  "institution": "Institución Educativa Cecilia de Lleras",
  "description": "Evaluación basada en la Guía de Estudio de Tercer Periodo: Recursos naturales y pisos térmicos, el planeta Tierra y océanos, fronteras y límites de Colombia, periodos históricos e indígenas, periodo hispánico y mestizaje, República y Constitución de 1886, sectores de la economía y diversidad cultural colombiana.",
  "badge": "Tercer Periodo 2026",
  "icon": "fa-earth-americas",
  "color": "emerald",
  "default_question_count": 15,
  "questions": [
    {
      "id": 1,
      "category": "Tema 1: Recursos Naturales",
      "question": "¿Qué son los recursos naturales según la guía de estudio?",
      "context": "Guía de Ciencias Sociales - Página 1: Recursos Naturales\nLos recursos que brinda la naturaleza.",
      "options": [
        "Son todos los elementos que nos brinda la naturaleza y que satisfacen las necesidades humanas",
        "Son objetos de plástico y metal fabricados únicamente dentro de las fábricas",
        "Son juegos y juguetes que compramos en los centros comerciales",
        "Son las monedas y billetes que se guardan en los bancos del país"
      ],
      "correct_answer": "Son todos los elementos que nos brinda la naturaleza y que satisfacen las necesidades humanas",
      "explanation": "Los recursos naturales son los elementos y riquezas que ofrece la naturaleza (agua, suelo, sol, aire, flora, fauna y minerales) útiles para satisfacer las necesidades del ser humano.",
      "image": "/static/img/questions_soc/q01.png",
      "image_alt": "Ilustración: ¿Qué son los Recursos Naturales?"
    },
    {
      "id": 2,
      "category": "Tema 1: Recursos Naturales",
      "question": "¿Cuáles son los dos factores principales que explican la enorme riqueza en recursos naturales de Colombia?",
      "context": "Guía de Ciencias Sociales - Página 1: Factores de la riqueza natural\nRelieve y posición geográfica.",
      "options": [
        "El origen y variedad de sus relieves y su estratégica posición astronómica en la zona tropical",
        "Tener grandes fábricas de automóviles y muchas computadoras modernas",
        "Estar rodeada únicamente de nieve y glaciares congelados",
        "El consumo exclusivo de productos importados de otros continentes"
      ],
      "correct_answer": "El origen y variedad de sus relieves y su estratégica posición astronómica en la zona tropical",
      "explanation": "Colombia es uno de los países más biodiversos y ricos del planeta gracias a la variedad de sus relieves (cordilleras, valles, costas) y su posición astronómica en la zona intertropical.",
      "image": "/static/img/questions_soc/q02.png",
      "image_alt": "Ilustración: Factores de la riqueza natural colombiana"
    },
    {
      "id": 3,
      "category": "Tema 1: Recursos Naturales",
      "question": "¿En qué regiones de Colombia se concentran los mayores bosques y selvas húmedas tropicales ricas en biodiversidad?",
      "context": "Guía de Ciencias Sociales - Página 1: Bosques y Selvas de Colombia\nPulmones naturales del país.",
      "options": [
        "En la Región Pacífica y en la Región de la Amazonia",
        "En los desiertos de La Guajira únicamente",
        "En los picos nevados por encima de los 5 000 metros",
        "En las plazas principales de las ciudades capitales"
      ],
      "correct_answer": "En la Región Pacífica y en la Región de la Amazonia",
      "explanation": "Las regiones del Pacífico y la Amazonia albergan las mayores extensiones de selvas húmedas y bosques tropicales, con una inmensa riqueza forestal, hídrica y de fauna.",
      "image": "/static/img/questions_soc/q03.png",
      "image_alt": "Ilustración: Bosques y Selvas - Pacífico y Amazonia"
    },
    {
      "id": 4,
      "category": "Tema 1: Recursos Naturales",
      "question": "¿Qué tipo de vegetación y actividades económicas predominan en las regiones del Caribe y los Llanos de la Orinoquia?",
      "context": "Guía de Ciencias Sociales - Página 1: Sabanas y Pastos\nGrandes llanuras ganaderas.",
      "options": [
        "Amplias sabanas con pastos naturales aptos para la ganadería y la agricultura",
        "Glaciares permanentes donde solo habitan pingüinos y osos polares",
        "Bosques de pino congelados sin ninguna clase de vegetación",
        "Túneles subterráneos donde no llega la luz del sol"
      ],
      "correct_answer": "Amplias sabanas con pastos naturales aptos para la ganadería y la agricultura",
      "explanation": "En la región Caribe y en los Llanos de la Orinoquia predominan las grandes llanuras y sabanas con pastos naturales, ideales para la ganadería extensiva y cultivos como el arroz y el maíz.",
      "image": "/static/img/questions_soc/q04.png",
      "image_alt": "Ilustración: Pastos y Sabanas - Caribe y Orinoquia"
    },
    {
      "id": 5,
      "category": "Tema 1: Recursos Naturales",
      "question": "¿Cuáles son algunos de los recursos minerales y energéticos más destacados que posee el subsuelo colombiano?",
      "context": "Guía de Ciencias Sociales - Página 1: Riqueza Minera y Energética\nMinerales valiosos del subsuelo.",
      "options": [
        "Carbón (La Guajira), petróleo (Llanos y Santander), esmeraldas y oro (Antioquia y Chocó)",
        "Diamantes espaciales traídos de la luna y mercurio puro de marte",
        "Únicamente arena de playa para hacer castillos de juguete",
        "Plástico reciclado y latas de gaseosa enterradas"
      ],
      "correct_answer": "Carbón (La Guajira), petróleo (Llanos y Santander), esmeraldas y oro (Antioquia y Chocó)",
      "explanation": "Colombia cuenta con importantes reservas de carbón en La Guajira y Cesar, petróleo en los Llanos Orientales y Santander, y reconocidas minas de esmeraldas y oro en Antioquia, Chocó y Boyacá.",
      "image": "/static/img/questions_soc/q05.png",
      "image_alt": "Ilustración: Minerales de Colombia - Carbón, Petróleo y Oro"
    },
    {
      "id": 6,
      "category": "Tema 2: El Planeta Tierra",
      "question": "¿Por qué razón a nuestro planeta Tierra se le conoce popularmente como 'el planeta azul'?",
      "context": "Guía de Ciencias Sociales - Página 2: El Planeta Azul\nVista de la Tierra desde el espacio.",
      "options": [
        "Porque al observarlo desde el espacio exterior la atmósfera y las nubes reflejan la luz solar sobre los inmensos océanos y mares",
        "Porque toda la tierra continental y las montañas están pintadas con pintura azul",
        "Porque el cielo de noche se congela y toma un color azul marino",
        "Porque los astronautas viajan en naves con vidrios teñidos de azul"
      ],
      "correct_answer": "Porque al observarlo desde el espacio exterior la atmósfera y las nubes reflejan la luz solar sobre los inmensos océanos y mares",
      "explanation": "La Tierra se denomina el planeta azul porque la mayor parte de su superficie está cubierta de agua líquida y nubes, las cuales al ser iluminadas por el Sol le dan ese hermoso aspecto azulado desde el espacio.",
      "image": "/static/img/questions_soc/q06.png",
      "image_alt": "Ilustración: La Tierra - El Planeta Azul"
    },
    {
      "id": 7,
      "category": "Tema 2: El Planeta Tierra",
      "question": "¿Qué porcentaje aproximado de la superficie del planeta Tierra corresponde a masas de agua y cuánto a tierra continental?",
      "context": "Guía de Ciencias Sociales - Página 2: Distribución de Agua y Tierra\nComparación de superficies.",
      "options": [
        "Aproximadamente 70% de agua (océanos y mares) y 30% de tierra continental",
        "50% de agua y 50% de tierra de manera exactamente simétrica",
        "95% de tierra seca y solo un 5% de pequeños arroyos",
        "10% de agua salada y 90% de grandes montañas rocosas"
      ],
      "correct_answer": "Aproximadamente 70% de agua (océanos y mares) y 30% de tierra continental",
      "explanation": "La superficie terrestre está conformada en un 70% aproximadamente por agua (océanos, mares y nubes) y solo el 30% restante por tierra firme emergida (los continentes e islas).",
      "image": "/static/img/questions_soc/q07.png",
      "image_alt": "Ilustración: Distribución - 70% Agua y 30% Continentes"
    },
    {
      "id": 8,
      "category": "Tema 2: El Planeta Tierra",
      "question": "¿Cuáles son los cinco grandes océanos que rodean los continentes en el planeta Tierra?",
      "context": "Guía de Ciencias Sociales - Página 2: Los 5 Grandes Océanos\nGrandes masas de agua salada.",
      "options": [
        "Pacífico, Atlántico, Índico, Glacial Ártico y Glacial Antártico",
        "Magdalena, Cauca, Sinú, Amazonas y Orinoco",
        "Mar Caribe, Golfo de Urabá, Bahía de Cartagena y Lago de Tota",
        "Mediterráneo, Rojo, Muerto, Caspio y Negro"
      ],
      "correct_answer": "Pacífico, Atlántico, Índico, Glacial Ártico y Glacial Antártico",
      "explanation": "Los 5 océanos de la Tierra son: el Pacífico (el más grande y profundo), el Atlántico, el Índico, el Ártico (en el polo norte) y el Antártico (rodeando el polo sur).",
      "image": "/static/img/questions_soc/q08.png",
      "image_alt": "Ilustración: Los 5 Grandes Océanos de la Tierra"
    },
    {
      "id": 9,
      "category": "Tema 2: El Planeta Tierra",
      "question": "¿Cuál es el continente que se encuentra en la zona polar del sur, cubierto de hielo y deshabitado por poblaciones permanentes?",
      "context": "Guía de Ciencias Sociales - Página 2: Continentes del Mundo\nEl continente helado del polo sur.",
      "options": [
        "El continente Antártico (Antártida)",
        "El continente Americano",
        "El continente Europeo",
        "El continente Africano"
      ],
      "correct_answer": "El continente Antártico (Antártida)",
      "explanation": "El Antártico está ubicado en el extremo sur del planeta, es un continente cubierto de hielo y nieve con temperaturas extremadamente bajas, por lo cual se encuentra deshabitado permanentemente.",
      "image": "/static/img/questions_soc/q09.png",
      "image_alt": "Ilustración: Los Continentes y el Continente Helado"
    },
    {
      "id": 10,
      "category": "Tema 2: El Planeta Tierra",
      "question": "¿En qué continente y en qué parte específica de dicho continente se encuentra situada la República de Colombia?",
      "context": "Guía de Ciencias Sociales - Página 2: Posición de Colombia en el Mapa Mundial\nUbicación geográfica continental.",
      "options": [
        "En el continente Americano, exactamente en la esquina noroccidental de América del Sur",
        "En el centro de Europa, entre Francia y Alemania",
        "En las costas occidentales del continente Africano",
        "En el archipiélago de islas de Oceanía cerca a Australia"
      ],
      "correct_answer": "En el continente Americano, exactamente en la esquina noroccidental de América del Sur",
      "explanation": "Colombia forma parte del continente Americano y está situada estratégicamente en el noroccidente de América del Sur, en la unión con América Central.",
      "image": "/static/img/questions_soc/q10.png",
      "image_alt": "Ilustración: Ubicación de Colombia en América"
    },
    {
      "id": 11,
      "category": "Tema 3: Fronteras de Colombia",
      "question": "Según los datos de la guía, ¿cuánto mide aproximadamente la superficie continental y el área marítima de Colombia?",
      "context": "Guía de Ciencias Sociales - Página 3: Extensión Territorial de Colombia\nÁrea terrestre y marina.",
      "options": [
        "1 141 748 km² de territorio continental y 928 660 km² de territorio marítimo",
        "100 000 km² de tierra firme y 50 000 km² de mares y lagunas",
        "5 000 000 km² de pura selva sin ningún acceso al mar",
        "500 km² de territorio en total entre tierra y mar"
      ],
      "correct_answer": "1 141 748 km² de territorio continental y 928 660 km² de territorio marítimo",
      "explanation": "Colombia tiene una extensión terrestre de 1 141 748 km² y un área marina de 928 660 km² (tras la reducción de 93 000 km² en el litigio de La Haya en 2012).",
      "image": "/static/img/questions_soc/q11.png",
      "image_alt": "Ilustración: Superficie Territorial y Marítima de Colombia"
    },
    {
      "id": 12,
      "category": "Tema 3: Fronteras de Colombia",
      "question": "¿Con cuáles 5 países comparte Colombia sus fronteras terrestres en el continente sudamericano?",
      "context": "Guía de Ciencias Sociales - Página 3: Países Limítrofes Terrestres\nVecinos internacionales de Colombia.",
      "options": [
        "Venezuela, Brasil, Perú, Ecuador y Panamá",
        "México, Estados Unidos, Canadá, Cuba y Jamaica",
        "Argentina, Chile, Paraguay, Uruguay y Bolivia",
        "España, Portugal, Francia, Italia e Inglaterra"
      ],
      "correct_answer": "Venezuela, Brasil, Perú, Ecuador y Panamá",
      "explanation": "Los 5 países limítrofes terrestres de Colombia son: Venezuela al oriente, Brasil al suroriente, Perú al sur, Ecuador al suroccidente y Panamá al noroccidente.",
      "image": "/static/img/questions_soc/q12.png",
      "image_alt": "Ilustración: Países Limítrofes Terrestres de Colombia"
    },
    {
      "id": 13,
      "category": "Tema 3: Fronteras de Colombia",
      "question": "¿Cuál es el país vecino con el cual Colombia comparte su frontera terrestre más extensa (más de 2200 km)?",
      "context": "Guía de Ciencias Sociales - Página 3: Frontera Más Larga\nMayor longitud fronteriza.",
      "options": [
        "Venezuela, con una línea fronteriza de 2219 kilómetros",
        "Panamá, con una frontera de solo 266 kilómetros",
        "Ecuador, con una frontera de 586 kilómetros",
        "Perú, con una frontera de 1626 kilómetros"
      ],
      "correct_answer": "Venezuela, con una línea fronteriza de 2219 kilómetros",
      "explanation": "La frontera terrestre más extensa de Colombia es con la República Bolivariana de Venezuela, con una longitud de 2219 km que va desde La Guajira hasta la Amazonia.",
      "image": "/static/img/questions_soc/q13.png",
      "image_alt": "Ilustración: Frontera más extensa - Venezuela (2219 km)"
    },
    {
      "id": 14,
      "category": "Tema 3: Fronteras de Colombia",
      "question": "¿Para qué sirven los tratados internacionales de límites que Colombia ha firmado con sus países vecinos?",
      "context": "Guía de Ciencias Sociales - Página 3: Tratados Internacionales de Límites\nAcuerdos pacíficos de límites.",
      "options": [
        "Para acordar y fijar con precisión las fronteras oficiales y garantizar la paz y el respeto mutuo entre las naciones",
        "Para declarar la guerra y conquistar territorios por la fuerza de las armas",
        "Para impedir por completo que las personas puedan hablar otros idiomas",
        "Para cambiar los mapas del mundo todos los meses sin ningún motivo"
      ],
      "correct_answer": "Para acordar y fijar con precisión las fronteras oficiales y garantizar la paz y el respeto mutuo entre las naciones",
      "explanation": "Los tratados de límites son acuerdos diplomáticos entre países soberanos que definen claramente los límites territoriales y marítimos para convivir en paz y cooperación.",
      "image": "/static/img/questions_soc/q14.png",
      "image_alt": "Ilustración: Tratados Internacionales de Límites"
    },
    {
      "id": 15,
      "category": "Tema 3: Fronteras de Colombia",
      "question": "¿Por qué son tan importantes las zonas fronterizas para el desarrollo y la convivencia de nuestro país?",
      "context": "Guía de Ciencias Sociales - Página 3: Zonas Fronterizas\nIntegración comercial y cultural.",
      "options": [
        "Porque permiten el intercambio comercial, facilitan la unión cultural y generan empleo y bienestar entre pueblos hermanos",
        "Porque son zonas donde nadie puede vivir ni circular jamás",
        "Porque solo sirven para construir murallas gigantescas de piedra",
        "Porque no tienen ningún valor para la economía ni la sociedad"
      ],
      "correct_answer": "Porque permiten el intercambio comercial, facilitan la unión cultural y generan empleo y bienestar entre pueblos hermanos",
      "explanation": "Las zonas de frontera son puntos dinámicos de integración, donde se dinamiza el comercio bilateral, la cultura compartida y la cooperación solidaria entre naciones.",
      "image": "/static/img/questions_soc/q15.png",
      "image_alt": "Ilustración: Importancia de las Zonas Fronterizas"
    },
    {
      "id": 16,
      "category": "Tema 4: Periodos Históricos",
      "question": "¿Cuáles son los cuatro grandes periodos en los que se divide el estudio de la historia de Colombia?",
      "context": "Guía de Ciencias Sociales - Página 4: Los 4 Periodos Históricos\nEtapas de la historia nacional.",
      "options": [
        "Periodo Indígena, Periodo Hispánico, Periodo de la Independencia y Periodo de la República",
        "Edad de Piedra, Edad de los Dinosaurios, Era del Hielo y Era Espacial",
        "Mes de Enero, Mes de Junio, Vacaciones de Mitad de Año y Navidad",
        "Primer Periodo Escolar, Segundo Periodo, Tercer Periodo y Cuarto Periodo"
      ],
      "correct_answer": "Periodo Indígena, Periodo Hispánico, Periodo de la Independencia y Periodo de la República",
      "explanation": "La historia colombiana se organiza en cuatro grandes épocas: Indígena (más de 20 000 años), Hispánico (1500-1810), Independencia (1810-1819) y República (1819 hasta el presente).",
      "image": "/static/img/questions_soc/q16.png",
      "image_alt": "Ilustración: Los 4 Grandes Periodos Históricos de Colombia"
    },
    {
      "id": 17,
      "category": "Tema 4: Periodos Históricos",
      "question": "¿Cuánto tiempo aproximadamente duró el poblamiento indígena en nuestro territorio antes del año 1500?",
      "context": "Guía de Ciencias Sociales - Página 4: El Periodo Indígena\nPobladores originarios de Colombia.",
      "options": [
        "Más de 20 000 años, ocupando diversas regiones desde la costa hasta los Andes",
        "Solamente dos semanas durante un viaje de campamento",
        "Cien años exactos desde la fundación de Bogotá",
        "Tres meses antes de la llegada de Cristóbal Colón"
      ],
      "correct_answer": "Más de 20 000 años, ocupando diversas regiones desde la costa hasta los Andes",
      "explanation": "El periodo indígena es el más extenso de nuestra historia: abarca más de 20 000 años desde que los primeros pobladores llegaron a Colombia hasta el año 1500.",
      "image": "/static/img/questions_soc/q17.png",
      "image_alt": "Ilustración: El Periodo Indígena en Colombia"
    },
    {
      "id": 18,
      "category": "Tema 4: Periodos Históricos",
      "question": "¿Cuáles fueron las tres familias lingüísticas indígenas más representativas que habitaron el territorio colombiano?",
      "context": "Guía de Ciencias Sociales - Página 4: Familias Lingüísticas Prehispánicas\nGrandes grupos aborígenes.",
      "options": [
        "La familia Chibcha, la familia Caribe y la familia Arawac",
        "La familia Pérez, la familia Gómez y la familia Rodríguez",
        "La familia del Inglés, la del Francés y la del Alemán",
        "La familia de los Reptiles, de las Aves y de los Mamíferos"
      ],
      "correct_answer": "La familia Chibcha, la familia Caribe y la familia Arawac",
      "explanation": "Las tres grandes familias lingüísticas que conformaron la población nativa colombiana fueron la Chibcha (Muiscas y Taironas), la Caribe (costas y ríos) y la Arawac (Llanos y selvas).",
      "image": "/static/img/questions_soc/q18.png",
      "image_alt": "Ilustración: Tres Familias Lingüísticas Prehispánicas"
    },
    {
      "id": 19,
      "category": "Tema 4: Periodos Históricos",
      "question": "¿En qué año concluyó el Periodo Indígena y qué hecho histórico marcó este gran cambio en Colombia?",
      "context": "Guía de Ciencias Sociales - Página 4: Fin del Periodo Indígena\nLlegada de los navegantes españoles.",
      "options": [
        "En el año 1500, con la llegada y expediciones marítimas de los españoles a las costas del mar Caribe",
        "En el año 2026, con la invención de los teléfonos inteligentes e internet",
        "En el año 1819, con la batalla final en el Puente de Boyacá",
        "En el año 1950, con la inauguración del primer aeropuerto en el país"
      ],
      "correct_answer": "En el año 1500, con la llegada y expediciones marítimas de los españoles a las costas del mar Caribe",
      "explanation": "El año 1500 señala el final del periodo indígena y el inicio de la presencia española en nuestro territorio a través de las expediciones en el litoral caribeño.",
      "image": "/static/img/questions_soc/q19.png",
      "image_alt": "Ilustración: Llegada de los Españoles en el Año 1500"
    },
    {
      "id": 20,
      "category": "Tema 4: Periodos Históricos",
      "question": "¿Por qué los historiadores dividen el pasado en 'periodos históricos'?",
      "context": "Guía de Ciencias Sociales - Página 4: Definición de Periodo Histórico\nOrganización cronológica del pasado.",
      "options": [
        "Porque facilita organizar, estudiar y comprender las grandes transformaciones sociales, políticas y culturales a lo largo del tiempo",
        "Porque es obligatorio que todos los libros tengan exactamente el mismo número de hojas",
        "Porque a los presidentes no les gustaba recordar los años anteriores",
        "Para que los estudiantes no tengan que estudiar las fechas de nacimiento de sus abuelos"
      ],
      "correct_answer": "Porque facilita organizar, estudiar y comprender las grandes transformaciones sociales, políticas y culturales a lo largo del tiempo",
      "explanation": "Un periodo histórico es un lapso en el que la sociedad comparte características y experimenta cambios estructurales, facilitando su comprensión paso a paso.",
      "image": "/static/img/questions_soc/q20.png",
      "image_alt": "Ilustración: ¿Qué es un Periodo Histórico?"
    },
    {
      "id": 21,
      "category": "Tema 5: Periodo Hispánico",
      "question": "¿Qué tres etapas o momentos consecutivos conforman el Periodo Hispánico en Colombia (1500 a 1810)?",
      "context": "Guía de Ciencias Sociales - Página 5: Fases del Periodo Hispánico\nDescubrimiento, Conquista y Colonia.",
      "options": [
        "Descubrimiento de las costas, Conquista del interior del territorio y Época de la Colonia",
        "Navidad, Año Nuevo y Vacaciones de Reyes Magos",
        "Siembra de semillas, regado con manguera y cosecha de frutos",
        "Desayuno campesino, almuerzo corriente y cena ligera"
      ],
      "correct_answer": "Descubrimiento de las costas, Conquista del interior del territorio y Época de la Colonia",
      "explanation": "El periodo hispánico comprende: 1) Descubrimiento (llegada a las costas), 2) Conquista (expedición armada y fundaciones) y 3) Colonia (administración colonial virreinal).",
      "image": "/static/img/questions_soc/q21.png",
      "image_alt": "Ilustración: El Periodo Hispánico - 1500 a 1810"
    },
    {
      "id": 22,
      "category": "Tema 5: Periodo Hispánico",
      "question": "¿Cuáles fueron las primeras ciudades y villas fundadas por los conquistadores españoles mencionadas en la guía?",
      "context": "Guía de Ciencias Sociales - Página 5: Ciudades Fundadas en la Conquista\nCentros urbanos coloniales.",
      "options": [
        "Santa Marta (1525), Cartagena de Indias (1533) y Santafé de Bogotá (1538)",
        "Montería, Cereté, Lorica y Sahagún",
        "Nueva York, Miami, Los Ángeles y Chicago",
        "Madrid, Barcelona, Sevilla y Valencia"
      ],
      "correct_answer": "Santa Marta (1525), Cartagena de Indias (1533) y Santafé de Bogotá (1538)",
      "explanation": "Entre las primeras ciudades fundadas se destacan Santa Marta (1525 por Rodrigo de Bastidas), Cartagena (1533 por Pedro de Heredia) y Bogotá (1538 por Jiménez de Quesada).",
      "image": "/static/img/questions_soc/q22.png",
      "image_alt": "Ilustración: Fundación de Ciudades en la Conquista"
    },
    {
      "id": 23,
      "category": "Tema 5: Periodo Hispánico",
      "question": "¿Cuántos años duró aproximadamente la época de la Colonia española en Colombia antes de los gritos de independencia?",
      "context": "Guía de Ciencias Sociales - Página 5: Duración de la Colonia\nTres siglos de dominio virreinal.",
      "options": [
        "Aproximadamente 300 años (tres siglos completos de administración colonial)",
        "Solamente 10 años entre 1800 y 1810",
        "Un siglo y medio (50 años)",
        "Mil quinientos años continuos"
      ],
      "correct_answer": "Aproximadamente 300 años (tres siglos completos de administración colonial)",
      "explanation": "La Colonia duró unos 300 años (aproximadamente desde mediados del siglo XVI hasta 1810), consolidando instituciones, pueblos y formas de vida virreinales.",
      "image": "/static/img/questions_soc/q23.png",
      "image_alt": "Ilustración: La Colonia - 300 Años de Dominio"
    },
    {
      "id": 24,
      "category": "Tema 5: Periodo Hispánico",
      "question": "¿Qué es el fenómeno del 'mestizaje' y qué tres grupos raciales y culturales se unieron en Colombia?",
      "context": "Guía de Ciencias Sociales - Página 5: El Mestizaje en Colombia\nFusión triétnica nacional.",
      "options": [
        "La mezcla biológica y cultural entre los indígenas nativos, los españoles blancos y los africanos negros",
        "La preparación de jugos mezclando frutas de tres colores diferentes",
        "Un desfile de trajes típicos que se realiza cada año en el mes de agosto",
        "La construcción de casas usando madera, cemento y ladrillos cocidos"
      ],
      "correct_answer": "La mezcla biológica y cultural entre los indígenas nativos, los españoles blancos y los africanos negros",
      "explanation": "El mestizaje fue el proceso de unión e integración de tres raíces fundamentales: los indígenas originarios, los colonizadores europeos españoles y los afrodescendientes traídos de África.",
      "image": "/static/img/questions_soc/q24.png",
      "image_alt": "Ilustración: El Mestizaje - Fusión de Tres Culturas"
    },
    {
      "id": 25,
      "category": "Tema 5: Periodo Hispánico",
      "question": "¿Cuáles fueron algunos de los principales aportes culturales, religiosos e instrumentales que trajeron los españoles a América?",
      "context": "Guía de Ciencias Sociales - Página 5: Aportes de la Cultura Hispánica\nHerencia colonial española.",
      "options": [
        "El idioma castellano o español, la religión católica, animales domésticos (vacas, caballos, gallinas) y nuevas formas de arquitectura",
        "El cultivo tradicional de la yuca y el uso de la cerbatana para cazar",
        "El tejido tradicional de las hamacas arawac y las mochilas arhuacas",
        "Los teléfonos celulares inteligentes y las computadoras portátiles"
      ],
      "correct_answer": "El idioma castellano o español, la religión católica, animales domésticos (vacas, caballos, gallinas) y nuevas formas de arquitectura",
      "explanation": "Los españoles introdujeron el idioma español, la religión católica, las leyes escritas, animales domésticos como el caballo y la vaca, la rueda y la arquitectura urbana de plazas e iglesias.",
      "image": "/static/img/questions_soc/q25.png",
      "image_alt": "Ilustración: Aportes Culturales de los Españoles"
    },
    {
      "id": 26,
      "category": "Tema 6: Periodo de la República",
      "question": "¿En qué año inició el Periodo de la República en Colombia y con qué histórico documento comenzó?",
      "context": "Guía de Ciencias Sociales - Página 6: Nacimiento del Periodo Republicano\nEl acta del 20 de julio de 1810.",
      "options": [
        "En 1810, con la firma del Acta de la proclamación de la Independencia de la Nueva Granada",
        "En 1500, con el desembarco de carabelas en la bahía de Santa Marta",
        "En 1991, con la inauguración del Metro de Medellín",
        "En 1492, con el descubrimiento del continente americano"
      ],
      "correct_answer": "En 1810, con la firma del Acta de la proclamación de la Independencia de la Nueva Granada",
      "explanation": "El periodo republicano inició en 1810 cuando los patriotas proclamaron la Independencia frente a la monarquía española a través del Acta del 20 de julio.",
      "image": "/static/img/questions_soc/q26.png",
      "image_alt": "Ilustración: El Periodo de la República - 1810 hasta hoy"
    },
    {
      "id": 27,
      "category": "Tema 6: Periodo de la República",
      "question": "¿En qué histórica batalla y en qué fecha exacta se selló definitivamente el triunfo de la Campaña Libertadora colombiana?",
      "context": "Guía de Ciencias Sociales - Página 6: La Batalla de Boyacá\nTriunfo del Ejército Libertador.",
      "options": [
        "En la Batalla de Boyacá, el 7 de agosto de 1819",
        "En el combate naval de San Andrés, el 20 de julio de 1810",
        "En la batalla de las Termópilas, el 1 de enero de 1900",
        "En la toma del Fuerte de Bocachica, el 12 de octubre de 1492"
      ],
      "correct_answer": "En la Batalla de Boyacá, el 7 de agosto de 1819",
      "explanation": "El 7 de agosto de 1819, en el Puente de Boyacá, el ejército libertador comandado por Simón Bolívar selló el triunfo definitivo que dio origen a la república independiente.",
      "image": "/static/img/questions_soc/q27.png",
      "image_alt": "Ilustración: Batalla de Boyacá - 7 de Agosto de 1819"
    },
    {
      "id": 28,
      "category": "Tema 6: Periodo de la República",
      "question": "Durante el siglo XIX, ¿cuáles fueron algunos de los nombres oficiales que tuvo nuestra nación antes del nombre actual?",
      "context": "Guía de Ciencias Sociales - Página 6: Nombres Históricos de Colombia\nEvolución constitucional de la nación.",
      "options": [
        "La Gran Colombia, República de la Nueva Granada, Confederación Granadina y Estados Unidos de Colombia",
        "Imperio Azteca, Reino de España, Virreinato del Perú y Capitanía de Chile",
        "República de Córdoba, Estado de Antioquia, Villa de Medellín y Reino de Cartagena",
        "Norteamérica del Sur, Antillas Mayores, Territorios del Amazonas y Patagonia"
      ],
      "correct_answer": "La Gran Colombia, República de la Nueva Granada, Confederación Granadina y Estados Unidos de Colombia",
      "explanation": "A lo largo de los siglos XIX, según las distintas constituciones, el país se llamó La Gran Colombia (1819), Rep. Neogranadina (1831), Conf. Granadina (1858) y EE.UU. de Colombia (1863).",
      "image": "/static/img/questions_soc/q28.png",
      "image_alt": "Ilustración: Evolución de Nombres de Colombia (Siglo XIX)"
    },
    {
      "id": 29,
      "category": "Tema 6: Periodo de la República",
      "question": "¿A partir de qué año y mediante qué Constitución política nuestro país adoptó el nombre definitivo de 'República de Colombia'?",
      "context": "Guía de Ciencias Sociales - Página 6: Nombre Definitivo de Colombia\nConstitución de 1886.",
      "options": [
        "Desde el año 1886, con la Constitución política de 1886",
        "Desde el año 1525, cuando se fundó la villa de Santa Marta",
        "Desde el año 1950, durante el gobierno de la Junta Militar",
        "Desde el año 1810, cuando se firmó el Acta de Independencia"
      ],
      "correct_answer": "Desde el año 1886, con la Constitución política de 1886",
      "explanation": "La Constitución de 1886 fijó definitivamente el nombre 'República de Colombia' que nos identifica hasta el día de hoy como una sola nación unificada.",
      "image": "/static/img/questions_soc/q29.png",
      "image_alt": "Ilustración: Desde 1886 - República de Colombia"
    },
    {
      "id": 30,
      "category": "Tema 6: Periodo de la República",
      "question": "¿Cuáles fueron los productos agrícolas y minerales que impulsaron las exportaciones de Colombia hacia los mercados mundiales en la era republicana?",
      "context": "Guía de Ciencias Sociales - Página 6: Economía de Exportación Republicana\nComercio exterior de Colombia.",
      "options": [
        "El café, el banano, las flores de exportación, el carbón, el petróleo y el oro",
        "La venta de nieve congelada traída de los polos árticos",
        "La fabricación y venta masiva de naves espaciales y satélites",
        "La exportación de automóviles de carreras de alta velocidad"
      ],
      "correct_answer": "El café, el banano, las flores de exportación, el carbón, el petróleo y el oro",
      "explanation": "Colombia se insertó en la economía internacional principalmente a través de la exportación de café de excelente calidad, banano, flores, carbón, petróleo y oro.",
      "image": "/static/img/questions_soc/q30.png",
      "image_alt": "Ilustración: Productos Clave de Exportación"
    },
    {
      "id": 31,
      "category": "Tema 7: Sectores de la Economía",
      "question": "¿Cuáles son los tres grandes sectores en los que se clasifican las actividades económicas de un país?",
      "context": "Guía de Ciencias Sociales - Página 7: Los 3 Sectores Económicos\nOrganización de la producción.",
      "options": [
        "Sector Primario (extracción), Sector Secundario (industria) y Sector Terciario (servicios)",
        "Sector de Juegos, Sector de Recreo y Sector de Descanso en la casa",
        "Sector de Verano, Sector de Invierno y Sector de Otoño",
        "Sector Escolar, Sector Universitario y Sector de Jubilados"
      ],
      "correct_answer": "Sector Primario (extracción), Sector Secundario (industria) y Sector Terciario (servicios)",
      "explanation": "Las actividades económicas se clasifican en tres sectores: Primario (obtención de recursos naturales), Secundario (transformación industrial) y Terciario (prestación de servicios).",
      "image": "/static/img/questions_soc/q31.png",
      "image_alt": "Ilustración: Los 3 Sectores de la Economía"
    },
    {
      "id": 32,
      "category": "Tema 7: Sectores de la Economía",
      "question": "¿Qué tipo de labores integran el Sector Primario de la economía según la guía de Sociales?",
      "context": "Guía de Ciencias Sociales - Página 7: El Sector Primario\nExtracción directa de la naturaleza.",
      "options": [
        "Actividades dedicadas a la extracción directa de la naturaleza: agricultura, ganadería, pesca, silvicultura y minería",
        "La atención de clientes en la ventanilla de un banco o una caja registradora",
        "El diseño de programas de computador y aplicaciones para celulares",
        "La confección de camisas y vestidos en una gran fábrica textil"
      ],
      "correct_answer": "Actividades dedicadas a la extracción directa de la naturaleza: agricultura, ganadería, pesca, silvicultura y minería",
      "explanation": "El sector primario abarca todas las actividades que obtienen materias primas directamente de los recursos naturales: cultivar café, ordeñar vacas, pescar y extraer carbón o petróleo.",
      "image": "/static/img/questions_soc/q32.png",
      "image_alt": "Ilustración: El Sector Primario - Recursos de la Naturaleza"
    },
    {
      "id": 33,
      "category": "Tema 7: Sectores de la Economía",
      "question": "¿Cuál es la función principal del Sector Secundario o industrial dentro de la economía colombiana?",
      "context": "Guía de Ciencias Sociales - Página 7: El Sector Secundario\nFábricas e industrias transformadoras.",
      "options": [
        "Transformar las materias primas que vienen de la naturaleza en productos elaborados listos para el consumo",
        "Sembrar semillas de tomate en una huerta escolar",
        "Vender pasajes aéreos en una agencia de viajes de la ciudad",
        "Cuidar a los pacientes enfermos en un hospital municipal"
      ],
      "correct_answer": "Transformar las materias primas que vienen de la naturaleza en productos elaborados listos para el consumo",
      "explanation": "El sector secundario comprende las fábricas e industrias que transforman las materias primas en bienes útiles, por ejemplo: convertir la leche en queso o el algodón en hilos y ropa.",
      "image": "/static/img/questions_soc/q33.png",
      "image_alt": "Ilustración: El Sector Secundario - Fábricas e Industrias"
    },
    {
      "id": 34,
      "category": "Tema 7: Sectores de la Economía",
      "question": "¿Qué clase de ocupaciones y oficios pertenecen al Sector Terciario de la economía?",
      "context": "Guía de Ciencias Sociales - Página 7: El Sector Terciario\nPrestación de servicios a la comunidad.",
      "options": [
        "La prestación de servicios como el comercio, transporte, banca, salud, educación y turismo",
        "La siembra de maíz y la recolección manual de granos de café",
        "La fundición de hierro en una acería pesada",
        "La extracción de oro en las profundidades de una mina subterránea"
      ],
      "correct_answer": "La prestación de servicios como el comercio, transporte, banca, salud, educación y turismo",
      "explanation": "El sector terciario no produce bienes materiales directos, sino servicios fundamentales para la comunidad: tiendas comerciales, transporte público, médicos en hospitales, profesores en colegios y bancos.",
      "image": "/static/img/questions_soc/q34.png",
      "image_alt": "Ilustración: El Sector Terciario - Prestación de Servicios"
    },
    {
      "id": 35,
      "category": "Tema 7: Sectores de la Economía",
      "question": "Según la guía, ¿cuál es uno de los mayores desafíos para el desarrollo socioeconómico de Colombia?",
      "context": "Guía de Ciencias Sociales - Página 7: Retos Económicos y Bienestar\nSuperación de la desigualdad.",
      "options": [
        "Superar las grandes desigualdades mediante una distribución más justa y equilibrada de los bienes y servicios para todas las familias",
        "Cerrar todos los colegios y hospitales para ahorrar energía eléctrica",
        "Dejar de producir alimentos en el campo para comprar todo en el extranjero",
        "Prohibir que los campesinos vendan sus cosechas en los mercados"
      ],
      "correct_answer": "Superar las grandes desigualdades mediante una distribución más justa y equilibrada de los bienes y servicios para todas las familias",
      "explanation": "Uno de los principales retos del país es garantizar que el crecimiento económico beneficie a todas las regiones y familias, reduciendo la pobreza con mejor educación, salud y empleo.",
      "image": "/static/img/questions_soc/q35.png",
      "image_alt": "Ilustración: Superar las Desigualdades Socioeconómicas"
    },
    {
      "id": 36,
      "category": "Tema 8: Diversidad Cultural",
      "question": "¿Por qué se dice que Colombia es un país con una gran diversidad cultural regional?",
      "context": "Guía de Ciencias Sociales - Página 8: Diversidad Cultural Regional\nRiqueza de tradiciones y costumbres.",
      "options": [
        "Porque sus regiones tienen costumbres propias, dialectos y formas de hablar variadas, trajes típicos, platos tradicionales y danzas folclóricas únicas",
        "Porque todas las personas de Colombia se visten y comen exactamente lo mismo a la misma hora",
        "Porque en el país solo existe un único pueblo y una sola fiesta patronal",
        "Porque los niños no tienen derecho a aprender a bailar ni cantar canciones tradicionales"
      ],
      "correct_answer": "Porque sus regiones tienen costumbres propias, dialectos y formas de hablar variadas, trajes típicos, platos tradicionales y danzas folclóricas únicas",
      "explanation": "Colombia es una nación pluriétnica y multicultural: cada región (costeña, paisa, andina, llanera, pacífica) tiene sus propias comidas, acentos, expresiones artísticas y tradiciones que nos enriquecen.",
      "image": "/static/img/questions_soc/q36.png",
      "image_alt": "Ilustración: Diversidad Regional y Costumbres"
    },
    {
      "id": 37,
      "category": "Tema 8: Diversidad Cultural",
      "question": "¿Quiénes son cuatro de los más destacados exponentes colombianos en las artes y la cultura reconocidos a nivel mundial según la guía?",
      "context": "Guía de Ciencias Sociales - Página 8: Exponentes de la Cultura Colombiana\nArtistas de talla mundial.",
      "options": [
        "Gabriel García Márquez, Fernando Botero, Shakira y Juanes",
        "Cristóbal Colón, Gonzalo Jiménez de Quesada, Rodrigo de Bastidas y Pedro de Heredia",
        "Simón Bolívar, Francisco de Paula Santander, Antonio Nariño y Policarpa Salavarrieta",
        "Albert Einstein, Isaac Newton, Thomas Alva Edison y Alexander Graham Bell"
      ],
      "correct_answer": "Gabriel García Márquez, Fernando Botero, Shakira y Juanes",
      "explanation": "Los 4 grandes exponentes de proyección internacional destacados en la guía son: Gabriel García Márquez (literatura), Fernando Botero (escultura y pintura), Shakira y Juanes (música).",
      "image": "/static/img/questions_soc/q37.png",
      "image_alt": "Ilustración: Exponentes de la Cultura Colombiana"
    },
    {
      "id": 38,
      "category": "Tema 8: Diversidad Cultural",
      "question": "¿Por qué es célebre y recordado en todo el mundo el escritor colombiano Gabriel García Márquez ('Gabo')?",
      "context": "Guía de Ciencias Sociales - Página 8: Gabriel García Márquez\nPremio Nobel de Literatura.",
      "options": [
        "Porque ganó el prestigioso Premio Nobel de Literatura (1982) y escribió obras maestras como 'Cien años de soledad'",
        "Porque fue un famoso arquero de fútbol que atajó un penal en un mundial",
        "Porque descubrió una cura médica para las enfermedades tropicales",
        "Porque construyó el puente más largo del río Magdalena en canoa"
      ],
      "correct_answer": "Porque ganó el prestigioso Premio Nobel de Literatura (1982) y escribió obras maestras como 'Cien años de soledad'",
      "explanation": "Gabriel García Márquez, nacido en Aracataca (Magdalena), recibió el Premio Nobel de Literatura en 1982 y es considerado uno de los escritores más geniales de la literatura universal por su 'realismo mágico'.",
      "image": "/static/img/questions_soc/q38.png",
      "image_alt": "Ilustración: Gabriel García Márquez - Premio Nobel"
    },
    {
      "id": 39,
      "category": "Tema 8: Diversidad Cultural",
      "question": "¿Cuál es el rasgo artístico más conocido de las pinturas y esculturas monumentales del maestro Fernando Botero?",
      "context": "Guía de Ciencias Sociales - Página 8: Maestro Fernando Botero\nEl estilo Boterismo.",
      "options": [
        "El estilo 'Boterismo', caracterizado por figuras humanas, animales y objetos de grandes volúmenes y formas redondeadas",
        "Pintar únicamente pequeños puntos negros diminutos invisibles a simple vista",
        "Hacer esculturas de hielo que se derriten en menos de dos minutos al sol",
        "Dibujar exclusivamente líneas rectas de color gris sobre lienzos vacíos"
      ],
      "correct_answer": "El estilo 'Boterismo', caracterizado por figuras humanas, animales y objetos de grandes volúmenes y formas redondeadas",
      "explanation": "El maestro antioqueño Fernando Botero creó una estética universal inconfundible conocida como el 'Boterismo', caracterizada por la exaltación del volumen y las formas robustas en pinturas y esculturas.",
      "image": "/static/img/questions_soc/q39.png",
      "image_alt": "Ilustración: Fernando Botero - Pintura y Escultura"
    },
    {
      "id": 40,
      "category": "Tema 8: Diversidad Cultural",
      "question": "¿En qué ámbito artístico han triunfado en los escenarios de todo el mundo los colombianos Shakira y Juanes?",
      "context": "Guía de Ciencias Sociales - Página 8: Shakira y Juanes\nEmbajadores de la música colombiana.",
      "options": [
        "En la música pop, rock y la difusión de los ritmos folclóricos colombianos a nivel internacional",
        "En la natación de carreras y clavados olímpicos de gran altura",
        "En la ingeniería civil para la construcción de túneles y rascacielos",
        "En la cocina molecular dentro de restaurantes espaciales"
      ],
      "correct_answer": "En la música pop, rock y la difusión de los ritmos folclóricos colombianos a nivel internacional",
      "explanation": "Shakira (desde Barranquilla) y Juanes (desde Antioquia) son embajadores culturales de Colombia en el mundo de la música, ganadores de múltiples premios Grammy y queridos por millones de personas.",
      "image": "/static/img/questions_soc/q40.png",
      "image_alt": "Ilustración: Shakira y Juanes - Embajadores Musicales"
    }
  ]
}

out_path = os.path.abspath("app/subjects/sociales.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(sociales_data, f, ensure_ascii=False, indent=2)

print(f"[OK] Creado exitosamente {out_path} con {len(sociales_data['questions'])} preguntas.")
