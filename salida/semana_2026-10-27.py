"""Guiones de la semana 27 oct - 1 nov 2026 (plantilla pinterest). Genera salida/<fecha_hora>/guion.json."""
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
f = lambda n: f"aritz927_{n:02d}.jpg"

C = []  # (carpeta, hora_publicacion, tema, formato, audio, slides, caption)

C.append(("2026-10-27_2040", "2026-10-27 20:40", "antes/ahora: de jugar a vender", "antes / ahora",
 "Untitled #13 (Slowed + Reverb) — glwzbll", [
  {"titulo": "2020:", "texto": "«bro, ¿dónde caemos?»", "foto": f(36), "vinted": True},
  {"titulo": "2026:", "texto": "«bro, ¿cuántos paquetes hemos mandado hoy?»", "foto": f(5)},
  {"titulo": "lo que cambió:", "texto": "dejé de pasar horas en el sofá y empecé a pasarlas subiendo prendas", "foto": f(32)},
  {"titulo": "¿y tú en qué año estás?", "texto": "{amarillo:2020} o {verde:2026} 👇", "foto": f(11)},
  {"titulo": "si quieres empezar,", "texto": "comenta “{verde:proveedores}” y te paso los míos", "foto": f(6), "guia": "pack"}],
 "2020 vs 2026 😂 ¿en qué año estás tú?\n\ncomenta “proveedores” y te paso los míos 📦\n👉 Guías en el link de mi bio\n\n#vinted #reventa #proveedores #fyp #emprender"))

C.append(("2026-10-27_2335", "2026-10-27 23:35", "motivación: empezar joven", "motivación con giro",
 "Im thinking of you again — wa", [
  {"titulo": "empieza tu negocio con 18 años", "foto": f(25), "vinted": True},
  {"titulo": "pero…", "foto": f(28)},
  {"titulo": "lo que nadie te cuenta:", "texto": "- vas a decir que no a muchos planes\n- tu familia no lo va a entender\n- habrá semanas sin una venta\n- pensarán que pierdes el tiempo", "foto": f(32)},
  {"titulo": "y un día", "texto": "miras atrás y entiendes por qué lo hiciste", "foto": f(30)},
  {"titulo": "¿cuántos años tienes tú?", "texto": "los míos están en la guía: escribe “{verde:proveedores}”", "foto": f(24), "guia": "pack"}],
 "nadie te avisa de esta parte 🌙\n¿cuántos años tienes tú?\n\nescribe “proveedores” y te los mando 📩\n👉 Guías en el link de mi bio\n\n#emprendimiento #vinted #reventa #mentalidad #proveedores"))

C.append(("2026-10-28_0935", "2026-10-28 09:35", "serie proveedores: ropa (parte 1)", "serie de proveedores",
 "tesla (slowed electro mix) — Fixupboy", [
  {"titulo": "proveedores de ropa que tienes que conocer", "sub": "(parte 1)", "foto": f(26), "vinted": True},
  {"titulo": "proveedor de sudaderas de marca", "texto": "lo que más rota en otoño e invierno. Margen alto y se vende rápido en Vinted.", "foto": f(38)},
  {"titulo": "proveedor de conjuntos deportivos", "texto": "camiseta + pantalón. Se venden en pack y suben el precio de cada venta.", "foto": f(17)},
  {"titulo": "proveedor por kilo", "texto": "lotes variados para empezar con poco. Clasificas y subes lo bueno.", "foto": f(29)},
  {"titulo": "los contactos están en la guía", "texto": "comenta “{verde:proveedores}” y te paso el link", "foto": f(9), "guia": "ropa"}],
 "proveedores de ropa para revender en Vinted (parte 1) 👕\n¿cuál quieres en la parte 2?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#proveedores #vinted #revenderropa #reventa #mayorista"))

