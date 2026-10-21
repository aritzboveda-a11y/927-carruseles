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
**Actualizado: 21 oct 2026** (Metricool, 14-21 oct, solo carruseles PHOTO con más de 12 h, emparejados con historial.json por hora; Metricool da la hora en UTC, aquí en hora de Madrid). 26 carruseles medibles (14 oct 09:30 → 19 oct 09:30): 18.156 visitas, 116 me gusta (6,4 por 1.000), 10 comentarios (0,55 por 1.000). Media: 698 por carrusel.
- 🚨 **Ayer (20 oct) no se publicó NADA: 0 visitas.** Los 7 programados desde el 19 oct 20:30 hasta el 21 oct 00:00 están en ERROR "You have reached your Metricool account limit". Los de hoy (09:30, 12:30, 17:30, 20:30) siguen en PENDING y lo más probable es que fallen igual. El último carrusel con datos es del 19 oct 09:30; el de 19 oct 12:30 ("3 cosas que se venden en noviembre") no aparece. Hasta que Aritz arregle el plan de Metricool, hay que subir a mano (TikTok Studio) o no habrá datos nuevos.
- 🆕 **"¿cuánto ganas si vendes 3 cosas a la semana?" se recuperó** (469 → 767). El cálculo de N ventas ya no es 3 de 3 hundidos (ahora 767 y 367; el de "10 ventas" ya salió de la ventana). Sigue por debajo de la media y con 0 me gusta: mantener la regla 3, pero el problema es menos grave de lo que parecía.
- **Error→solución sigue siendo el más estable**: 3 de 3 entre 827 y 895, y "3 fallos por los que no te compran" (830) tiene 2 de los 10 comentarios.
- **17:30 es la mejor franja** (844 de media, 5 de 5 por encima de 795). 12:30 es la peor (582), pero porque ahí cayeron armario y Navidad; con buen tema 12:30 da el récord (1.177).
- ⚠️ **Comentarios casi a 0**: ninguno pasa de 2. Los que más comentan son los que preguntan por SU caso (primera venta 2,8/1.000, "1 prenda al día" 2,7, primer mes 2,5), aunque tengan pocas visitas.

| Carrusel (gancho) | Formato | Diap. | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| 3 cosas que no deberías vender en Vinted | riesgo de cuenta | 5 | 14 oct 12:30 | 1.177 | 0 | 0 | 6,8 |
| 3 fallos en el título que hacen que no te vean | error→solución | 5 | 15 oct 17:30 | 895 | 0 | 0 | 5,6 |
| Vinted o Wallapop: ¿dónde vendes más? | comparación | 5 | 17 oct 17:30 | 872 | 0 | 0 | 4,6 |
| ¿cuánto te queda de verdad de cada venta? | dinero de 1 venta | 6 | 18 oct 09:30 | 849 | 1 | 1,2 | 5,9 |
| 3 fallos por los que no te compran | error→solución | 5 | 18 oct 17:30 | 830 | 2 | 2,4 | 7,2 |
| por qué tus favoritos no te compran | error→solución | 5 | 16 oct 17:30 | 827 | 1 | 1,2 | 8,5 |
| ¿a qué hora vendes más en Vinted? | truco | 5 | 15 oct 09:30 | 827 | 0 | 0 | 14,5 |
| la diferencia entre el que vende y el que no | reflexión | 5 | 19 oct 00:00 | 823 | 1 | 1,2 | 7,3 |
| ¿cuánto tiempo le dedicas a revender? | reflexión | 6 | 17 oct 20:30 | 823 | 1 | 1,2 | 7,3 |
| 3 cosas que se agotan antes de Black Friday | lista + temporada | 5 | 17 oct 09:30 | 812 | 1 | 1,2 | 3,7 |
| nadie empieza sabiendo, bro | reflexión | 6 | 16 oct 00:00 | 808 | 0 | 0 | 3,7 |
| por qué la mayoría lo deja en la primera semana | reflexión | 6 | 15 oct 00:00 | 807 | 0 | 0 | 7,4 |
| ¿vendes más con lotes? | truco | 6 | 16 oct 20:30 | 795 | 0 | 0 | 2,5 |
| ¿cuánto rebajas cuando te hacen una oferta? | dinero de 1 cosa | 6 | 14 oct 17:30 | 795 | 0 | 0 | 3,8 |
| ¿cuánto ganas revendiendo zapas? | dinero de 1 cosa | 6 | 15 oct 20:30 | 773 | 0 | 0 | 1,3 |
| ¿cuánto vale un abrigo usado en Vinted? | dinero de 1 cosa | 6 | 14 oct 20:30 | 773 | 0 | 0 | 1,3 |
| ¿cuánto vale tu ropa de esquí en Vinted? | dinero de 1 cosa | 6 | 18 oct 20:30 | 771 | 0 | 0 | 7,8 |
| ¿cuánto ganas si vendes 3 cosas a la semana? 🆕↑ | cálculo de N ventas | 6 | 19 oct 09:30 | 767 | 0 | 0 | 0 |
| ¿cuánto puedes ganar con tus primeros 100€? | dinero de 1 cosa | 6 | 15 oct 12:30 | 765 | 0 | 0 | 6,5 |
| ¿tu precio asusta a los compradores? | dinero (repetido) | 6 | 17 oct 12:30 | 422 | 0 | 0 | 19,0 |
| lo que nadie te cuenta del primer mes | reflexión primer mes | 6 | 17 oct 00:00 | 405 | 1 | 2,5 | 9,9 |
| ¿cuánto ganas vendiendo 1 prenda al día? | cálculo de N ventas | 6 | 14 oct 09:30 | 367 | 1 | 2,7 | 10,9 |
| ¿y si tu primera venta llega esta semana? | reflexión primera venta | 6 | 18 oct 00:00 | 357 | 1 | 2,8 | 19,6 |
| ¿cuánto vale tu armario en Vinted? | dinero vago | 6 | 16 oct 12:30 | 277 | 0 | 0 | 0 |
| 3 regalos de Navidad que se venden en Vinted | lista + Navidad | 5 | 18 oct 12:30 | 270 | 0 | 0 | 7,4 |
| 3 cosas que vas a vender en Navidad | lista + Navidad | 5 | 16 oct 09:30 | 269 | 0 | 0 | 7,4 |

