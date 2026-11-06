# ADN de los carruseles de 927studios

Cuenta: TikTok @927studios (Metricool blogId 7239868, zona Europe/Madrid).
Qué vende: guías de proveedores mayoristas (una por categoría) en https://927studios.myshopify.com/ (link en la bio).
Público: gente de 16-30 años que quiere empezar a revender (Vinted, Wallapop, tiendas online) con poco dinero.

## Mezcla de estilos
- **De Aritz (la base):** fotos reales de fondo (stock, paquetes, ropa, el portátil, el coche cargado), pasos numerados "1. 2. 3.", tono cercano de colega que ya lo hace, CTA de comentar una palabra.
  Sus carruseles que más funcionaron: "¿8 horas sentado?" (795 visualizaciones), "Siempre estoy pendiente a mi negocio" (746), "Cómo empezar de verdad a revender en Vinted con solo 50€" (730).
- **De la referencia ("PROVEEDORES EN BIO"):** letra gruesa en cursiva (Poppins Bold Italic), blanca con sombra, 1-3 **palabras clave en color** por diapositiva (amarillo, azul, rojo, verde), avisos cortos en rojo ("muy importante para evitar bloqueos"), "quédate hasta el final" en azul en la portada, la palabra VINTED grande en turquesa en la portada, CTA con la palabra entre comillas y en color.

## PLANTILLA DE ARITZ (9 oct 2026) — OBLIGATORIA para carruseles y vídeos
Usa siempre `"plantilla": "aritz"` en guion.json (formato en `plantilla.py`). Manda sobre los estilos de arriba si chocan.
- **Fondo**: la MISMA foto en todas las diapositivas del carrusel, en gris (blanco y negro con grano). **Cambia la foto de fondo en cada carrusel** (no pongas "fondo" ni "tema_fondo": el generador coge la menos usada de "fondo_gris"; nunca las del monedero).
- **Texto**: en etiquetas celestes con letra gruesa en cursiva azul oscuro, arriba y centrado. Corto.
- **Diapositiva 1 (portada)**: `titulo` = el problema/promesa, `sub` = gancho pequeño en etiqueta oscura ("espera hasta el final"), placa de **Vinted** debajo.
- **Diapositivas 2-5**: un paso de la solución cada una ("1. …", "2. …", "3. …", "4. …") + una **foto distinta** en el centro (`tema_foto` o `foto`). En el paso de proveedores pon la portada de la guía (`"guia": "pack"`) y abajo `"abajo": "link en mi bio 🔥"`.
- **Última**: derivar a comentar para conseguir los productos: "Comenta “proveedor” y te mando el acceso" + foto.
- **Zona visible (corrección de Aritz, 9 oct)**: en TikTok no puede haber texto ni foto en el 28 % de abajo (lo tapa el texto del post) ni pegado a la derecha (botones). El generador ya lo respeta; textos cortos para que quepan.
- Aquí sí se pueden usar emojis en el texto (se dibujan en color).
- Ejemplo de Aritz: "como pasar de 50€ → …" / 1. consigue buenos proveedores (pack) / 2. haz pedido y espera a que te llegue (cajas) / 3. haz buenas fotos y súbelas (ropa) / 4. disfruta de las ventas 📈💰 (monedero) / comenta "proveedor" (zapatillas lujo).

## Estructura (5-7 diapositivas)
1. **Portada / gancho**: promesa o curiosidad en 6-12 palabras + una línea pequeña en azul ("quédate hasta el final", "el 3 es el más importante") + marca "VINTED" opcional.
   Ganchos que funcionan: "Cómo empecé a revender con solo X€", "3 errores que…", "Top 3 nichos que tienes que vender sí o sí", "¿Has fallado? Enhorabuena…", "Consejos para nuevos revendedores 2026", "Si haces 5 ventas al día…".
2-5. **Un paso o consejo por diapositiva**: título "N. Algo" (tamaño l) + 1-2 frases de explicación (tamaño m) + aviso opcional en rojo (tamaño s).
Última. **CTA**: "Comenta “{amarillo:proveedores}” y te paso el link" + "Link en la bio !!" en rojo.