C.append(("2026-10-28_1240", "2026-10-28 12:40", "compra→venta: menos de 10€", "precio compra → venta",
 "Cavendish Banana — Bruno Boe", [
  {"titulo": "lo que compro a menos de 10€ y se vende solo", "sub": "(precios de ejemplo)", "foto": f(38), "vinted": True},
  {"titulo": "camiseta de marca", "precios": ["6€", "22€"], "foto": f(17)},
  {"titulo": "sudadera gráfica", "precios": ["9€", "35€"], "foto": f(38)},
  {"titulo": "caja de juguetes de colección", "precios": ["8€", "25€"], "foto": f(3)},
  {"titulo": "¿cuál comprarías tú primero?", "texto": "dónde comprarlos, en la guía: comenta “{verde:proveedores}”", "foto": f(6), "guia": "pack"}],
 "cosas de menos de 10€ que se venden solas en Vinted 💸 (precios de ejemplo)\n¿cuál comprarías tú?\n\n¿los quieres? comenta “proveedores” 📦\n👉 Guías en el link de mi bio\n\n#vinted #reventa #proveedores #negocio #fyp"))

C.append(("2026-10-28_1725", "2026-10-28 17:25", "error→solución: visitas sin ventas", "error → solución",
 "Time Back — Sinny & 7vvch", [
  {"titulo": "100 visitas y 0 ventas", "sub": "el fallo casi nunca es la prenda", "foto": f(23), "vinted": True},
  {"titulo": "1. tu precio no compite", "texto": "mira 3 prendas iguales vendidas y ponte un poco por debajo", "foto": f(28)},
  {"titulo": "2. la 1ª foto no enseña nada", "texto": "prenda entera, luz de ventana, fondo limpio", "foto": f(29)},
  {"titulo": "3. tardas en contestar", "texto": "quien pregunta y no recibe respuesta en 1 hora, compra en otra cuenta", "foto": f(11)},
  {"titulo": "¿cuántas visitas tiene tu última prenda?", "texto": "y si te falta buen stock: comenta “{verde:proveedores}”", "foto": f(32), "guia": "pack"}],
 "muchas visitas en Vinted pero 0 ventas 😩 mira esto\n¿cuántas visitas tiene tu última prenda?\n\ncomenta “proveedores” y te digo cuáles uso 👇\n👉 Guías en el link de mi bio\n\n#vinted #trucosvinted #revenderropa #proveedores #reventa"))

C.append(("2026-10-28_2035", "2026-10-28 20:35", "lista: errores de novato", "lista de errores",
 "sdp interlude (Slowed) — VTX", [
  {"titulo": "3 errores de todo revendedor novato", "sub": "(el 3 es el que más dinero cuesta)", "foto": f(32), "vinted": True},
  {"titulo": "1. comprar lo que te gusta a ti", "texto": "compra lo que ya se vende. Mira los «vendidos» antes de pedir nada.", "foto": f(22)},
  {"titulo": "2. gastarte lo que ganas", "texto": "las primeras ventas vuelven al stock. Así crece el negocio.", "foto": f(15)},
  {"titulo": "3. comprar al primer proveedor que ves", "texto": "pide muestras y reseñas. Un mal lote te come el margen de un mes.", "foto": f(26)},
  {"titulo": "guárdalo para cuando empieces", "texto": "y si quieres proveedores probados: comenta “{verde:proveedores}”", "foto": f(30), "guia": "pack"}],
 "3 errores que comete todo el que empieza a revender 🚫\n¿cuál has cometido tú? 1, 2 o 3\n\ncomenta “proveedores” y te paso el link 📦\n👉 Guías en el link de mi bio\n\n#reventa #vinted #emprendimiento #proveedores #wallapop"))

