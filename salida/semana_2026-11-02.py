"""Guiones de la semana 2-8 nov 2026 (plantilla pinterest). Genera salida/<fecha_hora>/guion.json.
Basado en: ganchos top de @927studios (avisos 🚫, dinero en Vinted, cuenta nueva, "¿te ha pasado?", qué vender por temporada)
y estructuras de carruseles virales del nicho (listas, antes/ahora, serie de proveedores, "cosas que aprendí")."""
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
f = lambda n: f"aritz927_{n:02d}.jpg"
C = []  # (carpeta, hora, tema, formato, sonido, slides, caption)

def cap(l1, q, cta, tags):
    return f"{l1}\n{q}\n\n{cta}\n👉 Guías en el link de mi bio\n\n{tags}"

# ---------------- LUNES 2 NOV ----------------
C.append(("2026-11-02_0935","2026-11-02 09:35","riesgo de cuenta: avisos de Vinted","riesgo de cuenta","selfaware",[
 {"titulo":"si Vinted te manda este aviso, para 🚫","caja":True,"foto":f(23),"vinted":True},
 {"titulo":"1. «tu artículo ha sido ocultado»","texto":"suele ser por foto copiada o marca dudosa. cambia fotos y descripción","foto":f(11)},
 {"titulo":"2. «actividad inusual»","texto":"subes o editas demasiado de golpe. baja el ritmo 48 h","foto":f(32)},
 {"titulo":"3. «verifica tu identidad»","texto":"hazlo cuanto antes. sin eso no puedes retirar","foto":f(25)},
 {"titulo":"¿te ha llegado alguno?","texto":"y si quieres stock que no dé problemas: comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("avisos de Vinted que no puedes ignorar 🚫","¿te ha llegado alguno?","comenta “proveedores” y te digo cuáles uso 👇","#vinted #cuentavinted #trucosvinted #proveedores #fyp")))

C.append(("2026-11-02_1240","2026-11-02 12:40","dinero: cuánto pagas de envío","dinero en Vinted","espresso",[
 {"titulo":"¿quién paga el envío en Vinted?","sub":"(casi nadie lo tiene claro)","foto":f(21),"vinted":True},
 {"titulo":"el envío lo paga el comprador","texto":"tú solo preparas el paquete y lo llevas al punto","foto":f(27)},
 {"titulo":"pero el tamaño lo eliges tú","texto":"si pones «pequeño» y no cabe, problemas. mide antes de subir","foto":f(35)},
 {"titulo":"truco:","texto":"bolsas de envío finas = paquete pequeño = más barato para quien compra = vendes antes","foto":f(15)},
 {"titulo":"¿qué tamaño pones tú?","texto":"los proveedores que uso, en la guía: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("¿quién paga el envío en Vinted? 📦","¿qué tamaño pones tú?","escribe “proveedores” y te los mando 📩","#vinted #enviosvinted #revenderropa #proveedores #reventa")))

C.append(("2026-11-02_1725","2026-11-02 17:25","error→solución: precio","error → solución","mint",[
 {"titulo":"por esto tu precio espanta","sub":"(y no es que sea caro)","foto":f(29),"vinted":True},
 {"titulo":"1. terminas en 0","texto":"20€ parece redondo. 18€ parece oferta","foto":f(17)},
 {"titulo":"2. no dejas margen para ofertas","texto":"en Vinted casi todos regatean. súbelo un poco y baja cuando te escriban","foto":f(38)},
 {"titulo":"3. no miras lo vendido","texto":"filtra «vendido» de la misma marca y talla. ese es tu precio real","foto":f(32)},
 {"titulo":"¿cuál hacías tú? 1, 2 o 3","texto":"y si te falta producto: comenta “{verde:proveedores}”","foto":f(28),"guia":"ropa"}],
 cap("tu precio en Vinted puede estar espantando 💸","¿cuál hacías tú? 1, 2 o 3","comenta “proveedores” y te paso el link 👇","#vinted #preciosvinted #trucosvinted #proveedores #revenderropa")))

C.append(("2026-11-02_2035","2026-11-02 20:35","lista negativa: qué no comprar en noviembre","lista negativa","zara",[
 {"titulo":"3 cosas que NO compraría para revender en noviembre","foto":f(13),"vinted":True},
 {"titulo":"1. ropa de verano","texto":"se queda parada hasta mayo. dinero dormido","foto":f(24)},
 {"titulo":"2. tallas muy raras","texto":"XXS o XXXL se venden, pero tardan el triple","foto":f(17)},
 {"titulo":"3. marcas que nadie busca","texto":"si no aparece en el buscador, no existe","foto":f(29)},
 {"titulo":"lo que sí: abrigos, sudaderas y regalos","texto":"proveedores de eso, en la guía: comenta “{verde:proveedores}”","foto":f(38),"guia":"ropa"}],
 cap("lo que yo NO compraría para revender ahora 🚫","¿cuál comprarías tú igual?","¿los quieres? comenta “proveedores” 📦","#reventa #vinted #noviembre #proveedores #revenderropa")))

C.append(("2026-11-02_2330","2026-11-02 23:30","reflexión: empezar lunes","reflexión","untitled",[
 {"titulo":"llevas meses diciendo «el lunes empiezo»","foto":f(36),"vinted":True},
 {"titulo":"hoy es lunes.","foto":f(32)},
 {"titulo":"no necesitas 500€","texto":"necesitas 1 prenda, 4 fotos y 10 minutos","foto":f(29)},
 {"titulo":"¿la subes hoy o el lunes que viene?","texto":"si te falta stock: escribe “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("hoy es lunes 🌙","¿la subes hoy o el lunes que viene?","escribe “proveedores” y te los mando 📩","#emprendimiento #vinted #reventa #mentalidad #proveedores")))

# ---------------- MARTES 3 NOV ----------------
C.append(("2026-11-03_0940","2026-11-03 09:40","riesgo: ventas fuera de Vinted","riesgo de cuenta","timeback",[
 {"titulo":"esto puede costarte la cuenta de Vinted 🚫","caja":True,"foto":f(25),"vinted":True},
 {"titulo":"1. poner tu Instagram en la descripción","foto":f(32)},
 {"titulo":"2. aceptar Bizum «para ir más rápido»","texto":"sin protección. si no llega, pierdes la prenda","foto":f(11)},
 {"titulo":"3. enviar sin generar la etiqueta","texto":"si se pierde, Vinted no te cubre","foto":f(21)},
 {"titulo":"guárdalo y que no te pase","texto":"¿te paso mis proveedores? comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("cosas que pueden costarte la cuenta de Vinted 🚫","¿alguna vez te han pedido Bizum?","¿te paso mis proveedores? comenta “proveedores” 📦","#vinted #cuentavinted #estafasvinted #proveedores #wallapop")))

C.append(("2026-11-03_1245","2026-11-03 12:45","compra→venta: abrigos (ejemplos)","precio compra → venta","didit",[
 {"titulo":"lo que más se mueve cuando llega el frío","sub":"(precios de ejemplo)","foto":f(28),"vinted":True},
 {"titulo":"plumífero de marca","precios":["25€","60€"],"foto":f(29)},
 {"titulo":"sudadera gruesa","precios":["9€","28€"],"foto":f(38)},
 {"titulo":"zapatillas de marca","precios":["30€","70€"],"foto":f(19)},
 {"titulo":"¿cuál pillarías primero?","texto":"dónde comprarlos, en la guía: comenta “{verde:proveedores}”","foto":f(18),"guia":"ropa"}],
 cap("lo que más se vende en Vinted cuando hace frío ❄️ (precios de ejemplo)","¿cuál pillarías primero?","comenta “proveedores” y te los paso 📦","#vinted #invierno #revenderropa #proveedores #reventa")))

C.append(("2026-11-03_1720","2026-11-03 17:20","error→solución: favoritos sin venta","error → solución","mint",[
 {"titulo":"20 favoritos y nadie compra 😩","foto":f(11),"vinted":True},
 {"titulo":"el favorito es un «me lo pienso»","texto":"hay que darles un empujón","foto":f(32)},
 {"titulo":"1. envía oferta a los favoritos","texto":"un 10 % menos. Vinted les avisa al momento","foto":f(23)},
 {"titulo":"2. haz pack","texto":"«llévate 2 y te hago descuento» en la descripción","foto":f(29)},
 {"titulo":"¿cuántos favoritos tiene tu prenda más vista?","texto":"para comprar barato: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("muchos favoritos y 0 ventas en Vinted 😩","¿cuántos tiene tu prenda más vista?","¿los quieres? escribe “proveedores” 📦","#vinted #trucosvinted #favoritosvinted #proveedores #fyp")))

C.append(("2026-11-03_2030","2026-11-03 20:30","serie proveedores: perfumes y belleza (parte 4)","serie de proveedores","tesla",[
 {"titulo":"proveedores de belleza que tienes que conocer","sub":"(parte 4)","foto":f(31),"vinted":True},
 {"titulo":"proveedor de perfumes nicho","texto":"formatos pequeños y decants. se envían fácil","foto":f(31)},
 {"titulo":"proveedor de cosmética coreana","texto":"tendencia todo el año. compra con fecha larga","foto":f(20)},
 {"titulo":"proveedor de packs de regalo","texto":"en noviembre y diciembre vuelan","foto":f(37)},
 {"titulo":"¿de qué quieres la parte 5?","texto":"los contactos, en la guía: comenta “{verde:proveedores}”","foto":f(20),"guia":"belleza"}],
 cap("proveedores de belleza para revender (parte 4) 💄","¿de qué quieres la parte 5?","comenta “proveedores” y te paso el link 👇","#proveedores #belleza #perfumes #reventa #mayorista")))

C.append(("2026-11-03_2335","2026-11-03 23:35","antes/ahora: armario","antes / ahora","another",[
 {"titulo":"2023:","texto":"«no tengo nada que ponerme»","foto":f(36),"vinted":True},
 {"titulo":"2026:","texto":"«no tengo sitio para tanto stock»","foto":f(35)},
 {"titulo":"lo que cambió:","texto":"dejé de comprar para mí y empecé a comprar para vender","foto":f(9)},
 {"titulo":"¿en qué año estás tú?","texto":"si quieres empezar: escribe “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("2023 vs 2026 😂","¿en qué año estás tú?","escribe “proveedores” y te los mando 📩","#vinted #reventa #fyp #proveedores #emprender")))

# ---------------- MIÉRCOLES 4 NOV ----------------
C.append(("2026-11-04_0930","2026-11-04 09:30","dinero: comisiones (lo que pagas)","dinero en Vinted","selfaware",[
 {"titulo":"¿cuánto te quita Vinted de cada venta?","foto":f(23),"vinted":True},
 {"titulo":"como vendedor particular:","texto":"la comisión la paga el comprador (protección). a ti te llega el precio que pones","foto":f(11)},
 {"titulo":"lo que sí te come margen:","texto":"bolsas, etiquetas, tu tiempo y las ofertas que aceptas","foto":f(15)},
 {"titulo":"y si vendes como negocio","texto":"las condiciones cambian. infórmate antes de crecer","foto":f(32)},
 {"titulo":"¿lo sabías?","texto":"el margen de verdad está en comprar bien: comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("lo que te quita Vinted de cada venta (de verdad) 👀","¿lo sabías?","comenta “proveedores” y te digo cuáles uso 👇","#vinted #comisionesvinted #dinero #proveedores #reventa")))

C.append(("2026-11-04_1235","2026-11-04 12:35","lista: marcas que suben en invierno","lista de marcas","zara",[
 {"titulo":"marcas que suben de precio en invierno","foto":f(7),"vinted":True},
 {"titulo":"The North Face","texto":"plumíferos y forros. se buscan muchísimo","foto":f(28)},
 {"titulo":"Ralph Lauren","texto":"jerséis de cable y polos de manga larga","foto":f(24)},
 {"titulo":"Nike Tech","texto":"conjuntos completos. mejor en pack","foto":f(17)},
 {"titulo":"Carhartt","texto":"chaquetas y gorros. aguantan precio","foto":f(38)},
 {"titulo":"¿cuál vendes más?","texto":"proveedores de ropa, en la guía: comenta “{verde:proveedores}”","foto":f(18),"guia":"ropa"}],
 cap("marcas que suben de precio en invierno en Vinted 🧥","¿cuál vendes más?","¿los quieres? comenta “proveedores” 📦","#vinted #marcas #revenderropa #proveedores #invierno")))

C.append(("2026-11-04_1730","2026-11-04 17:30","error→solución: título","error → solución","espresso",[
 {"titulo":"nadie encuentra tu prenda (y es por el título)","foto":f(32),"vinted":True},
 {"titulo":"mal:","texto":"«sudadera bonita como nueva»","foto":f(38)},
 {"titulo":"bien:","texto":"«sudadera Nike gris talla M algodón»","foto":f(17)},
 {"titulo":"la fórmula:","texto":"prenda + marca + color + talla + detalle","foto":f(29)},
 {"titulo":"guárdalo para tu próxima subida","texto":"y si te falta stock: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("tu título en Vinted puede estar escondiendo tu prenda ✍️","¿cómo lo escribes tú?","comenta “proveedores” y te paso el link 👇","#vinted #titulovinted #trucosvinted #proveedores #revenderropa")))

C.append(("2026-11-04_2040","2026-11-04 20:40","confesión: primer pedido a proveedor","confesión","timeback",[
 {"titulo":"mi primer pedido a un proveedor salió mal","foto":f(9),"vinted":True},
 {"titulo":"pedí demasiado de golpe","texto":"la mitad era talla única que nadie buscaba","foto":f(35)},
 {"titulo":"no pedí muestra","texto":"la calidad no era la de las fotos","foto":f(13)},
 {"titulo":"lo que hago ahora:","texto":"muestra primero, pedido pequeño, y repetir lo que se vende","foto":f(32)},
 {"titulo":"¿a ti te ha pasado?","texto":"los que uso ahora, en la guía: comenta “{verde:proveedores}”","foto":f(26),"guia":"pack"}],
 cap("mi primer pedido a un proveedor salió mal 😅","¿a ti te ha pasado?","escribe “proveedores” y te digo cuáles uso 📦","#proveedores #reventa #vinted #emprender #mayorista")))

C.append(("2026-11-04_2325","2026-11-04 23:25","reflexión: miércoles","reflexión","untitled",[
 {"titulo":"mitad de semana. ¿cuántas has subido?","foto":f(36),"vinted":True},
 {"titulo":"si son 0, no pasa nada","foto":f(32)},
 {"titulo":"sube 2 antes de dormir","texto":"mañana alguien las verá mientras desayuna","foto":f(29)},
 {"titulo":"dime un número abajo 👇","texto":"y si te falta stock: escribe “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("mitad de semana 🌙","¿cuántas has subido? dime un número","escribe “proveedores” y te los mando 📩","#vinted #constancia #reventa #proveedores #mentalidad")))

# ---------------- JUEVES 5 NOV ----------------
C.append(("2026-11-05_0935","2026-11-05 09:35","riesgo: estafas a vendedores","riesgo de cuenta","selfaware",[
 {"titulo":"3 estafas a vendedores en Vinted 🚩","caja":True,"foto":f(11),"vinted":True},
 {"titulo":"1. «te pago fuera y te mando el link»","texto":"links falsos para robarte datos. todo dentro de la app","foto":f(23)},
 {"titulo":"2. «me ha llegado vacío»","texto":"graba siempre el embalaje antes de cerrar","foto":f(15)},
 {"titulo":"3. «cambia la dirección por chat»","texto":"nunca. solo la que sale en la etiqueta","foto":f(21)},
 {"titulo":"¿te ha pasado alguna?","texto":"proveedores fiables, en la guía: comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("estafas a vendedores en Vinted 🚩","¿te ha pasado alguna?","comenta “proveedores” y te digo cuáles uso 👇","#vinted #estafasvinted #cuentavinted #proveedores #fyp")))

C.append(("2026-11-05_1240","2026-11-05 12:40","qué vender: Black Friday","temporada","didit",[
 {"titulo":"qué vender la semana del Black Friday","foto":f(22),"vinted":True},
 {"titulo":"1. cosas para regalar","texto":"perfumes, carteras, gorros. la gente busca regalo","foto":f(31)},
 {"titulo":"2. packs","texto":"2 o 3 prendas juntas con precio cerrado","foto":f(29)},
 {"titulo":"3. tecnología pequeña","texto":"auriculares y cargadores. con factura siempre","foto":f(33)},
 {"titulo":"¿qué vas a sacar tú?","texto":"proveedores de todo esto: comenta “{verde:proveedores}”","foto":f(37),"guia":"pack"}],
 cap("qué vender en Vinted la semana del Black Friday 🛍️","¿qué vas a sacar tú?","¿los quieres? comenta “proveedores” 📦","#blackfriday #vinted #reventa #proveedores #negocioonline")))

C.append(("2026-11-05_1725","2026-11-05 17:25","error→solución: devoluciones","error → solución","mint",[
 {"titulo":"me abrieron una devolución y la gané","sub":"(así)","foto":f(27),"vinted":True},
 {"titulo":"1. fotos reales con defectos","texto":"si sale en la foto, no hay discusión","foto":f(29)},
 {"titulo":"2. medidas en la descripción","texto":"«me queda pequeño» no es motivo si pusiste medidas","foto":f(17)},
 {"titulo":"3. vídeo del embalaje","texto":"10 segundos y te ahorras el problema","foto":f(15)},
 {"titulo":"¿te han abierto alguna?","texto":"y para vender producto bueno: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("cómo ganar una devolución en Vinted 📦","¿te han abierto alguna?","escribe “proveedores” y te los mando 📩","#vinted #devolucionesvinted #trucosvinted #proveedores #revenderropa")))

C.append(("2026-11-05_2035","2026-11-05 20:35","aprendizajes: 6 meses revendiendo","aprendizajes","another",[
 {"titulo":"cosas que nadie te dice de revender","foto":f(9),"vinted":True},
 {"titulo":"las primeras semanas no vendes","texto":"Vinted tiene que conocerte. sigue subiendo","foto":f(36)},
 {"titulo":"no todo se vende","texto":"y no pasa nada. lo bajas o lo metes en pack","foto":f(13)},
 {"titulo":"el dinero está al comprar","texto":"no al vender. compra barato o no compres","foto":f(26)},
 {"titulo":"y que se vuelve adictivo","texto":"cada notificación de venta 😂","foto":f(23)},
 {"titulo":"¿cuál te ha pasado?","texto":"los proveedores que uso: escribe “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("lo que nadie te dice de revender 🌙","¿cuál te ha pasado a ti?","escribe “proveedores” y te digo cuáles uso 📦","#vinted #reventa #emprender #proveedores #mentalidad")))

C.append(("2026-11-05_2330","2026-11-05 23:30","reflexión: 1 venta","reflexión","untitled",[
 {"titulo":"tu primera venta no te hará rico","foto":f(36),"vinted":True},
 {"titulo":"pero te demuestra que funciona","foto":f(21)},
 {"titulo":"y la segunda llega antes","texto":"y la tercera antes todavía","foto":f(5)},
 {"titulo":"¿cuántas llevas tú?","texto":"si te falta stock: escribe “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("la primera venta lo cambia todo 🌙","¿cuántas llevas tú?","escribe “proveedores” y te los mando 📩","#vinted #reventa #constancia #proveedores #emprendimiento")))

# ---------------- VIERNES 6 NOV ----------------
C.append(("2026-11-06_0940","2026-11-06 09:40","riesgo: cuenta nueva","riesgo de cuenta","timeback",[
 {"titulo":"¿cuenta nueva en Vinted? lee esto antes 🚫","caja":True,"foto":f(25),"vinted":True},
 {"titulo":"día 1-3:","texto":"completa perfil, foto y verifica el móvil. sube 3-5 prendas","foto":f(32)},
 {"titulo":"día 4-7:","texto":"5 más al día. contesta rápido a todo","foto":f(11)},
 {"titulo":"semana 2:","texto":"ya puedes subir más. lo que no: 50 de golpe el primer día","foto":f(5)},
 {"titulo":"guárdalo para tu cuenta nueva","texto":"¿te paso mis proveedores? comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("cuenta nueva en Vinted: haz esto antes de subir nada 📱","¿la tuya tiene menos de un mes?","¿te paso mis proveedores? comenta “proveedores” 📦","#vinted #cuentanueva #trucosvinted #proveedores #wallapop")))

C.append(("2026-11-06_1245","2026-11-06 12:45","compra→venta: menos de 15€","precio compra → venta","zara",[
 {"titulo":"lo que compro a menos de 15€ y se vende rápido","sub":"(precios de ejemplo)","foto":f(20),"vinted":True},
 {"titulo":"gorro de marca","precios":["4€","15€"],"foto":f(38)},
 {"titulo":"camiseta de fútbol","precios":["12€","35€"],"foto":f(17)},
 {"titulo":"auriculares sellados","precios":["14€","30€"],"foto":f(33)},
 {"titulo":"cinturón de piel","precios":["6€","20€"],"foto":f(22)},
 {"titulo":"¿cuál empezarías?","texto":"dónde comprarlo, en la guía: comenta “{verde:proveedores}”","foto":f(37),"guia":"pack"}],
 cap("cosas de menos de 15€ que se venden rápido en Vinted 💸 (precios de ejemplo)","¿con cuál empezarías?","comenta “proveedores” y te los paso 📦","#vinted #reventa #ideasdenegocio #proveedores #fyp")))

C.append(("2026-11-06_1725","2026-11-06 17:25","error→solución: fotos de noche","error → solución","espresso",[
 {"titulo":"¿haces las fotos por la noche? ojo","foto":f(36),"vinted":True},
 {"titulo":"luz amarilla = color falso","texto":"el gris parece beige y luego hay devolución","foto":f(29)},
 {"titulo":"solución 1:","texto":"fotos de día junto a la ventana, sin flash","foto":f(17)},
 {"titulo":"solución 2:","texto":"si es de noche, luz blanca y fondo liso","foto":f(38)},
 {"titulo":"¿a qué hora las haces tú?","texto":"y para tener qué fotografiar: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("tus fotos de noche te están quitando ventas 📸","¿a qué hora las haces tú?","escribe “proveedores” y te digo cuáles uso 📦","#vinted #fotosvinted #trucosvinted #proveedores #revenderropa")))

C.append(("2026-11-06_2030","2026-11-06 20:30","serie proveedores: tecnología (parte 5)","serie de proveedores","tesla",[
 {"titulo":"proveedores de tecnología que tienes que conocer","sub":"(parte 5)","foto":f(33),"vinted":True},
 {"titulo":"proveedor de auriculares","texto":"pide factura y garantía. sin eso no vendas","foto":f(26)},
 {"titulo":"proveedor de accesorios de móvil","texto":"fundas y cargadores. margen alto y poco peso","foto":f(11)},
 {"titulo":"proveedor de retro gaming","texto":"mandos y consolas pequeñas. coleccionistas pagan bien","foto":f(36)},
 {"titulo":"¿de qué quieres la parte 6?","texto":"los contactos, en la guía: comenta “{verde:proveedores}”","foto":f(37),"guia":"tecnologia"}],
 cap("proveedores de tecnología para revender (parte 5) 🎧","¿de qué quieres la parte 6?","comenta “proveedores” y te paso el link 👇","#proveedores #tecnologia #reventa #vinted #mayorista")))

C.append(("2026-11-06_2340","2026-11-06 23:40","relatable: viernes noche","relatable","timeback",[
 {"titulo":"viernes noche:","texto":"ellos de fiesta","foto":f(4),"vinted":True},
 {"titulo":"yo:","texto":"etiquetando 9 paquetes","foto":f(15)},
 {"titulo":"y no lo cambiaría","texto":"el lunes llegan las valoraciones 😂","foto":f(21)},
 {"titulo":"¿tú dónde estás ahora?","texto":"si quieres empezar: escribe “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("viernes noche de revendedor 📦😂","¿tú dónde estás ahora?","escribe “proveedores” y te los mando","#vinted #reventa #fyp #proveedores #emprendimiento")))

# ---------------- SÁBADO 7 NOV ----------------
C.append(("2026-11-07_0935","2026-11-07 09:35","dinero: cuándo te pagan","dinero en Vinted","selfaware",[
 {"titulo":"¿cuándo te paga Vinted de verdad?","foto":f(23),"vinted":True},
 {"titulo":"1. el comprador recibe","texto":"y confirma que todo está bien","foto":f(27)},
 {"titulo":"2. o pasan 2 días","texto":"si no dice nada, se confirma solo","foto":f(32)},
 {"titulo":"3. el dinero va a tu monedero","texto":"de ahí lo pasas al banco (tarda unos días)","foto":f(11)},
 {"titulo":"¿cuánto tienes en el monedero?","texto":"para que no pare de entrar: comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("¿cuándo te paga Vinted de verdad? 💸","¿lo sabías?","comenta “proveedores” y te digo cuáles uso 👇","#vinted #dinero #monederovinted #proveedores #reventa")))

C.append(("2026-11-07_1240","2026-11-07 12:40","Vinted vs Wallapop","comparación","didit",[
 {"titulo":"Vinted o Wallapop: dónde vendo cada cosa","foto":f(32),"vinted":True},
 {"titulo":"ropa y zapatillas → Vinted","texto":"más búsquedas y envío fácil","foto":f(38)},
 {"titulo":"cosas grandes → Wallapop","texto":"muebles, bicis. entrega en mano","foto":f(10)},
 {"titulo":"tecnología → las dos","texto":"sube en ambas y borra cuando vendas","foto":f(33)},
 {"titulo":"¿dónde vendes más tú?","texto":"proveedores para las dos: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("Vinted o Wallapop: dónde vender cada cosa 🤔","¿dónde vendes más tú?","¿los quieres? comenta “proveedores” 📦","#vinted #wallapop #reventa #proveedores #segundamano")))

C.append(("2026-11-07_1720","2026-11-07 17:20","lista: frases en la descripción","lista","mint",[
 {"titulo":"3 frases que hacen que te compren","foto":f(11),"vinted":True},
 {"titulo":"«envío en 24 h»","texto":"da confianza al momento","foto":f(21)},
 {"titulo":"«medidas en la foto 4»","texto":"menos preguntas, menos devoluciones","foto":f(17)},
 {"titulo":"«hago descuento en packs»","texto":"sube el ticket medio","foto":f(29)},
 {"titulo":"¿cuál pones tú?","texto":"y para tener buen producto: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("3 frases que hacen que te compren en Vinted 💬","¿cuál pones tú?","escribe “proveedores” y te los mando 📩","#vinted #descripcionvinted #trucosvinted #proveedores #revenderropa")))

C.append(("2026-11-07_2035","2026-11-07 20:35","plan: 100€ en un mes","plan paso a paso","zara",[
 {"titulo":"si tuviera 100€ y un mes, haría esto","foto":f(32),"vinted":True},
 {"titulo":"semana 1:","texto":"compro un lote pequeño a proveedor. nada de tiendas","foto":f(35)},
 {"titulo":"semana 2:","texto":"fotos de día y subo 3-5 al día","foto":f(29)},
 {"titulo":"semana 3:","texto":"ofertas a favoritos y packs","foto":f(11)},
 {"titulo":"semana 4:","texto":"vuelvo a comprar lo que se vendió. y repito","foto":f(5)},
 {"titulo":"¿con cuánto empezarías tú?","texto":"proveedores para empezar: comenta “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("si tuviera 100€ y un mes para revender, haría esto 💸","¿con cuánto empezarías tú?","¿te paso mis proveedores? comenta “proveedores” 📦","#reventa #vinted #emprender #proveedores #negocioonline")))

C.append(("2026-11-07_2330","2026-11-07 23:30","reflexión: sábado","reflexión","another",[
 {"titulo":"sábado noche y sigues pensando en tu negocio","foto":f(4),"vinted":True},
 {"titulo":"no estás loco","foto":f(36)},
 {"titulo":"estás construyendo algo","texto":"aunque todavía no lo vea nadie","foto":f(32)},
 {"titulo":"¿cuánto llevas?","texto":"y si te falta stock: escribe “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("si es sábado noche y piensas en tu negocio 🌙","¿cuánto llevas revendiendo?","escribe “proveedores” y te los mando 📩","#mentalidad #emprendimiento #vinted #reventa #proveedores")))

# ---------------- DOMINGO 8 NOV ----------------
C.append(("2026-11-08_0940","2026-11-08 09:40","riesgo: prendas prohibidas","riesgo de cuenta","timeback",[
 {"titulo":"3 cosas que Vinted no te deja vender 🚫","caja":True,"foto":f(11),"vinted":True},
 {"titulo":"1. réplicas","texto":"aunque pongas «inspirado en». te cierran la cuenta","foto":f(13)},
 {"titulo":"2. perfumes sin caja original","texto":"según el caso, te lo retiran","foto":f(31)},
 {"titulo":"3. cosmética abierta","texto":"usada o sin precinto, fuera","foto":f(20)},
 {"titulo":"¿lo sabías?","texto":"producto original y legal: comenta “{verde:proveedores}”","foto":f(4),"guia":"pack"}],
 cap("cosas que Vinted no te deja vender 🚫","¿lo sabías?","comenta “proveedores” y te digo cuáles uso 👇","#vinted #cuentavinted #normasvinted #proveedores #fyp")))

C.append(("2026-11-08_1235","2026-11-08 12:35","lista: qué subir el domingo","lista con promesa","didit",[
 {"titulo":"el domingo es el mejor día para subir","sub":"(y esto es lo que subo)","foto":f(32),"vinted":True},
 {"titulo":"1. lo de más valor","texto":"más gente mirando = más ofertas","foto":f(18)},
 {"titulo":"2. packs","texto":"la gente tiene tiempo para comparar","foto":f(29)},
 {"titulo":"3. renovar lo viejo","texto":"cambia la 1ª foto y el precio","foto":f(38)},
 {"titulo":"¿subes hoy?","texto":"si te falta stock: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("lo que subo a Vinted los domingos 📲","¿subes hoy?","¿los quieres? comenta “proveedores” 📦","#vinted #trucosvinted #reventa #proveedores #domingo")))

C.append(("2026-11-08_1730","2026-11-08 17:30","error→solución: preguntas","error → solución","espresso",[
 {"titulo":"«¿sigue disponible?» y luego nada 😩","foto":f(11),"vinted":True},
 {"titulo":"no contestes solo «sí»","texto":"pregunta talla o envía oferta del 5 %","foto":f(32)},
 {"titulo":"contesta en menos de 1 hora","texto":"después ya está mirando otra cuenta","foto":f(23)},
 {"titulo":"deja todo en la descripción","texto":"medidas, defectos, envío. menos dudas","foto":f(29)},
 {"titulo":"¿cuánto tardas en contestar?","texto":"y para comprar barato: comenta “{verde:proveedores}”","foto":f(5),"guia":"pack"}],
 cap("cuando te preguntan «¿sigue disponible?» y luego nada 😩","¿cuánto tardas en contestar?","escribe “proveedores” y te digo cuáles uso 📦","#vinted #trucosvinted #ventasvinted #proveedores #revenderropa")))

C.append(("2026-11-08_2040","2026-11-08 20:40","serie proveedores: relojes y joyas (parte 6)","serie de proveedores","tesla",[
 {"titulo":"proveedores de relojes y joyas que tienes que conocer","sub":"(parte 6)","foto":f(22),"vinted":True},
 {"titulo":"proveedor de relojes de acero","texto":"poco volumen, margen alto. envío en caja","foto":f(20)},
 {"titulo":"proveedor de plata 925","texto":"pide sello y certificado","foto":f(18)},
 {"titulo":"proveedor de bisutería por kilo","texto":"para packs y regalos de navidad","foto":f(13)},
 {"titulo":"¿de qué quieres la parte 7?","texto":"los contactos, en la guía: comenta “{verde:proveedores}”","foto":f(4),"guia":"relojes"}],
 cap("proveedores de relojes y joyas para revender (parte 6) ⌚","¿de qué quieres la parte 7?","comenta “proveedores” y te paso el link 👇","#proveedores #relojes #joyas #reventa #mayorista")))

C.append(("2026-11-08_2335","2026-11-08 23:35","reflexión: domingo semana","reflexión","untitled",[
 {"titulo":"la semana que viene puede ser distinta","foto":f(36),"vinted":True},
 {"titulo":"si haces 1 cosa distinta","foto":f(32)},
 {"titulo":"sube 1 prenda al día","texto":"7 días = 7 oportunidades más","foto":f(29)},
 {"titulo":"¿te apuntas?","texto":"si te falta stock: escribe “{verde:proveedores}”","foto":f(30),"guia":"pack"}],
 cap("nueva semana, mismo objetivo 🌙","¿te apuntas? escribe «yo»","escribe “proveedores” y te los mando 📩","#vinted #constancia #reventa #proveedores #emprender")))

if __name__ == "__main__":
    for carpeta, hora, tema, formato, sonido, slides, caption in C:
        d = os.path.join(AQUI, carpeta)
        os.makedirs(d, exist_ok=True)
        g = {"plantilla": "pinterest", "slides": slides, "caption": caption, "tema": tema, "formato": formato,
             "hora_publicacion": hora, "audio": sonido}
        json.dump(g, open(os.path.join(d, "guion.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(C))