## Texto del post (caption)
- 1 línea con gancho + emoji (🔥💸📦), 1 línea "Comenta “proveedores” y te paso el link 👇".
- Hashtags (4-6): #reventa #vinted #proveedores #dinero #emprendimiento #fyp (rota 1-2 de #wallapop #dropshipping #negocioonline #mayorista).

## Reglas (lo que Aritz no haría)
- Nunca copiar textos ni imágenes de otras cuentas: solo coger la estructura.
- No inventar cifras personales ("gané 10.000€") ni capturas de ventas: solo cifras que Aritz haya dado. Sí se pueden usar ejemplos ("compras a 3€, vendes a 15€") presentados como ejemplo.
- Nada de emojis dentro de las imágenes (la fuente no los dibuja); emojis solo en el caption.
- Español de España, frases cortas, tuteo, sin palabrotas.
- No repetir un tema publicado en los últimos 7 días (mirar historial.json).
- Una diapositiva = una idea. Máximo ~30 palabras por diapositiva.

## Reglas del algoritmo (v3, 8 oct 2026) — OBLIGATORIAS
Lo que miden TikTok, Instagram y YouTube: que pasen de la 1ª a la 2ª foto (objetivo 70 %), cuántas fotos ven, tiempo mirando, guardados, comentarios y compartidos. En Shorts: el 70 % de los que se van lo hacen en los 2 primeros segundos.

**Portada (diapositiva 1) = el 80 % del éxito**
- Máximo 40 caracteres. Se entiende en 1 segundo.
- Deja una PREGUNTA ABIERTA, nunca anuncies el tema. Mal: "5 consejos para Vinted". Bien: "Por esto pierdes dinero en Vinted", "El error que comete el 90 % al revender", "Nadie te dice esto de los proveedores", "Dejé de comprar en AliExpress por esto".
- Formatos que funcionan: error→solución, lista con promesa ("3 cosas que nadie te cuenta"), confesión ("Cuando empecé, hacía esto mal"), polémica suave, número concreto.
- Usa la etiqueta de color (estilo texto nativo de TikTok) en la parte clave: {"t": "dinero en Vinted", "tam": "xxl", "caja": "amarillo"}. Colores de caja: amarillo, blanco, rojo, verde, azul, rosa.
- El generador añade solo el botón "desliza >>" en la portada.

**Diapositiva 2 = segundo gancho** (Instagram la vuelve a enseñar a quien no deslizó)
- Tiene que funcionar sola: giro o promesa ("No es tu ropa. Es a quién se la compras." + "te lo explico en 4 pasos").

**Diapositivas intermedias**
- Una idea por foto. Título corto + máximo 15 palabras. Se lee en 3 segundos.
- Cada una debe dar ganas de ver la siguiente (orden lógico, la mejor al final de la lista).
- El contador "1/5" lo pone el generador.
- Una dato o ejemplo concreto vale más que una frase general ("pagas 8€ por lo que vale 3€").

**Última diapositiva = guardado + comentario**
- Resuelve lo que prometía la portada.
- Pregunta fácil de contestar en etiqueta blanca ("¿Tú a quién le compras?", "¿El 1, 2 o 3?") + CTA "Comenta “proveedores”…".
- A veces añade "guárdalo para…" en la penúltima.

**Número de fotos**: 6-8 (TikTok), el mismo guion sirve para Instagram.
**Formatos**: el generador saca a la vez TikTok 9:16 (salida/X/) e Instagram 4:5 (salida/X/ig/). Aritz quiere SOLO CARRUSELES (no vídeos): no uses video.py salvo que él lo pida.
**Caption**: 1ª línea = gancho con palabras que la gente busca ("proveedores Vinted", "revender ropa") + pregunta + CTA. 3-5 hashtags.
**Música**: en TikTok siempre autoAddMusic true.

