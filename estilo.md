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
**Actualizado: 17 oct 2026** (Metricool, 10-17 oct, solo carruseles PHOTO emparejados con historial.json; Metricool da la hora en UTC, aquí en hora de Madrid). 26 carruseles medibles (10-16 oct): 17.175 visitas, 149 me gusta, 12 comentarios. Desde el informe de ayer: **+4.011 visitas** (3.411 de 7 carruseles que entran hoy + 600 de los antiguos). Media: 661 por carrusel.
- ✅ Llegaron los que faltaban ayer (15 oct 12:30, 17:30, 20:30 y 16 oct 00:00): todos entre 754 y 813. Ahora salen justo a la hora del historial.
- **Patrón claro: todo o nada.** Cada carrusel acaba en 750-1.150 o se queda en 80-470; casi no hay término medio, y el que arranca mal no se recupera (frío 89→95, 10 ventas 131→139). Los 8 hundidos son: cálculo genérico de ganancias (2), lista de temporada repetida (frío, Navidad), polémica "nadie te dice/cuenta…" sin tema de cuenta (2), "un día revendiendo" y "armario" (aún <24 h).
- ⚠️ **Comentarios: 0 en los 9 carruseles más nuevos** (desde el 14 oct 17:30). En total 0,7 por 1.000 visitas. Los únicos con comentarios recientes: "bloqueo" (3), "si empezara hoy" (1), "1 prenda al día" (1).
- ℹ️ Fuera del análisis (sin emparejar): 12 oct 17:37 "#fyp…" (854), 12 oct 20:35 "#paratiii…" (820), 12 oct 00:49 sin texto (969).

| Carrusel (gancho) | Formato | Diap. | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| 3 cosas que no deberías vender en Vinted | lista riesgo de cuenta | 5 | 14 oct 12:30 | 1.148 | 0 | 0 | 7,0 |
| ¿cuánto se queda Vinted de tu venta? | pregunta dinero concreta | 6 | 11 oct 10:06 | 1.112 | 0 | 0 | 7,2 |
| ¿tu ropa lleva semanas sin venderse? | error→solución | 6 | 12 oct 20:30 | 998 | 0 | 0 | 8,0 |
| 3 cosas que se venden solas en invierno | lista + temporada | 5 | 11 oct 12:54 | 958 | 0 | 0 | 10,4 |
| ¿a cuánto vendes unas zapas en Vinted? | pregunta dinero concreta | 5 | 13 oct 09:30 | 870 | 0 | 0 | 9,2 |
| ¿pones bien el precio en Vinted? | pregunta dinero concreta | 6 | 10 oct 21:11 | 861 | 2 | 2,3 | 11,6 |
| si empezara hoy en Vinted, haría esto | historia/reto | 6 | 14 oct 00:00 | 829 | 1 | 1,2 | 7,2 |
| ¿a qué hora vendes más en Vinted? | truco | 5 | 15 oct 09:30 | 818 | 0 | 0 | 14,7 |
| 3 fallos en el título que hacen que no te vean 🆕 | lista error→solución | 5 | 15 oct 17:30 | 813 | 0 | 0 | 6,2 |
| nadie te dice esto si Vinted te bloquea | polémica cuenta | 5 | 13 oct 12:30 | 808 | 3 | 3,7 | 6,2 |
| por esto Vinted no enseña tu ropa | error→solución | 6 | 10 oct 12:59 | 796 | 0 | 0 | 16,3 |
| por qué la mayoría lo deja en la primera semana | reflexión | 6 | 15 oct 00:00 | 794 | 0 | 0 | 7,6 |
| ¿cuánto rebajas cuando te hacen una oferta? | pregunta dinero concreta | 6 | 14 oct 17:30 | 793 | 0 | 0 | 3,8 |
| nadie empieza sabiendo, bro 🆕 | reflexión | 6 | 16 oct 00:00 | 778 | 0 | 0 | 3,9 |
| ¿cuánto vale un abrigo usado en Vinted? | pregunta dinero + temporada | 6 | 14 oct 20:30 | 771 | 0 | 0 | 1,3 |
| ¿cuánto ganas revendiendo zapas? 🆕 | pregunta dinero concreta | 6 | 15 oct 20:30 | 755 | 0 | 0 | 1,3 |
| ¿cuánto puedes ganar con tus primeros 100€? 🆕 | pregunta dinero (inversión) | 6 | 15 oct 12:30 | 754 | 0 | 0 | 6,6 |
| ¿cuánto tardaste en tu primera venta? | reflexión | 6 | 13 oct 00:00 | 551 | 1 | 1,8 | 9,1 |
| así es un día revendiendo en Vinted | historia | 5 | 10 oct 17:34 | 466 | 0 | 0 | 17,2 |
| ¿cuánto ganas vendiendo 1 prenda al día? | cálculo genérico | 6 | 14 oct 09:30 | 362 | 1 | 2,8 | 11,0 |
| nadie te cuenta esto al revender | polémica genérica | 7 | 11 oct 00:11 | 326 | 2 | 6,1 | 18,4 |
| nadie te dice esto de tu primera venta | polémica genérica | 5 | 10 oct 09:34 | 269 | 1 | 3,7 | 33,5 |
| 3 cosas que vas a vender en Navidad 🆕 | lista + temporada | 5 | 16 oct 09:30 | 232 | 0 | 0 | 8,6 |
| 10 ventas en Vinted: ¿cuánto te queda? | cálculo genérico | 6 | 13 oct 20:30 | 139 | 0 | 0 | 7,2 |
| 3 cosas que se buscan en Vinted con el frío | lista + temporada | 5 | 13 oct 17:30 | 95 | 1 | 10,5 | 21,1 |
| ¿cuánto vale tu armario en Vinted? 🆕 (<24 h) | pregunta dinero vaga | 6 | 16 oct 12:30 | 79 | 0 | 0 | 0 |

