# Genera carrusel.html (estilo hoja de cuaderno + mapas mentales a mano)
import math, pathlib

HANDLE = "@jheitrujillob"
TOTAL = 6

# ---------- Íconos (trazos en caja 0..100) ----------
P = lambda d: f'<path d="{d}"/>'
C = lambda cx, cy, r, extra="": f'<circle cx="{cx}" cy="{cy}" r="{r}" {extra}/>'
R = lambda x, y, w, h, rx=0, extra="": f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" {extra}/>'
PAPER = 'fill="#ebe7e0"'

ICONS = {
 "lupa": C(42, 42, 24) + P("M60 60 L84 84") + P("M30 36 Q34 28 42 27"),
 "bombillo": P("M38 66 C38 56 26 50 26 36 A24 24 0 0 1 74 36 C74 50 62 56 62 66 Z") + P("M40 74 H60 M42 82 H58 M46 90 H54") + P("M44 60 V44 L50 50 L56 44 V60"),
 "lapiz": P("M18 82 L26 60 L66 20 L80 34 L40 74 Z") + P("M26 60 L40 74 M60 26 L74 40 M18 82 L30 78"),
 "calendario": R(14, 22, 72, 64, 6) + P("M14 38 H86 M32 14 V30 M68 14 V30") + P("M26 52 h8 M46 52 h8 M66 52 h8 M26 70 h8 M46 70 h8") + P("M64 68 L69 74 L80 62"),
 "pregunta": P("M14 18 H86 V68 H46 L28 86 V68 H14 Z") + P("M40 34 Q40 26 50 26 Q60 26 60 34 Q60 41 50 44 V51 M50 58 V60"),
 "prohibido": C(50, 50, 32) + P("M28 28 L72 72"),
 "enojado": C(50, 50, 34) + P("M34 38 L44 44 M66 38 L56 44") + C(40, 50, 3, 'fill="currentColor"') + C(60, 50, 3, 'fill="currentColor"') + P("M36 70 Q50 58 64 70"),
 "globo_lineas": P("M12 16 H88 V66 H44 L26 84 V66 H12 Z") + P("M26 32 H74 M26 44 H74 M26 56 H58"),
 "x_check": R(6, 32, 36, 36, 2) + P("M14 40 L34 60 M34 40 L14 60") + P("M54 74 L48 26") + R(58, 32, 36, 36, 2) + P("M64 50 L72 60 L88 38"),
 "tendencia": P("M10 88 H90") + R(18, 68, 12, 20) + R(38, 56, 12, 32) + R(58, 44, 12, 44) + R(78, 30, 10, 58) + P("M14 52 L36 36 L54 42 L80 14 M68 14 H80 V26"),
 "rayo": P("M58 8 L26 54 H48 L40 92 L76 40 H54 Z"),
 "tarjetas": R(36, 10, 48, 60, 4, PAPER) + R(26, 20, 48, 60, 4, PAPER) + R(16, 30, 48, 60, 4, PAPER) + P("M26 46 H54 M26 58 H54 M26 70 H44"),
 "reel": R(30, 8, 40, 84, 8) + P("M44 38 V62 L62 50 Z") + P("M44 16 H56"),
 "historia": C(50, 50, 36, 'stroke-dasharray="14 8"') + C(50, 42, 10) + P("M32 72 Q50 54 68 72"),
 "alerta": P("M50 10 L90 84 H10 Z") + P("M50 36 V60 M50 70 V72"),
 "antes_despues": C(20, 38, 9) + P("M5 80 Q5 56 20 56 Q35 56 35 80") + P("M42 62 H60 M53 55 L60 62 L53 69") + C(80, 38, 9) + P("M65 80 Q65 56 80 56 Q95 56 95 80") + P("M80 18 V22 M68 24 L71 27 M92 24 L89 27"),
 "persona": C(50, 30, 15) + P("M20 90 Q20 56 50 56 Q80 56 80 90"),
 "microfono": R(38, 10, 24, 46, 12) + P("M28 42 Q28 68 50 68 Q72 68 72 42 M50 68 V84 M36 88 H64") + P("M44 24 H56 M44 34 H56"),
 "estrella": P("M50 10 L61 37 L90 39 L67 57 L75 86 L50 70 L25 86 L33 57 L10 39 L39 37 Z"),
 "diana": C(46, 54, 34) + C(46, 54, 21) + C(46, 54, 8) + P("M46 54 L84 16 M74 12 L86 14 L88 26"),
 "etiqueta": P("M12 52 L48 14 H86 V52 L48 90 Z") + C(70, 30, 6),
 "x_caja": R(20, 20, 60, 60, 3) + P("M32 32 L68 68 M68 32 L32 68"),
 "pilares": P("M10 26 L50 10 L90 26 Z M10 88 H90 M8 80 H92") + P("M22 32 V76 M40 32 V76 M60 32 V76 M78 32 V76"),
 "bandera": P("M24 92 V10") + P("M24 14 Q42 4 58 16 Q72 26 88 16 V50 Q72 60 58 50 Q42 40 24 50"),
 "formatos": R(10, 10, 34, 34, 3) + C(72, 27, 17) + P("M10 88 L44 88 L27 58 Z") + R(56, 56, 32, 32, 3) + P("M67 64 V80 L80 72 Z"),
 "barras": P("M10 88 H90") + R(18, 62, 14, 26) + R(43, 44, 14, 44) + R(68, 22, 14, 66) + P("M22 72 H28 M47 56 H53 M72 34 H78"),
 "bolsa": P("M18 34 H82 L76 90 H24 Z M36 34 V26 Q36 10 50 10 Q64 10 64 26 V34") + P("M58 52 Q50 46 44 52 Q40 58 50 62 Q60 66 56 72 Q50 78 42 72 M50 44 V80"),
 "corazon_persona": C(30, 40, 11) + P("M10 88 Q10 60 30 60 Q50 60 50 88") + P("M56 12 H92 V44 H72 L62 54 V44 H56 Z") + P("M74 36 Q62 28 66 22 Q70 17 74 23 Q78 17 82 22 Q86 28 74 36 Z"),
 "exclama": C(50, 46, 34) + P("M30 74 L20 92 L42 79") + P("M50 26 V50 M50 60 V62"),
 "check_barras": C(50, 24, 16) + P("M42 24 L48 30 L58 18") + P("M10 92 H90") + R(18, 70, 14, 22) + R(43, 58, 14, 34) + R(68, 46, 14, 46),
 "pasos": C(22, 22, 10) + C(22, 50, 10) + C(22, 78, 10) + P("M20 18 L23 16 V28 M18 46 Q22 42 26 46 Q26 50 18 55 H27 M18 74 Q24 70 26 75 Q24 79 20 78 Q26 79 26 82 Q24 86 18 83") + P("M42 22 H86 M42 50 H86 M42 78 H76"),
 "corazon": P("M50 84 Q14 60 14 36 Q14 16 32 16 Q44 16 50 30 Q56 16 68 16 Q86 16 86 36 Q86 60 50 84 Z"),
 "caida": P("M10 88 H90") + P("M14 24 L36 44 L52 36 L80 72 M68 72 H80 V60"),
 "reloj": C(50, 56, 34) + P("M50 56 V34 M50 56 L64 64") + P("M42 12 H58 M50 12 V22") + P("M50 26 V28 M80 56 H78 M50 86 V84 M20 56 H22"),
 "chat_ia": P("M10 18 H90 V70 H44 L26 88 V70 H10 Z") + P("M50 26 Q52 40 64 44 Q52 48 50 62 Q48 48 36 44 Q48 40 50 26 Z") + P("M72 26 Q73 31 78 32 Q73 33 72 38 Q71 33 66 32 Q71 31 72 26 Z"),
}

