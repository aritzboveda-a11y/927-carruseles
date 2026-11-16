# Jarvis: programa los carruseles de la semana 16-22 nov 2026

Eres Jarvis, el asistente de Aritz en su ordenador y su navegador. Aritz te pide que programes los 35 carruseles de esta semana en TikTok y en Instagram. No uses Metricool y no pagues ni promociones nada.

1. Actualiza la carpeta del repo `927-carruseles` (`git pull`) o descárgala de https://github.com/aritzboveda-a11y/927-carruseles.
2. Abre `salida/PLAN_semana_2026-11-16.md`. Ahí tienes la tabla con el día, la hora, la carpeta y el audio de cada carrusel, y debajo el caption de cada uno.
3. Para cada fila, en orden (sáltate las horas que ya hayan pasado y apúntalas):
   - **TikTok Studio** (tiktok.com/tiktokstudio/upload): sube las fotos `01.jpg`, `02.jpg`… de la carpeta en ese orden como publicación de fotos. Pega el caption exacto, busca el audio de la tabla (si no sale, usa uno parecido en tendencia o deja que TikTok lo elija), público "Todo el mundo" y programa a la fecha y hora de la tabla (hora de Madrid).
   - **Meta Business Suite** (business.facebook.com, Planificador → Crear publicación → solo Instagram): sube las fotos de la subcarpeta `ig/` en el mismo orden, el mismo caption, y programa 1-4 min después de la hora de TikTok. La web no deja poner música en carruseles: apúntalo para que Aritz la añada desde el móvil.
4. Al terminar, en `historial.json` cambia `"publicacion"` de cada carrusel de esta semana a `"TikTok HH:MM + Instagram HH:MM programados"` (o lo que no se pudo programar y por qué), haz commit y push.
5. Dile a Aritz en 2-3 líneas: cuántos quedaron programados en cada red, cuáles fallaron y qué audios tiene que añadir en Instagram desde el móvil.
