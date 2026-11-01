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
**Actualizado: 1 nov 2026** (Metricool, 25 oct-1 nov, solo carruseles PHOTO con más de 12 h; Metricool da la hora en UTC, aquí pasada a Madrid; emparejados por caption con los guion.json de `salida/`). 20 carruseles medibles: 8.658 visitas, 85 me gusta (9,8 por 1.000), **7 comentarios (0,8 por 1.000)**.
- **Ayer (31 oct) la cuenta sumó ~2.200 visitas** (menos que las ~3.600 del 30 oct): 854 de los 4 carruseles del 31 oct, ~390 de "nadie te va a aplaudir" (30 oct 23:30), +332 de "te escriben pero no te compran" (243 → 575), +256 de "Pinterest te dice qué vas a vender" (28 → 284), +135 de "5 frases que te hacen perder dinero" (1.787 → 1.922), +113 de "lo que necesitas para revender" y +73 de zapatillas <30€.
- **Los carruseles siguen creciendo después de las 12 h** (Pinterest ×10, "te escriben" ×2,4): los del 31 oct todavía no están cerrados; no sacar conclusiones fuertes de ellos.
- 🚨 **Comentarios casi a cero**: los 13 carruseles desde el 29 oct tienen 3 comentarios en total (los 3 en "las marcas que más rápido se venden"). Con la plantilla pinterest el CTA "proveedores" solo en el caption no genera comentarios. La pregunta del caso y "Comenta “proveedores”" tienen que ir escritas en la última diapositiva.
- 🚨 **Siguen sin aparecer en Metricool**: "esto hace que Vinted te limite la cuenta 🚫" (salida/2026-10-29_0930) y los del 27-28 oct. Comprobar en TikTok Studio.
- 🚨 **historial.json no coincide con lo publicado**: p. ej. el 31 oct 20:44 el historial dice "por esto se te acumula el stock" y salió "si empezara hoy con 50€, haría esto" (salida/2026-10-31_2030); el 1 nov 17:41 dice "el título" y la carpeta real es "por qué te regatean tanto" (salida/2026-11-01_1735). El agente debe apuntar el gancho y la carpeta reales.
- **TikTok tiene 30 programados como límite**: no programar más de ~6 días por delante.

| Carrusel (gancho) | Formato | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|
| 5 frases que te hacen perder dinero en Vinted | lista negativa | 29 oct 17:20 | 1.922 | 0 | 0 | 7,3 |
| lo que necesitas para revender en serio | lista | 30 oct 09:40 | 633 | 0 | 0 | 9,5 |
| te escriben pero no te compran 😩 | error→solución | 30 oct 17:30 | 575 | 0 | 0 | 3,5 |
| 2022 vs 2026 (meme, 4 diap.) | relatable | 29 oct 23:35 | 553 | 0 | 0 | 10,8 |
| zapatillas por menos de 30€ (precios de ejemplo) | lista (precios) | 30 oct 12:35 | 453 | 0 | 0 | 17,7 |
| errores de envío que salen caros | riesgo de cuenta | 26 oct 09:45 | 420 | 0 | 0 | 2,4 |
| nadie te va a aplaudir cuando empieces | reflexión | 30 oct 23:30 | 386 | 0 | 0 | 31,1 |
| las marcas que más rápido se venden en Vinted | lista (precios) | 29 oct 12:45 | 380 | 3 | 7,9 | 18,4 |
| proveedores de perfumes (parte 1) | serie proveedores | 29 oct 20:30 | 349 | 0 | 0 | 5,7 |
| ¿subes fotos sacadas de internet? ojo | riesgo de cuenta | 25 oct 12:45 | 332 | 2 | 6,0 | 15,1 |
| muchas visitas y 0 favoritos | error→solución | 25 oct 17:50 | 328 | 1 | 3,0 | 9,1 |
| Black Friday: ¿subes o bajas precios? | temporada | 26 oct 12:35 | 316 | 1 | 3,2 | 0 |
| una gorra de marca: ¿a cuánto la vendes? | dinero de 1 cosa | 25 oct 09:45 | 299 | 0 | 0 | 10,0 |
| nueva semana: haz esto antes del martes | reflexión | 26 oct 00:15 | 292 | 0 | 0 | 10,3 |
| Pinterest te dice qué vas a vender | truco | 30 oct 20:40 | 284 | 0 | 0 | 14,1 |
| ¿proveedor o tiendas de segunda mano? | comparación | 25 oct 20:45 | 282 | 0 | 0 | 7,1 |
| preguntas que nunca debes hacerle a un proveedor | lista negativa | 31 oct 09:35 | 276 | 0 | 0 | 7,2 |
| la 1ª foto decide si te compran 📸 | error→solución | 31 oct 17:25 | 244 | 0 | 0 | 0 |
| proveedores de zapatillas (parte 2) | serie proveedores | 31 oct 12:45 | 235 | 0 | 0 | 12,8 |
| si empezara hoy con 50€, haría esto | lista/plan | 31 oct 20:30 | 99 | 0 | 0 | 20,2 (solo 12 h) |

