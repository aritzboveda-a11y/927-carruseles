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
**Actualizado: 4 nov 2026** (Metricool, 28 oct-4 nov, solo carruseles PHOTO con más de 12 h; hora de Metricool en UTC pasada a Madrid; emparejados por hora + caption con los guion.json de `salida/`, la portada real es la 1ª diapositiva del guion). **26 carruseles medibles: 13.242 visitas, 113 me gusta (8,5 por 1.000), 10 comentarios (0,8 por 1.000).**
- ✅ Metricool vuelve a actualizarse (ayer estaba parado desde el 1 nov). Pero del 3 nov solo salen 2 de 5 (09:40 y 12:45 = 570 visitas): los de 17:20, 20:30 y 23:35 todavía no aparecen. Se analizan mañana.
- **2º viral**: "si Vinted te manda este aviso, para 🚫" (2 nov 09:35) → 1.524 visitas. Junto con "5 frases que te hacen perder dinero" (2.113) son los únicos que pasan de 650. Los dos son **aviso/negativo sobre algo que el lector YA está haciendo o recibiendo** (frases que dice, avisos que le llegan), con un "para"/"perder" en la portada. El resto se queda en 250-640.
- **Comentarios siguen muy bajos** (10 en 26). 6 de los 10 salen a las 12:30 con pregunta cerrada sobre su situación: "¿cuál vendes tú?" (3), "¿qué tamaño pones tú?" (2), "¿tu cuenta tiene menos de un mes?" (1).
- **Ojo**: el 3 nov "esto puede costarte la cuenta de Vinted 🚫" se quedó en 310 → el tema riesgo solo funciona si la portada nombra algo concreto que le llega ("este aviso"), no una amenaza genérica.

| Carrusel (portada real) | Formato | Hora | Diap. | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| 5 frases que te hacen perder dinero en Vinted | lista negativa (frases) | 29 oct 17:20 | 6 | 2.113 | 0 | 0 | 7,1 |
| si Vinted te manda este aviso, para 🚫 | riesgo de cuenta | 2 nov 09:35 | 5 | 1.524 | 1 | 0,7 | 5,9 |
| por esto tu precio espanta | error→solución | 2 nov 17:25 | 5 | 639 | 1 | 1,6 | 12,5 |
| lo que necesitas para revender en serio | lista "lo que necesitas" | 30 oct 09:40 | 5 | 639 | 0 | 0 | 9,4 |
| te escriben pero no te compran 😩 | error→solución | 30 oct 17:30 | 5 | 602 | 0 | 0 | 3,3 |
| nunca hagas esto con una cuenta nueva de Vinted 🚫 | riesgo de cuenta | 1 nov 12:30 | 5 | 567 | 1 | 1,8 | 3,5 |
| 2022 vs 2026 (meme) | antes/ahora | 29 oct 23:35 | 4 | 557 | 0 | 0 | 10,8 |
| por qué te regatean tanto | error→solución | 1 nov 17:35 | 5 | 532 | 0 | 0 | 15,0 |
| zapatillas por menos de 30€ que se venden solas | compra→venta | 30 oct 12:35 | 5 | 474 | 0 | 0 | 16,9 |
| si este mes subes 1 prenda al día… | reflexión | 1 nov 23:30 | 5 | 429 | 0 | 0 | 0 |
| 5 cosas que puedes revender con menos de 50€ | lista | 1 nov 09:40 | 7 | 409 | 0 | 0 | 4,9 |
| nadie te va a aplaudir cuando empieces | motivación | 30 oct 23:30 | 5 | 405 | 0 | 0 | 29,6 |
| 3 cosas que NO compraría para revender en noviembre | lista negativa | 2 nov 20:35 | 5 | 393 | 1 | 2,5 | 2,5 |
| las marcas que más rápido se venden en Vinted | lista de marcas | 29 oct 12:45 | 6 | 391 | 3 | 7,7 | 17,9 |
| ¿quién paga el envío en Vinted? | dinero en Vinted | 2 nov 12:40 | 5 | 373 | 2 | 5,4 | 13,4 |
| proveedores de perfumes (parte 1) | serie proveedores | 29 oct 20:30 | 5 | 352 | 0 | 0 | 5,7 |
| esto puede costarte la cuenta de Vinted 🚫 | riesgo de cuenta | 3 nov 09:40 | 5 | 310 | 1 | 3,2 | 3,2 |
| llevas meses diciendo «el lunes empiezo» | reflexión | 2 nov 23:30 | 4 | 308 | 0 | 0 | 3,2 |
| si empezara hoy con 50€, haría esto | plan | 31 oct 20:30 | 6 | 304 | 0 | 0 | 6,6 |
| preguntas que nunca debes hacerle a un proveedor | lista negativa (proveedor) | 31 oct 09:35 | 5 | 301 | 0 | 0 | 10,0 |
| sábado noche de revendedor (meme) | relatable | 31 oct 23:40 | 4 | 292 | 0 | 0 | 3,4 |
| Pinterest te dice qué vas a vender | truco | 30 oct 20:40 | 5 | 288 | 0 | 0 | 13,9 |
| proveedores de accesorios (parte 3) | serie proveedores | 1 nov 20:35 | 5 | 281 | 0 | 0 | 7,1 |
| lo que más se mueve cuando llega el frío | compra→venta | 3 nov 12:45 | 5 | 260 | 0 | 0 | 11,5 |
| la 1ª foto decide si te compran 📸 | error→solución | 31 oct 17:25 | 6 | 255 | 0 | 0 | 0 |
| proveedores de zapatillas (parte 2) | serie proveedores | 31 oct 12:45 | 5 | 244 | 0 | 0 | 12,3 |

