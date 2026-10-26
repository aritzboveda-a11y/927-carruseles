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
**Actualizado: 26 oct 2026** (Metricool, 19-26 oct, solo carruseles PHOTO con más de 12 h, emparejados con historial.json por caption y hora; Metricool da la hora en UTC, aquí pasada a Madrid). 29 carruseles medibles: 7.582 visitas, 69 me gusta (9,1 por 1.000), 19 comentarios (2,5 por 1.000).
- ✅ **Corrección de ayer: SÍ se publicó.** Los carruseles del 22 oct tarde al 25 oct mañana están en TikTok con visitas, aunque en el planificador de Metricool salen como ERROR "account limit". Ese estado no es fiable: la analítica de Metricool llega con ~1 día de retraso. Para saber si algo salió, mirar getAnalyticsDataByMetrics al día siguiente, no el estado del planificador.
- Aún no aparecen en la analítica (ni se pueden medir): 25 oct 12:47 (fotos de internet), 17:49 (visitas y 0 favoritos), 20:44 (proveedor o segunda mano) y 26 oct 00:13. Comprobar mañana.
- **Cola casi vacía**: en Metricool solo quedan 2 programados (hoy 09:46 envíos y 12:35 Black Friday). Después de las 12:35 de hoy no hay nada programado.
- **Ayer (25 oct)** salieron 2 que se puedan medir: domingo 00:15 (284) y gorra 09:45 (192) = 476 visitas.
- **Alcance**: tras el hundimiento del 21-22 oct (7 en un día → 48-87 visitas), desde el 22 oct 17:50 se ha recuperado a una meseta de **~300 de media** (14 carruseles entre 144 y 555). Todavía lejos de los ~800 del 17-19 oct.
- **Comentarios**: suben respecto a la semana pasada (2,5 por 1.000 frente a 1,2). Los 3 que más comentan son los que preguntan por SU situación concreta: "te ven pero nadie te escribe" (11,7/1.000), "3 trucos para que tu prenda salga más" (11,2), "1 cosa al día" (10,5).

| Carrusel (gancho) | Formato | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|
| ¿cuánto ganas si vendes 3 cosas a la semana? | cálculo | 19 oct 09:30 | 778 | 0 | 0 | 0 |
| esto hace que Vinted desconfíe de ti | riesgo de cuenta | 23 oct 09:45 | 555 | 0 | 0 | 5,4 |
| tus fotos espantan a los compradores | error→solución | 20 oct 19:10 | 527 | 0 | 0 | 3,8 |
| si solo hicieras 1 cosa al día en Vinted | reflexión | 23 oct 00:20 | 380 | 4 | 10,5 | 10,5 |
| por esto te devuelven los pedidos | error→solución | 23 oct 17:45 | 371 | 0 | 0 | 21,6 |
| te ven pero nadie te escribe | error→solución | 22 oct 17:50 | 343 | 4 | 11,7 | 17,5 |
| ¿ropa de marca o sin marca? | comparación | 23 oct 20:45 | 318 | 0 | 0 | 3,1 |
| vender poco también es avanzar, bro | reflexión | 21 oct 00:05 | 316 | 1 | 3,2 | 3,2 |
| nunca escribas esto en el chat | riesgo de cuenta | 20 oct 22:15 | 314 | 1 | 3,2 | 15,9 |
| por qué Vinted te oculta las prendas | riesgo de cuenta | 20 oct 20:40 | 309 | 0 | 0 | 3,2 |
| ¿cuánto vale una camiseta de fútbol? | dinero de 1 cosa | 21 oct 09:35 | 305 | 1 | 3,3 | 0 |
| antes de subir la ropa, mira esto | error→solución | 24 oct 17:50 | 291 | 0 | 0 | 10,3 |
| lo que haces el domingo decide tu semana | reflexión | 25 oct 00:15 | 284 | 1 | 3,5 | 10,6 |
| ¿te piden pagar fuera de Vinted? | riesgo de cuenta | 24 oct 12:50 | 281 | 1 | 3,6 | 10,7 |
| ¿Vinted o tu propia tienda online? | comparación | 24 oct 20:50 | 277 | 0 | 0 | 3,6 |
| ¿a cuánto vendes unos vaqueros de marca? | dinero de 1 cosa | 23 oct 12:35 | 272 | 0 | 0 | 14,7 |
| ¿cuántas veces has pensado en dejarlo? | reflexión | 24 oct 00:10 | 272 | 1 | 3,7 | 7,4 |
| ¿proveedor de España o de China? | comparación | 20 oct 17:45 | 270 | 2 | 7,4 | 7,4 |
| 3 trucos para que tu prenda salga más | lista | 24 oct 09:40 | 269 | 3 | 11,2 | 14,9 |
| una gorra de marca: ¿a cuánto la vendes? | dinero de 1 cosa | 25 oct 09:45 | 192 | 0 | 0 | 10,4 |
| ¿vender barato y rápido o caro y despacio? | comparación | 22 oct 20:50 | 144 | 0 | 0 | 20,8 |
| ¿a cuánto vendes una sudadera de marca? | dinero de 1 cosa | 21 oct 15:00 | 87 | 0 | 0 | 11,5 |
| tu descripción te está quitando ventas | error→solución | 21 oct 12:50 | 81 | 0 | 0 | 12,3 |
| ¿comprar por kilo o por unidad? | comparación | 21 oct 17:35 | 72 | 0 | 0 | 41,7 |
| si empezara otra vez, no haría esto | confesión | 21 oct 22:45 | 60 | 0 | 0 | 16,7 |
| ¿borras y vuelves a subir tus prendas? ojo | riesgo de cuenta | 22 oct 09:50 | 60 | 0 | 0 | 50,0 |
| nadie ve lo que hay detrás de cada venta | reflexión | 22 oct 00:20 | 56 | 0 | 0 | 0 |
| ¿cuenta nueva? no hagas esto | riesgo de cuenta | 21 oct 20:50 | 50 | 0 | 0 | 20,0 |
| ¿a cuánto vendes un bolso en Vinted? | dinero de 1 cosa | 22 oct 12:45 | 48 | 0 | 0 | 20,8 |