- **Mejores 3 (visitas)**: "5 frases que te hacen perder dinero en Vinted" (1.922, 0 com.), "lo que necesitas para revender en serio" (633, 0), "te escriben pero no te compran 😩" (575, 0). **Por comentarios**: "las marcas que más rápido se venden" (380, 3 com.). **Por me gusta**: "nadie te va a aplaudir cuando empieces" (31 MG/1.000).
- **Peores 3 (visitas)**: "si empezara hoy con 50€, haría esto" (99, 0; solo 12 h, mirar mañana), "proveedores de zapatillas (parte 2)" (235, 0), "la 1ª foto decide si te compran 📸" (244, 0; 0 me gusta).
- **Por formato**: lista 627 de media (6; 368 sin el de 1.922), relatable/meme 553 (1), error→solución 382 (3), riesgo de cuenta 376 (2; el que más comenta, 2,7 com/1.000), reflexión 339 (2; la que más gusta, 22 MG/1.000), temporada 316, dinero de 1 cosa 299, serie proveedores 292 (2; baja: perfumes 349 → zapatillas 235), truco 284, comparación 282.
- **Por franja**: 17:30 → 767 (4; 382 sin el de 1.922), 23:30 → 470 (2), 09:30 → 407 (4), 12:30 → 343 (5; la única que comenta, 3,5 com/1.000), 00:00 → 292 (1), 20:30 → 254 (4; la peor por tercer día).
- **Nº de diapositivas**: 6 diap. 661 de media (4; incluye el de 1.922), 4 diap. 553 (1, meme), 5 diap. 399 (8). Sin diferencia clara quitando el viral. Guía del CTA: siempre "proveedores", no se puede comparar.
- **Datos limitados**: 1-6 carruseles por grupo y un solo viral mueve todas las medias. Son pistas, no reglas firmes.

**Reglas (basadas en 20 carruseles)**
1. **Repite "N cosas/frases/errores que te hacen perder dinero 💸"** (lista negativa) a las 17:30: sigue siendo el único que ha despegado (1.922) y 17:30 es la mejor franja. Varía el objeto (fotos, precios, títulos, envíos).
2. **Pon la pregunta y "Comenta “proveedores”" en la última diapositiva**, con una pregunta concreta de elegir ("¿cuál vendes tú?", como en "marcas que más rápido se venden", el único con comentarios esta semana). Las preguntas abiertas tipo "¿cuánto llevas revendiendo?" dan 0.
3. **Listas de "lo que necesitas / lo que compro" con precios de ejemplo a las 09:30-12:30** (633 y 453 visitas, 10-18 MG/1.000): repetir.
4. **20:30 es la peor franja por tercer día (254)**: no gastar ahí los mejores ganchos; la serie proveedores baja (349 → 235), si sigue, a las 12:30 con "¿cuál vendes tú?".
5. **Evita comparaciones ("¿X o Y?"), "¿a cuánto vendes X?" y Black Friday "¿subes o bajas?"**: <320 visitas y casi 0 interacción. Siguen prohibidos Navidad y "primera venta/primer mes".

**Temas/ganchos a priorizar los próximos días**
1. "5 fotos que te hacen perder ventas en Vinted 📸" (lista negativa; 17:30).
2. "3 precios que te hacen perder dinero en Vinted 💸" (lista negativa; 17:30).
3. "lo que compro con 100€ para revender (precios de ejemplo)" (lista tipo "lo que necesitas"; 09:30).
4. "marcas que suben de precio en invierno en Vinted 🧥 ¿cuál vendes tú?" (lista con precios; 12:30).
5. "2023 vs 2026 😂" / "nadie te va a aplaudir" (meme o reflexión corta; 23:30).
