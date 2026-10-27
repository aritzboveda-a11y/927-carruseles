"""Plantilla "pinterest" (27 oct 2026): el estilo de los carruseles virales del nicho (+10k likes).

Foto a color distinta en cada diapositiva, a pantalla completa, y texto blanco pequeño en el centro
con sombra suave, como el texto nativo de TikTok. Nada de etiquetas ni diseños recargados.

guion.json:
{
  "plantilla": "pinterest",
  "slides": [
    {"titulo": "3 errores de todo revendedor novato", "sub": "(el 3 es el peor)", "foto": "aritz927_32.jpg", "vinted": true},
    {"titulo": "1. subir 50 prendas el primer día", "texto": "Vinted lo ve raro. Empieza con 5-10.", "foto": "aritz927_05.jpg"},
    {"titulo": "zapatilla de marca", "precios": ["25€", "70€"], "foto": "aritz927_22.jpg"},      # compra (rojo) -> venta (verde)
    {"titulo": "te paso mis proveedores", "texto": "comenta “proveedores”", "foto": "aritz927_06.jpg", "guia": "pack"}
  ]
}
- "caja": true en una diapositiva pone el título en etiqueta blanca (texto nativo con fondo).
- Colores dentro del texto: {rojo:…} {verde:…} {amarillo:…} {azul:…}.
- Respeta la zona segura de TikTok (abajo el texto del post, a la derecha los botones).
"""
import os, re
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

import carrusel as C
import plantilla as P

AQUI = os.path.dirname(os.path.abspath(__file__))
F_TIT = os.path.join(AQUI, "fuentes", "Inter-Bold.otf")
F_TXT = os.path.join(AQUI, "fuentes", "Inter-SemiBold.otf")
COL = {"rojo": (255, 72, 72), "verde": (70, 225, 120), "amarillo": (255, 205, 60), "azul": (90, 170, 255), "blanco": (255, 255, 255)}
TOK = re.compile(r"\{(\w+):([^}]*)\}|([^{]+)")


