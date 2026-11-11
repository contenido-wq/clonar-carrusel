#!/usr/bin/env python3
"""Biblioteca de estilos de carrusel.

Hay dos bibliotecas:
  - estilos incluidos: vienen dentro de la skill (carpeta estilos/ junto a scripts/), solo lectura.
  - estilos propios: los que guarda cada persona, en carruseles/estilos (cámbiala con --bib).
listar, catalogo, ver y usar muestran las dos. guardar siempre escribe en la propia.

Uso:
  estilos.py guardar <carpeta_proyecto> <nombre> [--html carrusel.html] [--build build.py] [--nota "..."]
  estilos.py usar <nombre> <carpeta_proyecto_nuevo>   # copia el estilo para hacer un carrusel nuevo
  estilos.py empaquetar <salida.zip>                    # la skill + estilos incluidos + estilos propios, lista para subir
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


SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCLUIDOS = os.path.join(SKILL, "estilos")
TEXTO = (".html", ".py", ".css", ".js")
IMG = (".jpg", ".jpeg", ".png", ".webp")


def buscar(bib, nombre):
    """Carpeta del estilo: primero los propios, después los incluidos en la skill."""
    for base, origen in ((bib, "propio"), (INCLUIDOS, "incluido")):
        d = os.path.join(base, slug(nombre))
        if os.path.exists(os.path.join(d, "estilo.json")):
            return d, origen
    sys.exit(f"No existe el estilo '{nombre}'. Usa: estilos.py listar")


def cargar(bib, nombre):
    d, origen = buscar(bib, nombre)
    if origen == "incluido":  # para escribir en él (rendimiento), primero pasa a la biblioteca propia
        dst = os.path.join(bib, os.path.basename(d))
        shutil.copytree(d, dst)
        d = dst
    p = os.path.join(d, "estilo.json")
    return p, json.load(open(p, encoding="utf-8"))


def relativizar(carpeta, abs_src):
    """Quita las rutas absolutas del proyecto de origen en los .py/.html copiados, para que el estilo funcione en cualquier carpeta."""
    abs_src = abs_src.rstrip("/")
    for f in os.listdir(carpeta):
        p = os.path.join(carpeta, f)
        if not (os.path.isfile(p) and f.endswith(TEXTO)):
            continue
        t = open(p, encoding="utf-8").read()
        if abs_src not in t:
            continue
        if f.endswith(".py"):
            t = re.sub(r"(['\"])" + re.escape(abs_src) + r"/([^'\"]+)\1", r"_os.path.join(_D, '\2')", t)
            t = re.sub(r"(['\"])" + re.escape(abs_src) + r"/?\1", "_D", t)
            t = "import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__))\n" + t
        else:
            t = t.replace("file://" + abs_src + "/", "").replace(abs_src + "/", "")
        open(p, "w", encoding="utf-8").write(t)


def aligerar(carpeta):
    """Deja el estilo liviano para empaquetarlo: solo lo que usa la plantilla, imágenes a tamaño de slide y muestras en JPG."""
    from PIL import Image
    textos = [os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith(TEXTO)]
    leer = lambda: "\n".join(open(t, encoding="utf-8").read() for t in textos)
    todo = leer()
    for raiz, dirs, files in os.walk(carpeta, topdown=True):
        rel_dir = os.path.relpath(raiz, carpeta)
        if rel_dir == "muestras" or "__pycache__" in raiz:
            continue
        for f in files:
            p = os.path.join(raiz, f)
            rel = os.path.relpath(p, carpeta)
            if rel == "estilo.json" or (rel_dir == "." and f.endswith(TEXTO + (".md",))):
                continue
            # Con build.py los nombres se pueden armar en el código (f"cols/{x}.png"): se conserva la carpeta citada.
            dinamico = os.path.exists(os.path.join(carpeta, "build.py"))
            usado = rel.replace(os.sep, "/") in todo or (dinamico and rel_dir != "." and rel_dir.split(os.sep)[0] + "/" in todo)
            if not usado:
                os.remove(p)
    for raiz, dirs, files in os.walk(carpeta):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(raiz, "__pycache__")); dirs.remove("__pycache__")
        for f in files:
            p = os.path.join(raiz, f)
            if not f.lower().endswith(IMG) or os.path.relpath(raiz, carpeta) == "muestras" or os.path.getsize(p) < 200_000:
                continue
            im = Image.open(p)
            im.thumbnail((1350, 1350), Image.LANCZOS)
            rel = os.path.relpath(p, carpeta).replace(os.sep, "/")
            opaca = im.mode in ("RGB", "L") or (im.mode in ("RGBA", "LA") and im.getchannel("A").getextrema()[0] == 255)
            if f.lower().endswith(".png") and opaca and rel in todo:  # foto sin transparencia: JPG y se actualiza la referencia
                nuevo = rel[:-4] + ".jpg"
                im.convert("RGB").save(os.path.join(carpeta, nuevo), quality=85)
                os.remove(p)
                for t in textos:
                    c = open(t, encoding="utf-8").read()
                    if rel in c:
                        open(t, "w", encoding="utf-8").write(c.replace(rel, nuevo))
                todo = leer()
            elif f.lower().endswith((".jpg", ".jpeg")):
                im.convert("RGB").save(p, quality=85)
            else:
                im.save(p, optimize=True)
                if os.path.getsize(p) > 200_000 and im.mode != "P":  # PNG con nombre armado en el código: 256 colores, mismo nombre
                    modo = "RGBA" if im.mode in ("RGBA", "LA") else "RGB"
                    q = Image.FASTOCTREE if modo == "RGBA" else Image.MEDIANCUT
                    im.convert(modo).quantize(256, method=q).save(p, optimize=True)
    m = os.path.join(carpeta, "muestras")
    for f in sorted(glob.glob(os.path.join(m, "slide_*.png"))):
        Image.open(f).convert("RGB").resize((540, 675), Image.LANCZOS).save(f[:-4] + ".jpg", quality=82)
        os.remove(f)


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
    build_txt = ""
    if a.build and os.path.exists(os.path.join(src, a.build)):
        shutil.copy(os.path.join(src, a.build), os.path.join(dst, "build.py"))
        build_txt = open(os.path.join(src, a.build), encoding="utf-8").read()
    # Archivos de texto que usa el build o la plantilla (head.html, módulos .py, .css).
    ref = open(html, encoding="utf-8").read() + build_txt
    for f in os.listdir(src):
        if f.endswith(TEXTO) and f not in (a.html, a.build) and os.path.isfile(os.path.join(src, f)) \
                and (f in ref or (f.endswith(".py") and re.search(r"\b(from|import)\s+" + re.escape(f[:-3]) + r"\b", ref))):
            shutil.copy(os.path.join(src, f), dst)
    # Recursos que usa la plantilla (fotos, fuentes locales) para que renderice sola.
    for f in os.listdir(src):
        p = os.path.join(src, f)
        if os.path.isfile(p) and f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".svg", ".woff", ".woff2", ".ttf")) and f != "comparacion.png" and not f.startswith("comparacion"):
            shutil.copy(p, dst)
    # Subcarpetas que usa la plantilla (fuentes, fotos, imágenes generadas). No copia capturas ni renders.
    html_txt = open(html, encoding="utf-8").read()
    for d in os.listdir(src):
        if os.path.isdir(os.path.join(src, d)) and (d == "fonts" or f'{d}/' in html_txt) \
                and d not in ("original", "muestras") and not d.startswith("final"):
            shutil.copytree(os.path.join(src, d), os.path.join(dst, d), dirs_exist_ok=True)
    relativizar(dst, os.path.abspath(src))
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
    """Estilos propios primero y después los incluidos en la skill (si un propio tiene el mismo id, gana el propio)."""
    out, vistos = [], set()
    for base, origen in ((bib, "propio"), (INCLUIDOS, "incluido")):
        for p in sorted(glob.glob(os.path.join(base, "*", "estilo.json"))):
            e = json.load(open(p, encoding="utf-8"))
            if e["id"] in vistos:
                continue
            vistos.add(e["id"])
            e["_dir"], e["_origen"] = os.path.dirname(p), origen
            out.append(e)
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
        print(f"- {e['nombre']} [{e['id']}] ({e['_origen']}): {e.get('slides')} slides · {n} publicación/es medidas · modelo: {e.get('fuente_modelo') or '—'}" + (f" · {e['nota']}" if e.get("nota") else ""))


def ver(a):
    d, origen = buscar(a.bib, a.nombre)
    p = os.path.join(d, "estilo.json")
    e = json.load(open(p, encoding="utf-8"))
    print(f"Estilo {origen}.")
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
        tag = "  · tuyo" if e["_origen"] == "propio" else ""
        d.text((G, y + 14), f"{i + 1}. {e['nombre']}  ({e.get('slides')} slides){tag}", fill="white", font=f)
        ms = sorted(glob.glob(os.path.join(e["_dir"], "muestras", "slide_*.*")))
        for j, m in enumerate(ms[:1] + ms[1:3]):
            sheet.paste(Image.open(m).convert("RGB").resize((W, H), Image.LANCZOS), (G + j * (W + G), y + T))
    sheet.save(a.salida)
    print(a.salida, sheet.size)


def usar(a):
    d, origen = buscar(a.bib, a.nombre)
    if os.path.exists(a.destino) and os.listdir(a.destino):
        sys.exit(f"{a.destino} ya existe y no está vacía. Usa otra carpeta.")
    shutil.copytree(d, a.destino, dirs_exist_ok=True, ignore=shutil.ignore_patterns("muestras", "__pycache__"))
    shutil.move(os.path.join(a.destino, "plantilla.html"), os.path.join(a.destino, "carrusel.html"))
    e = json.load(open(os.path.join(d, "estilo.json"), encoding="utf-8"))
    gen = "edita build.py y córrelo" if os.path.exists(os.path.join(a.destino, "build.py")) else "edita carrusel.html"
    print(f"Listo: {a.destino} con el estilo '{e['nombre']}' ({origen}, {e.get('slides')} slides). Para el tema nuevo, {gen}.")
    print(f"Muestras para comparar: {os.path.join(d, 'muestras')}")
    if origen == "incluido":
        print("Es un estilo de ejemplo: cambia el @, el nombre, la foto, la palabra del CTA y la oferta por los de la persona.")


def empaquetar(a):
    """Arma un ZIP de la skill con los estilos incluidos y los propios, para subirlo a Claude.ai y no perder los estilos nuevos."""
    import tempfile, zipfile
    tmp = tempfile.mkdtemp()
    raiz = os.path.join(tmp, "clonar-carrusel")
    os.makedirs(raiz)
    for f in ("SKILL.md", "LICENSE"):
        if os.path.exists(os.path.join(SKILL, f)):
            shutil.copy(os.path.join(SKILL, f), raiz)
    for d in ("references", "scripts"):
        shutil.copytree(os.path.join(SKILL, d), os.path.join(raiz, d), ignore=shutil.ignore_patterns("__pycache__", "node_modules"))
    n = {"incluido": 0, "propio": 0}
    for e in todos(a.bib):
        dst = os.path.join(raiz, "estilos", e["id"])
        shutil.copytree(e["_dir"], dst, ignore=shutil.ignore_patterns("__pycache__"))
        if e["_origen"] == "propio":
            aligerar(dst)
        n[e["_origen"]] += 1
    salida = os.path.abspath(a.salida)
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, files in os.walk(raiz):
            for f in sorted(files):
                p = os.path.join(r, f)
                z.write(p, os.path.relpath(p, tmp))
    shutil.rmtree(tmp)
    mb = os.path.getsize(salida) / 1e6
    print(f"{salida}: {n['incluido']} estilos incluidos + {n['propio']} propios, {mb:.1f} MB")


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
u = sp.add_parser("usar"); u.add_argument("nombre"); u.add_argument("destino")
e_ = sp.add_parser("empaquetar"); e_.add_argument("salida", nargs="?", default="clonar-carrusel.zip")
a = ap.parse_args()
{"guardar": guardar, "rendimiento": rendimiento, "ranking": ranking, "listar": listar, "ver": ver, "catalogo": catalogo,
 "usar": usar, "empaquetar": empaquetar}[a.cmd](a)
