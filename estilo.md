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
**Actualizado: 22 oct 2026** (Metricool, 15-22 oct, solo carruseles PHOTO con más de 12 h, emparejados con historial.json por caption y hora; hora de Madrid). 29 carruseles medibles: 16.257 visitas, 105 me gusta (6,5 por 1.000), 13 comentarios (0,8 por 1.000).
- 🚨 **Caída de alcance de TODA la cuenta desde el 20 oct.** Hasta el 19 oct: 21 carruseles, 681 de media. Del 20 oct 17:45 al 21 oct 15:00: 8 carruseles, **245 de media**, y los 2 últimos (descripción 34, sudadera 29) casi no se han enseñado. Han caído también los formatos que mejor iban (error→solución 467, riesgo de cuenta 285-296, comparación 267), así que **no es el tema, es la cuenta**.
- Lo que coincide con la caída: 1) 34 h sin publicar (19 oct 09:30 → 20 oct 17:45) por el límite de Metricool; 2) luego **4 carruseles en 4,5 h** (17:45, 19:10, 20:40, 22:15 del 20 oct); 3) Metricool sigue marcando en ERROR "You have reached your Metricool account limit" los programados del 19-22 oct 00:19, aunque 8 sí aparecen en TikTok. No aparecen publicados "si empezara otra vez", "¿comprar por kilo o por unidad?", "¿cuenta nueva? no hagas esto" ni "nadie ve lo que hay detrás de cada venta". Los de hoy 22 oct siguen en PENDING.
- **Lo bueno**: con menos alcance, los comentarios por 1.000 subieron (España o China 7,5; chat 3,5; avanzar 3,3). Las preguntas sobre su caso ("¿tú a quién le compras?", "¿te han mandado un aviso?") siguen siendo las que más hacen comentar.
- **Hasta el 19 oct** (antes de la caída) se mantiene lo de ayer: error→solución 855 de media (3), comparación 872 (1), reflexión 825 (3), truco 811 (2), Black Friday 813 (1), dinero de 1 cosa 793 (4); Navidad 272 (2), dinero vago 277, primera venta/primer mes 357-405, precio repetido 422. Franjas: 17:30 → 859, 20:30 → 793, 09:30 → 708, 00:00 → 603, 12:30 → 435. Diapositivas: 5 → 718 (9), 6 → 653 (12).

| Carrusel (gancho) | Formato | Diap. | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| 3 fallos en el título que hacen que no te vean | error→solución | 5 | 15 oct 17:30 | 902 | 0 | 0 | 5,5 |
| Vinted o Wallapop: ¿dónde vendes más? | comparación | 5 | 17 oct 17:30 | 872 | 0 | 0 | 4,6 |
| ¿cuánto te queda de verdad de cada venta? | dinero de 1 venta | 6 | 18 oct 09:30 | 853 | 1 | 1,2 | 5,9 |
| la diferencia entre el que vende y el que no | reflexión | 5 | 19 oct 00:00 | 843 | 1 | 1,2 | 7,1 |
| 3 fallos por los que no te compran | error→solución | 5 | 18 oct 17:30 | 832 | 2 | 2,4 | 7,2 |
| por qué tus favoritos no te compran | error→solución | 5 | 16 oct 17:30 | 830 | 1 | 1,2 | 8,4 |
| ¿a qué hora vendes más en Vinted? | truco | 5 | 15 oct 09:30 | 827 | 0 | 0 | 14,5 |
| ¿cuánto tiempo le dedicas a revender? | reflexión | 6 | 17 oct 20:30 | 825 | 1 | 1,2 | 7,3 |
| 3 cosas que se agotan antes de Black Friday | lista + temporada | 5 | 17 oct 09:30 | 813 | 1 | 1,2 | 3,7 |
| nadie empieza sabiendo, bro | reflexión | 6 | 16 oct 00:00 | 808 | 0 | 0 | 3,7 |
| ¿vendes más con lotes? | truco | 6 | 16 oct 20:30 | 795 | 0 | 0 | 2,5 |
| ¿cuánto vale tu ropa de esquí en Vinted? | dinero de 1 cosa | 6 | 18 oct 20:30 | 778 | 0 | 0 | 7,7 |
| ¿cuánto ganas si vendes 3 cosas a la semana? | cálculo de N ventas | 6 | 19 oct 09:30 | 775 | 0 | 0 | 0 |
| ¿cuánto ganas revendiendo zapas? | dinero de 1 cosa | 6 | 15 oct 20:30 | 773 | 0 | 0 | 1,3 |
| ¿cuánto puedes ganar con tus primeros 100€? | dinero de 1 cosa | 6 | 15 oct 12:30 | 767 | 0 | 0 | 6,5 |
| tus fotos espantan a los compradores 🆕 | error→solución | 5 | 20 oct 19:10 | 467 | 0 | 0 | 4,3 |
| ¿tu precio asusta a los compradores? | dinero (repetido) | 6 | 17 oct 12:30 | 422 | 0 | 0 | 19,0 |
| lo que nadie te cuenta del primer mes | primer mes | 6 | 17 oct 00:00 | 405 | 1 | 2,5 | 9,9 |
| ¿y si tu primera venta llega esta semana? | primera venta | 6 | 18 oct 00:00 | 357 | 1 | 2,8 | 19,6 |
| vender poco también es avanzar, bro 🆕 | reflexión | 6 | 21 oct 00:05 | 307 | 1 | 3,3 | 3,3 |
| por qué Vinted te oculta las prendas 🆕 | riesgo de cuenta | 5 | 20 oct 20:40 | 296 | 0 | 0 | 3,4 |
| nunca escribas esto en el chat 🆕 | riesgo de cuenta | 6 | 20 oct 22:15 | 285 | 1 | 3,5 | 17,5 |
| ¿cuánto vale tu armario en Vinted? | dinero vago | 6 | 16 oct 12:30 | 277 | 0 | 0 | 0 |
| ¿cuánto vale una camiseta de fútbol? 🆕 | dinero de 1 cosa | 5 | 21 oct 09:35 | 275 | 0 | 0 | 0 |
| 3 regalos de Navidad que se venden en Vinted | lista + Navidad | 5 | 18 oct 12:30 | 273 | 0 | 0 | 7,3 |
| 3 cosas que vas a vender en Navidad | lista + Navidad | 5 | 16 oct 09:30 | 270 | 0 | 0 | 7,4 |
| ¿proveedor de España o de China? 🆕 | comparación | 6 | 20 oct 17:45 | 267 | 2 | 7,5 | 7,5 |
| tu descripción te está quitando ventas 🆕 | error→solución | 6 | 21 oct 12:50 | 34 | 0 | 0 | 0 |
| ¿a cuánto vendes una sudadera de marca? 🆕 | dinero de 1 cosa | 6 | 21 oct 15:00 | 29 | 0 | 0 | 0 |

