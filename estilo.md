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
**Actualizado: 15 oct 2026** (Metricool, 8-15 oct, solo carruseles PHOTO emparejados con historial/manifest y con más de 12 h; horas en Madrid). 26 carruseles medibles (8-14 oct): 13.854 visitas, 190 me gusta, 16 comentarios, 13 compartidos. En las últimas 24 h los carruseles sumaron ≈2.600 visitas nuevas (≈1.800 de los 5 que entran hoy por primera vez + 828 de los antiguos, que siguen creciendo).
- **Nuevos desde ayer**: "nadie te dice esto si Vinted te bloquea" (13 oct 12:30, 787 visitas, **3 comentarios**), "si empezara hoy en Vinted, haría esto" (14 oct 00:00, 771, 1 com.), y tres que se hundieron seguidos: "3 cosas que se buscan en Vinted con el frío" (13 oct 17:30, 68), "10 ventas en Vinted: ¿cuánto te queda?" (13 oct 20:30, 93), "¿cuánto ganas vendiendo 1 prenda al día?" (14 oct 09:30, 87). "¿a cuánto vendes unas zapas?" subió de 344 a 857.
- 🚨 Los del manifest de 14 oct 12:30 ("3 cosas que no deberías vender"), 17:30 ("¿cuánto rebajas…?") y 20:30 ("¿cuánto vale un abrigo usado…?") **no aparecen en Metricool**. Comprueba en TikTok Studio si se subieron.
- ℹ️ Fuera del análisis (no se pueden emparejar): posts de fotos con caption solo "#fyp…" (12 oct 17:37, 848; 12 oct 20:35, 805; 9 oct 07:08, 230) y uno sin texto (12 oct 00:49, 962). "¿Sabes cuánto ganas…?" y "Cómo saber si un proveedor es fiable" ya salen de la ventana de 7 días.

| Carrusel (gancho) | Formato | Diap. | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| ¿cuánto se queda Vinted de tu venta? | pregunta dinero | 6 | 11 oct 10:06 | 1.091 | 0 | 0 | 7,3 |
| Nadie te dice esto cuando abres una cuenta nueva | polémica | 6 | 8 oct 03:19 | 992 | 0 | 0 | 14,1 |
| ¿tu ropa lleva semanas sin venderse? | error→solución | 6 | 12 oct 20:30 | 987 | 0 | 0 | 9,1 |
| 3 cosas que se venden solas en invierno | lista + temporada | 5 | 11 oct 12:54 | 953 | 0 | 0 | 10,5 |
| 3 cosas que tienes que vender en Vinted este otoño | lista + temporada | 5 | 8 oct 06:26 | 877 | 1 | 1,1 | 19,4 |
| ¿a cuánto vendes unas zapas en Vinted? | pregunta dinero | 5 | 13 oct 09:30 | 857 | 0 | 0 | 9,3 |
| ¿pones bien el precio en Vinted? | pregunta dinero | 6 | 10 oct 21:11 | 853 | 2 | 2,3 | 11,7 |
| nadie te dice esto si Vinted te bloquea 🆕 | polémica | 5 | 13 oct 12:30 | 787 | 3 | 3,8 | 6,4 |
| por esto Vinted no enseña tu ropa | error→solución | 6 | 10 oct 12:59 | 786 | 0 | 0 | 16,5 |
| si empezara hoy en Vinted, haría esto 🆕 | historia/reto | 6 | 14 oct 00:00 | 771 | 1 | 1,3 | 7,8 |
| 3 cosas que se agotan en Black Friday | lista + temporada | 7 | 9 oct 10:04 | 767 | 1 | 1,3 | 10,4 |
| ¿cometes estos errores al revender? | pregunta errores | 6 | 9 oct 21:04 | 762 | 1 | 1,3 | 7,9 |
| ¿cuánto tardaste en tu primera venta? | reflexión | 6 | 13 oct 00:00 | 533 | 1 | 1,9 | 9,4 |
| así es un día revendiendo en Vinted | historia | 5 | 10 oct 17:34 | 461 | 0 | 0 | 17,4 |
| Si tus fotos no venden, haz esto | error→solución | 7 | 8 oct 09:20 | 441 | 0 | 0 | 22,7 |
| Cuando empecé, aceptaba todas las ofertas | confesión | 6 | 8 oct 12:25 | 323 | 1 | 3,1 | 15,5 |
| nadie te cuenta esto al revender | polémica | 7 | 11 oct 00:11 | 321 | 2 | 6,2 | 18,7 |
| con 50€ yo empezaría así | historia/reto | 6 | 9 oct 12:31 | 313 | 1 | 3,2 | 41,5 |
| nadie te dice esto de tu primera venta | polémica | 5 | 10 oct 09:34 | 265 | 1 | 3,8 | 34,0 |
| ¿tu proveedor te va a estafar? | pregunta nicho | 5 | 9 oct 17:35 | 233 | 0 | 0 | 17,2 |
| ¿Proveedor chino o europeo? | pregunta nicho | 7 | 8 oct 18:08 | 107 | 0 | 0 | 46,7 |
| 10 ventas en Vinted: ¿cuánto te queda? 🆕 | pregunta dinero | 6 | 13 oct 20:30 | 93 | 0 | 0 | 10,8 |
| ¿cuánto ganas vendiendo 1 prenda al día? 🆕 | pregunta dinero | 6 | 14 oct 09:30 | 87 | 0 | 0 | 11,5 |
| 3 cosas que se buscan en Vinted con el frío 🆕 | lista + temporada | 5 | 13 oct 17:30 | 68 | 1 | 14,7 | 29,4 |
| Lo que nadie mira al comprar por kilo | polémica | 6 | 8 oct 21:03 | 68 | 0 | 0 | 44,1 |
| ¿Tus paquetes parecen baratos? | pregunta nicho | 4 | 8 oct 14:57 | 58 | 0 | 0 | 69,0 |