- **Mejores 3**: "3 cosas que no deberías vender en Vinted" (1.148 visitas, 0 com.), "¿cuánto se queda Vinted de tu venta?" (1.112, 0), "¿tu ropa lleva semanas sin venderse?" (998, 0).
- **Peores 3** (con más de 24 h): "3 cosas que se buscan en Vinted con el frío" (95, 1), "10 ventas en Vinted: ¿cuánto te queda?" (139, 0), "3 cosas que vas a vender en Navidad" (232, 0). "¿cuánto vale tu armario?" va en 79 a las 20 h: pinta a hundido.
- **Formato (media de visitas)**: riesgo de cuenta 978 (2), error→solución 869 (3, contando "3 fallos en el título"), truco 818, historia/reto "si empezara hoy" 829, pregunta de dinero concreta 860 (6: comisión, zapas ×2, precio, oferta, abrigo), reflexión 708 (3), cálculo genérico de ganancias 251 (2), polémica genérica 298 (2), lista de temporada 428 (3: invierno 958 pero frío 95 y Navidad 232).
- **Temporada**: la PRIMERA lista de temporada de cada tanda funciona (Black Friday 768, invierno 958); las siguientes parecidas se hunden (frío 95, Navidad 232). El algoritmo parece castigar la repetición del ángulo "3 cosas que se venden en…".
- **Diapositivas**: 6 → 691 (15), 5 → 648 (10), 7 → 326 (1). Diferencia pequeña; pesa más el tema.
- **Hora**: 00:00 → 738 (4), 12:30 → 697 (4), 20:30 → 666 (4), 09:30 → 570 (4), 17:30 → 567 (3). Poca diferencia: la hora no explica los hundidos.
- **Guía del CTA**: todos "proveedor(es)", sin diferencia medible.

**Reglas (basadas en 26 carruseles)**
1. **Repite "riesgo de tu cuenta de Vinted"** cada 2 días como mínimo, con ángulo nuevo (lo que no debes escribir en el chat, por qué Vinted te oculta, cuenta nueva, subir muchas prendas de golpe). Lista "3 cosas que…" o error→solución.
2. **Preguntas de dinero: solo si nombran UNA cosa concreta** (comisión, unas zapas, una oferta, un abrigo, un precio). **Prohibido el cálculo genérico** "¿cuánto ganas/te queda si vendes N…?" y las vagas ("¿cuánto vale tu armario?"): 79-362 visitas.
3. **Máximo 1 lista de temporada cada 4 días** y con ángulo distinto de la anterior (no "invierno"→"frío", no "Black Friday"→"Navidad"→"noviembre" seguidos).
4. **Nada de polémica genérica "nadie te cuenta/dice esto…"** si no va de la cuenta de Vinted (266-326).
5. **Comentarios a 0**: termina la última diapositiva con una pregunta de respuesta de una palabra o un número fácil ("¿te ha pasado? sí/no", "¿1, 2 o 3?") además del CTA de "proveedores"; las de "¿te ha pasado alguna vez?" (bloqueo) son las que más comentarios dieron.

**Temas/ganchos a priorizar los próximos días** (⚠️ la tanda ya programada tiene 2 ganchos de cálculo genérico: 18 oct 09:30 "¿cuánto te queda de verdad de cada venta?" y 19 oct 09:30 "¿cuánto ganas si vendes 3 cosas a la semana?", y 2 listas de temporada seguidas: 18 oct 12:30 Navidad y 19 oct 12:30 noviembre → si se generan de nuevo, cambiarlos por los de abajo)
1. "3 cosas que nunca debes escribir en el chat de Vinted 🚫" (riesgo de cuenta, el tema top).
2. "por qué Vinted te oculta las prendas 👀" (riesgo de cuenta + error→solución).
3. "3 fallos en las fotos que hacen que no te compren 📸" (error→solución, como "3 fallos en el título", 813).
4. "¿cuánto se queda Correos/el envío de tu venta? 📦" (pregunta de dinero concreta, como la comisión, 1.112).
5. "si empezara hoy con 0 seguidores en Vinted, haría esto" (historia/reto, 829).
