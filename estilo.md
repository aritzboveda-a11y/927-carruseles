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
**Actualizado: 23 oct 2026** (Metricool, 16-23 oct, solo carruseles PHOTO con más de 12 h, emparejados con historial.json por caption y hora; hora de Madrid). 30 carruseles medibles: 12.677 visitas, 85 me gusta (6,7 por 1.000), 14 comentarios (1,1 por 1.000).
- 🚨 **La caída de alcance ha ido a peor.** Hasta el 19 oct: 16 carruseles, **641 de media**. 20 oct: 5 carruseles, 341 de media. 21 oct: **7 carruseles** en un día (09:35 → 22:45), y desde las 12:50 ninguno pasa de 80. 22 oct: 3 carruseles con **19, 34 y 41** visitas. Ayer (22 oct) la cuenta sumó solo **94 visitas** en sus publicaciones del día.
- Ha caído TODO por igual: comparación (873 → 66), error→solución (835 → 71), reflexión (846 → 41), dinero de 1 cosa (858 → 19). **No es el tema ni el formato: TikTok está enseñando muy poco la cuenta.**
- Lo que coincide con la caída: 1) desde el 20 oct se publica en ráfagas y a horas que se mueven (el 21 oct salieron 7, más que el máximo de 5 de la regla de ayer); 2) Metricool sigue con "You have reached your Metricool account limit": los del 22 oct 17:52, 20:52 y 23 oct 00:22 están en ERROR y **no se han publicado**; el del bolso (12:44) también sale en ERROR pero sí salió. Los "programados 19 oct" que ayer parecían perdidos (kilo o unidad, cuenta nueva, si empezara otra vez, nadie ve) sí salieron el 21 oct por la tarde/noche, todos amontonados.
- **Lo único que se mantiene**: las preguntas sobre su caso siguen sacando comentarios cuando hay algo de alcance (España o China 7,4 por 1.000; chat 3,3; camiseta 3,3; avanzar 3,2). "kilo o unidad" tuvo 45 me gusta por 1.000 (3 de 66): el tema gusta, salió sin alcance.
- **Antes de la caída (16-19 oct)**: comparación 873 (1), dinero de 1 venta 858 (1), reflexión 838 (2), error→solución 834 (2), Black Friday 814, truco 797, dinero de 1 cosa 779; Navidad 270-274, dinero vago 278, primera venta/primer mes 360-405, precio repetido 424. Franjas: 17:30 → 847, 20:30 → 802, 09:30 → 680, 00:00 → 537, 12:30 → 325.

| Carrusel (gancho) | Formato | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|
| Vinted o Wallapop: ¿dónde vendes más? | comparación | 17 oct 17:30 | 873 | 0 | 0 | 4,6 |
| ¿cuánto te queda de verdad de cada venta? | dinero de 1 venta | 18 oct 09:30 | 858 | 1 | 1,2 | 5,8 |
| la diferencia entre el que vende y el que no | reflexión | 19 oct 00:00 | 846 | 1 | 1,2 | 7,1 |
| por qué tus favoritos no te compran | error→solución | 16 oct 17:30 | 835 | 1 | 1,2 | 8,4 |
| 3 fallos por los que no te compran | error→solución | 18 oct 17:30 | 833 | 2 | 2,4 | 7,2 |
| ¿cuánto tiempo le dedicas a revender? | reflexión | 17 oct 20:30 | 829 | 1 | 1,2 | 7,2 |
| 3 cosas que se agotan antes de Black Friday | Black Friday | 17 oct 09:30 | 814 | 1 | 1,2 | 3,7 |
| ¿vendes más con lotes? | truco | 16 oct 20:30 | 797 | 0 | 0 | 2,5 |
| ¿cuánto vale tu ropa de esquí en Vinted? | dinero de 1 cosa | 18 oct 20:30 | 779 | 0 | 0 | 7,7 |
| ¿cuánto ganas si vendes 3 cosas a la semana? | cálculo | 19 oct 09:30 | 777 | 0 | 0 | 0 |
| tus fotos espantan a los compradores | error→solución | 20 oct 19:10 | 522 | 0 | 0 | 3,8 |
| ¿tu precio asusta a los compradores? | precio repetido | 17 oct 12:30 | 424 | 0 | 0 | 18,9 |
| lo que nadie te cuenta del primer mes | primer mes | 17 oct 00:00 | 405 | 1 | 2,5 | 9,9 |
| ¿y si tu primera venta llega esta semana? | primera venta | 18 oct 00:00 | 360 | 1 | 2,8 | 19,4 |
| vender poco también es avanzar, bro | reflexión | 21 oct 00:05 | 314 | 1 | 3,2 | 3,2 |
| nunca escribas esto en el chat | riesgo de cuenta | 20 oct 22:15 | 307 | 1 | 3,3 | 16,3 |
| por qué Vinted te oculta las prendas | riesgo de cuenta | 20 oct 20:40 | 307 | 0 | 0 | 3,3 |
| ¿cuánto vale una camiseta de fútbol? | dinero de 1 cosa | 21 oct 09:35 | 302 | 1 | 3,3 | 0 |
| ¿cuánto vale tu armario en Vinted? | dinero vago | 16 oct 12:30 | 278 | 0 | 0 | 0 |
| 3 regalos de Navidad que se venden en Vinted | Navidad | 18 oct 12:30 | 274 | 0 | 0 | 7,3 |
| 3 cosas que vas a vender en Navidad | Navidad | 16 oct 09:30 | 270 | 0 | 0 | 7,4 |
| ¿proveedor de España o de China? | comparación | 20 oct 17:45 | 269 | 2 | 7,4 | 7,4 |
| ¿a cuánto vendes una sudadera de marca? | dinero de 1 cosa | 21 oct 15:00 | 80 | 0 | 0 | 12,5 |
| tu descripción te está quitando ventas | error→solución | 21 oct 12:50 | 71 | 0 | 0 | 0 |
| ¿comprar por kilo o por unidad? 🆕 | comparación | 21 oct 17:35 | 66 | 0 | 0 | 45,5 |
| si empezara otra vez, no haría esto 🆕 | confesión | 21 oct 22:45 | 52 | 0 | 0 | 19,2 |
| ¿cuenta nueva? no hagas esto 🆕 | riesgo de cuenta | 21 oct 20:50 | 41 | 0 | 0 | 24,4 |
| nadie ve lo que hay detrás de cada venta 🆕 | reflexión | 22 oct 00:20 | 41 | 0 | 0 | 0 |
| ¿borras y vuelves a subir tus prendas? ojo 🆕 | riesgo de cuenta | 22 oct 09:50 | 34 | 0 | 0 | 0 |
| ¿a cuánto vendes un bolso en Vinted? 🆕 | dinero de 1 cosa | 22 oct 12:45 | 19 | 0 | 0 | 0 |

