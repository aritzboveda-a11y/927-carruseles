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
Tamaños: xxl (portada impactante, pocas palabras), xl (portada), l (título de paso), m (texto normal), s (texto pequeño / aviso)
Fondo por tema: "tema_fondo": coche | portatil | cajas | paquetes | zapatillas | ropa | almacen | perfume (ver fondos/etiquetas.json)
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
TAMS_BASE = {"xxl": 118, "xl": 96, "l": 80, "m": 62, "s": 52}
TAMS = dict(TAMS_BASE)
MAX_ANCHO = 930
# Zonas seguras: en TikTok abajo (texto del post) y a la derecha (botones) no debe haber texto.
FORMATOS = {
    "tiktok": {"W": 1080, "H": 1920, "centro": (0.36, 0.44), "ancho": 900, "escala": 1.0, "ymin": 240, "ymax": 0.70},
    "instagram": {"W": 1080, "H": 1350, "centro": (0.47, 0.50), "ancho": 880, "escala": 0.86, "ymin": 150, "ymax": 0.85},
}
FORMATO = FORMATOS["tiktok"]


def set_formato(nombre):
    global W, H, MAX_ANCHO, TAMS, FORMATO
    FORMATO = FORMATOS[nombre]
    W, H, MAX_ANCHO = FORMATO["W"], FORMATO["H"], FORMATO["ancho"]
    TAMS = {k: int(v * FORMATO["escala"]) for k, v in TAMS_BASE.items()}


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
    # evitar una palabra sola en la última línea: bajar una palabra de la línea anterior
    if len(lineas) > 1 and len(lineas[-1][0]) == 1 and len(lineas[-2][0]) >= 3:
        def ancho_de(gs):
            return sum(sum(draw.textlength(w, font=font) for w, _ in g) for g in gs) + esp * (len(gs) - 1)
        prev, ult = lineas[-2][0], lineas[-1][0]
        nuevo_ult = [prev[-1]] + ult
        if ancho_de(nuevo_ult) <= MAX_ANCHO:
            lineas[-2] = (prev[:-1], ancho_de(prev[:-1]))
            lineas[-1] = (nuevo_ult, ancho_de(nuevo_ult))
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


def fondo_foto(ruta, rnd=None):
    """Foto de fondo. Con rnd, cada uso sale distinto (zoom, encuadre, espejo, giro, tono)
    para que una foto repetida nunca sea idéntica a la anterior."""
    rnd = rnd or random.Random()
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    ang = rnd.uniform(-2.5, 2.5)
    img = img.rotate(ang, resample=Image.BICUBIC, expand=False)
    zoom = rnd.uniform(1.08, 1.4)
    cx, cy = rnd.uniform(0.3, 0.7), rnd.uniform(0.3, 0.7)
    img = ImageOps.fit(img, (int(W * zoom), int(H * zoom)), Image.LANCZOS, centering=(cx, cy))
    ox = rnd.randint(0, img.width - W); oy = rnd.randint(0, img.height - H)
    img = img.crop((ox, oy, ox + W, oy + H))
    from PIL import ImageEnhance
    img = ImageEnhance.Color(img).enhance(rnd.uniform(0.75, 1.25))
    img = ImageEnhance.Contrast(img).enhance(rnd.uniform(0.9, 1.15))
    tinte = rnd.choice([(255, 170, 90), (90, 150, 255), (255, 255, 255), (120, 255, 200), (255, 120, 200)])
    img = Image.blend(img, Image.new("RGB", (W, H), tinte), rnd.uniform(0.0, 0.08))
    oscuro = Image.new("RGB", (W, H), (0, 0, 0))
    img = Image.blend(img, oscuro, rnd.uniform(0.18, 0.30))
    viñeta = Image.new("L", (W, H), 0)
    ImageDraw.Draw(viñeta).ellipse((-300, -200, W + 300, H + 200), fill=255)
    viñeta = viñeta.filter(ImageFilter.GaussianBlur(250))
    return Image.composite(img, oscuro, viñeta)


def fotos_disponibles():
    d = os.path.join(AQUI, "fondos")
    if not os.path.isdir(d):
        return []
    return sorted(f for f in os.listdir(d) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))


USO = os.path.join(AQUI, "fondos_uso.json")
ETIQ = os.path.join(AQUI, "fondos", "etiquetas.json")


def _cargar(ruta, defecto):
    try:
        return json.load(open(ruta, encoding="utf-8"))
    except Exception:
        return defecto