- **Mejores 3 (visitas)**: "5 frases que te hacen perder dinero en Vinted" (2.113, 0 com.), "si Vinted te manda este aviso, para 🚫" (1.524, 1), "por esto tu precio espanta" (639, 1). **Por comentarios**: "las marcas que más rápido se venden" (7,7 por 1.000) y "¿quién paga el envío?" (5,4). **Por me gusta**: "nadie te va a aplaudir cuando empieces" (29,6 por 1.000).
- **Peores 3 (visitas)**: "proveedores de zapatillas (parte 2)" (244, 0), "la 1ª foto decide si te compran 📸" (255, 0; 0 me gusta), "lo que más se mueve cuando llega el frío" (260, 0).
- **Por formato** (media de visitas): riesgo de cuenta 800 (3; mediana 567), error→solución 507 (4; muy estable 532-639 menos "la 1ª foto"), compra→venta 367 (2; bajando 474 → 260), reflexión/motivación 381 (3), **serie proveedores 292 (3; la peor, 0 comentarios)**, listas variadas 300-640.
- **Por franja**: 17:30 → 828 (5; mediana 602, la mejor), 09:30 → 637 (5; mediana 409), 23:30 → 398 (5), 12:30 → 385 (6; la que más comenta: 6 de 10), **20:30 → 324 (5; la peor otra vez)**.
- **Nº de diapositivas**: 5 diap. es lo normal (18; mediana 399). 6 diap. 766 de media pero 348 de mediana (el viral la sube), 4 diap. 386, 7 diap. 409 (1). Sin diferencia clara: quedarse en 5-6.
- **Guía del CTA**: siempre "proveedores", no se puede comparar.
- **Datos limitados**: 26 carruseles, 1-6 por grupo, dos virales mueven las medias. Son pistas, no reglas firmes.

**Reglas (basadas en 26 carruseles)**
1. **Repite la portada "aviso/pérdida sobre algo que ya le pasa"**: "si Vinted te manda este aviso, para 🚫", "N frases que te hacen perder dinero 💸". Tiene que nombrar algo concreto que el lector reconoce (un mensaje, una frase, un aviso). Las amenazas genéricas ("esto puede costarte la cuenta", 310) y los consejos suaves ("la 1ª foto decide…", 255) no funcionan.
2. **Pon los mejores ganchos a las 17:30 y 09:30**; a las 20:30 nada fuerte (peor franja 2 días seguidos).
3. **A las 12:30, temas de dinero/marcas con pregunta cerrada al final** ("¿cuál vendes tú?", "¿qué tamaño pones tú?", "¿te ha llegado alguno?"): es donde salen los comentarios. Nada de "¿cómo es la tuya?", "¿dónde estás ahora?", "¿cuántas tienes?" (0 comentarios).
4. **Error→solución con "por esto tu X espanta / no te compran" a las 17:30**: es el formato más estable (530-640). Mantener 5 diapositivas.
5. **Para la serie proveedores (parte N) después de las partes ya programadas** y evita repetir memes ("20XX vs 2026", "sábado/viernes noche") y "compra→venta por temporada" (bajó a 260). Siguen prohibidos Navidad y "primera venta/primer mes".

**Temas/ganchos a priorizar los próximos días**
1. "si un comprador te escribe esto en Vinted, para 🚩" (riesgo concreto, mismo molde que el de 1.524; 09:30).
2. "4 frases que te hacen perder ventas en Vinted 💸" (lista negativa de frases, parte 2 del viral; 17:30).
3. "por esto tu descripción espanta a los compradores" (error→solución; 17:30).
4. "¿quién paga la devolución en Vinted?" con cierre "¿te ha pasado alguna vez?" (dinero; 12:30, para comentarios).
5. "si Vinted te oculta un artículo, haz esto 🚫" (riesgo concreto; 09:30).
