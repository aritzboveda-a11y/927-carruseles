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
**Actualizado: 31 oct 2026** (Metricool, 24-31 oct, solo carruseles PHOTO con más de 12 h; Metricool da la hora en UTC, aquí pasada a Madrid; emparejados por caption con los guion.json de `salida/`). 20 carruseles medibles: 7.936 visitas, 76 me gusta (9,6 por 1.000), 12 comentarios (1,5 por 1.000).
- **Ayer (30 oct) la cuenta sumó ~3.600 visitas** (diferencia con el análisis de ayer): ~1.170 de los 4 carruseles del 30 oct, +1.564 de "5 frases que te hacen perder dinero" (223 → 1.787, el primer carrusel que despega), +531 del meme "2022 vs 2026", +239 de perfumes parte 1 (96 → 335), +93 de "marcas que más rápido se venden" y ~30 de los antiguos.
- **Plantilla pinterest va mejor que la de Aritz en alcance**: 525 visitas de media (8 carruseles; 345 sin el de 1.787) frente a 312 (12). Pero comenta menos: 0,7 com/1.000 frente a 2,4. Seguir con pinterest y meter la pregunta del caso en la diapositiva final, no solo en el caption.
- 🚨 **Siguen sin aparecer en Metricool**: "esto hace que Vinted te limite la cuenta 🚫" (salida/2026-10-29_0930) y los del 27-28 oct. Comprobar en TikTok Studio.
- 🚨 **historial.json sigue sin coincidir con lo publicado (29-31 oct)**: p. ej. el historial dice "por esto no te ponen 5 estrellas" el 29 oct 17:22, pero lo publicado fue "5 frases que te hacen perder dinero" (salida/2026-10-29_1720); el 30 oct 20:45 dice "3 errores que te hacen perder dinero" y salió "Pinterest te dice qué vas a vender" (salida/2026-10-30_2040). Las carpetas reales no son las del historial (_0940, _1235, _2040…). El agente debe apuntar el gancho y la carpeta reales.
- **TikTok tiene 30 programados como límite**: el 8 nov ya hay carruseles que no entraron. No programar más de ~6 días por delante.

| Carrusel (gancho) | Formato | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|
| 5 frases que te hacen perder dinero en Vinted | lista negativa | 29 oct 17:20 | 1.787 | 0 | 0 | 7,8 |
| 2022 vs 2026 (meme, 4 diap.) | relatable | 29 oct 23:35 | 531 | 0 | 0 | 11,3 |
| lo que necesitas para revender en serio | lista | 30 oct 09:40 | 520 | 0 | 0 | 11,5 |
| errores de envío que salen caros | riesgo de cuenta | 26 oct 09:45 | 416 | 0 | 0 | 2,4 |
| zapatillas que compras por menos de 30€ y se venden solas | lista (precios) | 30 oct 12:35 | 380 | 0 | 0 | 21,1 |
| las marcas que más rápido se venden en Vinted | lista | 29 oct 12:45 | 373 | 3 | 8,0 | 18,8 |
| proveedores de perfumes que tienes que conocer (parte 1) | serie proveedores | 29 oct 20:30 | 335 | 0 | 0 | 6,0 |
| antes de subir la ropa, mira esto | error→solución | 24 oct 17:50 | 334 | 0 | 0 | 9,0 |
| muchas visitas y 0 favoritos | error→solución | 25 oct 17:50 | 328 | 1 | 3,0 | 9,1 |
| ¿subes fotos sacadas de internet? ojo | riesgo de cuenta | 25 oct 12:45 | 328 | 2 | 6,1 | 15,2 |
| Black Friday: ¿subes o bajas precios? | temporada | 26 oct 12:35 | 313 | 1 | 3,2 | 0 |
| lo que haces el domingo decide tu semana | reflexión | 25 oct 00:15 | 303 | 1 | 3,3 | 9,9 |
| una gorra de marca: ¿a cuánto la vendes? | dinero de 1 cosa | 25 oct 09:45 | 297 | 0 | 0 | 10,1 |
| nueva semana: haz esto antes del martes | reflexión | 26 oct 00:15 | 292 | 0 | 0 | 10,3 |
| ¿te piden pagar fuera de Vinted? | riesgo de cuenta | 24 oct 12:50 | 288 | 1 | 3,5 | 10,4 |
| ¿Vinted o tu propia tienda online? | comparación | 24 oct 20:50 | 287 | 0 | 0 | 3,5 |
| ¿proveedor o tiendas de segunda mano? | comparación | 25 oct 20:45 | 279 | 0 | 0 | 7,2 |
| 3 trucos para que tu prenda salga más | lista | 24 oct 09:40 | 274 | 3 | 10,9 | 14,6 |
| te escriben pero no te compran 😩 | error→solución | 30 oct 17:30 | 243 | 0 | 0 | 8,2 |
| Pinterest te dice qué vas a vender el mes que viene | truco | 30 oct 20:40 | 28 | 0 | 0 | 0 (solo 12 h) |

