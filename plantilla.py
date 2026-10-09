"""Plantilla de Aritz (oct 2026): fondo fijo en blanco y negro + etiquetas celestes + foto distinta en cada paso.

Se activa poniendo "plantilla": "aritz" en guion.json:
{
  "plantilla": "aritz",
  "fondo": "auto",                 # foto de fondo de TODAS las diapositivas (nombre en fondos/ o "auto")
  "tema_fondo": "coche_lujo",      # si fondo es "auto", de qué tema se elige
  "slides": [
    {"titulo": "cómo pasar de 0 a vender todos los días", "sub": "espera hasta el final", "vinted": true},   # portada: problema + gancho + Vinted
    {"titulo": "1. consigue buenos proveedores", "guia": "pack", "abajo": "link en mi bio 🔥"},          # paso con portada de guía
    {"titulo": "2. haz pedido y espera a que te llegue", "tema_foto": "cajas"},                          # paso con foto (por tema)
    {"titulo": "3. haz buenas fotos y súbelas", "foto": "aritz927_17.jpg"},                              # paso con foto concreta
    {"titulo": "4. disfruta de las ventas 📈💰", "tema_foto": "ventas"},
    {"titulo": "comenta “proveedor” y te mando el acceso", "tema_foto": "lujo"}                          # CTA
  ]
}
Los emojis se dibujan en color (Noto Color Emoji).
"""
import os, re
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

import carrusel as C

CELESTE = (209, 243, 251)
TINTA = (10, 61, 78)
TEAL = (4, 73, 90)
EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
RECURSOS = os.path.join(C.AQUI, "recursos")
EMOJI_RE = re.compile("([\U0001F000-\U0001FAFF☀-➿⬀-⯿️‍]+)")


def _esc():
    return C.FORMATO["escala"]


def fondo_bn(ruta):
    """Foto en blanco y negro cálido, con contraste y grano (como la referencia)."""
    W, H = C.W, C.H
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    img = ImageOps.fit(img, (W, H), Image.LANCZOS)
    g = ImageOps.grayscale(img)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.15)
    img = ImageOps.colorize(g, (16, 16, 16), (232, 230, 226))
    ruido = Image.effect_noise((W, H), 40).convert("RGB")
    return Image.blend(img, ruido, 0.07)


# ---------- texto con emojis ----------
_emoji_cache = {}


def _emoji(ch, alto):
    k = (ch, alto)
    if k not in _emoji_cache:
        try:
            f = ImageFont.truetype(EMOJI_FONT, 109)
            im = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((8, 8), ch, font=f, embedded_color=True)
            bb = im.getbbox()
            im = im.crop(bb) if bb else im
            r = alto / max(1, im.height)
            _emoji_cache[k] = im.resize((max(1, int(im.width * r)), alto), Image.LANCZOS)
        except Exception:
            _emoji_cache[k] = None
    return _emoji_cache[k]


def _trozos(texto):
    return [(t, bool(EMOJI_RE.fullmatch(t))) for t in EMOJI_RE.split(texto) if t]


def _ancho(texto, font):
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    a = 0
    for t, es_emoji in _trozos(texto):
        if es_emoji:
            for ch in [c for c in t if c not in "️‍"]:
                e = _emoji(ch, int(font.size * 0.95))
                a += (e.width if e else 0) + font.size * 0.08
        else:
            a += d.textlength(t, font=font)
    return a


def _dibujar(capa, xy, texto, font, col):
    d = ImageDraw.Draw(capa)
    x, y = xy
    for t, es_emoji in _trozos(texto):
        if es_emoji:
            for ch in [c for c in t if c not in "️‍"]:
                e = _emoji(ch, int(font.size * 0.95))
                if e:
                    capa.alpha_composite(e, (int(x), int(y + font.size * 0.22)))
                    x += e.width + font.size * 0.08
        else:
            d.text((x, y), t, font=font, fill=col + (255,))
            x += d.textlength(t, font=font)


def _lineas(texto, font, max_ancho):
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if actual and _ancho(prueba, font) > max_ancho:
            lineas.append(actual)
            actual = p
        else:
            actual = prueba
    if actual:
        lineas.append(actual)
    if len(lineas) > 1 and len(lineas[-1].split()) == 1 and len(lineas[-2].split()) >= 3:
        a = lineas[-2].split()
        nueva = a[-1] + " " + lineas[-1]
        if _ancho(nueva, font) <= max_ancho:
            lineas[-2], lineas[-1] = " ".join(a[:-1]), nueva
    return lineas


def etiqueta(capa, texto, y, tam, fondo=CELESTE, tinta=TINTA, max_ancho=None):
    """Texto centrado con una etiqueta por línea (estilo texto de Instagram/TikTok). Devuelve la y final."""
    W = C.W
    font = ImageFont.truetype(C.F_BOLD, tam)
    max_ancho = max_ancho or int(W * 0.72)
    lineas = _lineas(texto, font, max_ancho)
    lh = int(tam * 1.13)
    pad_x, pad_y = int(tam * 0.32), int(tam * 0.16)
    d = ImageDraw.Draw(capa)
    # primero todas las cajas (se funden entre sí), luego el texto
    cajas = []
    for i, ln in enumerate(lineas):
        a = _ancho(ln, font)
        x = (W - a) / 2
        top = y + i * lh
        cajas.append((x, top, a, ln))
        d.rounded_rectangle((x - pad_x, top - pad_y, x + a + pad_x, top + lh + pad_y * 0.6),
                            radius=int(tam * 0.22), fill=fondo + (255,))
    for x, top, a, ln in cajas:
        _dibujar(capa, (x, top - tam * 0.08), ln, font, tinta)
    return y + len(lineas) * lh + pad_y