- **Mejores 3**: "3 cosas que no deberías vender en Vinted" (1.177 visitas, 0 com.), "3 fallos en el título que hacen que no te vean" (895, 0), "Vinted o Wallapop: ¿dónde vendes más?" (872, 0).
- **Peores 3**: "3 cosas que vas a vender en Navidad" (269, 0), "3 regalos de Navidad que se venden en Vinted" (270, 0), "¿cuánto vale tu armario en Vinted?" (277, 0).
- **Formato (media de visitas)**: riesgo de cuenta 1.177 (1), comparación 872 (1), error→solución 851 (3), reflexión de constancia 815 (4), truco 811 (2), Black Friday 812 (1), dinero de 1 cosa/venta 788 (6, todos 765-849), cálculo de N ventas 567 (2), precio repetido 422 (1), primera venta/primer mes 381 (2), dinero vago 277 (1), Navidad 270 (2).
- **Diapositivas**: 5 → 760 (10), 6 → 660 (16). Los hundidos de 6 son por tema; con el mismo tema la diferencia es pequeña, pero los 3 mejores tienen 5.
- **Hora**: 17:30 → 844, 20:30 → 787, 09:30 → 649, 00:00 → 640, 12:30 → 582. Los hundidos de 09:30/12:30/00:00 son por tema (Navidad, armario, primera venta).
- **Guía del CTA**: todos los de esta ventana llevan el mismo CTA de "proveedores"; no hay conclusión.
- **Datos limitados**: solo hay un carrusel de riesgo de cuenta y uno de comparación medidos en esta ventana; sus medias son de 1 caso. Sin publicaciones desde el 19 oct no se puede comprobar si la semana 20-26 oct funciona.

**Reglas (basadas en 26 carruseles)**
1. **Riesgo de cuenta y error→solución son los fijos**: al menos uno de cada al día. Pon el error→solución o la comparación a las 17:30 (la mejor franja: 844 de media, 5 de 5 por encima de 795).
2. **Comparaciones "X o Y"** (872): mínimo una cada 2 días.
3. **Dinero solo de UNA cosa o UNA venta** (765-849). Evita multiplicar ventas ("al día", "a la semana": 367 y 767, por debajo de la media) y las preguntas vagas ("tu armario", 277).
4. **Prohibido Navidad y "primera venta / primer mes"** (269-405). Black Friday sí (812). A las 00:00, reflexiones de constancia/mentalidad (807-823).
5. **5 diapositivas por defecto** (760 frente a 660; los 3 mejores tienen 5) y cierra con una pregunta sobre su caso o de opción ("¿cuál haces tú? 1, 2 o 3"), porque los comentarios siguen casi a 0 (0,55 por 1.000).

**Temas/ganchos a priorizar los próximos días** (⚠️ ninguno de la semana 20 oct ha salido por el límite de Metricool: repetirlos en cuanto se pueda publicar, empezando por estos)
1. "nunca escribas esto en el chat 🚫" (riesgo de cuenta, como "3 cosas que no deberías vender", 1.177; falló el 19 oct).
2. "tus fotos espantan a los compradores" (error→solución, como "3 fallos en el título", 895; falló el 20 oct) → ponerlo a las 17:30.
3. "¿proveedor de España o de China? 🤔" (comparación, como "Vinted o Wallapop", 872; falló el 20 oct).
4. "por qué Vinted te oculta las prendas 👀" (riesgo de cuenta; falló el 20 oct).
5. "si empezara otra vez, no haría esto" (reflexión 00:00, como "la diferencia entre el que vende y el que no", 823; falló el 20 oct).