- **Mejores 3 (visitas)**: "5 frases que te hacen perder dinero en Vinted" (1.787, 0 com.), "2022 vs 2026" (531, 0), "lo que necesitas para revender en serio" (520, 0). **Por comentarios**: "las marcas que más rápido se venden" (373, 3 com.) y "3 trucos para que tu prenda salga más" (274, 3).
- **Peores 3 (visitas)**: "Pinterest te dice qué vas a vender" (28, 0; solo 12 h, mirar mañana), "te escriben pero no te compran 😩" (243, 0), "3 trucos para que tu prenda salga más" (274, pero 3 com.).
- **Por formato**: lista 560 de media (6; sin el de 1.787 y el de 12 h, 387; 1,8 com/1.000 y 11,6 MG/1.000), relatable/meme 531 (1), riesgo de cuenta 344 (3; 2,9 com/1.000), serie proveedores 335 (1), error→solución 302 (3), reflexión 298 (2), comparación 283 (2; 0 com.), dinero de 1 cosa 297 (1).
- **Por franja**: 17:30 → 673 (4; 291 sin el de 1.787), 23:30 → 531 (1), 09:30 → 377 (4), 12:30 → 336 (5; la que más comenta, 4,2 com/1.000), 00:00 → 298 (2), 20:30 → 232 (4; la peor por segundo día).
- **Nº de diapositivas y guía del CTA**: sin diferencias claras (casi todos 5-6 diapositivas y el CTA "proveedores"); el meme de 4 diapositivas fue el 2º con más visitas.
- **Datos limitados**: 1-6 carruseles por grupo y un solo carrusel viral (1.787) mueve todas las medias. Son pistas, no reglas firmes.

**Reglas (basadas en 20 carruseles)**
1. **Repite el formato "N frases/errores que te hacen perder dinero"** (lista negativa con 💸): es el único que ha despegado (1.787). Hacer variantes: frases, fotos, precios, envíos… 1 al día, a las 17:30.
2. **Repite los memes "antes/ahora" y "sábado/viernes noche"** de 4 diapositivas a las 23:30: 531 visitas, más que cualquier reflexión (298).
3. **Listas de marcas/productos con precios de ejemplo a las 12:30** ("marcas que más rápido se venden", "zapatillas por menos de 30€"): las que más gustan (19-21 MG/1.000) y comentan. Termina con "¿cuál vendes tú?".
4. **Evita comparaciones ("¿X o Y?") y "¿a cuánto vendes X?"**: 0 comentarios y <300 visitas otra vez. Siguen prohibidos Navidad y "primera venta/primer mes".
5. **20:30 es la peor franja** (232 de media): poner ahí lo menos importante o mover la serie proveedores a 09:30/12:30. Perfumes parte 1 subió a 335, así que la serie puede seguir.

**Temas/ganchos a priorizar los próximos días**
1. "5 fotos que te hacen perder ventas en Vinted 📸" (variante del de 1.787; 17:30).
2. "3 precios que te hacen perder dinero en Vinted 💸" (lista negativa; 17:30).
3. "2023 vs 2026 😂" / "viernes noche de revendedor 📦😂" (meme 4 diapositivas; 23:30; ya hay varios programados, mantenerlos).
4. "marcas que suben de precio en invierno en Vinted 🧥" (lista con precios; 12:30).
5. "esto hace que Vinted te limite la cuenta 🚫" (salida/2026-10-29_0930; sigue sin aparecer publicado; 09:30).