C.append(("2026-10-28_2340", "2026-10-28 23:40", "aprendizajes revendiendo", "aprendizajes",
 "Untitled #13 (Slowed + Reverb) — glwzbll", [
  {"titulo": "cosas que aprendí revendiendo en Vinted", "foto": f(4), "vinted": True},
  {"titulo": "vender barato no es vender más", "texto": "es trabajar el doble por lo mismo", "foto": f(13)},
  {"titulo": "el stock parado es dinero dormido", "texto": "si en 3 semanas no se vende, baja el precio y rota", "foto": f(20)},
  {"titulo": "la constancia gana a la suerte", "texto": "subir un poco cada día > subir 50 un domingo", "foto": f(32)},
  {"titulo": "y que el proveedor lo es todo", "texto": "los míos, en la guía: escribe “{verde:proveedores}”", "foto": f(30), "guia": "pack"}],
 "lo que aprendí revendiendo, de verdad 🌙\n¿cuál te ha pasado a ti?\n\nescribe “proveedores” y te los mando 📩\n👉 Guías en el link de mi bio\n\n#vinted #reventa #mentalidad #proveedores #emprender"))

C.append(("2026-10-29_0930", "2026-10-29 09:30", "riesgo de cuenta: limitaciones", "riesgo de cuenta",
 "Self Aware — Mark Allan Wolfe", [
  {"titulo": "esto hace que Vinted te limite la cuenta 🚫", "caja": True, "foto": f(23), "vinted": True},
  {"titulo": "1. subir muchas prendas de golpe en una cuenta nueva", "foto": f(5)},
  {"titulo": "2. la misma descripción copiada en todo", "foto": f(32)},
  {"titulo": "3. pasar tu número o enlaces por el chat", "texto": "todo dentro de Vinted, siempre", "foto": f(11)},
  {"titulo": "¿te ha pasado alguna vez?", "texto": "¿te paso mis proveedores? comenta “{verde:proveedores}”", "foto": f(25), "guia": "pack"}],
 "cosas que hacen que Vinted te limite la cuenta 🚫\n¿te ha pasado?\n\n¿te paso mis proveedores? comenta “proveedores” 📦\n👉 Guías en el link de mi bio\n\n#vinted #cuentavinted #trucosvinted #proveedores #fyp"))

C.append(("2026-10-29_1245", "2026-10-29 12:45", "lista: marcas que más rápido se venden", "lista de marcas",
 "zara house — ostaprod", [
  {"titulo": "las marcas que más rápido se venden en Vinted", "foto": f(7), "vinted": True},
  {"titulo": "sudaderas de marcas streetwear", "texto": "la gente las busca por nombre y paga por ellas", "foto": f(38)},
  {"titulo": "zapatillas clásicas", "texto": "modelos de siempre: nunca pasan de moda", "foto": f(18)},
  {"titulo": "ropa deportiva de marca", "texto": "conjuntos y camisetas: rotan todo el año", "foto": f(17)},
  {"titulo": "accesorios de lujo", "texto": "carteras y cinturones: poco espacio, buen margen", "foto": f(22)},
  {"titulo": "¿cuál vendes tú?", "texto": "dónde comprarlas: comenta “{verde:proveedores}”", "foto": f(19), "guia": "pack"}],
 "marcas que vuelan en Vinted 👟 ¿cuál vendes tú?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#vinted #revenderropa #marcas #proveedores #reventa"))

C.append(("2026-10-29_1720", "2026-10-29 17:20", "frases que hacen perder dinero", "frases a evitar",
 "Time Back — Sinny & 7vvch", [
  {"titulo": "5 frases que te hacen perder dinero en Vinted", "foto": f(11), "vinted": True},
  {"titulo": "«ok, te lo dejo a lo que digas»", "texto": "pon tú el precio mínimo. Siempre.", "foto": f(23)},
  {"titulo": "«es que lo necesito vender ya»", "texto": "el comprador huele la prisa y baja la oferta", "foto": f(32)},
  {"titulo": "«no sé si es original»", "texto": "si dudas tú, duda él. Vende solo lo que sabes de dónde viene.", "foto": f(22)},
  {"titulo": "«envío gratis, no pasa nada»", "texto": "ese envío sale de tu margen", "foto": f(21)},
  {"titulo": "«bueno, ya lo bajo más»", "texto": "¿cuál decías tú? y si quieres stock: comenta “{verde:proveedores}”", "foto": f(36), "guia": "pack"}],
 "frases que te están costando dinero en Vinted 💸\n¿cuál decías tú?\n\nte dejo mis proveedores: comenta “proveedores” 📦\n👉 Guías en el link de mi bio\n\n#vinted #trucosvinted #reventa #proveedores #segundamano"))