## CTA que convierte (v4, 8 oct) — OBLIGATORIO
- **Última diapositiva = enseñar el producto.** Pon "guia": "<categoría>" y el generador pega la portada REAL de la guía. Categorías: ropa, calzado, relojes, joyas, perfumes, belleza, accesorios, tecnologia, vaporizadores, bonus, pack. Elige la guía que encaja con el tema; si el tema es general (proveedores, Vinted, margen), usa "pack".
- Texto de la última: lo que se llevan, concreto ("Te paso mis proveedores de relojes", "Los 10 proveedores que uso, en una guía") en caja blanca + "Comenta “{verde:proveedores}”". Pon "tema_fondo": "objetivo" en esa diapositiva.
- **CTA suave a mitad** (penúltima o antepenúltima): una línea pequeña "los míos están en la guía de mi bio" o "el proveedor de esto está en mi bio".
- La pregunta para comentar puede ir en la diapositiva 2 o en la penúltima, para que la última se centre en la guía.
- Caption: termina con "👉 Guías en el link de mi bio" además de "Comenta “proveedores”".

## Fotos de estilo de vida ("objetivo") — reglas
- Fondos "objetivo", "reloj", "viaje", "escritorio", "coche_lujo", "ciudad": solo en la portada, en la diapositiva 2 o en la última.
- Siempre presentados como META ("tu objetivo", "que tu negocio pague esto"), NUNCA como "esto lo gané yo" ni como prueba de ganancias.
- Prohibido: fajos de billetes, capturas de ingresos, "hazte rico", "dinero fácil", "gana X€ al mes sin hacer nada". TikTok saca del Para ti el contenido de "hazte rico rápido".
- Los precios de ejemplo se presentan como "ejemplo", nunca como "real" ni como ventas de Aritz (salvo que Aritz pase capturas suyas).

## Anti-bot: que cada carrusel parezca hecho a mano (OBLIGATORIO)
Antes de escribir, lee los últimos 10 carruseles de historial.json y NO repitas:
- el mismo gancho ni la misma primera palabra del gancho que los 3 anteriores;
- la misma frase de CTA ni el mismo caption que el anterior;
- el mismo número de diapositivas dos veces seguidas (alterna entre 4, 5, 6 y 7);
- los mismos hashtags en el mismo orden (cambia 2-3 cada vez y el orden).
Varía también:
- **Formato de portada**: pregunta ("¿Sabes por qué no vendes en Vinted?"), lista ("3 errores que…"), historia ("Cuando empecé a revender…"), polémica ("Nadie te dice esto de los proveedores"), reto ("Si tienes 50€, haz esto").
- **Línea pequeña de la portada**: "quédate hasta el final", "el último es el más importante", "guárdalo para luego", "lee hasta el final", "el 3 te va a sorprender"… o ninguna.
- **Sello de Vinted en la portada: SIEMPRE** ("vinted": true en la plantilla aritz, "marca": "VINTED" en la normal). Aritz lo pidió el 12 oct.
- **CTA** (rota, siempre con la palabra “proveedores”):
  "Comenta “proveedores” y te paso el link" · "Escribe “proveedores” y te los mando" · "¿Los quieres? Comenta “proveedores”" · "Comenta “proveedores” y te digo cuáles uso" · "Te dejo mis proveedores: comenta “proveedores”"
  + a veces "Link en la bio !!", a veces "Están en mi bio", a veces nada más.
- **Colores**: no uses siempre amarillo; reparte entre amarillo, azul, verde, rojo y rosa.
- **Caption**: cambia la estructura (a veces pregunta, a veces frase corta, a veces 2 líneas), los emojis y la longitud.
- **Hora**: la publicación se programa con un retraso aleatorio de 5 a 50 minutos, nunca a la misma hora exacta.
- **Escritura natural**: algún "bro", "de verdad", "ojo", "literal", minúsculas al empezar alguna línea, como escribe Aritz. Sin pasarse.

