#!/usr/bin/env python3
"""Biblioteca de estilos de carrusel.

Uso (la biblioteca por defecto es carruseles/estilos; cámbiala con --bib):
  estilos.py guardar <carpeta_proyecto> <nombre> [--html carrusel.html] [--build build.py] [--nota "..."]
  estilos.py rendimiento <nombre> --alcance N [--guardados N --compartidos N --comentarios N
                         --palabra N --seguidores N --leads N --link URL --fecha AAAA-MM-DD]
  estilos.py ranking [--objetivo seguidores|autoridad|leads|venta]
  estilos.py listar
  estilos.py ver <nombre>
  estilos.py catalogo [salida.png]      # portada + 2 slides de cada estilo, con su nombre, para elegir
"""
import argparse, glob, json, os, re, shutil, sys, unicodedata
from datetime import date

# Métrica principal por objetivo: lo que de verdad mueve ese objetivo, por cada 1.000 de alcance.
METRICA = {
    "seguidores": ("seguidores", "seguidores ganados"),
    "autoridad": ("guardados", "guardados"),
    "leads": ("palabra", "comentarios con la palabra clave"),
    "venta": ("leads", "leads o ventas"),
}
CAMPOS = ["alcance", "guardados", "compartidos", "comentarios", "palabra", "seguidores", "leads"]


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def cargar(bib, nombre):
    p = os.path.join(bib, slug(nombre), "estilo.json")
    if not os.path.exists(p):
        sys.exit(f"No existe el estilo '{nombre}'. Usa: estilos.py listar")
    return p, json.load(open(p, encoding="utf-8"))