def rays(r1=58, r2=68):
    out = []
    for deg in (150, 180, 210, -30, 0, 30):
        a = math.radians(deg)
        out.append(f"M{50 + r1*math.cos(a):.1f} {50 + r1*math.sin(a):.1f} L{50 + r2*math.cos(a):.1f} {50 + r2*math.sin(a):.1f}")
    return P(" ".join(out))

def icon(name, cx, cy, size=175, with_rays=True):
    s = size / 140
    body = ICONS[name] + (rays() if with_rays else "")
    return (f'<g transform="translate({cx - 70*s:.1f},{cy - 70*s:.1f}) scale({s:.3f}) translate(20,20)" '
            f'class="ink" filter="url(#rough)">{body}</g>')

def arrow(x1, y1, x2, y2, bend=0.12):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    qx, qy = mx - dy * bend, my + dx * bend
    ang = math.atan2(y2 - qy, x2 - qx)
    h = 22
    a1, a2 = ang + math.radians(150), ang - math.radians(150)
    head = f"M{x2 + h*math.cos(a1):.1f} {y2 + h*math.sin(a1):.1f} L{x2} {y2} L{x2 + h*math.cos(a2):.1f} {y2 + h*math.sin(a2):.1f}"
    return f'<path class="ink" filter="url(#rough)" d="M{x1} {y1} Q{qx:.1f} {qy:.1f} {x2} {y2} {head}"/>'