## Temas (rotar y crear nuevos parecidos)
- Cómo empezar a revender con 50€ paso a paso
- 3 errores al empezar a revender
- Top 3 nichos para vender en Vinted ahora (ropa vintage por kilo, perfumes, electrónica pequeña, zapatillas, ropa de fútbol)
- Cómo saber si un proveedor es fiable (reseñas, muestras, pago seguro, tiempos de envío)
- Proveedores europeos vs chinos: ventajas de cada uno
- Cómo hacer fotos que venden (fondo neutro, luz natural, Photoroom)
- Cómo calentar una cuenta de Vinted nueva para evitar bloqueos
- Qué comprar por kilo y cómo clasificarlo
- Cómo calcular el margen antes de comprar (precio + envío + comisión)
- Cómo responder ofertas en Vinted sin perder dinero
- Rutina diaria de un revendedor (publicar, responder, enviar)
- Packaging barato que da buena impresión
- Temporadas: qué vender en otoño / Navidad / Black Friday / verano
- Señales de un proveedor estafa

## Aprendizajes de los datos (se actualiza cada día)
**Actualizado: 6 nov 2026** (Metricool, 30 oct 09:40 - 6 nov 08:40, solo carruseles PHOTO con más de 12 h; hora de Metricool en UTC pasada a Madrid; emparejados por hora + caption con historial.json y los guion.json de `salida/`). **33 carruseles medibles: 14.640 visitas, 143 me gusta (9,8 por 1.000), 8 comentarios (0,5 por 1.000), 6 compartidos.**
- ⚠️ Del 5 nov Metricool solo trae 3 de 5 (09:35, 12:40, 17:25 = 1.604 visitas). Los de 20:35 y 23:30 aún no salen. El viral del 29 oct ("5 frases que te hacen perder dinero", 2.166) ya queda fuera de la ventana de 7 días.
- **Nuevo hit**: "3 estafas a vendedores en Vinted 🚩" (5 nov 09:35) → 1.036 visitas en 23 h. Con "si Vinted te manda este aviso, para 🚫" (1.625) son los 2 mejores: **riesgo/aviso concreto con número y emoji 🚩/🚫, a las 09:30**.
- **17:30 se ha caído**: los 3 últimos (favoritos 334, título 295, devolución 297) no pasan de 340. Tienen muchos me gusta (24-34 por 1.000) pero la portada error→solución suave no frena el scroll. La única de 17:30 que funcionó fue "por esto tu precio espanta (y no es que sea caro)" (804): culpa directa + giro.
- **Comentarios casi a cero**: 8 en 33 carruseles y **0 en los 8 últimos (4-5 nov)**. Los que comentan responden a preguntas cerradas con opciones: "¿qué tamaño pones tú?" (2), "¿cuál hacías tú? 1, 2 o 3" (1), "¿alguna vez te han pedido Bizum?" (1). Las preguntas tipo "¿te ha pasado alguna?", "¿lo sabías?", "¿a ti te ha pasado?" dan 0.

