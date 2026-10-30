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
**Actualizado: 30 oct 2026** (Metricool, 23-30 oct, solo carruseles PHOTO con más de 12 h; Metricool da la hora en UTC, aquí pasada a Madrid). 20 carruseles medibles: 6.277 visitas, 61 me gusta (9,7 por 1.000), 11 comentarios (1,8 por 1.000).
- **Ayer (29 oct) se volvió a publicar** tras 3 días parados (27-28 oct = 0). Ayer sumó **~660 visitas**: 599 de los 3 carruseles nuevos + ~60 de los antiguos (que ya crecen solo +0 a +14 cada uno).
- 🚨 **Del 29 oct solo aparecen 3 de 5 en Metricool**: falta el de las 09:30 ("esto hace que Vinted te limite la cuenta 🚫", salida/2026-10-29_0930); el de las 23:35 (2022 vs 2026) aún no tiene 12 h. Comprobar en TikTok Studio si salió; si no, subirlo en la próxima franja de 09:30.
- 🚨 **historial.json no coincide con lo publicado el 29 oct**: dice "señales de proveedor estafa", "3 cosas que Vinted no te deja vender", "5 estrellas", "3 nichos"… pero lo que salió (carpetas 2026-10-29_0930/_1245/_1720/_2030/_2335) fue: limitar la cuenta, marcas que más rápido se venden, 5 frases que te hacen perder dinero, proveedores de perfumes (parte 1) y 2022 vs 2026. El agente debe apuntar en el historial lo que de verdad se publica (tema, gancho y carpeta reales).
- **Plantilla pinterest (primeros datos, 3 carruseles)**: alcance igual o algo menor que la anterior (280, 223, 96), pero "5 frases que te hacen perder dinero" tiene 31 me gusta por 1.000, el triple de la media. Aún pocos datos para juzgarla.

| Carrusel (gancho) | Formato | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|
| esto hace que Vinted desconfíe de ti | riesgo de cuenta | 23 oct 09:45 | 715 | 0 | 0 | 5,6 |
| errores de envío que salen caros | riesgo de cuenta | 26 oct 09:45 | 409 | 0 | 0 | 2,4 |
| por esto te devuelven los pedidos | error→solución | 23 oct 17:45 | 375 | 0 | 0 | 21,3 |
| antes de subir la ropa, mira esto | error→solución | 24 oct 17:50 | 333 | 0 | 0 | 9,0 |
| muchas visitas y 0 favoritos | error→solución | 25 oct 17:50 | 326 | 1 | 3,1 | 9,2 |
| ¿subes fotos sacadas de internet? ojo | riesgo de cuenta | 25 oct 12:45 | 326 | 2 | 6,1 | 15,3 |
| ¿ropa de marca o sin marca? | comparación | 23 oct 20:45 | 325 | 0 | 0 | 3,1 |
| Black Friday: ¿subes o bajas precios? | temporada | 26 oct 12:35 | 304 | 1 | 3,3 | 0 |
| lo que haces el domingo decide tu semana | reflexión | 25 oct 00:15 | 303 | 1 | 3,3 | 9,9 |
| una gorra de marca: ¿a cuánto la vendes? | dinero de 1 cosa | 25 oct 09:45 | 296 | 0 | 0 | 10,1 |
| ¿te piden pagar fuera de Vinted? | riesgo de cuenta | 24 oct 12:50 | 288 | 1 | 3,5 | 10,4 |
| nueva semana: haz esto antes del martes | reflexión | 26 oct 00:15 | 288 | 0 | 0 | 10,4 |
| ¿Vinted o tu propia tienda online? | comparación | 24 oct 20:50 | 287 | 0 | 0 | 3,5 |
| las marcas que más rápido se venden en Vinted | lista (pinterest) | 29 oct 12:45 | 280 | 1 | 3,6 | 14,3 |
| ¿cuántas veces has pensado en dejarlo? | reflexión | 24 oct 00:10 | 278 | 1 | 3,6 | 7,2 |
| ¿a cuánto vendes unos vaqueros de marca? | dinero de 1 cosa | 23 oct 12:35 | 277 | 0 | 0 | 14,4 |
| ¿proveedor o tiendas de segunda mano? | comparación | 25 oct 20:45 | 275 | 0 | 0 | 7,3 |
| 3 trucos para que tu prenda salga más | lista | 24 oct 09:40 | 273 | 3 | 11,0 | 14,7 |
| 5 frases que te hacen perder dinero en Vinted | lista (pinterest) | 29 oct 17:20 | 223 | 0 | 0 | 31,4 |
| proveedores de perfumes que tienes que conocer (parte 1) | serie proveedores | 29 oct 20:30 | 96 | 0 | 0 | 0 |