C.append(("2026-10-29_2030", "2026-10-29 20:30", "serie proveedores: perfumes (parte 2)", "serie de proveedores",
 "tesla (slowed electro mix) — Fixupboy", [
  {"titulo": "proveedores de perfumes que tienes que conocer", "sub": "(parte 2)", "foto": f(31), "vinted": True},
  {"titulo": "proveedor de perfumes de marca", "texto": "precintados y con factura. El nicho que más se guarda en Vinted.", "foto": f(31)},
  {"titulo": "proveedor de decants y miniaturas", "texto": "precio bajo, mucha venta. Ideal para empezar con poco.", "foto": f(9)},
  {"titulo": "proveedor de sets de regalo", "texto": "en noviembre y diciembre se venden solos", "foto": f(26)},
  {"titulo": "¿quieres la parte 3?", "texto": "los contactos, en la guía: comenta “{verde:proveedores}”", "foto": f(24), "guia": "perfumes"}],
 "proveedores de perfumes para revender (parte 2) 🧴\n¿de qué quieres la parte 3?\n\ncomenta “proveedores” y te digo cuáles uso 👇\n👉 Guías en el link de mi bio\n\n#perfumes #proveedores #vinted #reventa #mayorista"))

C.append(("2026-10-29_2335", "2026-10-29 23:35", "antes/ahora: planes vs envíos", "antes / ahora",
 "Im thinking of you again — wa", [
  {"titulo": "2022:", "texto": "«¿salimos este finde?»", "foto": f(25), "vinted": True},
  {"titulo": "2026:", "texto": "«no puedo, tengo 12 envíos para mañana»", "foto": f(35)},
  {"titulo": "y no lo cambio", "texto": "cada paquete es una venta que antes no existía", "foto": f(21)},
  {"titulo": "¿te ha pasado ya?", "texto": "si quieres empezar: comenta “{verde:proveedores}”", "foto": f(10), "guia": "pack"}],
 "2022 vs 2026 📦 ¿te ha pasado?\n\n¿los quieres? escribe “proveedores”\n👉 Guías en el link de mi bio\n\n#vinted #reventa #fyp #proveedores #emprender"))

C.append(("2026-10-30_0940", "2026-10-30 09:40", "herramientas para revender", "herramientas",
 "Espresso Soul — edivieira", [
  {"titulo": "lo que necesitas para revender en serio", "foto": f(20), "vinted": True},
  {"titulo": "bolsas de envío de colores", "texto": "baratas y el paquete llega con buena imagen", "foto": f(13)},
  {"titulo": "una mesa limpia junto a la ventana", "texto": "luz natural = fotos que venden, sin gastar en focos", "foto": f(32)},
  {"titulo": "el punto de envío más cercano", "texto": "taquillas y puntos de recogida: envías en 2 minutos", "foto": f(21)},
  {"titulo": "y un buen proveedor", "texto": "sin stock bueno no hay nada. Comenta “{verde:proveedores}”", "foto": f(9), "guia": "pack"}],
 "lo que de verdad necesitas para revender (sin gastar de más) 📦\n¿qué te falta a ti?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#reventa #vinted #emprendimiento #proveedores #negocioonline"))