# Posiciones de los 6 nodos (coordenadas de la slide 1080x1350), espejo del modelo
SLOTS = [
    # etiqueta (x,y), ícono (x,y), flecha (desde, hasta)
    dict(lab=(330, 650), ic=(318, 760), arr=((470, 790), (395, 700))),
    dict(lab=(840, 650), ic=(850, 760), arr=((660, 790), (740, 700))),
    dict(lab=(240, 880), ic=(235, 1000), arr=((392, 905), (368, 905))),
    dict(lab=(925, 880), ic=(925, 1000), arr=((735, 905), (800, 905))),
    dict(lab=(370, 1110), ic=(370, 1225), arr=((480, 990), (420, 1065))),
    dict(lab=(760, 1110), ic=(770, 1225), arr=((660, 990), (720, 1065))),
]
CENTER = (570, 900)

def mindmap(center_txt, nodes, dy=0):
    cx, cy = CENTER
    svg = [f'<ellipse class="ink" filter="url(#rough)" cx="{cx}" cy="{cy}" rx="178" ry="104"/>',
           f'<ellipse class="ink thin" filter="url(#rough)" cx="{cx+3}" cy="{cy-2}" rx="170" ry="98" transform="rotate(-3 {cx} {cy})"/>']
    labels = []
    for slot, (txt, ic) in zip(SLOTS, nodes):
        (a, b) = slot["arr"]
        svg.append(arrow(a[0], a[1], b[0], b[1]))
        svg.append(icon(ic, *slot["ic"]))
        lx, ly = slot["lab"]
        labels.append(f'<div class="node" style="left:{lx}px;top:{ly}px">{txt}</div>')
    return (f'<div class="mapwrap" style="transform:translateY({dy}px)"><svg class="map" viewBox="0 0 1080 1350">{"".join(svg)}</svg>'
            f'<div class="center" style="left:{cx}px;top:{cy}px">{center_txt}</div>' + "".join(labels) + '</div>')

def underline(cls=""):
    return ('<svg class="ul ' + cls + '" viewBox="0 0 1000 30" preserveAspectRatio="none">'
            '<path d="M4 9 Q240 3 500 8 T996 6"/><path d="M14 23 Q300 17 520 21 T990 19"/></svg>')

def chrome(i, swipe=False):
    s = f'<div class="handle">{HANDLE}</div><div class="num">{i}/{TOTAL}</div>'
    if swipe:
        s += '<div class="swipe">Desliza →</div>'
    return s

def paper(inner, i, swipe=False):
    return (f'<section class="slide"><div class="lines"></div><div class="margin"></div>'
            f'<i class="hole" style="top:88px"></i><i class="hole" style="top:640px"></i><i class="hole" style="top:1205px"></i>'
            f'{chrome(i, swipe)}{inner}<div class="grain"></div></section>')

slides = []

# 1. Portada
cover_icons = (icon("bombillo", 215, 990, 150) + arrow(300, 995, 350, 990, .1) +
               icon("corazon_persona", 452, 985, 150) + arrow(540, 995, 590, 990, .1) +
               icon("check_barras", 692, 985, 150) + arrow(778, 995, 828, 990, .1) +
               icon("exclama", 930, 985, 150))
slides.append(paper(
    '<div class="cover"><h1 class="title big uline">4 TIPOS DE CONTENIDO<br>QUE IMPRIMEN DINERO</h1>' +
    '<p class="sub">Enseñar. Conectar. Demostrar. Opinar.</p></div>'
    f'<svg class="map" viewBox="0 0 1080 1350">{cover_icons}</svg>', 1, swipe=True))