def foto_color(ruta, W, H):
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    img = ImageOps.fit(img, (W, H), Image.LANCZOS, centering=(0.5, 0.45))
    img = ImageEnhance.Contrast(img).enhance(1.05)
    img = ImageEnhance.Color(img).enhance(1.05)
    # oscurecido suave general + viñeta: que el texto blanco se lea sin parecer un filtro
    img = Image.blend(img, Image.new("RGB", (W, H), (0, 0, 0)), 0.18)
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse((-W * 0.35, -H * 0.2, W * 1.35, H * 1.2), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(W // 4))
    return Image.composite(img, Image.blend(img, Image.new("RGB", (W, H), (0, 0, 0)), 0.55), m)


def banda(img, y0, y1):
    W, H = img.size
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rectangle((0, y0 - 60, W, y1 + 60), fill=95)
    m = m.filter(ImageFilter.GaussianBlur(90))
    return Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, m)


def _toks(t):
    """Palabras como listas de trozos [(texto, color)], para que “{verde:x}” no meta espacios."""
    palabras, act = [], []
    for m in TOK.finditer(t):
        col = COL.get(m.group(1), COL["blanco"]) if m.group(1) else COL["blanco"]
        txt = m.group(2) if m.group(1) else m.group(3)
        partes = re.split(r"(\s+)", txt)
        for p in partes:
            if not p:
                continue
            if p.isspace():
                if act:
                    palabras.append(act); act = []
            else:
                act.append((p, col))
    if act:
        palabras.append(act)
    return palabras


def _txt(palabra):
    return "".join(x for x, _ in palabra)


def _filas(texto, font, maxw):
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    filas, act = [], []
    for w in _toks(texto):
        prueba = " ".join(_txt(x) for x in act + [w])
        if act and P._ancho(prueba, font) > maxw:
            filas.append(act); act = [w]
        else:
            act.append(w)
    if act:
        filas.append(act)
    if len(filas) > 1 and len(filas[-1]) == 1 and len(filas[-2]) >= 3:
        filas[-1].insert(0, filas[-2].pop())
    return filas


def _bloque_alto(texto, tam, maxw):
    f = ImageFont.truetype(F_TIT, tam)
    return sum(len(_filas(t, f, maxw)) for t in texto.split("\n")) * int(tam * 1.22)


def dibujar(capa, texto, y, tam, fuente, maxw, caja=False):
    """Texto centrado blanco con sombra (o en etiqueta blanca si caja). Devuelve y final."""
    if "\n" in texto:
        for t in texto.split("\n"):
            y = dibujar(capa, t, y, tam, fuente, maxw, caja)
        return y
    W = capa.width
    font = ImageFont.truetype(fuente, tam)
    lh = int(tam * (1.3 if caja else 1.22))
    filas = _filas(texto, font, maxw)
    sombra = Image.new("RGBA", capa.size, (0, 0, 0, 0))
    ds = ImageDraw.Draw(sombra)
    d = ImageDraw.Draw(capa)
    pos = []
    for i, fila in enumerate(filas):
        linea = " ".join(_txt(w) for w in fila)
        a = P._ancho(linea, font)
        x, yy = (W - a) / 2, y + i * lh
        pos.append((x, yy, fila, a))
        if caja:
            pad = tam * 0.3
            d.rounded_rectangle((x - pad, yy - tam * 0.12, x + a + pad, yy + tam * 1.18), radius=int(tam * 0.22), fill=(255, 255, 255, 255))
        else:
            ds.text((x + 2, yy + 4), linea, font=font, fill=(0, 0, 0, 210))
    if not caja:
        capa.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(max(3, tam // 12))))
    esp = d.textlength(" ", font=font)
    for x, yy, fila, a in pos:
        for palabra in fila:
            for w, c in palabra:
                col = (20, 20, 20) if (caja and c == COL["blanco"]) else c
                if P.EMOJI_RE.search(w):
                    P._dibujar(capa, (x, yy), w, font, col)
                else:
                    d.text((x, yy), w, font=font, fill=col + (255,),
                           stroke_width=0 if caja else max(1, tam // 40), stroke_fill=(0, 0, 0, 120))
                x += P._ancho(w, font)
            x += esp
    return y + len(filas) * lh


def fondos_y_textos(guion, carpeta, rnd):
    P.C = C
    W, H = C.W, C.H
    tiktok = H > 1500
    e = C.FORMATO["escala"]
    maxw = int(W * (0.74 if tiktok else 0.8))
    y_min = int(H * (0.17 if tiktok else 0.10))
    y_max = int(H * (0.66 if tiktok else 0.90))
    out = []
    for i, s in enumerate(guion["slides"]):
        ruta = os.path.join(AQUI, "fondos", s["foto"])
        bg = foto_color(ruta, W, H)
        capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        t_tit = int((70 if i == 0 else 60) * e)
        t_txt = int(46 * e)
        # alto del bloque para centrarlo
        alto = _bloque_alto(s["titulo"], t_tit, maxw)
        if s.get("sub"):
            alto += int(18 * e) + _bloque_alto(s["sub"], int(40 * e), maxw)
        if s.get("texto"):
            alto += int(26 * e) + _bloque_alto(s["texto"], t_txt, maxw)
        if s.get("precios"):
            alto += int(30 * e) + int(80 * e)
        extra = 0
        if i == 0 and s.get("vinted"):
            extra = int(260 * e)
        if s.get("guia"):
            extra = 600 if tiktok else 430
        centro = H * (0.40 if tiktok else 0.46)
        y = int(max(y_min, min(centro - (alto + extra) / 2, y_max - alto - extra)))
        y0 = y
        y = dibujar(capa, s["titulo"], y, t_tit, F_TIT, maxw, caja=s.get("caja", False))
        if s.get("sub"):
            y = dibujar(capa, s["sub"], y + int(18 * e), int(40 * e), F_TXT, maxw)
        if s.get("texto"):
            y = dibujar(capa, s["texto"], y + int(26 * e), t_txt, F_TXT, maxw)
        if s.get("precios"):
            compra, venta = s["precios"]
            y = dibujar(capa, "{rojo:" + compra + "} → {verde:" + venta + "}", y + int(30 * e), int(72 * e), F_TIT, maxw)
        if i == 0 and s.get("vinted"):
            P.placa_vinted(capa, y + int(50 * e), int(250 * e))
            y += int(250 * e)
        if s.get("guia"):
            C.tarjeta_guia(capa, s["guia"], y + int(30 * e))
            y += extra
        out.append((banda(bg, y0, y), capa))
    return out
