#!/usr/bin/env python3
"""Vídeo 9:16 a partir del mismo guion.json que carrusel.py.

Uso:  python3 video.py guion.json salida/NOMBRE/video.mp4 [--sin-musica]

Cada diapositiva: la foto hace un zoom/paneo lento (efecto Ken Burns), el texto entra
deslizándose desde abajo, y entre diapositivas hay un corte rápido con flash suave.
El tiempo de cada diapositiva depende de cuántas palabras tiene (para que dé tiempo a leer).
La música es un ritmo sencillo generado aquí mismo (sin copyright).
"""
import math, os, random, re, subprocess, sys, tempfile, wave
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carrusel as C

FPS = 30
W, H = C.W, C.H


def duracion(s):
    palabras = sum(len(re.sub(r"\{\w+:|\}", "", l["t"]).split()) for l in s["lineas"])
    return min(max(1.2 + 0.20 * palabras, 1.8), 3.6)


def ease(t):
    return 1 - (1 - t) ** 3


def frame_fondo(bg, t, sentido):
    """Zoom lento 1.00 -> 1.08 con un pequeño paneo."""
    z = 1.0 + 0.08 * t
    w, h = W / z, H / z
    dx = (W - w) * (0.5 + 0.35 * sentido * (t - 0.5))
    dy = (H - h) * 0.5
    return bg.resize((W, H), Image.BILINEAR, box=(dx, dy, dx + w, dy + h))


def musica(ruta, segundos, bpm=96, sr=44100, semilla=0):
    rnd = random.Random(semilla)
    n = int(segundos * sr)
    t = np.arange(n) / sr
    out = np.zeros(n)
    beat = 60 / bpm
    # acordes suaves (pad) que cambian cada 2 compases
    progresiones = [[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 55, 59]]
    rnd.shuffle(progresiones)
    for k in range(int(segundos / (beat * 8)) + 1):
        notas = progresiones[k % 4]
        a, b = int(k * beat * 8 * sr), min(n, int((k + 1) * beat * 8 * sr))
        tt = t[a:b] - t[a]
        env = np.minimum(1, tt / 0.4) * np.minimum(1, (tt[-1] - tt + 1e-9) / 0.4) if b > a else 0
        for m in notas:
            f = 440 * 2 ** ((m - 69) / 12)
            out[a:b] += 0.05 * np.sin(2 * np.pi * f * tt) * env
        fb = 440 * 2 ** ((notas[0] - 12 - 69) / 12)
        out[a:b] += 0.08 * np.sin(2 * np.pi * fb * tt) * env
    # bombo en cada tiempo, charles en cada corchea, palmada en 2 y 4
    for i in range(int(segundos / beat * 2) + 1):
        a = int(i * beat / 2 * sr)
        if a >= n:
            break
        if i % 2 == 0:
            L = min(int(0.25 * sr), n - a); tt = np.arange(L) / sr
            out[a:a + L] += 0.5 * np.sin(2 * np.pi * (55 + 90 * np.exp(-tt * 25)) * tt) * np.exp(-tt * 9)
            if (i // 2) % 2 == 1:
                L2 = min(int(0.12 * sr), n - a); tt2 = np.arange(L2) / sr
                out[a:a + L2] += 0.18 * np.random.uniform(-1, 1, L2) * np.exp(-tt2 * 30)
        L = min(int(0.04 * sr), n - a); tt = np.arange(L) / sr
        out[a:a + L] += 0.06 * np.random.uniform(-1, 1, L) * np.exp(-tt * 90)
    fade = np.minimum(1, np.minimum(t / 0.5, (segundos - t) / 1.0))
    out = np.clip(out * fade, -1, 1)
    with wave.open(ruta, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((out * 32767 * 0.8).astype(np.int16).tobytes())


def render_video(guion, salida, con_musica=True):
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    capas = C.fondos_y_textos(guion, os.path.dirname(salida))
    durs = [duracion(s) for s in guion["slides"]]
    durs[-1] += 1.0  # el CTA se queda un poco más
    total = sum(durs)
    tmp = tempfile.mkdtemp()
    audio = os.path.join(tmp, "m.wav")
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    if con_musica:
        musica(audio, total + 0.5, semilla=hash(salida) % 1000)
        cmd += ["-i", audio, "-shortest", "-c:a", "aac", "-b:a", "128k"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", salida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i, ((bg, capa), d) in enumerate(zip(capas, durs)):
        nf = int(d * FPS)
        sentido = 1 if i % 2 == 0 else -1
        bgr = bg.convert("RGB")
        for f in range(nf):
            t = f / nf
            fr = frame_fondo(bgr, t, sentido).convert("RGBA")
            ts = f / FPS
            k = 1.0 if i == 0 else ease(min(1, max(0, (ts - 0.08) / 0.3)))
            if k > 0:
                c = capa if k >= 1 else Image.fromarray((np.asarray(capa).astype(np.float32) * [1, 1, 1, k]).astype(np.uint8))
                fr.alpha_composite(c, (0, int(60 * (1 - k))))
            if i > 0 and ts < 0.12:  # flash suave al cambiar
                fr = Image.blend(fr, Image.new("RGBA", (W, H), (255, 255, 255, 255)), 0.35 * (1 - ts / 0.12))
            p.stdin.write(fr.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    return salida, total


if __name__ == "__main__":
    import json
    g = json.load(open(sys.argv[1], encoding="utf-8"))
    out, seg = render_video(g, sys.argv[2], "--sin-musica" not in sys.argv)
    print(out, f"{seg:.1f}s")
    # tiempos de cada diapositiva (para revisar fotogramas)
    acc = 0
    for s_ in g["slides"]:
        d = duracion(s_); print(f"  {acc + d / 2:.1f}s"); acc += d