- **Mejores 3**: "¿cuánto se queda Vinted de tu venta?" (1.091 visitas, 0 com.), "Nadie te dice esto cuando abres una cuenta nueva" (992, 0, 5 compartidos), "¿tu ropa lleva semanas sin venderse?" (987, 0).
- **Peores 3**: "¿Tus paquetes parecen baratos?" (58, 0), "3 cosas que se buscan en Vinted con el frío" (68, 1), "Lo que nadie mira al comprar por kilo" (68, 0).
- **Formato (media de visitas)**: error→solución 738 (3), lista + temporada 666 (4; sin el de "frío" serían 866), pregunta de dinero 596 (5; muy partido: 853-1.091 los tres primeros, 87-93 los dos últimos), polémica "nadie te dice…" 487 (5; 787-992 si el tema es la cuenta/bloqueo, 68-321 si no), historia/reto 542, confesión/reflexión 323-533, pregunta de nicho 133.
- 🔎 **El bajón del 13-14 oct no es del formato**: los 3 hundidos usan los formatos que mejor iban, pero **repiten tema de hace 1-3 días** ("frío" ≈ "invierno" del 11 oct; "10 ventas: ¿cuánto te queda?" y "1 prenda al día" ≈ "¿cuánto se queda Vinted…?" / "¿cuánto ganas de verdad…?"). En medio, uno de tema distinto ("si empezara hoy") hizo 771. Hipótesis (pocos datos): TikTok frena lo que se parece demasiado a lo reciente. Además, muchos ganchos seguidos empiezan por "¿cuánto…?".
- **Tema**: lo amplio de Vinted (cuenta nueva, bloqueo, precio, ropa que no se vende, comisiones) sigue arriba; proveedores, packaging, kilo y chino/europeo, abajo.
- **Diapositivas**: 6 → 589 de media (13), 5 → 563 (8), 7 → 409 (4), 4 → 58 (1).
- **Hora**: 00:00-07:00 699 (5), 07:00-12:00 585 (6), 12:00-17:00 537 (6), 17:00-24:00 404 (9). La franja de 00:00 sigue siendo la más fiable (771 y 533 esta semana); la hora pesa menos que el tema.
- **Guía del CTA**: no marca diferencia (casi todos "pack"/"proveedores").
- **Comentarios**: 1,2 por 1.000 visitas (sube un poco). El que más ha sacado es el del bloqueo (3) con una pregunta de **experiencia propia** en el caption ("¿a ti te ha pasado alguna vez?"); las preguntas de número/opinión ("¿cuántos días…?", "¿abrigo o botas?") sacan 0-1.

**Reglas (basadas en 26 carruseles)**
1. **No repitas tema ni gancho parecido en 4 días**: antes de publicar, si el tema o la primera palabra del gancho se parece a uno de los últimos 8 carruseles (p. ej. otro "¿cuánto ganas/te queda…?" o otro "3 cosas… frío/invierno"), cámbialo por otro tema amplio de la lista. Máximo 1 gancho que empiece por "¿cuánto…?" al día.
2. **Repite** error→solución y polémica sobre la cuenta de Vinted (cuenta nueva, bloqueo, "no enseña tu ropa", "no se vende"): 787-992 visitas. Y lista + temporada, pero cada vez con una fecha distinta (Black Friday, Navidad, regalos), no otra vez "frío/invierno".
3. **Evita** temas solo de proveedores, packaging, ropa por kilo o chino vs europeo, y 4 o 7 diapositivas: usa 5 o 6.
4. **Para comentarios**: termina el caption y la penúltima diapositiva con una pregunta de experiencia ("¿a ti te ha pasado?", "¿cuál te ha pasado a ti?") en vez de pedir un número.
5. **Comprueba que se publica**: si un carrusel de la tanda no aparece en Metricool al día siguiente (como 14 oct 12:30, 17:30, 20:30), avisa a Aritz.

**Temas/ganchos a priorizar los próximos días** (de la tanda manual del 15-19 oct, reordenados; ojo: la tanda tiene 9 ganchos con "¿cuánto…?", espaciarlos o cambiar algunos)
1. "por qué tus favoritos no te compran 👀" (16 oct 17:30; error→solución de cuenta, el formato top).
2. "3 fallos en el título que hacen que no te vean" (15 oct 17:30; error→solución, tipo "Vinted no enseña tu ropa").
3. "3 cosas que vas a vender en Navidad 🎄" / "3 cosas que se agotan antes de Black Friday 🛍️" (lista + temporada con fecha nueva; no juntarlas el mismo día).
4. "¿tu precio asusta a los compradores? 💸" (17 oct 12:30; parecido a "¿pones bien el precio?", 853).
5. "¿cuánto vale tu armario en Vinted? 💸" (16 oct 12:30; tema amplio, pero que sea el único "¿cuánto…?" de ese día).