SECTIONS = [
    ("1. CONTENIDO EDUCATIVO",
     "Resuelve hoy la duda que tu cliente tiene antes de comprarte. Si le ahorras un error, te ganas su confianza.",
     "QUÉ<br>ENSEÑAR",
     [("Errores que ves<br>en tus clientes", "alerta"), ("Preguntas antes<br>de comprar", "pregunta"),
      ("Lo que nadie<br>te explica", "bombillo"), ("Tu proceso<br>en 3 pasos", "pasos"),
      ("Comparativas<br>A vs. B", "x_check"), ("Herramientas<br>que usas", "lapiz")]),
    ("2. CONTENIDO QUE CONECTA",
     "Te compran a ti antes que a tu producto. Muestra el camino, no solo la foto del resultado.",
     "CUENTA",
     [("Por qué<br>empezaste", "bandera"), ("Lo que casi<br>te hace cerrar", "caida"),
      ("Tus valores", "corazon"), ("Detrás de<br>cámaras", "reel"),
      ("Tu día<br>a día", "reloj"), ("Errores que<br>te enseñaron", "historia")]),
    ("3. CONTENIDO QUE DEMUESTRA",
     "Decir que eres bueno no convence. Mostrarlo, sí. Deja que los resultados hablen por ti.",
     "MUESTRA",
     [("Casos de<br>clientes", "persona"), ("Números que<br>puedes probar", "barras"),
      ("Mensajes de<br>clientes", "globo_lineas"), ("Reseñas", "estrella"),
      ("Antes y<br>después", "antes_despues"), ("Tu proceso<br>en vivo", "reel")]),
    ("4. CONTENIDO QUE OPINA",
     "Si no tomas postura, nadie te recuerda. El que opina gana seguidores y también clientes.",
     "DI LO QUE<br>PIENSAS",
     [("Lo que odias de<br>tu industria", "enojado"), ("Lo que no<br>recomiendas", "prohibido"),
      ("Creencias que<br>hay que romper", "x_caja"), ("Tu postura sobre<br>las tendencias", "tendencia"),
      ("Lo que harías<br>diferente", "rayo"), ("Una verdad<br>incómoda", "exclama")]),
]
for n, (t, body, center, nodes) in enumerate(SECTIONS, start=2):
    slides.append(paper(
        f'<div class="head"><h2 class="title uline">{t}</h2></div><p class="body">{body}</p>' + mindmap(center, nodes), n))

# 6. CTA
cta_svg = ('<ellipse class="red" filter="url(#rough)" cx="545" cy="725" rx="370" ry="150" transform="rotate(-2 545 725)"/>'
           '<path class="red" filter="url(#rough)" d="M190 640 Q300 575 420 572"/>'
           + icon("reloj", 420, 1185, 175) + arrow(535, 1190, 605, 1190, .05) + icon("chat_ia", 720, 1180, 175))
slides.append(paper(
    '<p class="q">¿Sabes que tienes que publicar, pero el día nunca te alcanza?</p>'
    '<p class="comenta">Comenta</p><div class="kw">TALLER</div><svg class="kw-ul" viewBox="0 0 1000 30" preserveAspectRatio="none"><path d="M4 9 Q240 3 500 8 T996 6"/><path d="M14 23 Q300 17 520 21 T990 19"/></svg>' +
    '<p class="give">y te llevo a mi taller de<br>contenido que vende con IA</p>'
    f'<svg class="map" viewBox="0 0 1080 1350">{cta_svg}</svg>', 6))