| Carrusel (portada real) | Formato | Hora | Diap. | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| si Vinted te manda este aviso, para 🚫 | riesgo concreto | 2 nov 09:35 | 5 | 1.625 | 1 | 0,6 | 5,5 |
| 3 estafas a vendedores en Vinted 🚩 (23 h) | riesgo concreto | 5 nov 09:35 | 5 | 1.036 | 0 | 0 | 5,8 |
| por esto tu precio espanta (y no es que sea caro) | error→solución | 2 nov 17:25 | 5 | 804 | 1 | 1,2 | 11,2 |
| lo que necesitas para revender en serio | lista | 30 oct 09:40 | 5 | 640 | 0 | 0 | 9,4 |
| te escriben pero no te compran 😩 | error→solución | 30 oct 17:30 | 5 | 602 | 0 | 0 | 3,3 |
| nunca hagas esto con una cuenta nueva de Vinted 🚫 | riesgo de cuenta | 1 nov 12:30 | 5 | 584 | 1 | 1,7 | 3,4 |
| por qué te regatean tanto | error→solución | 1 nov 17:35 | 5 | 534 | 0 | 0 | 15,0 |
| zapatillas por menos de 30€ que se venden solas | compra→venta | 30 oct 12:35 | 5 | 478 | 0 | 0 | 16,7 |
| 3 cosas que NO compraría para revender en noviembre | lista negativa | 2 nov 20:35 | 5 | 473 | 1 | 2,1 | 2,1 |
| si este mes subes 1 prenda al día… | reflexión | 1 nov 23:30 | 5 | 443 | 0 | 0 | 0 |
| esto puede costarte la cuenta de Vinted 🚫 | riesgo genérico | 3 nov 09:40 | 5 | 442 | 1 | 2,3 | 4,5 |
| 5 cosas que puedes revender con menos de 50€ | lista | 1 nov 09:40 | 7 | 412 | 0 | 0 | 4,9 |
| nadie te va a aplaudir cuando empieces | motivación | 30 oct 23:30 | 5 | 411 | 0 | 0 | 29,2 |
| ¿quién paga el envío en Vinted? | dinero en Vinted | 2 nov 12:40 | 5 | 383 | 2 | 5,2 | 13,1 |
| ¿cuánto te quita Vinted de cada venta? | dinero en Vinted | 4 nov 09:30 | 5 | 367 | 0 | 0 | 19,1 |
| mitad de semana. ¿cuántas has subido? | reflexión | 4 nov 23:25 | 4 | 365 | 0 | 0 | 5,5 |
| llevas meses diciendo «el lunes empiezo» | reflexión | 2 nov 23:30 | 4 | 335 | 0 | 0 | 3,0 |
| 20 favoritos y nadie compra 😩 | error→solución | 3 nov 17:20 | 5 | 334 | 1 | 3,0 | 24,0 |
| marcas que suben de precio en invierno | lista de marcas | 4 nov 12:35 | 6 | 321 | 0 | 0 | 15,6 |
| 2023 vs 2026 (meme) | antes/ahora | 3 nov 23:35 | 4 | 320 | 0 | 0 | 9,4 |
| lo que más se mueve cuando llega el frío | compra→venta | 3 nov 12:45 | 5 | 311 | 0 | 0 | 12,9 |
| si empezara hoy con 50€, haría esto | plan | 31 oct 20:30 | 6 | 310 | 0 | 0 | 6,5 |
| mi primer pedido a un proveedor salió mal | confesión | 4 nov 20:40 | 5 | 309 | 0 | 0 | 6,5 |
| preguntas que nunca debes hacerle a un proveedor | lista negativa | 31 oct 09:35 | 5 | 303 | 0 | 0 | 9,9 |
| me abrieron una devolución y la gané (así) (15 h) | confesión/solución | 5 nov 17:25 | 5 | 297 | 0 | 0 | 33,7 |
| nadie encuentra tu prenda (y es por el título) | error→solución | 4 nov 17:30 | 5 | 295 | 0 | 0 | 23,7 |
| sábado noche de revendedor (meme) | relatable | 31 oct 23:40 | 4 | 295 | 0 | 0 | 3,4 |
| Pinterest te dice qué vas a vender | truco | 30 oct 20:40 | 5 | 288 | 0 | 0 | 13,9 |
| proveedores de accesorios (parte 3) | serie proveedores | 1 nov 20:35 | 5 | 287 | 0 | 0 | 7,0 |
| qué vender la semana del Black Friday (20 h) | compra→venta | 5 nov 12:40 | 5 | 271 | 0 | 0 | 22,1 |
| proveedores de belleza (parte 4) | serie proveedores | 3 nov 20:30 | 5 | 264 | 0 | 0 | 3,8 |
| la 1ª foto decide si te compran 📸 | error→solución | 31 oct 17:25 | 6 | 256 | 0 | 0 | 0 |
| proveedores de zapatillas (parte 2) | serie proveedores | 31 oct 12:45 | 5 | 245 | 0 | 0 | 12,2 |

