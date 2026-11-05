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
**Actualizado: 5 nov 2026** (Metricool, 29 oct-5 nov, solo carruseles PHOTO con más de 12 h; hora de Metricool en UTC pasada a Madrid; emparejados por hora + caption con historial.json y los guion.json de `salida/`). **30 carruseles medibles: 14.846 visitas, 133 me gusta (9,0 por 1.000), 11 comentarios (0,7 por 1.000), 5 compartidos.**
- ⚠️ Del 4 nov Metricool solo trae 1 de 5 (09:30 "¿cuánto te quita Vinted…?", 190 visitas con 23 h). Los de 12:35 y 17:30 no aparecen todavía; se analizan mañana. El 3 nov ya está completo: 5 carruseles = 1.587 visitas.
- Los dos virales siguen siendo los únicos por encima de 800: "5 frases que te hacen perder dinero en Vinted" (2.166) y "si Vinted te manda este aviso, para 🚫" (1.582). Los dos son **aviso/pérdida sobre algo concreto que el lector ya hace o recibe**. El resto se queda en 190-780.
- El 3 nov no hubo ningún carrusel por encima de 430: "esto puede costarte la cuenta" (430), "20 favoritos y nadie compra 😩" (310), "2023 vs 2026" (288), "lo que más se mueve con el frío" (297), "proveedores de belleza (parte 4)" (262).
- **Me gusta altos pero pocas visitas**: "20 favoritos y nadie compra 😩" (25,8 MG/1.000) y "¿cuánto te quita Vinted…?" (26,3): el tema gusta, la portada no frena el scroll. Hacen falta portadas más concretas/negativas.
- **Comentarios siguen muy bajos** (11 en 30). 6 de 11 salen a las 12:30 con pregunta cerrada: "¿cuál vendes tú?" (3), "¿qué tamaño pones tú?" (2), "¿la tuya tiene menos de un mes?" (1).

| Carrusel (portada real) | Formato | Hora | Diap. | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| 5 frases que te hacen perder dinero en Vinted | lista negativa (frases) | 29 oct 17:20 | 6 | 2.166 | 0 | 0 | 6,9 |
| si Vinted te manda este aviso, para 🚫 | riesgo de cuenta | 2 nov 09:35 | 5 | 1.582 | 1 | 0,6 | 5,7 |
| por esto tu precio espanta | error→solución | 2 nov 17:25 | 5 | 778 | 1 | 1,3 | 11,6 |
| lo que necesitas para revender en serio | lista | 30 oct 09:40 | 5 | 639 | 0 | 0 | 9,4 |
| te escriben pero no te compran 😩 | error→solución | 30 oct 17:30 | 5 | 602 | 0 | 0 | 3,3 |
| nunca hagas esto con una cuenta nueva de Vinted 🚫 | riesgo de cuenta | 1 nov 12:30 | 5 | 582 | 1 | 1,7 | 3,4 |
| 2022 vs 2026 (meme) | antes/ahora | 29 oct 23:35 | 4 | 557 | 0 | 0 | 10,8 |
| por qué te regatean tanto | error→solución | 1 nov 17:35 | 5 | 533 | 0 | 0 | 15,0 |
| zapatillas por menos de 30€ que se venden solas | compra→venta | 30 oct 12:35 | 5 | 476 | 0 | 0 | 16,8 |
| 3 cosas que NO compraría para revender en noviembre | lista negativa | 2 nov 20:35 | 5 | 460 | 1 | 2,2 | 2,2 |
| si este mes subes 1 prenda al día… | reflexión | 1 nov 23:30 | 5 | 439 | 0 | 0 | 0 |
| esto puede costarte la cuenta de Vinted 🚫 | riesgo de cuenta | 3 nov 09:40 | 5 | 430 | 1 | 2,3 | 4,7 |
| 5 cosas que puedes revender con menos de 50€ | lista | 1 nov 09:40 | 7 | 410 | 0 | 0 | 4,9 |
| nadie te va a aplaudir cuando empieces | motivación | 30 oct 23:30 | 5 | 408 | 0 | 0 | 29,4 |
| las marcas que más rápido se venden en Vinted | lista de marcas | 29 oct 12:45 | 6 | 398 | 3 | 7,5 | 17,6 |
| ¿quién paga el envío en Vinted? | dinero en Vinted | 2 nov 12:40 | 5 | 380 | 2 | 5,3 | 13,2 |
| proveedores de perfumes (parte 1) | serie proveedores | 29 oct 20:30 | 5 | 352 | 0 | 0 | 5,7 |
| llevas meses diciendo «el lunes empiezo» | reflexión | 2 nov 23:30 | 4 | 330 | 0 | 0 | 3,0 |
| 20 favoritos y nadie compra 😩 | error→solución | 3 nov 17:20 | 5 | 310 | 1 | 3,2 | 25,8 |
| si empezara hoy con 50€, haría esto | plan | 31 oct 20:30 | 6 | 309 | 0 | 0 | 6,5 |
| preguntas que nunca debes hacerle a un proveedor | lista negativa (proveedor) | 31 oct 09:35 | 5 | 302 | 0 | 0 | 9,9 |
| lo que más se mueve cuando llega el frío | compra→venta | 3 nov 12:45 | 5 | 297 | 0 | 0 | 13,5 |
| sábado noche de revendedor (meme) | relatable | 31 oct 23:40 | 4 | 293 | 0 | 0 | 3,4 |
| 2023 vs 2026 (meme) | antes/ahora | 3 nov 23:35 | 4 | 288 | 0 | 0 | 10,4 |
| Pinterest te dice qué vas a vender | truco | 30 oct 20:40 | 5 | 288 | 0 | 0 | 13,9 |
| proveedores de accesorios (parte 3) | serie proveedores | 1 nov 20:35 | 5 | 284 | 0 | 0 | 7,0 |
| proveedores de belleza (parte 4) | serie proveedores | 3 nov 20:30 | 5 | 262 | 0 | 0 | 3,8 |
| la 1ª foto decide si te compran 📸 | error→solución | 31 oct 17:25 | 6 | 256 | 0 | 0 | 0 |
| proveedores de zapatillas (parte 2) | serie proveedores | 31 oct 12:45 | 5 | 245 | 0 | 0 | 12,2 |
| ¿cuánto te quita Vinted de cada venta? (solo 23 h) | dinero en Vinted | 4 nov 09:30 | 5 | 190 | 0 | 0 | 26,3 |

