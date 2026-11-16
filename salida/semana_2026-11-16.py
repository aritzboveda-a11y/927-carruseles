"""Guiones de la semana 16-22 nov 2026 (plantilla pinterest). Genera salida/<fecha_hora>/guion.json.

Análisis (vistas máximas de cada carrusel, 29 oct - 8 nov):
- GANAN: riesgo de Vinted en lista CONCRETA por la mañana (2.615, 1.668, 1.523), listas negativas de frases
  (2.166), historia propia + solución (2.033), error→solución con culpable (845), lista "qué subo el domingo" (806),
  frases exactas (713, el que más comenta).
- PIERDEN: serie de proveedores (245-352), reflexiones/memes de noche (295-444), compra→venta con precios (92-478),
  "dinero en Vinted" (386-411), Vinted vs Wallapop (380), plan "si tuviera 100€" (383).
- Comentarios casi a 0 en todo: cierre siempre con elección fácil (1, 2 o 3 / A o B / un número).
Mejoras de esta semana: fuera serie de proveedores y reflexiones; 09:30 riesgo concreto, 17:30 historia o frases,
20:30 lista negativa/aprendizajes; ~30 % formatos nuevos (POV, test "cuántas haces", "¿cuál se vendió antes?",
"pregunta con respuesta al final", "esto vs esto"); nº de diapositivas variado (4-7); audios en tendencia.
"""
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
f = lambda n: f"aritz927_{n:02d}.jpg"
C = []  # (carpeta, hora, tema, formato, audio, slides, caption)

AUD = {
    "neonnights": "Neon Nights (Adrian Rover) — tendencia España",
    "neonbass": "Neon Bass (Tangelene Bolton) — tendencia España",
    "kaleido": "Kaleidoscope (Adrián Berenguer) — tendencia España",
    "coolgirl": "Cool Girl (Jayde Mari) — tendencia España",
    "maybeyou": "Maybe You (Muspace Lofi) — tendencia España",
    "polar": "Polar Winds (Lofi) (Muspace Lofi) — tendencia España",
    "timeback": "Time Back (Sinny) — el del carrusel top (2.615)",
    "mint": "Mint Breeze (RITA) — el de «3 frases» (713)",
    "zara": "Zara House (ostaprod)",
    "didit": "Did It First instrumental (Ice Spice)",
}


def cap(l1, q, cta, tags, bio=True):
    t = f"{l1}\n{q}\n\n{cta}"
    if bio:
        t += "\n👉 Guías en el link de mi bio"
    return t + f"\n\n{tags}"


def add(carpeta, tema, formato, audio, slides, caption):
    hora = f"{carpeta[:10]} {carpeta[11:13]}:{carpeta[13:]}"
    C.append((carpeta, hora, tema, formato, audio, slides, caption))


