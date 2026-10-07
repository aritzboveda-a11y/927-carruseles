#!/usr/bin/env python3
"""Generador de carruseles 927studios (estilo Aritz + referencia "PROVEEDORES EN BIO").

Uso:  python3 carrusel.py guion.json salida/NOMBRE
Crea salida/NOMBRE/01.jpg, 02.jpg ... (1080x1920, formato foto de TikTok).

guion.json:
{
  "slides": [
    {"lineas": [
        {"t": "Así puedes {amarillo:empezar}", "tam": "xl"},
        {"t": "en la reventa con 50€", "tam": "xl"},
        {"t": "quédate hasta el final ➡", "tam": "s", "color": "azul"}
     ],
     "marca": "VINTED",          # opcional: palabra grande en turquesa debajo del texto
     "fondo": "auto"             # opcional: nombre de archivo en fondos/ o "auto"
    }
  ]
}
Resaltar palabras: {amarillo:texto} {azul:texto} {rojo:texto} {verde:texto} {rosa:texto} {turquesa:texto}
Tamaños: xl (portada), l (título de paso), m (texto normal), s (texto pequeño / aviso)
"""
import json, os, random, re, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
F_BOLD = os.path.join(AQUI, "fuentes", "Poppins-BoldItalic.ttf")
F_MED = os.path.join(AQUI, "fuentes", "Poppins-MediumItalic.ttf")
COLORES = {
    "blanco": (255, 255, 255), "amarillo": (255, 196, 46), "azul": (40, 150, 255),
    "rojo": (255, 45, 60), "verde": (60, 220, 110), "rosa": (255, 60, 190),
    "turquesa": (0, 170, 175),
}
TAMS = {"xl": 84, "l": 76, "m": 64, "s": 50}
MAX_ANCHO = 930


def tokens(texto, color_base):
    """Divide '{amarillo:hola} mundo' en [(palabra, color), ...]."""
    out = []
    for m in re.finditer(r"\{(\w+):([^}]*)\}|([^{]+)", texto):
        if m.group(1):
            col = COLORES.get(m.group(1), color_base)
            frag = m.group(2)
        else:
            col, frag = color_base, m.group(3)
        for i, w in enumerate(re.split(r"(\s+)", frag)):
            if w and not w.isspace():
                out.append([w, col, False])
            elif w:
                out.append([" ", col, True])
    return out


def envolver(toks, font, draw):
    lineas, actual, ancho = [], [], 0
    esp = draw.textlength(" ", font=font)
    palabras = []
    pegar = False
    for w, c, es_esp in toks:
        if es_esp:
            pegar = False
            continue
        if pegar and palabras:
            palabras[-1].append((w, c))
        else:
            palabras.append([(w, c)])
        pegar = True
    for grupo in palabras:
        gw = sum(draw.textlength(w, font=font) for w, _ in grupo)
        if actual and ancho + esp + gw > MAX_ANCHO:
            lineas.append((actual, ancho))
            actual, ancho = [], 0
        if actual:
            ancho += esp
        actual.append(grupo)
        ancho += gw
    if actual:
        lineas.append((actual, ancho))
    return lineas


def texto_con_sombra(base, xy, w, font, col):
    sombra = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(sombra)
    d.text((xy[0] + 3, xy[1] + 5), w, font=font, fill=(0, 0, 0, 200))
    sombra = sombra.filter(ImageFilter.GaussianBlur(6))
    base.alpha_composite(sombra)
    d = ImageDraw.Draw(base)
    d.text(xy, w, font=font, fill=col + (255,), stroke_width=2, stroke_fill=(0, 0, 0, 160))


def fondo_generado(semilla):
    rnd = random.Random(semilla)
    paletas = [((8, 10, 20), (30, 40, 80)), ((10, 10, 12), (45, 45, 55)),
               ((5, 20, 25), (0, 90, 95)), ((15, 8, 25), (70, 30, 110)),
               ((20, 10, 8), (110, 50, 20))]
    a, b = rnd.choice(paletas)
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / H
        col = tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))
        for x in range(W):
            px[x, y] = col
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    cx, cy = rnd.randint(200, 880), rnd.randint(500, 1400)
    gd.ellipse((cx - 600, cy - 600, cx + 600, cy + 600), fill=110)
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    img = Image.composite(Image.new("RGB", (W, H), tuple(min(255, c + 60) for c in b)), img, glow)
    ruido = Image.effect_noise((W, H), 28).convert("RGB")
    return Image.blend(img, ruido, 0.06)


def fondo_foto(ruta):
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    img = ImageOps.fit(img, (W, H), Image.LANCZOS)
    oscuro = Image.new("RGB", (W, H), (0, 0, 0))
    img = Image.blend(img, oscuro, 0.38)
    viñeta = Image.new("L", (W, H), 0)
    ImageDraw.Draw(viñeta).ellipse((-300, -200, W + 300, H + 200), fill=255)
    viñeta = viñeta.filter(ImageFilter.GaussianBlur(250))
    return Image.composite(img, oscuro, viñeta)


def fotos_disponibles():
    d = os.path.join(AQUI, "fondos")
    if not os.path.isdir(d):
        return []
    return sorted(f for f in os.listdir(d) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))


def render(guion, carpeta):
    os.makedirs(carpeta, exist_ok=True)
    fotos = fotos_disponibles()
    rnd = random.Random(carpeta)
    rnd.shuffle(fotos)
    rutas = []
    for i, s in enumerate(guion["slides"]):
        f = s.get("fondo", "auto")
        if f != "auto" and os.path.exists(os.path.join(AQUI, "fondos", f)):
            bg = fondo_foto(os.path.join(AQUI, "fondos", f))
        elif fotos:
            bg = fondo_foto(os.path.join(AQUI, "fondos", fotos[i % len(fotos)]))
        else:
            bg = fondo_generado(carpeta)
        base = bg.convert("RGBA")
        draw = ImageDraw.Draw(base)
        bloques = []
        for ln in s["lineas"]:
            tam = TAMS.get(ln.get("tam", "m"), 64)
            font = ImageFont.truetype(F_BOLD if tam >= 60 else F_BOLD, tam)
            col = COLORES.get(ln.get("color", "blanco"), COLORES["blanco"])
            filas = envolver(tokens(ln["t"], col), font, draw)
            bloques.append((font, filas, int(tam * 1.22), int(tam * 0.55)))
        alto = sum(len(f) * lh + gap for _, f, lh, gap in bloques)
        marca = s.get("marca")
        fm = ImageFont.truetype(F_BOLD, 190) if marca else None
        alto_total = alto + (260 if marca else 0)
        y = int(H * 0.40 - alto_total / 2)
        y = max(y, 260)
        esp_cache = {}
        for font, filas, lh, gap in bloques:
            esp = esp_cache.setdefault(font.size, draw.textlength(" ", font=font))
            for grupos, ancho in filas:
                x = (W - ancho) / 2
                for grupo in grupos:
                    for w, c in grupo:
                        texto_con_sombra(base, (x, y), w, font, c)
                        x += draw.textlength(w, font=font)
                    x += esp
                y += lh
            y += gap
        if marca:
            mw = draw.textlength(marca, font=fm)
            texto_con_sombra(base, ((W - mw) / 2, y + 20), marca, fm, COLORES["turquesa"])
        ruta = os.path.join(carpeta, f"{i + 1:02d}.jpg")
        base.convert("RGB").save(ruta, quality=88)
        rutas.append(ruta)
    return rutas


if __name__ == "__main__":
    guion = json.load(open(sys.argv[1], encoding="utf-8"))
    for r in render(guion, sys.argv[2]):
        print(r)