- **Mejores 3 (visitas)**: "esto hace que Vinted desconfíe de ti" (715, 0 com.), "errores de envío que salen caros" (409, 0), "por esto te devuelven los pedidos" (375, 0). **Por comentarios**: "3 trucos para que tu prenda salga más" (273, 3 com.) y "¿subes fotos sacadas de internet? ojo" (326, 2).
- **Peores 3 (visitas)**: "proveedores de perfumes… (parte 1)" (96, 0; solo 12 h, puede subir), "5 frases que te hacen perder dinero" (223, 0; pero el que más gusta), "3 trucos para que tu prenda salga más" (273, 3; poco alcance pero el que más comenta).
- **Por formato**: riesgo de cuenta 435 de media (4; sin el de 715, 341; 1,7 com/1.000), error→solución 345 (3; 1,0 com/1.000), reflexión 290 (3), comparación 296 (3; 0 com.), dinero de 1 cosa 287 (2; 0 com.), lista 259 (3; 5,2 com/1.000, la que más comenta y gusta).
- **Por franja**: 09:30 → 423 (4), 17:30 → 314 (4), 12:30 → 295 (5), 00:00 → 290 (3), 20:30 → 246 (4; comparaciones y la parte 1 recién publicada).
- **Nº de diapositivas y guía del CTA**: sin diferencias medibles (casi todos 5-6 diapositivas y el mismo CTA "proveedores").
- **Datos limitados**: 2-4 carruseles por grupo; los comentarios son tan pocos (11 en 20) que 1 comentario cambia el ranking. Son pistas, no reglas firmes.

**Reglas (basadas en 20 carruseles)**
1. **Publicar todos los días sin huecos**: 3 días parados dejaron la cuenta en ~50 visitas/día; los antiguos ya no crecen. 4-5 al día, separados 3 h o más (7 en un día hundió el alcance el 22 oct).
2. **Riesgo de cuenta (🚫/"ojo"/"salen caros") a las 09:30**: sigue siendo la combinación con más visitas (423 de media). No saltarse esa franja.
3. **Más listas con pregunta sobre SU caso** ("¿cuál no hacías?", "¿cuántas tiene tu última prenda?"): las listas son lo que más comenta y gusta (3 trucos 11 com/1.000, 5 frases 31 MG/1.000). Añadir esa pregunta también a los riesgos de cuenta, que tienen alcance pero 0 comentarios.
4. **Evita comparaciones ("¿X o Y?") y "¿a cuánto vendes X?"**: 0 comentarios en 8 carruseles. Siguen prohibidos Navidad y "primera venta/primer mes".
5. **Serie proveedores**: la parte 1 (perfumes) va floja en sus primeras 12 h (96). Mirar mañana sus visitas antes de seguir; si no pasa de ~200, no poner más "partes" a las 20:30 y probar la serie a las 09:30 o 17:30.

**Temas/ganchos a priorizar los próximos días**
1. "esto hace que Vinted te limite la cuenta 🚫" (salida/2026-10-29_0930; no aparece publicado; 09:30).
2. "avisos de Vinted que no puedes ignorar 🚫" (riesgo de cuenta; 09:30).
3. "estafas a vendedores en Vinted 🚩" (riesgo; buena franja 09:30 o 17:30).
4. "muchos favoritos y 0 ventas en Vinted 😩" (error→solución en forma de lista con "¿cuántos tiene tu última prenda?"; 17:30).
5. "te escriben pero no te compran 😩" (ya preparado para hoy 17:30, salida/2026-10-30_1730; lista + pregunta de su caso).
