# 927-carruseles

Agente de carruseles de TikTok de 927studios. Cada 3 horas Claude:
1. Lee `estilo.md` (el estilo de Aritz) e `historial.json` (lo ya publicado).
2. Escribe un carrusel nuevo y lo dibuja con `carrusel.py` (usa las fotos de `fondos/` si hay).
3. Sube las imágenes a `salida/` y las publica en TikTok con Metricool.

- **Para cambiar el estilo**: edita `estilo.md` (o díselo a Claude).
- **Para añadir fondos**: sube fotos a la carpeta `fondos/` (Add file → Upload files).
- **Para pararlo**: desactiva la tarea programada "Carruseles 927 cada 3h" en Claude.