CSS = """
:root{
  --bg:#e9e6df; --bg2:#e0dbd2; --fg:#0f2a96; --accent:#da4048; --margin:#ce6d74; --rule:#a5b3bc;
  --f-title:'Patrick Hand SC',cursive; --f-body:'Patrick Hand',cursive;
  --t-big:104px; --t-title:84px; --t-body:56px; --t-node:44px; --t-center:60px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#777;display:flex;flex-direction:column;gap:40px;align-items:center;padding:40px 0}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--fg);
  background:radial-gradient(ellipse at 55% 45%,#eeebe5 40%,var(--bg) 75%,var(--bg2) 100%);font-family:var(--f-body)}
.lines{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,transparent 0 62px,var(--rule) 62px 64.5px);background-position:0 86px;opacity:.85}
.margin{position:absolute;top:0;bottom:0;left:104px;width:2.5px;background:var(--margin);opacity:.9}
.hole{position:absolute;left:28px;width:46px;height:46px;border-radius:50%;
  background:radial-gradient(circle at 50% 55%,#fbfaf7 0 55%,#d9d4cb 70%,#b9b2a7 100%);box-shadow:inset 2px 3px 4px rgba(0,0,0,.25)}
.grain{position:absolute;inset:0;pointer-events:none;mix-blend-mode:multiply;opacity:.22;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55  0 0 0 0 .5  0 0 0 0 .45  0 0 0 .5 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.handle,.num,.swipe{position:absolute;z-index:3;font-family:var(--f-body);font-size:32px;color:var(--fg);opacity:.75}
.handle{top:26px;left:132px}.num{top:26px;right:44px}
.swipe{bottom:40px;right:56px;font-size:40px;opacity:.9}
.title{font-family:var(--f-title);font-weight:400;line-height:1.02;letter-spacing:1px;-webkit-text-stroke:1px var(--fg)}
.uline{display:inline-block;padding-bottom:34px;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 30' preserveAspectRatio='none'><path d='M4 9 Q240 3 500 8 T996 6' fill='none' stroke='%23da4048' stroke-width='5' stroke-linecap='round' vector-effect='non-scaling-stroke'/><path d='M14 23 Q300 17 520 21 T990 19' fill='none' stroke='%23da4048' stroke-width='5' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>") left bottom/100% 30px no-repeat}
.head{position:absolute;left:140px;top:150px;display:inline-block}
.head .title{font-size:var(--t-title)}
.ul{display:block;width:100%;height:30px;margin-top:4px;fill:none;stroke:var(--accent);stroke-width:5;stroke-linecap:round}
.ul path{vector-effect:non-scaling-stroke}
.body{position:absolute;left:140px;right:50px;top:318px;font-size:var(--t-body);line-height:64.5px}
.mapwrap{position:absolute;inset:0;z-index:1}
.cover{position:absolute;left:135px;right:40px;top:390px;text-align:center}
.cover .title{font-size:var(--t-big);line-height:1.12}
.cover-ul{width:92%;margin:6px auto 0}
.sub{font-size:60px;margin-top:60px}
svg.map{position:absolute;inset:0;width:1080px;height:1350px;z-index:1;overflow:visible}
.ink{fill:none;stroke:var(--fg);stroke-width:4.6;stroke-linecap:round;stroke-linejoin:round;color:var(--fg)}
.ink.thin{stroke-width:2.4}
.red{fill:none;stroke:var(--accent);stroke-width:6;stroke-linecap:round}
.center{position:absolute;z-index:2;transform:translate(-50%,-50%);font-family:var(--f-title);-webkit-text-stroke:1.4px var(--fg);font-size:var(--t-center);line-height:1.05;text-align:center;white-space:nowrap}
.node{position:absolute;z-index:2;transform:translate(-50%,-50%);font-size:var(--t-node);line-height:1.02;text-align:center;white-space:nowrap}
.q{position:absolute;left:130px;right:30px;top:230px;text-align:center;font-size:62px;line-height:1.2}
.comenta{position:absolute;left:0;right:0;top:500px;text-align:center;font-size:66px;padding-left:60px;z-index:2}
.kw{position:absolute;left:0;right:0;top:585px;text-align:center;font-family:var(--f-title);font-size:190px;line-height:1;padding-left:60px;letter-spacing:8px;-webkit-text-stroke:5px var(--fg);z-index:2}
.kw-ul{position:absolute;left:290px;width:580px;top:790px;height:30px;fill:none;stroke:var(--accent);stroke-width:6;stroke-linecap:round;z-index:2}
.kw-ul path{vector-effect:non-scaling-stroke}
.give{position:absolute;left:140px;right:50px;top:915px;text-align:center;font-size:62px;line-height:1.2}
"""

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Carrusel tipos de contenido</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand+SC&family=Patrick+Hand&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<svg width="0" height="0" style="position:absolute"><filter id="rough" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="3.5"/></filter></svg>
{''.join(slides)}
<script>
document.fonts.ready.then(()=>{{document.querySelectorAll('.title').forEach(t=>{{
  t.style.whiteSpace='nowrap';const max=t.classList.contains('big')?880:900;let f=parseFloat(getComputedStyle(t).fontSize);
  while(t.scrollWidth>max&&f>40){{f-=2;t.style.fontSize=f+'px';}}}});document.body.dataset.fit='1';}});
</script>
</body></html>"""
pathlib.Path(__file__).with_name("carrusel_v2.html").write_text(html, encoding="utf-8")
print("ok")