def guardar(a):
    src = a.proyecto
    html = os.path.join(src, a.html)
    if not os.path.exists(html):
        sys.exit(f"No encuentro {html}. Pasa --html con el HTML del carrusel.")
    dst = os.path.join(a.bib, slug(a.nombre))
    if os.path.exists(dst) and not a.reemplazar:
        sys.exit(f"Ya existe el estilo '{slug(a.nombre)}'. Usa otro nombre o --reemplazar.")
    os.makedirs(dst, exist_ok=True)
    shutil.copy(html, os.path.join(dst, "plantilla.html"))
    if a.build and os.path.exists(os.path.join(src, a.build)):
        shutil.copy(os.path.join(src, a.build), os.path.join(dst, "build.py"))
    # Recursos que usa la plantilla (fotos, fuentes locales) para que renderice sola.
    for f in os.listdir(src):
        p = os.path.join(src, f)
        if os.path.isfile(p) and f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".svg", ".woff", ".woff2", ".ttf")) and f != "comparacion.png" and not f.startswith("comparacion"):
            shutil.copy(p, dst)
    if os.path.isdir(os.path.join(src, "fonts")):
        shutil.copytree(os.path.join(src, "fonts"), os.path.join(dst, "fonts"), dirs_exist_ok=True)
    finales = sorted(glob.glob(os.path.join(src, a.final, "slide_*.png")))
    if finales:
        os.makedirs(os.path.join(dst, "muestras"), exist_ok=True)
        for f in finales:
            shutil.copy(f, os.path.join(dst, "muestras"))
    adn = {}
    if os.path.exists(os.path.join(src, "adn.json")):
        adn = json.load(open(os.path.join(src, "adn.json"), encoding="utf-8"))
    prev = {}
    if os.path.exists(os.path.join(dst, "estilo.json")):
        prev = json.load(open(os.path.join(dst, "estilo.json"), encoding="utf-8"))
    estilo = {
        "nombre": a.nombre,
        "id": slug(a.nombre),
        "creado": prev.get("creado", date.today().isoformat()),
        "fuente_modelo": adn.get("fuente", ""),
        "proyecto_origen": os.path.abspath(src),
        "slides": len(finales) or adn.get("slides"),
        "nota": a.nota or prev.get("nota", ""),
        "adn": adn,
        "rendimiento": prev.get("rendimiento", []),
    }
    json.dump(estilo, open(os.path.join(dst, "estilo.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Guardado: {dst} ({estilo['slides']} slides)")


def rendimiento(a):
    p, e = cargar(a.bib, a.nombre)
    reg = {"fecha": a.fecha or date.today().isoformat(), "link": a.link or ""}
    for c in CAMPOS:
        v = getattr(a, c)
        if v is not None:
            reg[c] = v
    e.setdefault("rendimiento", []).append(reg)
    json.dump(e, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Rendimiento registrado en '{e['nombre']}' ({len(e['rendimiento'])} publicación/es).")


def tasas(e):
    """Suma todas las publicaciones del estilo y devuelve tasas por cada 1.000 de alcance."""
    tot = {c: 0 for c in CAMPOS}
    tiene = {c: False for c in CAMPOS}
    for r in e.get("rendimiento", []):
        for c in CAMPOS:
            if c in r:
                tot[c] += r[c]; tiene[c] = True
    if not tot["alcance"]:
        return None
    return {c: round(tot[c] * 1000 / tot["alcance"], 1) for c in CAMPOS if c != "alcance" and tiene[c]} | {"alcance": tot["alcance"], "publicaciones": len(e["rendimiento"])}


def todos(bib):
    out = []
    for p in sorted(glob.glob(os.path.join(bib, "*", "estilo.json"))):
        out.append(json.load(open(p, encoding="utf-8")))
    return out


def ranking(a):
    clave, etiqueta = METRICA[a.objetivo]
    filas = []
    for e in todos(a.bib):
        t = tasas(e)
        filas.append((t.get(clave) if t else None, e, t))
    if not filas:
        sys.exit("La biblioteca está vacía.")
    filas.sort(key=lambda x: (x[0] is None, -(x[0] or 0)))
    print(f"Ranking por objetivo '{a.objetivo}': {etiqueta} por cada 1.000 de alcance\n")
    for i, (v, e, t) in enumerate(filas, 1):
        if t is None:
            print(f"{i}. {e['nombre']} [{e['id']}]: sin datos de rendimiento")
            continue
        extra = ", ".join(f"{k} {v2}" for k, v2 in t.items() if k not in ("alcance", "publicaciones", clave))
        val = v if v is not None else "sin dato"
        print(f"{i}. {e['nombre']} [{e['id']}]: {val} {etiqueta}/1.000 · alcance {t['alcance']} en {t['publicaciones']} post(s)" + (f" · {extra}" if extra else ""))
    sin = [e["nombre"] for v, e, t in filas if v is None]
    if sin:
        print(f"\nSin el dato principal: {', '.join(sin)}. No se pueden comparar con los demás todavía.")


def listar(a):
    es = todos(a.bib)
    if not es:
        print("La biblioteca está vacía."); return
    for e in es:
        n = len(e.get("rendimiento", []))
        print(f"- {e['nombre']} [{e['id']}]: {e.get('slides')} slides · {n} publicación/es medidas · modelo: {e.get('fuente_modelo') or '—'}" + (f" · {e['nota']}" if e.get("nota") else ""))


def ver(a):
    p, e = cargar(a.bib, a.nombre)
    adn = e.get("adn", {})
    print(json.dumps({k: e[k] for k in ("nombre", "id", "creado", "fuente_modelo", "slides", "nota")}, ensure_ascii=False, indent=2))
    for k in ("paleta", "tipografias", "narrativa"):
        if k in adn:
            print(f"\n{k}:", json.dumps(adn[k], ensure_ascii=False, indent=2))
    print("\nRendimiento:", json.dumps(tasas(e), ensure_ascii=False) if tasas(e) else "sin datos")
    print("Carpeta:", os.path.dirname(p))


def catalogo(a):
    from PIL import Image, ImageDraw, ImageFont
    es = todos(a.bib)
    if not es:
        sys.exit("La biblioteca está vacía.")
    W, H, G, T = 270, 338, 14, 56
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    except OSError:
        f = ImageFont.load_default()
    sheet = Image.new("RGB", (3 * (W + G) + G, len(es) * (H + T + G) + G), "#222")
    d = ImageDraw.Draw(sheet)
    for i, e in enumerate(es):
        y = G + i * (H + T + G)
        d.text((G, y + 14), f"{i + 1}. {e['nombre']}  ({e.get('slides')} slides)", fill="white", font=f)
        ms = sorted(glob.glob(os.path.join(a.bib, e["id"], "muestras", "slide_*.png")))
        for j, m in enumerate(ms[:1] + ms[1:3]):
            sheet.paste(Image.open(m).convert("RGB").resize((W, H), Image.LANCZOS), (G + j * (W + G), y + T))
    sheet.save(a.salida)
    print(a.salida, sheet.size)


ap = argparse.ArgumentParser(description="Biblioteca de estilos de carrusel")
ap.add_argument("--bib", default="carruseles/estilos")
sp = ap.add_subparsers(dest="cmd", required=True)
g = sp.add_parser("guardar"); g.add_argument("proyecto"); g.add_argument("nombre")
g.add_argument("--html", default="carrusel.html"); g.add_argument("--build", default="build.py")
g.add_argument("--final", default="final"); g.add_argument("--nota"); g.add_argument("--reemplazar", action="store_true")
r = sp.add_parser("rendimiento"); r.add_argument("nombre"); r.add_argument("--link"); r.add_argument("--fecha")
for c in CAMPOS:
    r.add_argument("--" + c, type=int, required=(c == "alcance"))
k = sp.add_parser("ranking"); k.add_argument("--objetivo", choices=list(METRICA), default="leads")
sp.add_parser("listar")
v = sp.add_parser("ver"); v.add_argument("nombre")
c = sp.add_parser("catalogo"); c.add_argument("salida", nargs="?", default="catalogo_estilos.png")
a = ap.parse_args()
{"guardar": guardar, "rendimiento": rendimiento, "ranking": ranking, "listar": listar, "ver": ver, "catalogo": catalogo}[a.cmd](a)
