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
**Actualizado: 16 oct 2026** (Metricool, 9-16 oct, solo carruseles PHOTO emparejados con historial/semana_manifest y con más de 12 h; Metricool da la hora en UTC, aquí en hora de Madrid). 24 carruseles medibles (9-15 oct): 15.243 visitas, 160 me gusta, 15 comentarios, 6 compartidos. Desde el informe de ayer: **+4.255 visitas** (≈3.810 de 5 carruseles que entran hoy por primera vez + ≈445 de los antiguos).
- ✅ **Falsa alarma de ayer**: los de 14 oct 12:30, 17:30 y 20:30 sí se publicaron; Metricool tarda ~1 día en mostrarlos. Hoy faltan los de 15 oct 12:30, 17:30, 20:30 y 16 oct 00:00 (probablemente el mismo retraso).
- **Nuevos**: "3 cosas que no deberías vender en Vinted" (caption "3 cosas que te pueden costar la cuenta", 14 oct 12:30) → **1.128, el mejor de la semana**; "¿cuánto rebajas cuando te hacen una oferta?" 779; "¿cuánto vale un abrigo usado?" 731; "por qué la mayoría lo deja en la primera semana" 697; "¿a qué hora vendes más?" 475 (aún <24 h). "¿cuánto ganas vendiendo 1 prenda al día?" se recuperó de 87 a 355; "10 ventas: ¿cuánto te queda?" (131) y "frío" (89) siguen hundidos.
- ℹ️ Fuera del análisis (sin emparejar): posts con caption solo "#fyp…" (12 oct 17:37, 851; 12 oct 20:35, 815; 9 oct 07:08, 231) y uno sin texto (12 oct 00:49, 964).

| Carrusel (gancho) | Formato | Diap. | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| 3 cosas que no deberías vender en Vinted 🆕 | lista de riesgo de cuenta | 5 | 14 oct 12:30 | 1.128 | 0 | 0 | 7,1 |
| ¿cuánto se queda Vinted de tu venta? | pregunta dinero | 6 | 11 oct 10:06 | 1.100 | 0 | 0 | 7,3 |
| ¿tu ropa lleva semanas sin venderse? | error→solución | 6 | 12 oct 20:30 | 990 | 0 | 0 | 9,1 |
| 3 cosas que se venden solas en invierno | lista + temporada | 5 | 11 oct 12:54 | 956 | 0 | 0 | 10,5 |
| ¿a cuánto vendes unas zapas en Vinted? | pregunta dinero | 5 | 13 oct 09:30 | 865 | 0 | 0 | 9,2 |
| ¿pones bien el precio en Vinted? | pregunta dinero | 6 | 10 oct 21:11 | 855 | 2 | 2,3 | 11,7 |
| si empezara hoy en Vinted, haría esto | historia/reto | 6 | 14 oct 00:00 | 820 | 1 | 1,2 | 7,3 |
| nadie te dice esto si Vinted te bloquea | polémica cuenta | 5 | 13 oct 12:30 | 803 | 3 | 3,7 | 6,2 |
| por esto Vinted no enseña tu ropa | error→solución | 6 | 10 oct 12:59 | 791 | 0 | 0 | 16,4 |
| ¿cuánto rebajas cuando te hacen una oferta? 🆕 | pregunta dinero | 6 | 14 oct 17:30 | 779 | 0 | 0 | 3,9 |
| 3 cosas que se agotan en Black Friday | lista + temporada | 7 | 9 oct 10:04 | 768 | 1 | 1,3 | 10,4 |
| ¿cometes estos errores al revender? | pregunta errores | 6 | 9 oct 21:04 | 763 | 1 | 1,3 | 7,9 |
| ¿cuánto vale un abrigo usado en Vinted? 🆕 | pregunta dinero + temporada | 6 | 14 oct 20:30 | 731 | 0 | 0 | 1,4 |
| por qué la mayoría lo deja en la primera semana 🆕 | reflexión | 6 | 15 oct 00:00 | 697 | 0 | 0 | 8,6 |
| ¿cuánto tardaste en tu primera venta? | reflexión | 6 | 13 oct 00:00 | 546 | 1 | 1,8 | 9,2 |
| ¿a qué hora vendes más en Vinted? 🆕 | truco | 5 | 15 oct 09:30 | 475 | 0 | 0 | 14,7 |
| así es un día revendiendo en Vinted | historia | 5 | 10 oct 17:34 | 464 | 0 | 0 | 17,2 |
| ¿cuánto ganas vendiendo 1 prenda al día? | pregunta dinero | 6 | 14 oct 09:30 | 355 | 1 | 2,8 | 11,3 |
| nadie te cuenta esto al revender | polémica | 7 | 11 oct 00:11 | 323 | 2 | 6,2 | 18,6 |
| con 50€ yo empezaría así | historia/reto | 6 | 9 oct 12:31 | 314 | 1 | 3,2 | 41,4 |
| nadie te dice esto de tu primera venta | polémica | 5 | 10 oct 09:34 | 266 | 1 | 3,8 | 33,8 |
| ¿tu proveedor te va a estafar? | pregunta nicho | 5 | 9 oct 17:35 | 234 | 0 | 0 | 17,1 |
| 10 ventas en Vinted: ¿cuánto te queda? | pregunta dinero | 6 | 13 oct 20:30 | 131 | 0 | 0 | 7,6 |
| 3 cosas que se buscan en Vinted con el frío | lista + temporada | 5 | 13 oct 17:30 | 89 | 1 | 11,2 | 22,5 |