def insertar(capa, img, caja, radio=26):
    """Pega una foto (o portada de guía) centrada dentro de caja=(x0,y0,x1,y1), con esquinas redondeadas."""
    x0, y0, x1, y1 = caja
    mw, mh = int(x1 - x0), int(y1 - y0)
    img = ImageOps.exif_transpose(img).convert("RGBA")
    r = min(mw / img.width, mh / img.height)
    # fotos muy anchas: recortar a vertical para que no quede una tira
    if img.width / img.height > 0.85:
        img = ImageOps.fit(img, (int(img.height * 0.75), img.height), Image.LANCZOS)
        r = min(mw / img.width, mh / img.height)
    img = img.resize((max(1, int(img.width * r)), max(1, int(img.height * r))), Image.LANCZOS)
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius=radio, fill=255)
    img.putalpha(m)
    sombra = Image.new("RGBA", (img.width + 80, img.height + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle((40, 50, img.width + 40, img.height + 50), radius=radio, fill=(0, 0, 0, 150))
    sombra = sombra.filter(ImageFilter.GaussianBlur(20))
    px, py = int((C.W - img.width) / 2), int(y0 + (mh - img.height) / 2)
    capa.alpha_composite(sombra, (px - 40, py - 40))
    capa.alpha_composite(img, (px, py))
    return py + img.height


def placa_vinted(capa, y, ancho):
    """Placa de Vinted de la portada: usa recursos/vinted.png si existe; si no, una placa con el nombre."""
    ruta = os.path.join(RECURSOS, "vinted.png")
    if os.path.exists(ruta):
        return insertar(capa, Image.open(ruta), (0, y, C.W, y + ancho * 0.66), radio=22)
    alto = int(ancho * 0.62)
    x = int((C.W - ancho) / 2)
    d = ImageDraw.Draw(capa)
    d.rounded_rectangle((x, y, x + ancho, y + alto), radius=24, fill=TEAL + (255,))
    f = ImageFont.truetype(C.F_BOLD, int(alto * 0.42))
    tw = d.textlength("Vinted", font=f)
    d.text((C.W / 2 - tw / 2, y + alto / 2 - f.size * 0.62), "Vinted", font=f, fill=(255, 255, 255, 255))
    return y + alto


def fondos_y_textos(guion, carpeta, rnd):
    W, H, e = C.W, C.H, _esc()
    alto_fmt = H / 1920
    slides = guion["slides"]
    todas = C.fotos_disponibles()
    # 1 foto de fondo para todo el carrusel
    pedido = [{"fondo": guion.get("fondo", "auto"), "tema_fondo": guion.get("tema_fondo", "fondo_gris")}]
    fondo = C.elegir_fotos(pedido, rnd)[0]
    bg = fondo_bn(os.path.join(C.AQUI, "fondos", fondo)) if fondo else C.fondo_generado(carpeta)
    # 1 foto distinta por paso (sin repetir el fondo)
    peticiones = [{"fondo": s.get("foto", "auto"), "tema_fondo": s.get("tema_foto", "")} for s in slides]
    fotos = C.elegir_fotos(peticiones, rnd)
    usadas = {fondo}
    for i, f in enumerate(fotos):
        if f in usadas and len(todas) > len(slides) + 1:
            libres = [x for x in todas if x not in usadas]
            fotos[i] = rnd.choice(libres)
        usadas.add(fotos[i])

    out = []
    for i, s in enumerate(slides):
        capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        portada = i == 0 and (s.get("vinted") or s.get("sub"))
        # zona segura de TikTok: arriba las pestañas, abajo el texto del post, a la derecha los botones
        tiktok = H > 1500
        limite = H * (0.72 if tiktok else 0.92)
        y = int((330 if portada else 290) * alto_fmt) if tiktok else int(110)
        y = etiqueta(capa, s["titulo"], y, int((80 if portada else 84) * e))
        if s.get("sub"):
            y = etiqueta(capa, s["sub"], y + int(28 * e), int(44 * e), fondo=TEAL, tinta=(235, 250, 255))
        fin = limite
        if s.get("abajo"):
            ta = int(64 * e)
            n = len(_lineas(s["abajo"], ImageFont.truetype(C.F_BOLD, ta), int(W * 0.72)))
            ya = int(limite - n * ta * 1.13 - ta * 0.16)
            etiqueta(capa, s["abajo"], ya, ta)
            fin = ya - int(40 * e)
        if portada:
            if s.get("vinted", True):
                ancho = int(500 * e)
                alto_placa = int(ancho * 0.66)
                yv = min(max(y + int(120 * e), int(H * 0.42)), int(fin - alto_placa))
                placa_vinted(capa, yv, ancho)
        else:
            caja = (W * 0.2, y + int(40 * e), W * 0.8, fin)
            img = None
            if s.get("guia") and os.path.exists(os.path.join(C.GUIAS, f"guia927_{s['guia']}.png")):
                img = Image.open(os.path.join(C.GUIAS, f"guia927_{s['guia']}.png"))
            elif fotos[i]:
                img = Image.open(os.path.join(C.AQUI, "fondos", fotos[i]))
            if img is not None:
                insertar(capa, img, caja)
        out.append((bg, capa))
    return out