def elegir_fotos(slides, rnd):
    """Una foto por diapositiva: del tema pedido (tema_fondo) si hay, y siempre las menos usadas primero."""
    todas = fotos_disponibles()
    if not todas:
        return [None] * len(slides)
    uso = _cargar(USO, {})
    etiq = _cargar(ETIQ, {})
    elegidas, usadas_aqui = [], set()
    for s in slides:
        if s.get("fondo", "auto") != "auto":
            elegidas.append(s["fondo"]); continue
        pool = [f for f in etiq.get(s.get("tema_fondo", ""), []) if f in todas] or todas
        cand = [f for f in pool if f not in usadas_aqui] or pool
        rnd.shuffle(cand)
        cand.sort(key=lambda f: uso.get(f, 0))
        f = cand[0]
        elegidas.append(f); usadas_aqui.add(f)
        uso[f] = uso.get(f, 0) + 1
    json.dump(uso, open(USO, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return elegidas


def _contraste(rgb):
    return (0, 0, 0) if (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) > 150 else (255, 255, 255)


def chip(capa, texto, xy, tam=40, fondo=(255, 255, 255), alpha=235, anclaje="la"):
    """Etiqueta redondeada pequeña (contador 2/6, 'desliza ->')."""
    d = ImageDraw.Draw(capa)
    f = ImageFont.truetype(F_BOLD, tam)
    x0, y0, x1, y1 = d.textbbox((0, 0), texto, font=f)
    w, h = x1 - x0 + 44, y1 - y0 + 26
    x, y = xy
    if anclaje == "ra":
        x -= w
    elif anclaje == "ma":
        x -= w / 2
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=fondo + (alpha,))
    d.text((x + 22 - x0, y + 13 - y0), texto, font=f, fill=_contraste(fondo) + (255,))


def capa_texto(s, centro, idx=0, total=1):
    """Devuelve (capa RGBA con el texto, caja (y0, y1) que ocupa).
    Opciones por línea: "caja": "<color>" dibuja una etiqueta de color detrás (estilo texto nativo de TikTok)."""
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(capa)
    bloques = []
    for ln in s["lineas"]:
        tam = TAMS.get(ln.get("tam", "m"), TAMS["m"])
        font = ImageFont.truetype(F_BOLD, tam)
        col = COLORES.get(ln.get("color", "blanco"), COLORES["blanco"])
        caja = COLORES.get(ln.get("caja")) if ln.get("caja") else None
        if caja:
            col = _contraste(caja)
        filas = envolver(tokens(ln["t"], col), font, draw)
        lh = int(tam * (1.38 if caja else 1.2))
        bloques.append((font, filas, lh, int(tam * 0.5), caja))
    alto = sum(len(f) * lh + gap for _, f, lh, gap, _ in bloques)
    marca = s.get("marca")
    fm = ImageFont.truetype(F_BOLD, int(190 * FORMATO["escala"])) if marca else None
    alto_total = alto + (int(260 * FORMATO["escala"]) if marca else 0)
    y = max(int(H * centro - alto_total / 2), FORMATO["ymin"])
    y0 = y
    for font, filas, lh, gap, caja in bloques:
        esp = draw.textlength(" ", font=font)
        for grupos, ancho in filas:
            x = (W - ancho) / 2
            if caja:
                pad = font.size * 0.28
                draw.rounded_rectangle((x - pad, y - pad * 0.35, x + ancho + pad, y + font.size * 1.18),
                                       radius=int(font.size * 0.22), fill=caja + (255,))
            for grupo in grupos:
                for w, c in grupo:
                    if caja:
                        draw.text((x, y), w, font=font, fill=c + (255,))
                    else:
                        texto_con_sombra(capa, (x, y), w, font, c)
                    x += draw.textlength(w, font=font)
                x += esp
            y += lh
        y += gap
    if marca:
        mw = draw.textlength(marca, font=fm)
        texto_con_sombra(capa, ((W - mw) / 2, y + 20), marca, fm, COLORES["turquesa"])
        y += int(260 * FORMATO["escala"])
    # señales para que deslicen: contador en las intermedias y "desliza" en la portada
    if total > 1 and 0 < idx < total - 1:
        chip(capa, f"{idx}/{total - 2}", (W / 2, FORMATO["ymin"] - 110), tam=34, anclaje="ma", fondo=(20, 20, 20), alpha=170)
    if total > 1 and idx == 0 and s.get("desliza", True):
        chip(capa, s.get("texto_desliza", "desliza  >>"), (W / 2, min(y + 40, H * FORMATO["ymax"])), tam=38, anclaje="ma")
    return capa, (y0, y)


def banda_oscura(base, caja):
    """Oscurece suavemente la zona del texto para que se lea sobre cualquier foto."""
    y0, y1 = caja
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rectangle((0, y0 - 120, W, y1 + 120), fill=150)
    m = m.filter(ImageFilter.GaussianBlur(110))
    return Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), base, m)


def fondos_y_textos(guion, carpeta):
    """Para cada diapositiva: (fondo RGB sin texto, capa de texto RGBA)."""
    rnd = random.Random()
    fotos = elegir_fotos(guion["slides"], rnd)
    centro = rnd.uniform(*FORMATO["centro"])
    out = []
    n = len(guion["slides"])
    for i, s in enumerate(guion["slides"]):
        f = fotos[i]
        bg = fondo_foto(os.path.join(AQUI, "fondos", f), rnd) if f else fondo_generado(carpeta)
        capa, caja = capa_texto(s, centro, i, n)
        out.append((banda_oscura(bg, caja), capa))
    return out


def render(guion, carpeta, formato="tiktok"):
    set_formato(formato)
    os.makedirs(carpeta, exist_ok=True)
    rutas = []
    for i, (bg, capa) in enumerate(fondos_y_textos(guion, carpeta)):
        base = bg.convert("RGBA")
        base.alpha_composite(capa)
        ruta = os.path.join(carpeta, f"{i + 1:02d}.jpg")
        base.convert("RGB").save(ruta, quality=88)
        rutas.append(ruta)
    return rutas


if __name__ == "__main__":
    # python3 carrusel.py guion.json salida/X            -> salida/X/01.jpg ... (TikTok 9:16)
    #                                                     + salida/X/ig/01.jpg ... (Instagram 4:5)
    guion = json.load(open(sys.argv[1], encoding="utf-8"))
    for r in render(guion, sys.argv[2], "tiktok"):
        print(r)
    if "--sin-ig" not in sys.argv:
        for r in render(guion, os.path.join(sys.argv[2], "ig"), "instagram"):
            print(r)