- **Mejores 3 (visitas)**: "si Vinted te manda este aviso, para 🚫" (1.625, 1 com.), "3 estafas a vendedores en Vinted 🚩" (1.036, 0), "por esto tu precio espanta" (804, 1). **Por comentarios**: "¿quién paga el envío?" (5,2 por 1.000) y "20 favoritos y nadie compra" (3,0).
- **Peores 3 (visitas, con más de 24 h)**: "proveedores de zapatillas (parte 2)" (245, 0), "la 1ª foto decide si te compran 📸" (256, 0), "proveedores de belleza (parte 4)" (264, 0). (Black Friday, 271, y devolución, 297, tienen menos de 24 h.)
- **Por formato** (media / mediana de visitas): **riesgo de cuenta/estafas 922 / 810 (4; los 2 concretos 1.625 y 1.036, los 2 genéricos 584 y 442)**, error→solución 446 / 334 (7), listas y compra→venta 401 / 392 (8), dinero en Vinted 375 (2; muchos me gusta), reflexión/memes de noche 362 / 350 (6, muy estables), plan/confesión/truco 302 (3), **serie proveedores 265 (3; la peor, 0 comentarios)**.
- **Por franja** (media / mediana): **09:30 → 689 / 442 (la mejor ahora)**, 17:30 → 446 / 334 (bajando), 12:30 → 370 / 321, 23:30 → 362 / 350, **20:30 → 322 / 299 (la peor 4 días seguidos)**. Ojo: el riesgo de cuenta casi siempre va a las 09:30, así que franja y formato van mezclados.
- **Nº de diapositivas**: casi todo es de 5. 4 diap. (noche) 295-365, 6-7 diap. 256-412. Sin diferencia clara: quedarse en 5.
- **Guía del CTA**: siempre "proveedores" (pack), no se puede comparar.
- **Datos limitados**: 33 carruseles y dos virales mueven las medias. Son pistas, no reglas firmes.

**Reglas (basadas en 33 carruseles)**
1. **Repite más el riesgo/aviso CONCRETO con número + 🚩/🚫 a las 09:30** ("3 estafas a vendedores en Vinted 🚩", "si Vinted te manda este aviso, para 🚫"). Nombra la estafa, el aviso o el mensaje exacto. Evita la amenaza genérica ("esto puede costarte la cuenta", 442).
2. **A las 17:30, error→solución solo con culpa directa y giro** ("por esto tu precio espanta (y no es que sea caro)", 804). Evita portadas suaves o de consejo ("nadie encuentra tu prenda", "la 1ª foto decide", "me abrieron una devolución y la gané"): gustan pero no frenan (≤340).
3. **Cierre con pregunta cerrada de opciones** ("¿cuál hacías tú? 1, 2 o 3", "¿qué tamaño pones tú? S, M o L", "¿te han pedido Bizum? sí o no"). Evita "¿te ha pasado alguna?", "¿lo sabías?", "¿a ti te ha pasado?": 0 comentarios en los 8 últimos.
4. **20:30 sigue siendo la peor franja y la serie proveedores la peor**: no programes la parte 7 después de las ya programadas (5 y 6). A las 20:30 mejor una lista negativa ("3 cosas que NO compraría…", 473, la mejor de esa hora).
5. **Noche (23:30): reflexión/meme de 4 diap. es estable (~350)**; mantener, sin gastar ahí ganchos fuertes. No repetir en 7 días un tema ya publicado/programado (estafas: 5 nov; avisos: 2 nov; favoritos: 3 nov). Siguen fuera Navidad y "primera venta/primer mes".

**Temas/ganchos a priorizar los próximos días** (no están en lo ya programado hasta el 8 nov)
1. "si Vinted te oculta un artículo, haz esto 🚫" (aviso concreto, molde del de 1.625; 09:30).
2. "3 mensajes de «Vinted» que son falsos 🚩" (estafas por correo/WhatsApp, molde del de 1.036; 09:30, a partir del 12 nov).
3. "4 frases que te hacen perder ventas en Vinted 💸" (lista negativa de frases, molde del viral de 2.166; 17:30).
4. "por esto te regatean (y no es tu precio) 💸" (culpa directa + giro, molde del de 804; 17:30). Cierre: "¿cuánto te suelen ofrecer? ¿la mitad, un 30% o un 10%?".
5. "las marcas que menos se venden en Vinted (y cuáles sí)" (12:30, cierre "¿cuál vendes tú? 1, 2 o 3").