# ---------------- LUNES 16 NOV ----------------
add("2026-11-16_1140", "riesgo: mensajes falsos de Vinted", "riesgo concreto (lista)", "neonnights", [
    {"titulo": "3 mensajes de «Vinted» que son falsos 🚩", "caja": True, "foto": f(11), "vinted": True},
    {"titulo": "1. «verifica tu cuenta en este link»", "texto": "Vinted no te manda links por WhatsApp ni SMS. nunca lo abras", "foto": f(32)},
    {"titulo": "2. «el comprador ya ha pagado, mete tu tarjeta»", "texto": "para cobrar no tienes que meter nada. el dinero llega solo al monedero", "foto": f(23)},
    {"titulo": "3. «paga el seguro de envío para recibir el dinero»", "texto": "eso no existe. si te lo piden, es estafa", "foto": f(21)},
    {"titulo": "¿cuál te ha llegado? 1, 2 o 3", "texto": "y si quieres stock sin líos: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("3 mensajes de «Vinted» que son falsos 🚩", "¿cuál te ha llegado a ti? 1, 2 o 3", "comenta “proveedores” y te digo cuáles uso 👇",
        "#vinted #estafasvinted #cuentavinted #proveedores #fyp"))

add("2026-11-16_1305", "pregunta con respuesta: misma prenda, distinta venta", "pregunta con respuesta al final (nuevo)", "neonbass", [
    {"titulo": "misma sudadera. una se vende en 1 día y la otra en 1 mes", "sub": "(la respuesta al final)", "foto": f(28), "vinted": True},
    {"titulo": "la que tarda 1 mes:", "texto": "foto de noche en la cama. título «sudadera bonita». 30€", "foto": f(36)},
    {"titulo": "la que se vende en 1 día:", "texto": "luz de ventana. «sudadera Nike gris talla M». 28€", "foto": f(17)},
    {"titulo": "¿la diferencia?", "texto": "no es la prenda. es cómo la subes", "foto": f(29)},
    {"titulo": "foto + título + precio", "texto": "los míos los compro barato: proveedores en la guía de mi bio", "foto": f(38)},
    {"titulo": "¿cuál subes tú: la 1 o la 2?", "texto": "comenta “{amarillo:proveedores}” y te paso los míos", "foto": f(9), "guia": "ropa"}],
    cap("misma sudadera, una se vende en 1 día y otra en 1 mes 👀", "¿tú cuál subes, la 1 o la 2?", "escribe “proveedores” y te los mando 📦",
        "#trucosvinted #vinted #revenderropa #proveedores #reventa"))

add("2026-11-16_1730", "historia: pago retenido", "historia + solución", "kaleido", [
    {"titulo": "el comprador no confirmaba y mi dinero no llegaba 😩", "foto": f(27), "vinted": True},
    {"titulo": "lo que hice:", "texto": "nada de agobiarme ni de escribirle 20 veces", "foto": f(32)},
    {"titulo": "1. miré el seguimiento", "texto": "si pone entregado, Vinted libera el pago solo a los 2 días si no hay reclamación", "foto": f(21)},
    {"titulo": "2. guardé captura del envío", "texto": "si algo sale mal, soporte te lo pide", "foto": f(11)},
    {"titulo": "¿cuántos días te ha tardado a ti?", "texto": "los proveedores que uso: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("el comprador no confirmaba y mi dinero no llegaba 😩", "¿cuántos días te ha tardado a ti?", "¿los quieres? comenta “proveedores” 📩",
        "#vinted #pagovinted #ventasvinted #proveedores #wallapop"))

add("2026-11-16_2035", "lista negativa: deja de hacer esto", "deja de hacer esto (nuevo)", "coolgirl", [
    {"titulo": "deja de hacer esto si quieres vender en Vinted 🛑", "foto": f(29), "vinted": True},
    {"titulo": "1. bajar el precio cada día", "texto": "parece desesperado. mejor manda una oferta a los favoritos", "foto": f(38)},
    {"titulo": "2. contestar «último precio» y ya", "texto": "contraoferta siempre. «te lo dejo en 18 si lo pillas hoy»", "foto": f(11)},
    {"titulo": "3. subir 30 prendas de golpe", "texto": "mejor 3-5 al día. la cuenta se ve viva", "foto": f(35)},
    {"titulo": "4. comprar stock caro", "texto": "si compras caro, no hay precio que te salve", "foto": f(9)},
    {"titulo": "¿cuál hacías tú? 1, 2, 3 o 4", "texto": "y para comprar barato: comenta “{verde:proveedores}”", "foto": f(26), "guia": "pack"}],
    cap("deja de hacer esto si quieres vender en Vinted 🛑", "¿cuál hacías tú? dime el número", "te dejo mis proveedores: comenta “proveedores” 👇",
        "#vinted #revenderropa #trucosvinted #proveedores #emprendimiento"))

add("2026-11-16_2330", "POV: primera venta", "POV relatable (nuevo)", "polar", [
    {"titulo": "POV: vendes tu primera prenda en Vinted", "foto": f(36), "vinted": True},
    {"titulo": "buscas una bolsa por toda la casa", "foto": f(13)},
    {"titulo": "vas a la taquilla como si llevaras oro", "foto": f(21)},
    {"titulo": "y ya quieres subir 10 más 😂", "texto": "¿te acuerdas de la tuya? si te falta stock: comenta “{azul:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("POV: tu primera venta en Vinted 📦😂", "¿qué fue lo primero que vendiste?", "comenta “proveedores” y te paso el link", "#vinted #reventa #fyp #primeraventa #proveedores"))

# ---------------- MARTES 17 NOV ----------------
add("2026-11-17_0935", "riesgo: artículo oculto", "riesgo concreto (lista)", "timeback", [
    {"titulo": "3 cosas que hacen que Vinted oculte tu artículo 🚫", "caja": True, "foto": f(32), "vinted": True},
    {"titulo": "1. fotos sacadas de internet", "texto": "usa siempre fotos tuyas, de la prenda real", "foto": f(17)},
    {"titulo": "2. poner una marca que no es", "texto": "«tipo Nike» para salir en búsquedas = te lo quitan", "foto": f(38)},
    {"titulo": "3. subir lo mismo 5 veces", "texto": "un anuncio por prenda. renueva, no dupliques", "foto": f(35)},
    {"titulo": "guárdalo y revisa tus anuncios", "texto": "los míos están en la guía de mi bio", "foto": f(29)},
    {"titulo": "¿cuál hacías tú? 1, 2 o 3", "texto": "producto de marca original: comenta “{verde:proveedores}”", "foto": f(4), "guia": "pack"}],
    cap("3 cosas que hacen que Vinted oculte tu artículo 🚫", "¿cuál hacías tú?", "escribe “proveedores” y te digo cuáles uso 📦",
        "#vinted #normasvinted #cuentavinted #proveedores #revenderropa"))

add("2026-11-17_1240", "lista: antes de subir una prenda", "lista qué hacer", "neonbass", [
    {"titulo": "lo que hago antes de subir cualquier prenda ✅", "sub": "(el 4 casi nadie lo hace)", "foto": f(17), "vinted": True},
    {"titulo": "1. quitar pelusas y planchar", "texto": "parece nueva = se vende antes", "foto": f(28)},
    {"titulo": "2. medir largo y ancho", "texto": "menos preguntas y menos devoluciones", "foto": f(29)},
    {"titulo": "3. foto de la etiqueta", "texto": "marca y talla a la vista. da confianza", "foto": f(38)},
    {"titulo": "4. mirar lo vendido", "texto": "filtra «vendido» con tu marca y talla. ese es tu precio", "foto": f(32)},
    {"titulo": "guárdalo para tu próxima subida", "foto": f(13)},
    {"titulo": "¿cuál no hacías? 1, 2, 3 o 4", "texto": "y si te falta producto: comenta “{azul:proveedores}”", "foto": f(9), "guia": "ropa"}],
    cap("lo que hago antes de subir cualquier prenda a Vinted ✅", "¿cuál no hacías?", "¿los quieres? comenta “proveedores” 📦",
        "#vinted #trucosvinted #revender #proveedores #negocioonline"))

add("2026-11-17_1720", "historia: no le llegó", "historia + solución", "kaleido", [
    {"titulo": "me dijeron que no les llegó el paquete (y no perdí nada)", "foto": f(21), "vinted": True},
    {"titulo": "1. miré el seguimiento", "texto": "ponía entregado en la taquilla", "foto": f(27)},
    {"titulo": "2. contesté con calma y dentro de Vinted", "texto": "nada de WhatsApp ni discutir", "foto": f(11)},
    {"titulo": "3. mandé captura a soporte", "texto": "con el código de envío. resuelto a mi favor", "foto": f(32)},
    {"titulo": "¿envías con Correos, InPost o Seur?", "texto": "los proveedores que uso: comenta “{verde:proveedores}”", "foto": f(34), "guia": "pack"}],
    cap("me dijeron que no les llegó el paquete (y no perdí nada) 📦", "¿tú envías con Correos, InPost o Seur?", "comenta “proveedores” y te digo cuáles uso",
        "#vinted #enviosvinted #inpost #proveedores #reventa"))

add("2026-11-17_2030", "riesgo: proveedor estafa", "lista negativa (señales)", "coolgirl", [
    {"titulo": "3 señales de que un proveedor te va a estafar 🚩", "foto": f(9), "vinted": True},
    {"titulo": "1. solo cobra por transferencia a una persona", "texto": "o cripto. sin forma de reclamar", "foto": f(32)},
    {"titulo": "2. no te deja pedir muestra", "texto": "si no te deja probar con poco, no te fíes", "foto": f(26)},
    {"titulo": "3. marca de lujo a precio de risa", "texto": "eso no es original. y en Vinted te cierran la cuenta", "foto": f(18)},
    {"titulo": "cómo lo hago yo:", "texto": "muestra primero, pago con protección y pedido pequeño", "foto": f(33)},
    {"titulo": "¿te ha pasado alguna?", "texto": "los que yo uso, revisados: comenta “{verde:proveedores}”", "foto": f(35), "guia": "pack"}],
    cap("3 señales de que un proveedor te va a estafar 🚩", "¿te ha pasado alguna?", "¿los quieres? escribe “proveedores” 📩",
        "#proveedores #mayorista #reventa #vinted #estafas"))

add("2026-11-17_2325", "confesión: comprar para mí", "confesión", "maybeyou", [
    {"titulo": "el error que cometí al empezar (y casi todos)", "foto": f(36), "vinted": True},
    {"titulo": "compraba lo que me gustaba a mí", "texto": "no lo que la gente busca", "foto": f(7)},
    {"titulo": "ahora primero miro lo vendido", "texto": "y luego compro. al revés, nunca", "foto": f(32)},
    {"titulo": "¿te ha pasado?", "texto": "dónde compro yo: comenta “{amarillo:proveedores}”", "foto": f(9), "guia": "pack"}],
    cap("el error que cometí al empezar a revender (y casi todos)", "¿te ha pasado? 🫠", "comenta “proveedores” y te paso el link",
        "#reventa #vinted #emprender #proveedores #fyp", bio=False))

# ---------------- MIÉRCOLES 18 NOV ----------------
add("2026-11-18_0940", "riesgo: perder una reclamación", "riesgo concreto (lista)", "neonnights", [
    {"titulo": "3 cosas que te hacen perder una reclamación en Vinted 🚫", "caja": True, "foto": f(15), "vinted": True},
    {"titulo": "1. no poner los defectos", "texto": "si no está en la descripción, el comprador tiene razón", "foto": f(17)},
    {"titulo": "2. fotos que no son de la prenda", "texto": "si llega distinta a la foto, pierdes", "foto": f(28)},
    {"titulo": "3. paquete sin proteger", "texto": "si llega roto, el problema es tuyo", "foto": f(13)},
    {"titulo": "¿te han abierto alguna?", "texto": "y si quieres stock que llegue bien: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("3 cosas que te hacen perder una reclamación en Vinted 🚫", "¿te han abierto alguna?", "comenta “proveedores” y te paso el link 👇",
        "#vinted #reclamacionvinted #trucosvinted #proveedores #wallapop"))

add("2026-11-18_1235", "esto vs esto: fotos", "esto vs esto (nuevo)", "didit", [
    {"titulo": "foto que no vende vs foto que vende 📸", "sub": "(guárdalo)", "foto": f(17), "vinted": True},
    {"titulo": "❌ arrugada en la cama", "texto": "✅ colgada en una puerta, sin arrugas", "foto": f(36)},
    {"titulo": "❌ con flash de noche", "texto": "✅ de día, al lado de la ventana", "foto": f(32)},
    {"titulo": "❌ solo 1 foto", "texto": "✅ delante, detrás, etiqueta y detalle", "foto": f(29)},
    {"titulo": "❌ la prenda lejos", "texto": "✅ que ocupe toda la foto", "foto": f(28)},
    {"titulo": "¿cuál hacías mal?", "texto": "y si te falta stock: comenta “{azul:proveedores}”", "foto": f(38), "guia": "ropa"}],
    cap("foto que no vende vs foto que vende en Vinted 📸", "¿cuál hacías mal?", "escribe “proveedores” y te los mando",
        "#fotosvinted #vinted #revenderropa #proveedores #trucos"))

add("2026-11-18_1725", "frases: cuando te ofrecen la mitad", "frases exactas", "mint", [
    {"titulo": "3 respuestas cuando te ofrecen la mitad 💬", "foto": f(11), "vinted": True},
    {"titulo": "1. «gracias! te lo dejo en 22, está casi nuevo»", "texto": "contraoferta siempre. nunca un «no» seco", "foto": f(32)},
    {"titulo": "2. «si te llevas 2, te hago mejor precio»", "texto": "vendes más y pagas un envío", "foto": f(29)},
    {"titulo": "3. «ahora no, pero si sigue en 3 días te aviso»", "texto": "se queda pendiente. muchos vuelven", "foto": f(23)},
    {"titulo": "¿cuál usarías: 1, 2 o 3?", "texto": "y para comprar barato: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("qué contestar cuando te ofrecen la mitad en Vinted 💬", "¿cuál usarías: 1, 2 o 3?", "¿los quieres? comenta “proveedores” 📦",
        "#vinted #ofertasvinted #ventasvinted #proveedores #reventa"))

add("2026-11-18_2040", "lista negativa: qué no comprar para Navidad", "lista negativa", "zara", [
    {"titulo": "lo que NO compraría para revender en Navidad 🚫", "foto": f(3), "vinted": True},
    {"titulo": "1. decoración navideña", "texto": "se vende 2 semanas. luego, 11 meses parada", "foto": f(20)},
    {"titulo": "2. tecnología sin factura", "texto": "te la reclaman o no te la compran", "foto": f(33)},
    {"titulo": "3. tallas raras de abrigo", "texto": "el frío no espera. lo que no sale en noviembre, no sale", "foto": f(29)},
    {"titulo": "lo que sí: perfumes, carteras, sudaderas", "texto": "regalo fácil. los proveedores, en la guía de mi bio", "foto": f(31)},
    {"titulo": "¿qué vas a vender tú?", "texto": "comenta “{rojo:proveedores}” y te los paso", "foto": f(22), "guia": "pack"}],
    cap("lo que NO compraría para revender en Navidad 🚫🎄", "¿qué vas a vender tú?", "comenta “proveedores” y te paso el link",
        "#navidad #vinted #reventa #proveedores #negocioonline"))

add("2026-11-18_2330", "POV: ¿me lo guardas?", "POV relatable (nuevo)", "polar", [
    {"titulo": "POV: «¿me lo guardas hasta el mes que viene?»", "foto": f(11), "vinted": True},
    {"titulo": "a las 2 de la mañana", "foto": f(36)},
    {"titulo": "con 0 valoraciones", "foto": f(32)},
    {"titulo": "y no ha comprado nada nunca 😂", "texto": "¿qué contestas? si te falta stock: comenta “{amarillo:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("POV: «¿me lo guardas hasta el mes que viene?» 😂", "¿qué le contestas?", "comenta “proveedores” y te paso el link",
        "#vinted #humor #reventa #fyp #proveedores"))

# ---------------- JUEVES 19 NOV ----------------
add("2026-11-19_0935", "riesgo: tallas y devoluciones", "riesgo concreto (lista)", "timeback", [
    {"titulo": "3 errores con la talla que acaban en devolución 🚫", "caja": True, "foto": f(38), "vinted": True},
    {"titulo": "1. poner la talla de la etiqueta y ya", "texto": "hay marcas que tallan pequeño. dilo", "foto": f(17)},
    {"titulo": "2. no decir si es de hombre o de mujer", "texto": "una M no es igual en las dos", "foto": f(28)},
    {"titulo": "3. no poner medidas en cm", "texto": "largo, ancho y manga. 1 minuto con el metro", "foto": f(29)},
    {"titulo": "las medidas en la foto 2", "texto": "así lo hago yo. los proveedores, en mi bio", "foto": f(32)},
    {"titulo": "¿cuál te ha pasado?", "texto": "te paso mis proveedores: comenta “{verde:proveedores}”", "foto": f(9), "guia": "ropa"}],
    cap("3 errores con la talla que acaban en devolución en Vinted 🚫", "¿cuál te ha pasado?", "comenta “proveedores” y te digo cuáles uso 👇",
        "#vinted #devolucionvinted #trucosvinted #proveedores #revenderropa"))

add("2026-11-19_1240", "quiz: cuál se vendió antes", "¿cuál se vendió antes? (nuevo)", "neonbass", [
    {"titulo": "¿cuál se vendió antes: la 1 o la 2?", "sub": "(ejemplo. respuesta al final)", "foto": f(7), "vinted": True},
    {"titulo": "1. sudadera de marca básica", "texto": "gris, talla M, 25€", "foto": f(28)},
    {"titulo": "2. camiseta de diseñador", "texto": "blanca, talla S, 40€", "foto": f(17)},
    {"titulo": "la 1. y por mucho", "texto": "es temporada, talla que busca todo el mundo y precio fácil", "foto": f(38)},
    {"titulo": "¿acertaste?", "texto": "dónde compro lo que se vende: comenta “{azul:proveedores}”", "foto": f(9), "guia": "ropa"}],
    cap("¿cuál se vendió antes en Vinted: la 1 o la 2? 👀", "dímelo antes de ver la respuesta", "escribe “proveedores” y te los mando 📦",
        "#vinted #revenderropa #reventa #proveedores #fyp"))

add("2026-11-19_1730", "historia: devolución manchada", "historia + solución", "kaleido", [
    {"titulo": "me devolvieron una prenda manchada que no estaba así 😤", "foto": f(34), "vinted": True},
    {"titulo": "lo que me salvó:", "texto": "las fotos que hice antes de enviarla", "foto": f(17)},
    {"titulo": "1. abrí la devolución grabando", "texto": "de principio a fin, sin cortes", "foto": f(15)},
    {"titulo": "2. comparé con mis fotos", "texto": "misma prenda, sin mancha. fecha incluida", "foto": f(29)},
    {"titulo": "3. lo mandé todo a soporte", "texto": "sin discutir en el chat", "foto": f(32)},
    {"titulo": "¿haces fotos antes de enviar?", "texto": "los proveedores que uso: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("me devolvieron una prenda manchada que no estaba así 😤", "¿tú haces fotos antes de enviar?", "te dejo mis proveedores: comenta “proveedores”",
        "#vinted #devolucionvinted #ventasvinted #proveedores #wallapop"))

add("2026-11-19_2035", "lista negativa: comprar stock mal", "deja de hacer esto", "coolgirl", [
    {"titulo": "deja de comprar stock así 🛑", "foto": f(35), "vinted": True},
    {"titulo": "1. sin mirar lo vendido", "texto": "lo que ya se vende es lo único seguro", "foto": f(32)},
    {"titulo": "2. todo de la misma talla", "texto": "S, M y L. reparte", "foto": f(38)},
    {"titulo": "3. porque está barato", "texto": "barato y que nadie busca = dinero parado", "foto": f(3)},
    {"titulo": "¿cuál hacías: 1, 2 o 3?", "texto": "los míos, en la guía: comenta “{verde:proveedores}”", "foto": f(9), "guia": "pack"}],
    cap("deja de comprar stock así 🛑", "¿cuál hacías: 1, 2 o 3?", "¿los quieres? comenta “proveedores” 👇",
        "#proveedores #mayorista #reventa #vinted #emprender"))

add("2026-11-19_2325", "confesión: vergüenza al empezar", "confesión", "maybeyou", [
    {"titulo": "lo que más vergüenza me daba al empezar a vender", "foto": f(21), "vinted": True},
    {"titulo": "que me vieran llevando paquetes", "texto": "como si fuera algo malo", "foto": f(10)},
    {"titulo": "ahora es lo que más me gusta del día", "foto": f(34)},
    {"titulo": "¿a ti qué te frena?", "texto": "si quieres empezar: comenta “{azul:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("lo que más vergüenza me daba al empezar a vender 🫣", "¿a ti qué te frena?", "comenta “proveedores” y te paso el link",
        "#reventa #vinted #mentalidad #proveedores #fyp", bio=False))

# ---------------- VIERNES 20 NOV ----------------
add("2026-11-20_0940", "riesgo: errores de precio", "riesgo concreto (lista)", "neonnights", [
    {"titulo": "3 errores con el precio que te hacen perder dinero 🚫", "caja": True, "foto": f(29), "vinted": True},
    {"titulo": "1. no contar la bolsa y la etiqueta", "texto": "parecen céntimos. en 50 ventas no lo son", "foto": f(13)},
    {"titulo": "2. aceptar la primera oferta", "texto": "contraoferta siempre. casi todos suben", "foto": f(11)},
    {"titulo": "3. bajar todo a la vez", "texto": "baja solo lo que lleva 2 semanas sin favoritos", "foto": f(38)},
    {"titulo": "¿cuál haces tú?", "texto": "el margen está en comprar bien: comenta “{verde:proveedores}”", "foto": f(4), "guia": "pack"}],
    cap("3 errores con el precio que te hacen perder dinero en Vinted 🚫", "¿cuál haces tú?", "escribe “proveedores” y te digo cuáles uso 📦",
        "#vinted #preciosvinted #revender #proveedores #dinero"))

add("2026-11-20_1235", "temporada: antes del Black Friday", "lista temporada", "didit", [
    {"titulo": "lo que subiría antes del Black Friday 🛍️", "sub": "(es el 27 de noviembre)", "foto": f(22), "vinted": True},
    {"titulo": "1. cosas para regalar", "texto": "perfumes, carteras, gorros. la gente busca regalo", "foto": f(31)},
    {"titulo": "2. packs cerrados", "texto": "«3 sudaderas por 45€». se ven como oferta", "foto": f(38)},
    {"titulo": "3. lo de abrigo", "texto": "plumíferos y sudaderas gordas. el frío ya está aquí", "foto": f(29)},
    {"titulo": "súbelo esta semana, no la que viene", "texto": "el algoritmo necesita unos días", "foto": f(32)},
    {"titulo": "¿tú qué vas a subir?", "texto": "proveedores de todo esto: comenta “{amarillo:proveedores}”", "foto": f(18), "guia": "pack"}],
    cap("lo que subiría a Vinted antes del Black Friday 🛍️", "¿tú qué vas a subir?", "comenta “proveedores” y te paso el link 👇",
        "#blackfriday #vinted #reventa #proveedores #negocioonline"))

add("2026-11-20_1720", "frases: descripción sin devoluciones", "frases exactas", "mint", [
    {"titulo": "3 frases que pongo para que no me devuelvan nada ✍️", "foto": f(32), "vinted": True},
    {"titulo": "1. «medidas en la foto 2. compáralas con una tuya»", "foto": f(17)},
    {"titulo": "2. «tiene una marca pequeña en la manga (foto 5)»", "texto": "el defecto dicho = no hay reclamación", "foto": f(28)},
    {"titulo": "3. «lo que ves en las fotos es lo que te llega»", "foto": f(29)},
    {"titulo": "¿cuál pones tú?", "texto": "y si te falta stock: comenta “{verde:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("3 frases que pongo en Vinted para que no me devuelvan nada ✍️", "¿cuál pones tú?", "¿los quieres? comenta “proveedores” 📩",
        "#vinted #descripcionvinted #trucosvinted #proveedores #revenderropa"))

add("2026-11-20_2030", "aprendizajes: perder dinero", "aprendizajes", "zara", [
    {"titulo": "3 cosas que aprendí perdiendo dinero revendiendo", "foto": f(20), "vinted": True},
    {"titulo": "1. la muestra primero", "texto": "un pedido grande sin probar es una apuesta", "foto": f(26)},
    {"titulo": "2. lo que no se vende en 30 días, fuera", "texto": "pack o rebaja. el dinero parado no sirve", "foto": f(35)},
    {"titulo": "3. un proveedor bueno vale más que 10 baratos", "texto": "los míos están en la guía de mi bio", "foto": f(9)},
    {"titulo": "guárdalo y ahórrate el error", "foto": f(32)},
    {"titulo": "¿cuál te ha costado más?", "texto": "comenta “{verde:proveedores}” y te digo cuáles uso", "foto": f(5), "guia": "pack"}],
    cap("3 cosas que aprendí perdiendo dinero revendiendo 💸", "¿cuál te ha costado más a ti?", "comenta “proveedores” y te digo cuáles uso",
        "#reventa #vinted #emprendimiento #proveedores #mayorista"))

add("2026-11-20_2340", "POV: Black Friday", "POV relatable (nuevo)", "polar", [
    {"titulo": "POV: llega el Black Friday y ya no piensas en comprar", "foto": f(22), "vinted": True},
    {"titulo": "piensas en qué revender 😂", "foto": f(3)},
    {"titulo": "¿te pasa ya?", "texto": "si quieres empezar: comenta “{amarillo:proveedores}”", "foto": f(5), "guia": "pack"},
    {"titulo": "los proveedores que uso", "texto": "están en la guía de mi bio", "foto": f(9)}],
    cap("POV: llega el Black Friday y ya no piensas en comprar 😂", "¿te pasa ya?", "escribe “proveedores” y te los mando",
        "#blackfriday #reventa #vinted #fyp #proveedores"))

# ---------------- SÁBADO 21 NOV ----------------
add("2026-11-21_0935", "riesgo: lo que no debes aceptar", "riesgo concreto (lista)", "timeback", [
    {"titulo": "3 cosas que nunca debes aceptar como vendedor 🚫", "caja": True, "foto": f(23), "vinted": True},
    {"titulo": "1. «envíalo a otra dirección»", "texto": "solo la de la etiqueta de Vinted. siempre", "foto": f(21)},
    {"titulo": "2. «te pago más si lo hacemos fuera de la app»", "texto": "sin protección. si sale mal, nadie te ayuda", "foto": f(11)},
    {"titulo": "3. «mándame tú el código a mi WhatsApp»", "texto": "todo por el chat de Vinted", "foto": f(32)},
    {"titulo": "¿te han pedido alguna?", "texto": "proveedores fiables, en la guía: comenta “{verde:proveedores}”", "foto": f(4), "guia": "pack"}],
    cap("3 cosas que nunca debes aceptar como vendedor en Vinted 🚫", "¿te han pedido alguna?", "comenta “proveedores” y te paso el link 👇",
        "#vinted #estafasvinted #cuentavinted #proveedores #wallapop"))

add("2026-11-21_1230", "test: eres revendedor", "test «cuántas haces» (nuevo)", "neonbass", [
    {"titulo": "¿eres revendedor de verdad? cuenta cuántas haces", "foto": f(35), "vinted": True},
    {"titulo": "1. tienes un cajón solo de bolsas", "foto": f(13)},
    {"titulo": "2. sabes dónde está cada taquilla de tu barrio", "foto": f(21)},
    {"titulo": "3. miras la etiqueta de todo lo que tocas", "foto": f(7)},
    {"titulo": "4. contestas mensajes en la cena", "foto": f(11)},
    {"titulo": "5. tu casa es un almacén", "foto": f(9)},
    {"titulo": "dime tu número 👇", "texto": "si te falta stock: comenta “{azul:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("¿eres revendedor de verdad? cuenta cuántas haces 😂", "dime tu número 👇", "comenta “proveedores” y te los paso",
        "#reventa #vinted #fyp #humor #proveedores"))

add("2026-11-21_1735", "historia: subía y no vendía", "historia + solución", "kaleido", [
    {"titulo": "al principio subía y no vendía nada (esto cambié)", "foto": f(10), "vinted": True},
    {"titulo": "1. la primera foto", "texto": "de día, prenda entera, fondo limpio", "foto": f(17)},
    {"titulo": "2. el título", "texto": "prenda + marca + color + talla", "foto": f(38)},
    {"titulo": "3. el stock", "texto": "dejé de comprar lo que me gustaba a mí", "foto": f(9)},
    {"titulo": "¿cuál te falta: 1, 2 o 3?", "texto": "el 3, en la guía: comenta “{verde:proveedores}”", "foto": f(26), "guia": "pack"}],
    cap("al principio subía a Vinted y no vendía nada (esto cambié)", "¿cuál te falta: 1, 2 o 3?", "te dejo mis proveedores: comenta “proveedores”",
        "#vinted #revenderropa #trucosvinted #proveedores #emprender"))

add("2026-11-21_2035", "lista negativa: ropa por kilo", "lista negativa", "coolgirl", [
    {"titulo": "lo que NO compraría en un lote de ropa por kilo 🚫", "foto": f(13), "vinted": True},
    {"titulo": "1. lotes «mixtos» sin fotos", "texto": "suele ser marca blanca y cosas rotas", "foto": f(35)},
    {"titulo": "2. lotes de verano en noviembre", "texto": "los tienes parados hasta mayo", "foto": f(24)},
    {"titulo": "3. lotes sin decir tallas", "texto": "te pueden llegar todo XS o todo XXL", "foto": f(38)},
    {"titulo": "lo que sí: lote con marcas y fotos reales", "texto": "los proveedores que uso, en mi bio", "foto": f(29)},
    {"titulo": "¿has comprado por kilo?", "texto": "comenta “{verde:proveedores}” y te paso los míos", "foto": f(9), "guia": "ropa"}],
    cap("lo que NO compraría en un lote de ropa por kilo 🚫", "¿has comprado alguna vez por kilo?", "¿los quieres? comenta “proveedores” 📦",
        "#ropaporkilo #vinted #reventa #proveedores #mayorista"))

add("2026-11-21_2330", "pregunta con respuesta: cuándo subir", "pregunta con respuesta al final", "maybeyou", [
    {"titulo": "¿a qué hora subo a Vinted? (te lo digo al final)", "foto": f(2), "vinted": True},
    {"titulo": "por la mañana no", "texto": "la gente está trabajando o en clase", "foto": f(32)},
    {"titulo": "por la noche y el domingo", "texto": "cuando tu comprador está en el sofá con el móvil. a mí es lo que mejor me va", "foto": f(11)},
    {"titulo": "¿a qué hora subes tú?", "texto": "si te falta stock: comenta “{azul:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("¿a qué hora subo a Vinted? 🌙", "¿a qué hora subes tú?", "comenta “proveedores” y te paso el link",
        "#vinted #trucosvinted #reventa #proveedores #fyp", bio=False))

# ---------------- DOMINGO 22 NOV ----------------
add("2026-11-22_0940", "riesgo: perfil que da desconfianza", "riesgo concreto (lista)", "neonnights", [
    {"titulo": "3 cosas de tu perfil que hacen que no te compren 🚩", "caja": True, "foto": f(32), "vinted": True},
    {"titulo": "1. sin foto de perfil ni descripción", "texto": "parece cuenta falsa", "foto": f(11)},
    {"titulo": "2. 0 valoraciones", "texto": "vende 2-3 cosas baratas primero para tenerlas", "foto": f(13)},
    {"titulo": "3. tardar un día en contestar", "texto": "en ese tiempo ya han comprado otra", "foto": f(23)},
    {"titulo": "¿cuál te falta?", "texto": "y si quieres stock: comenta “{verde:proveedores}”", "foto": f(4), "guia": "pack"}],
    cap("3 cosas de tu perfil de Vinted que hacen que no te compren 🚩", "¿cuál te falta?", "escribe “proveedores” y te digo cuáles uso 📦",
        "#vinted #perfilvinted #trucosvinted #proveedores #revenderropa"))

add("2026-11-22_1235", "lista: checklist del domingo", "lista qué hacer", "didit", [
    {"titulo": "lo que hago cada domingo en Vinted (10 min) 📲", "sub": "(guárdalo)", "foto": f(32), "vinted": True},
    {"titulo": "1. subo lo mejor de la semana", "texto": "el domingo hay más gente mirando", "foto": f(18)},
    {"titulo": "2. mando ofertas a los favoritos", "texto": "un 10 % menos. les llega aviso", "foto": f(11)},
    {"titulo": "3. cambio la 1ª foto de lo que no se mueve", "foto": f(17)},
    {"titulo": "4. preparo los envíos del lunes", "texto": "bolsas y etiquetas listas", "foto": f(34)},
    {"titulo": "5. apunto qué se ha vendido", "texto": "eso es lo que vuelvo a comprar", "foto": f(9)},
    {"titulo": "¿cuál haces ya?", "texto": "dónde lo compro: comenta “{amarillo:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("lo que hago cada domingo en Vinted (10 min) 📲", "¿cuál haces ya?", "comenta “proveedores” y te paso el link 👇",
        "#vinted #domingo #trucosvinted #proveedores #reventa"))

add("2026-11-22_1725", "frases: nunca en la descripción", "frases exactas (negativa)", "mint", [
    {"titulo": "3 frases que nunca pondría en Vinted ✍️🚫", "foto": f(29), "vinted": True},
    {"titulo": "1. «como nuevo» (si no lo está)", "texto": "te abren reclamación y la pierdes", "foto": f(28)},
    {"titulo": "2. «no hago devoluciones»", "texto": "el comprador está protegido igual. solo espanta", "foto": f(11)},
    {"titulo": "3. «precio negociable»", "texto": "te van a ofrecer la mitad. mejor pon el precio bien", "foto": f(38)},
    {"titulo": "¿cuál tenías puesta?", "texto": "los míos, en la guía: comenta “{verde:proveedores}”", "foto": f(9), "guia": "pack"}],
    cap("3 frases que nunca pondría en una descripción de Vinted ✍️🚫", "¿cuál tenías puesta?", "¿los quieres? comenta “proveedores” 📦",
        "#vinted #descripcionvinted #trucosvinted #proveedores #wallapop"))

add("2026-11-22_2035", "aprendizajes: empezar hoy", "aprendizajes", "zara", [
    {"titulo": "lo que haría distinto si empezara a revender hoy", "foto": f(32), "vinted": True},
    {"titulo": "1. empezar con poco", "texto": "10 prendas buenas, no 100 regulares", "foto": f(17)},
    {"titulo": "2. un solo nicho", "texto": "zapatillas, perfumes o ropa. no todo a la vez", "foto": f(18)},
    {"titulo": "3. buscar proveedor desde el día 1", "texto": "comprar suelto en tiendas no da margen", "foto": f(35)},
    {"titulo": "4. subir algo cada día", "texto": "aunque sea 1 prenda", "foto": f(13)},
    {"titulo": "¿cuál te falta?", "texto": "te paso los míos: comenta “{verde:proveedores}”", "foto": f(9), "guia": "pack"}],
    cap("lo que haría distinto si empezara a revender hoy", "¿cuál te falta a ti?", "te dejo mis proveedores: comenta “proveedores” 👇",
        "#reventa #emprender #vinted #proveedores #negocioonline"))

add("2026-11-22_2335", "POV: domingo noche envíos", "POV relatable (nuevo)", "polar", [
    {"titulo": "POV: domingo noche preparando los envíos del lunes", "foto": f(34), "vinted": True},
    {"titulo": "el salón lleno de bolsas", "foto": f(15)},
    {"titulo": "y piensas: «el lunes empiezo otra cosa» 😂", "texto": "mentira. el lunes subes más", "foto": f(13)},
    {"titulo": "¿cuántos envías mañana?", "texto": "si te falta stock: comenta “{rojo:proveedores}”", "foto": f(5), "guia": "pack"}],
    cap("POV: domingo noche preparando los envíos del lunes 📦", "¿cuántos envías mañana?", "comenta “proveedores” y te paso el link",
        "#vinted #reventa #fyp #envios #proveedores", bio=False))


if __name__ == "__main__":
    for carpeta, hora, tema, formato, audio, slides, caption in C:
        d = os.path.join(AQUI, carpeta)
        os.makedirs(d, exist_ok=True)
        g = {"plantilla": "pinterest", "slides": slides, "caption": caption, "tema": tema, "formato": formato,
             "hora_publicacion": hora, "audio": AUD[audio]}
        json.dump(g, open(os.path.join(d, "guion.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(C), [len(c[5]) for c in C])