C.append(("2026-10-30_1235", "2026-10-30 12:35", "compra→venta: zapatillas", "precio compra → venta",
 "Did It First Beat — Majorzin", [
  {"titulo": "zapatillas que compras por menos de 30€ y se venden solas", "sub": "(precios de ejemplo)", "foto": f(18), "vinted": True},
  {"titulo": "running clásicas", "precios": ["25€", "65€"], "foto": f(22)},
  {"titulo": "zapatillas de skate", "precios": ["20€", "50€"], "foto": f(7)},
  {"titulo": "modelos retro", "precios": ["28€", "70€"], "foto": f(19)},
  {"titulo": "¿cuál pillarías?", "texto": "el proveedor está en la guía: comenta “{verde:proveedores}”", "foto": f(9), "guia": "calzado"}],
 "zapatillas que se venden solas en Vinted 👟 (precios de ejemplo)\n¿cuál pillarías?\n\ncomenta “proveedores” y te los paso 📦\n👉 Guías en el link de mi bio\n\n#zapatillas #sneakers #vinted #proveedores #reventa"))

C.append(("2026-10-30_1730", "2026-10-30 17:30", "error→solución: te escriben y no compran", "error → solución",
 "Mint Breeze — RITA", [
  {"titulo": "te escriben pero no te compran 😩", "caja": True, "foto": f(11), "vinted": True},
  {"titulo": "1. contestas tarde", "texto": "si tardas horas, ya compró en otra cuenta", "foto": f(23)},
  {"titulo": "2. respondes solo «sí»", "texto": "añade medidas, estado y una foto extra", "foto": f(28)},
  {"titulo": "3. no cierras", "texto": "termina con «si quieres te lo reservo hoy»", "foto": f(32)},
  {"titulo": "¿cuánto tardas tú en contestar?", "texto": "y para el stock: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
 "te preguntan en Vinted pero luego no compran 😩\n¿cuánto tardas en contestar?\n\n¿los quieres? escribe “proveedores” 📦\n👉 Guías en el link de mi bio\n\n#vinted #trucosvinted #revenderropa #proveedores #fyp"))

C.append(("2026-10-30_2040", "2026-10-30 20:40", "Pinterest para saber qué vender", "truco Pinterest",
 "Another Life — SZA", [
  {"titulo": "Pinterest te dice qué vas a vender el mes que viene", "foto": f(32), "vinted": True},
  {"titulo": "1. busca «outfit invierno 2026»", "texto": "mira qué prendas se repiten en los pines más guardados", "foto": f(28)},
  {"titulo": "2. apunta 3 prendas", "texto": "las que salen en todos los outfits", "foto": f(38)},
  {"titulo": "3. búscalas en Vinted", "texto": "si hay pocas y caras: ahí tienes tu próxima compra", "foto": f(29)},
  {"titulo": "4. consigue proveedor antes que nadie", "texto": "los míos, en la guía: comenta “{verde:proveedores}”", "foto": f(26), "guia": "ropa"}],
 "el truco de Pinterest para saber qué revender 📌\n¿lo sabías?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#pinterest #vinted #reventa #proveedores #tendencias"))

C.append(("2026-10-30_2330", "2026-10-30 23:30", "motivación: nadie te aplaude", "motivación",
 "Untitled #13 (Slowed + Reverb) — glwzbll", [
  {"titulo": "nadie te va a aplaudir cuando empieces", "foto": f(36), "vinted": True},
  {"titulo": "ni con la primera venta", "texto": "ni con el primer paquete que mandas", "foto": f(11)},
  {"titulo": "te aplaudirán cuando ya no lo necesites", "foto": f(25)},
  {"titulo": "así que sigue igual", "texto": "una prenda más hoy", "foto": f(32)},
  {"titulo": "¿en qué día vas tú?", "texto": "si quieres empezar: escribe “{verde:proveedores}”", "foto": f(30), "guia": "pack"}],
 "sigue aunque nadie te aplauda 🌙\n¿cuánto llevas revendiendo?\n\nescribe “proveedores” y te los mando 📩\n👉 Guías en el link de mi bio\n\n#mentalidad #emprendimiento #vinted #reventa #proveedores"))

C.append(("2026-10-31_0935", "2026-10-31 09:35", "preguntas a no hacer a un proveedor", "errores con proveedores",
 "Self Aware — Mark Allan Wolfe", [
  {"titulo": "preguntas que nunca debes hacerle a un proveedor", "foto": f(26), "vinted": True},
  {"titulo": "«¿cuál es el precio más bajo?»", "texto": "mejor: «¿qué precio tienes para 20 unidades?»", "foto": f(37)},
  {"titulo": "«¿es bueno?»", "texto": "mejor: «¿me mandas fotos reales y una muestra?»", "foto": f(33)},
  {"titulo": "«¿cuándo llega?»", "texto": "mejor: «¿cuánto tarda a España y con qué envío?»", "foto": f(35)},
  {"titulo": "¿cuál preguntabas tú?", "texto": "proveedores ya probados: comenta “{verde:proveedores}”", "foto": f(9), "guia": "pack"}],
 "lo que nunca debes preguntarle a un proveedor (y qué decir) 📦\n¿cuál preguntabas tú?\n\ncomenta “proveedores” y te digo cuáles uso 👇\n👉 Guías en el link de mi bio\n\n#proveedores #reventa #mayorista #vinted #importar"))

C.append(("2026-10-31_1245", "2026-10-31 12:45", "serie proveedores: zapatillas (parte 3)", "serie de proveedores",
 "tesla (slowed electro mix) — Fixupboy", [
  {"titulo": "proveedores de zapatillas que tienes que conocer", "sub": "(parte 3)", "foto": f(18), "vinted": True},
  {"titulo": "proveedor de zapatillas de running", "texto": "las que más se buscan por modelo en Vinted", "foto": f(22)},
  {"titulo": "proveedor de modelos retro", "texto": "suben de precio en otoño, cuando vuelven las colecciones", "foto": f(19)},
  {"titulo": "proveedor de tiendas con stock", "texto": "tallas sueltas a precio de liquidación", "foto": f(7)},
  {"titulo": "¿quieres la parte 4?", "texto": "los contactos, en la guía: comenta “{verde:proveedores}”", "foto": f(9), "guia": "calzado"}],
 "proveedores de zapatillas para revender (parte 3) 👟\n¿de qué quieres la parte 4?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#zapatillas #proveedores #vinted #sneakers #reventa"))

C.append(("2026-10-31_1725", "2026-10-31 17:25", "error→solución: la primera foto", "error → solución",
 "Mint Breeze — RITA", [
  {"titulo": "la 1ª foto decide si te compran 📸", "foto": f(19), "vinted": True},
  {"titulo": "1. prenda entera, nada cortado", "texto": "el comprador tiene que ver qué es en medio segundo", "foto": f(17)},
  {"titulo": "2. luz de ventana", "texto": "nada de flash ni luz amarilla de noche", "foto": f(32)},
  {"titulo": "3. fondo limpio", "texto": "sin cama deshecha ni ropa detrás", "foto": f(31)},
  {"titulo": "4. puesta, si puedes", "texto": "la prenda puesta vende más que doblada", "foto": f(28)},
  {"titulo": "¿cómo es tu 1ª foto?", "texto": "y si te falta stock: comenta “{verde:proveedores}”", "foto": f(6), "guia": "pack"}],
 "tu primera foto en Vinted lo decide todo 📸\n¿cómo es la tuya?\n\ncomenta “proveedores” y te paso el link 📦\n👉 Guías en el link de mi bio\n\n#vinted #fotosvinted #trucosvinted #proveedores #revenderropa"))

C.append(("2026-10-31_2030", "2026-10-31 20:30", "plan: empezar hoy con 50€", "plan paso a paso",
 "sdp interlude (Slowed) — VTX", [
  {"titulo": "si empezara hoy con 50€, haría esto", "foto": f(32), "vinted": True},
  {"titulo": "1. un solo nicho", "texto": "sudaderas, perfumes o zapatillas. Uno.", "foto": f(38)},
  {"titulo": "2. un proveedor fiable", "texto": "muestras primero, pedido pequeño después", "foto": f(26)},
  {"titulo": "3. fotos buenas y precio justo", "texto": "y contestar rápido a todos", "foto": f(29)},
  {"titulo": "4. reinvertir todo el primer mes", "texto": "cada venta = más stock", "foto": f(5)},
  {"titulo": "¿con cuánto empezarías tú?", "texto": "mis proveedores, en la guía: comenta “{verde:proveedores}”", "foto": f(30), "guia": "pack"}],
 "cómo empezaría a revender con 50€ si lo hiciera hoy 💸\n¿con cuánto empezarías tú?\n\n¿te paso mis proveedores? comenta “proveedores” 📦\n👉 Guías en el link de mi bio\n\n#reventa #vinted #emprender #proveedores #negocioonline"))

C.append(("2026-10-31_2340", "2026-10-31 23:40", "relatable: sábado noche", "relatable",
 "Time Back — Sinny & 7vvch", [
  {"titulo": "sábado noche:", "texto": "ellos de fiesta. yo etiquetando paquetes.", "foto": f(25), "vinted": True},
  {"titulo": "parece aburrido", "foto": f(35)},
  {"titulo": "hasta que el lunes", "texto": "te llegan 4 valoraciones de 5 estrellas", "foto": f(11)},
  {"titulo": "¿tú dónde estás ahora?", "texto": "si quieres empezar: escribe “{verde:proveedores}”", "foto": f(21), "guia": "pack"}],
 "sábado noche de revendedor 📦😂\n¿tú dónde estás ahora?\n\nescribe “proveedores” y te los mando\n👉 Guías en el link de mi bio\n\n#vinted #reventa #fyp #proveedores #emprendimiento"))

C.append(("2026-11-01_0940", "2026-11-01 09:40", "lista: revender con menos de 50€", "lista con promesa",
 "Cavendish Banana — Bruno Boe", [
  {"titulo": "5 cosas que puedes revender con menos de 50€", "foto": f(3), "vinted": True},
  {"titulo": "1. sudaderas de marca", "texto": "2-3 unidades para probar", "foto": f(38)},
  {"titulo": "2. perfumes en miniatura", "texto": "poco precio, mucha venta", "foto": f(31)},
  {"titulo": "3. juguetes de colección", "texto": "cajas de construcción: se buscan todo el año", "foto": f(3)},
  {"titulo": "4. conjuntos deportivos", "texto": "se venden en pack", "foto": f(17)},
  {"titulo": "5. carteras y accesorios", "texto": "ocupan poco y el margen es bueno", "foto": f(22)},
  {"titulo": "¿con cuál empezarías?", "texto": "dónde comprarlo: comenta “{verde:proveedores}”", "foto": f(9), "guia": "pack"}],
 "5 cosas que puedes revender con menos de 50€ 💸\n¿con cuál empezarías?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#reventa #vinted #ideasdenegocio #proveedores #fyp"))

C.append(("2026-11-01_1230", "2026-11-01 12:30", "riesgo de cuenta: cuenta nueva", "riesgo de cuenta",
 "Self Aware — Mark Allan Wolfe", [
  {"titulo": "nunca hagas esto con una cuenta nueva de Vinted 🚫", "caja": True, "foto": f(23), "vinted": True},
  {"titulo": "subir 30 prendas el primer día", "texto": "empieza con pocas y ve subiendo cada día", "foto": f(15)},
  {"titulo": "usar fotos sacadas de internet", "texto": "haz las tuyas, aunque sean con el móvil", "foto": f(28)},
  {"titulo": "cambiar el precio 10 veces", "texto": "ajústalo una vez y espera unos días", "foto": f(32)},
  {"titulo": "¿tu cuenta tiene menos de un mes?", "texto": "¿te paso mis proveedores? comenta “{verde:proveedores}”", "foto": f(4), "guia": "pack"}],
 "cuenta nueva en Vinted: no hagas esto 🚫\n¿la tuya tiene menos de un mes?\n\ncomenta “proveedores” y te digo cuáles uso 👇\n👉 Guías en el link de mi bio\n\n#vinted #cuentavinted #trucosvinted #proveedores #wallapop"))

C.append(("2026-11-01_1735", "2026-11-01 17:35", "error→solución: regateos", "error → solución",
 "Did It First Beat — Majorzin", [
  {"titulo": "por qué te regatean tanto", "sub": "(y cómo pararlo)", "foto": f(11), "vinted": True},
  {"titulo": "1. tu precio no tiene margen", "texto": "súbelo un 10-15 %: así puedes bajar sin perder", "foto": f(38)},
  {"titulo": "2. aceptas la primera oferta", "texto": "contraoferta siempre, aunque sea 1€ menos", "foto": f(23)},
  {"titulo": "3. tu anuncio parece de saldo", "texto": "buenas fotos = menos regateo", "foto": f(29)},
  {"titulo": "¿cuánto te suelen ofrecer?", "texto": "y para comprar barato: comenta “{verde:proveedores}”", "foto": f(26), "guia": "pack"}],
 "si en Vinted solo te hacen ofertas bajas, mira esto 💸\n¿cuánto te suelen ofrecer?\n\n¿los quieres? comenta “proveedores” 📦\n👉 Guías en el link de mi bio\n\n#vinted #ofertasvinted #revender #proveedores #reventa"))

C.append(("2026-11-01_2035", "2026-11-01 20:35", "serie proveedores: accesorios (parte 4)", "serie de proveedores",
 "tesla (slowed electro mix) — Fixupboy", [
  {"titulo": "proveedores de accesorios que tienes que conocer", "sub": "(parte 4)", "foto": f(9), "vinted": True},
  {"titulo": "proveedor de carteras y cinturones", "texto": "ocupan poco, se envían barato y dejan margen", "foto": f(22)},
  {"titulo": "proveedor de auriculares y tecnología pequeña", "texto": "se buscan todo el año. Pide siempre factura.", "foto": f(37)},
  {"titulo": "proveedor de gorras y complementos", "texto": "perfectos para hacer packs con ropa", "foto": f(7)},
  {"titulo": "¿de qué quieres la parte 5?", "texto": "los contactos, en la guía: comenta “{verde:proveedores}”", "foto": f(24), "guia": "accesorios"}],
 "proveedores de accesorios para revender (parte 4) 👜\n¿de qué quieres la parte 5?\n\ncomenta “proveedores” y te paso el link 👇\n👉 Guías en el link de mi bio\n\n#proveedores #accesorios #vinted #reventa #mayorista"))

C.append(("2026-11-01_2330", "2026-11-01 23:30", "reflexión: 1 prenda al día", "reflexión",
 "Untitled #13 (Slowed + Reverb) — glwzbll", [
  {"titulo": "si este mes subes 1 prenda al día…", "foto": f(2), "vinted": True},
  {"titulo": "el día 30 tienes 30 prendas a la venta", "foto": f(29)},
  {"titulo": "y más prendas = más visitas = más ventas", "foto": f(35)},
  {"titulo": "no hace falta hacerlo todo hoy", "texto": "solo 1. mañana otra.", "foto": f(32)},
  {"titulo": "¿cuántas tienes subidas ahora?", "texto": "si te falta stock: escribe “{verde:proveedores}”", "foto": f(30), "guia": "pack"}],
 "noviembre empieza hoy: 1 prenda al día 🌙\n¿cuántas tienes subidas ahora?\n\nescribe “proveedores” y te los mando 📩\n👉 Guías en el link de mi bio\n\n#vinted #constancia #reventa #proveedores #emprender"))

if __name__ == "__main__":
    for carpeta, hora, tema, formato, audio, slides, caption in C:
        d = os.path.join(AQUI, carpeta)
        os.makedirs(d, exist_ok=True)
        g = {"plantilla": "pinterest", "slides": slides, "caption": caption, "tema": tema, "formato": formato,
             "hora_publicacion": hora, "audio": audio}
        json.dump(g, open(os.path.join(d, "guion.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(C))