- **Mejores 3**: "¿cuánto ganas si vendes 3 cosas a la semana?" (778 visitas, 0 com.), "esto hace que Vinted desconfíe de ti" (555, 0), "tus fotos espantan a los compradores" (527, 0). Por comentarios: "te ven pero nadie te escribe" (343, 4) y "1 cosa al día" (380, 4).
- **Peores 3**: "¿a cuánto vendes un bolso en Vinted?" (48, 0), "¿cuenta nueva? no hagas esto" (50, 0), "nadie ve lo que hay detrás de cada venta" (56, 0). Todos del día del hundimiento (21-22 oct), así que dicen más de la frecuencia que del tema.
- **Por formato (solo la meseta desde el 22 oct 17:50, 14 carruseles)**: riesgo de cuenta 418 de media (2), error→solución 335 (3, 4 com/1.000), reflexión 312 (3, 6,4 com/1.000), lista 269 (1, 11,2 com/1.000), comparación 246 (3, 0 comentarios), dinero de 1 cosa 232 (2, 0 comentarios).
- **Por franja (misma meseta)**: 09:30 → 339, 17:30 → 335, 00:00 → 312, 12:30 → 276, 20:30 → 246. Diferencias pequeñas con 2-3 carruseles por franja: orientativo.
- **Guía del CTA y nº de diapositivas**: todos llevan CTA de "proveedores" (guía pack o accesorios) y 5-6 diapositivas; no hay variación suficiente para comparar.
- **Datos limitados**: 2-3 carruseles por formato y franja. Las tendencias son pistas, no reglas firmes.

**Reglas (basadas en 29 carruseles)**
1. **No fiarse del estado ERROR del planificador de Metricool**: comprobar en la analítica del día siguiente si salió. Si la analítica tampoco lo muestra 24 h después, entonces sí avisar a Aritz.
2. **Máximo 4-5 carruseles al día, separados 3 h o más**; nunca 7 en un día como el 21 oct (hundió el alcance a <90).
3. **Repite más error→solución sobre un problema concreto de Vinted** ("te ven pero nadie te escribe", "por esto te devuelven", "Vinted desconfía de ti"): mejor alcance y comentarios de la semana. Mejor a las 09:30 o 17:30.
4. **Pregunta final sobre SU caso con número o elección** ("¿cuántas visitas tiene tu última prenda?", "¿cuál no hacías?"): es lo que saca comentarios.
5. **Evita de momento "¿a cuánto vendes X?" (dinero de 1 cosa) y las comparaciones a las 20:30**: 0 comentarios y por debajo de la media en la meseta. Siguen prohibidos Navidad y "primera venta/primer mes".

**Temas/ganchos a priorizar los próximos días**
1. "por esto Vinted te limita la cuenta 🚫" (riesgo de cuenta, como el 555; 09:30).
2. "3 cosas que haces y espantan compradores" (lista + error→solución; 17:30).
3. "te escriben pero no te compran 😩" (error→solución, continuación del que más comentó; 17:30).
4. "si solo tuvieras 10 min al día para Vinted" (reflexión tipo "1 cosa al día"; 00:00).
5. "¿cuánto ganas si vendes 1 cosa al día?" (cálculo, como el récord de 778; 09:30, sin cifras personales).
