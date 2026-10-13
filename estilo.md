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
**Actualizado: 13 oct 2026** (Metricool, 6-13 oct, solo carruseles PHOTO del agente con más de 12 h; horas en Madrid). 20 carruseles medibles (7-11 oct): 10.531 visitas, 165 me gusta, 10 comentarios, 13 compartidos.
🚨 **Ayer (12 oct) no se publicó NADA**: los 3 carruseles programados ("¿cuánto tardaste en tu primera venta?", "¿a cuánto vendes unas zapas?", "10 ventas: ¿cuánto te queda?") dieron ERROR en Metricool: "You have reached your Metricool account limit" (igual que los 3 de la tarde del 11 oct). Por eso **no hay datos nuevos** y los números de abajo son los mismos que ayer: no se sacan conclusiones nuevas.
ℹ️ Para la semana 13-19 oct se han preparado 29 carruseles para **subida manual** (`salida/semana_manifest.json`). Mientras siga el límite de Metricool, no programes con createScheduledPost sin comprobar después con getScheduledPosts que no sale ERROR.
ℹ️ Hay un post de fotos sin texto del 12 oct 00:49 (199 visitas) que no es del agente. No entra en el análisis.
ℹ️ Los carruseles siguen creciendo días después de publicarse (p. ej. "por esto Vinted no enseña tu ropa" 541 → 770).

| Carrusel (gancho) | Formato | Diap. | Hora | Visitas | Com. | Com/1000 | MG/1000 |
|---|---|---|---|---|---|---|---|
| ¿cuánto se queda Vinted de tu venta? | pregunta dinero | 6 | 11 oct 10:06 | 1.052 | 0 | 0 | 6,7 |
| Nadie te dice esto cuando abres una cuenta nueva | polémica | 6 | 8 oct 03:19 | 985 | 0 | 0 | 14,2 |
| 3 cosas que se venden solas en invierno | lista + temporada | 5 | 11 oct 12:54 | 907 | 0 | 0 | 8,8 |
| 3 cosas que tienes que vender en Vinted este otoño | lista + temporada | 5 | 8 oct 06:26 | 876 | 1 | 1,1 | 19,4 |
| ¿pones bien el precio en Vinted? | pregunta dinero | 6 | 10 oct 21:11 | 830 | 1 | 1,2 | 12,0 |
| por esto Vinted no enseña tu ropa | error→solución | 6 | 10 oct 12:59 | 770 | 0 | 0 | 16,9 |
| ¿cometes estos errores al revender? | pregunta errores | 6 | 9 oct 21:04 | 762 | 1 | 1,3 | 7,9 |
| 3 cosas que se agotan en Black Friday | lista + temporada | 7 | 9 oct 10:04 | 761 | 1 | 1,3 | 10,5 |
| ¿Sabes cuánto ganas de verdad con cada venta? | pregunta dinero | 5 | 8 oct 00:31 | 752 | 0 | 0 | 12,0 |
| así es un día revendiendo en Vinted | historia | 5 | 10 oct 17:34 | 456 | 0 | 0 | 15,4 |
| Si tus fotos no venden, haz esto | error→solución | 7 | 8 oct 09:20 | 438 | 0 | 0 | 22,8 |
| Cuando empecé, aceptaba todas las ofertas | confesión | 6 | 8 oct 12:25 | 323 | 1 | 3,1 | 15,5 |
| con 50€ yo empezaría así | historia/reto | 6 | 9 oct 12:31 | 310 | 1 | 3,2 | 41,9 |
| nadie te cuenta esto al revender | polémica/reflexión | 7 | 11 oct 00:11 | 309 | 2 | 6,5 | 19,4 |
| Cómo saber si un proveedor es fiable | cómo/aviso | 6 | 7 oct 21:52 | 279 | 1 | 3,6 | 32,3 |
| nadie te dice esto de tu primera venta | polémica | 5 | 10 oct 09:34 | 261 | 1 | 3,8 | 30,7 |
| ¿tu proveedor te va a estafar? | pregunta nicho | 5 | 9 oct 17:35 | 232 | 0 | 0 | 17,2 |
| ¿Proveedor chino o europeo? | pregunta nicho | 7 | 8 oct 18:08 | 104 | 0 | 0 | 38,5 |
| Lo que nadie mira al comprar por kilo | polémica | 6 | 8 oct 21:03 | 66 | 0 | 0 | 45,5 |
| ¿Tus paquetes parecen baratos? | pregunta nicho | 4 | 8 oct 14:57 | 58 | 0 | 0 | 69,0 |

- **Mejores 3**: "¿cuánto se queda Vinted de tu venta?" (1.052 visitas, 0 com.), "Nadie te dice esto cuando abres una cuenta nueva" (985, 0, 5 compartidos), "3 cosas que se venden solas en invierno" (907, 0).
- **Peores 3**: "¿Tus paquetes parecen baratos?" (58, 0), "Lo que nadie mira al comprar por kilo" (66, 0), "¿Proveedor chino o europeo?" (104, 0).
- **Formato (media de visitas)**: pregunta de dinero 878 (3 de 3 por encima de 750), lista + temporada 848 (3 de 3 por encima de 750), errores 762, error→solución 604, polémica "nadie te dice…" 437, historia/confesión/reflexión ≈310-456, pregunta de nicho 131.
- **Tema**: lo amplio de Vinted + dinero/temporada funciona; proveedores, packaging, kilo y chino/europeo no.
- **Diapositivas**: 6 → 597 de media (9), 5 → 581 (6), 7 → 403 (4), 4 → 58 (1).
- **Hora**: 00:00-07:00 730 (4), 07:00-12:00 628 (4), 12:00-17:00 474 (5), 17:00-24:00 390 (7); pero con tema amplio las 21:00 también llegan a 760-830.
- **Guía del CTA**: no marca diferencia en visitas ni comentarios.
- **Comentarios**: ≈1 por 1.000 visitas. Los que más comentan por visita son los de tono personal/reflexión ("nadie te cuenta esto al revender" 6,5/1000), aunque tengan menos alcance.

**Reglas (basadas en 20 carruseles; sin datos nuevos desde el 11 oct)**
1. **Repite más** la pregunta de dinero ("¿cuánto…?") y la lista + temporada ("3 cosas que…" + invierno/Navidad/Black Friday): al menos 2 de cada 3 carruseles.
2. **Evita** temas solo de proveedores, packaging, ropa por kilo o chino vs europeo: los proveedores van en el CTA, no en el tema.
3. **Para sacar comentarios**: gancho amplio en la portada + en la penúltima una pregunta personal que se conteste con un número o una palabra ("¿a cuánto lo vendes tú?", "¿abrigo o botas?").
4. **5 o 6 diapositivas**; 7 como mucho una vez cada 4; nunca 4.
5. **Comprueba que se publica**: tras createScheduledPost, mira getScheduledPosts; si sale ERROR ("account limit"), no sigas creando carruseles y avisa a Aritz.

**Temas/ganchos a priorizar los próximos días** (de la tanda manual de esta semana, los que encajan con lo que mejor funciona; súbelos primero)
1. "¿cuánto ganas vendiendo 1 prenda al día? 🤔" (pregunta de dinero).
2. "3 cosas que se buscan en Vinted con el frío 🧥" (lista + temporada).
3. "¿cuánto puedes ganar con tus primeros 100€? 💸" (pregunta de dinero).
4. "3 cosas que se agotan antes de Black Friday 🛍️" (lista + temporada).
5. "¿cuánto vale tu armario en Vinted? 💸" (pregunta de dinero, tema amplio).