- **Mejores 3**: "3 fallos en el título que hacen que no te vean" (902 visitas, 0 com.), "Vinted o Wallapop: ¿dónde vendes más?" (872, 0), "¿cuánto te queda de verdad de cada venta?" (853, 1).
- **Peores 3**: "¿a cuánto vendes una sudadera de marca?" (29, 0), "tu descripción te está quitando ventas" (34, 0), "¿proveedor de España o de China?" (267, 2 — pero el que más comenta: 7,5 por 1.000).
- **Guía del CTA**: todos llevan el CTA de "proveedores"; no hay datos para comparar guías.
- **Datos limitados**: los 8 carruseles del 20-21 oct salieron en mal momento para la cuenta; sus visitas dicen poco del tema. No hay datos de "kilo o unidad", "cuenta nueva" ni "nadie ve" porque no se publicaron.

**Reglas (basadas en 29 carruseles)**
1. **Máximo 1 carrusel cada 3 horas y como mucho 5 al día.** Nunca recuperar de golpe lo que no salió (el 20 oct se subieron 4 en 4,5 h y la cuenta cayó a 245 de media). Si se pierde una franja, se salta; no se amontona.
2. **Antes de programar, comprobar que Metricool publica** (getScheduledPosts: si el anterior está en ERROR por límite de cuenta, no programar más y avisar a Aritz para subir a mano).
3. **Mientras se recupera la cuenta, solo los formatos probados**: error→solución (855) y comparación (872) a las 17:30, truco o dinero de 1 cosa a las 09:30/20:30, reflexión a las 00:00. Nada nuevo ni experimental.
4. **Siguen prohibidos** Navidad, "primera venta/primer mes", "tu armario" y repetir el tema de precios (270-422 incluso con la cuenta bien).
5. **5 diapositivas por defecto** (718 frente a 653) y última pregunta sobre su caso ("¿tú a quién le compras?", "¿te ha pasado?"): con menos alcance es lo único que ha subido (hasta 7,5 com./1.000).

**Temas/ganchos a priorizar los próximos días** (los 3 primeros no llegaron a publicarse o salieron en plena caída: repetirlos cuando la cuenta vuelva a 600+)
1. "¿comprar por kilo o por unidad? 🤔" (comparación, 17:30; no se publicó el 21 oct).
2. "3 fallos en el título que hacen que no te vean" → versión nueva: "3 fallos en tus fotos que espantan" (error→solución, el récord de la ventana con 902; la de fotos salió el 20 oct en la caída).
3. "¿cuenta nueva? no hagas esto 🚫" (riesgo de cuenta; no se publicó el 21 oct).
4. "si empezara otra vez, no haría esto" (reflexión 00:00; no se publicó el 20 oct).
5. "¿a qué hora publicas tú en Vinted?" → nuevo truco tipo "¿a qué hora vendes más?" (827, el que más me gusta tuvo: 14,5 por 1.000).