- **Mejores 3 (visitas)**: "5 frases que te hacen perder dinero en Vinted" (2.166, 0 com.), "si Vinted te manda este aviso, para 🚫" (1.582, 1), "por esto tu precio espanta" (778, 1). **Por comentarios**: "las marcas que más rápido se venden" (7,5 por 1.000) y "¿quién paga el envío?" (5,3).
- **Peores 3 (visitas, con más de 24 h)**: "proveedores de zapatillas (parte 2)" (245, 0), "la 1ª foto decide si te compran 📸" (256, 0; 0 me gusta), "proveedores de belleza (parte 4)" (262, 0). (El de 190 del 4 nov aún es pronto para juzgarlo.)
- **Por formato** (media de visitas): riesgo de cuenta 865 (3; mediana 582), error→solución 496 (5; mediana 533), listas negativas 976 (3; mediana 460, el viral la sube), reflexión/motivación 392 (3), memes antes/ahora/relatable 379 (3; bajando 557 → 288), compra→venta 387 (2; 476 → 297), **serie proveedores 286 (4; la peor, 0 comentarios en las 4)**, dinero en Vinted 285 (2, uno aún fresco).
- **Por franja** (6 cada una): **17:30 → 774 (mediana 568, la mejor)**, 09:30 → 592 (mediana 420), 12:30 → 396 (389; la que más comenta), 23:30 → 386 (369), **20:30 → 326 (mediana 299, la peor 3 días seguidos)**.
- **Nº de diapositivas**: casi todo es de 5 (mediana ~400). 4 diap. (memes/reflexión) 309-557. Sin diferencia clara: quedarse en 5-6.
- **Guía del CTA**: siempre "proveedores" (pack), no se puede comparar.
- **Datos limitados**: 30 carruseles, 2-6 por grupo y dos virales mueven las medias. Son pistas, no reglas firmes.

**Reglas (basadas en 30 carruseles)**
1. **Repite la portada "aviso/pérdida sobre algo concreto que ya le pasa"** ("si Vinted te manda este aviso, para 🚫", "N frases que te hacen perder dinero 💸"). Nombra el mensaje, la frase o el aviso exacto. Amenazas genéricas ("esto puede costarte la cuenta", 430) y consejos suaves ("la 1ª foto decide…", 256) no despegan.
2. **El gancho más fuerte del día va a las 17:30, el segundo a las 09:30.** A las 20:30 nada importante (peor franja 3 días seguidos): ahí van temas de relleno, nunca un gancho de los de abajo.
3. **A las 12:30, dinero/marcas con pregunta cerrada al final** ("¿cuál vendes tú?", "¿qué tamaño pones tú?"): es donde salen los comentarios. Evita preguntas abiertas ("¿cómo es la tuya?", "¿dónde estás ahora?").
4. **Si el tema gusta pero la portada es suave, ponla en negativo y con número**: "20 favoritos y nadie compra 😩" (310) y "¿cuánto te quita Vinted?" (190) tienen los me gusta más altos (26 por 1.000) pero pocas visitas. Mejor "si tienes favoritos y 0 ventas, para y haz esto 🚫".
5. **Serie proveedores (parte N) y memes "20XX vs 2026"/"sábado noche": parar** después de lo ya programado (4 partes: 245-352 visitas, 0 comentarios). No repetir en 7 días un tema ya programado (ojo: "Vinted o Wallapop" está el 1 y el 7 nov). Siguen fuera Navidad y "primera venta/primer mes".

**Temas/ganchos a priorizar los próximos días** (no están en lo ya programado hasta el 8 nov)
1. "4 frases que te hacen perder ventas en Vinted 💸" (lista negativa de frases, molde del viral de 2.166; 17:30).
2. "si Vinted te oculta un artículo, haz esto 🚫" (aviso concreto, molde del de 1.582; 09:30).
3. "si tienes favoritos y 0 ventas, para y haz esto 🚫" (versión negativa del de 25,8 MG/1.000; 17:30).
4. "las marcas que menos se venden en Vinted (y cuáles sí)" con cierre "¿cuál vendes tú?" (marcas = más comentarios; 12:30).
5. "por esto tu descripción espanta a los compradores" (error→solución, el formato más estable; 09:30 o 17:30).