- **Mejores 3**: "Vinted o Wallapop: ¿dónde vendes más?" (873 visitas, 0 com.), "¿cuánto te queda de verdad de cada venta?" (858, 1), "la diferencia entre el que vende y el que no" (846, 1).
- **Peores 3**: "¿a cuánto vendes un bolso en Vinted?" (19, 0), "¿borras y vuelves a subir tus prendas? ojo" (34, 0), "nadie ve lo que hay detrás de cada venta" y "¿cuenta nueva? no hagas esto" (41, 0).
- **Guía del CTA y nº de diapositivas**: todos llevan el CTA de "proveedores" y 5-6 diapositivas; con la cuenta caída no se puede comparar nada de esto.
- **Datos limitados**: los 14 carruseles desde el 20 oct dicen poco de sus temas; solo dicen que la cuenta está frenada.

**Reglas (basadas en 30 carruseles)**
1. **Bajar el ritmo mientras la cuenta esté por debajo de 200 de media: máximo 2 carruseles al día** (17:30 y 20:30, las mejores franjas), separados 3 h o más. Nunca más de 5 al día aunque vuelva a ir bien; el 21 oct salieron 7 y fue el peor día.
2. **No programar nada nuevo en Metricool mientras haya publicaciones en ERROR por "account limit"**: comprobar con getScheduledPosts antes y, si hay ERROR, dejar las imágenes en salida/ y avisar a Aritz para que lo suba a mano desde la app (los programados viejos salen amontonados y a deshora).
3. **Solo formatos probados hasta recuperar 600+**: comparación y error→solución a las 17:30, reflexión o dinero de 1 venta a las 20:30. Nada nuevo.
4. **Siguen prohibidos** Navidad, "primera venta/primer mes", "tu armario", repetir el tema de precios y la franja de las 12:30 (325 de media incluso con la cuenta bien).
5. **Última diapositiva con pregunta sobre su caso** ("¿tú a quién le compras?", "¿te ha pasado?"): es lo único que sigue sacando comentarios con poco alcance.

**Temas/ganchos a priorizar los próximos días** (cuando la cuenta vuelva a 300+, repetir los que salieron sin alcance)
1. "¿comprar por kilo o por unidad? 🤔" con gancho nuevo (comparación, 17:30; 45 me gusta por 1.000 con solo 66 visitas).
2. "¿Vinted, Wallapop o Milanuncios?" (comparación tipo el récord de 873; 17:30).
3. "¿cuánto te queda de verdad de cada venta?" → versión nueva con otro producto (dinero de 1 venta, 858; 20:30).
4. "3 fallos por los que no te compran" → versión "3 fallos en tus fotos" (error→solución, 833-835; 17:30).
5. "la diferencia entre el que vende y el que no" → versión nueva tipo reflexión (846; 20:30, no a las 00:00).