- **Mejores 3**: "3 cosas que no deberías vender en Vinted" (1.128 visitas, 0 com.), "¿cuánto se queda Vinted de tu venta?" (1.100, 0), "¿tu ropa lleva semanas sin venderse?" (990, 0).
- **Peores 3**: "3 cosas que se buscan en Vinted con el frío" (89, 1), "10 ventas en Vinted: ¿cuánto te queda?" (131, 0), "¿tu proveedor te va a estafar?" (234, 0).
- **Tema "riesgo de tu cuenta de Vinted"** (bloqueo, lo que no debes vender, cuenta nueva): 1.128, 803 y 992 (este último ya fuera de la ventana). Es el tema más fiable que tenemos.
- **Formato (media de visitas)**: error→solución 890 (2), pregunta de dinero 688 (7; 731-1.100 si la pregunta es concreta —comisión, zapas, oferta, abrigo—, 131-355 si es "¿cuánto ganas/te queda con X ventas?"), reflexión 622 (2), lista 604 (3; sin "frío" 862), historia/reto 567, polémica genérica "nadie te cuenta…" sin tema de cuenta 294, nicho/proveedores 234.
- **Diapositivas**: 6 → 682 de media (13), 5 → 587 (9), 7 → 546 (2).
- **Hora**: 12:30 → 798 (5), 09:30 → 638 (6), 00:00 → 596 (4), 17:30 → 391 (4; incluye los dos peores de la franja), 20:30/21:00 → 694 (5). La hora pesa menos que el tema.
- **Guía del CTA**: no marca diferencia (casi todos "pack"/"proveedores").
- **Comentarios**: 1,0 por 1.000 visitas (bajo). Las preguntas de experiencia dieron 3 (bloqueo) pero también 0 en el de 1.128 ("¿te ha pasado alguna? cuéntamelo"): con 24 carruseles no hay patrón claro. Me gusta: los de "¿cuánto vale/rebajas…?" sacan 1-4 por 1.000 (se ven pero no gustan).

**Reglas (basadas en 24 carruseles)**
1. **Repite el tema "riesgo de tu cuenta"** al menos 1 vez cada 2 días, con ángulo nuevo cada vez (lo que no debes vender, lo que no debes escribir en el chat, lo que hace que Vinted te oculte, errores al subir muchas prendas). Formato lista "3 cosas que…" o error→solución, 5-6 diapositivas, a las 12:30 si se puede.
2. **Preguntas de dinero, solo concretas** (una prenda/marca/comisión/oferta: "¿a cuánto vendes unas zapas?", "¿cuánto se queda Vinted?"). **Evita** las de cálculo genérico "¿cuánto ganas/te queda con N ventas?" (131-355). Máximo 1 gancho "¿cuánto…?" al día.
3. **No repitas tema en 4 días** (sigue valiendo: "frío" justo después de "invierno" hizo 89). Y **evita** temas solo de proveedores/packaging/kilo y la polémica genérica "nadie te cuenta esto…" si no va de la cuenta.
4. **Usa 6 diapositivas** por defecto (682 vs 587 con 5); 7 solo si hace falta.
5. **Metricool va ~1 día por detrás**: solo avisa de un carrusel "no publicado" si no aparece después de 36 h.

**Temas/ganchos a priorizar los próximos días** (la tanda manual llega hasta el 19 oct; ojo: el 18 oct tiene dos "¿cuánto…?" a las 09:30 y 20:30 → cambiar uno)
1. "3 cosas que te pueden costar la cuenta de Vinted 🚫" con otro ángulo: "3 cosas que nunca debes escribir en el chat de Vinted" o "por qué Vinted te oculta las prendas" (tema top, 12:30).
2. "por qué tus favoritos no te compran 👀" (16 oct 17:30) y "3 fallos por los que no te compran" (18 oct 17:30): error→solución, el segundo formato más fuerte.
3. "¿cuánto vale tu armario en Vinted? 💸" (16 oct 12:30): pregunta de dinero concreta en la mejor franja.
4. "3 cosas que se agotan antes de Black Friday 🛍️" (17 oct 09:30): lista con fecha nueva (Black Friday hizo 768).
5. "¿tu precio asusta a los compradores? 💸" (17 oct 12:30): parecido a "¿pones bien el precio?" (855).
