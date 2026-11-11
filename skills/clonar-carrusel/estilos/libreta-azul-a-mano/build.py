# Genera carrusel.html: cuaderno + lapicero azul + Jhei dibujado en tinta
import pathlib

HANDLE = "@jheitrujillob"

# ---------- doodles (viewBox 0 0 100 100, trazo azul) ----------
D = {
 "chispa": '<path d="M50 6 Q54 44 94 50 Q54 56 50 94 Q46 56 6 50 Q46 44 50 6 Z"/>',
 "estrella": '<path d="M50 8 L61 38 L93 39 L67 58 L77 90 L50 71 L23 90 L33 58 L7 39 L39 38 Z"/><path d="M30 44 L70 44 M36 62 L64 62"/>',
 "bombillo": '<path d="M36 64 C36 54 22 48 22 32 A28 28 0 0 1 78 32 C78 48 64 54 64 64 Z"/><path d="M38 72 H62 M40 80 H60 M44 88 H56"/><path d="M42 60 V44 Q46 36 50 44 Q54 36 58 44 V60"/>',
 "camara": '<rect x="8" y="28" width="84" height="60" rx="6"/><path d="M34 28 L40 16 H62 L68 28"/><circle cx="50" cy="58" r="20"/><circle cx="50" cy="58" r="11"/><path d="M14 40 H86 M14 44 H86"/><rect x="74" y="34" width="10" height="5"/><path d="M42 52 Q46 48 50 49"/>',
 "claqueta": '<rect x="8" y="40" width="84" height="52" rx="4"/><path d="M8 40 L88 18 L92 30 L12 52 Z"/><path d="M22 36 L30 46 M40 31 L48 41 M58 26 L66 36 M76 21 L84 31"/><path d="M44 58 V78 L62 68 Z"/>',
 "libreta": '<rect x="18" y="8" width="66" height="86" rx="4" transform="rotate(8 50 50)"/><path d="M26 22 H70 M26 34 H66 M26 46 H70 M26 58 H62 M26 70 H68" transform="rotate(8 50 50)"/><path d="M14 18 h8 M13 30 h8 M12 42 h8 M11 54 h8 M10 66 h8 M9 78 h8"/><path d="M80 12 L92 18 L66 92 L58 96 L58 86 Z"/>',
 "corazon": '<path d="M50 86 Q14 60 14 36 Q14 16 32 16 Q44 16 50 30 Q56 16 68 16 Q86 16 86 36 Q86 60 50 86 Z"/>',
 "flecha_curva": '<path d="M92 70 Q60 4 10 52"/><path d="M8 34 L10 54 L28 52"/>',
}


def doodle(name, x, y, size, rot=0, extra=""):
    return (f'<svg class="dd" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;transform:rotate({rot}deg)" '
            f'viewBox="0 0 100 100">{D[name]}{extra}</svg>')


def rayos(x, y, size, lado="izq", rot=0):
    """Tres rayitas de énfasis, como las del modelo."""
    p = "M90 20 L60 34 M92 50 L58 50 M90 80 L60 66" if lado == "izq" else "M10 20 L40 34 M8 50 L42 50 M10 80 L40 66"
    return f'<svg class="dd" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;transform:rotate({rot}deg)" viewBox="0 0 100 100"><path d="{p}"/></svg>'


def handle():
    return (f'<div class="hdl">{rayos(-70, -8, 60, "izq")}{HANDLE}'
            f'{rayos(None, -8, 60, "der").replace("left:Nonepx", "right:-70px")}</div>')


def hoja(inner, extra_cls=""):
    holes = "".join(f'<i class="hole" style="top:{t}px"></i>' for t in (60, 290, 560, 830, 1100))
    return (f'<section class="slide {extra_cls}"><div class="lines"></div><div class="margin"></div>{holes}'
            f'{inner}{handle()}<div class="grain"></div></section>')


S = []

# 1. Gancho
S.append(hoja(
    doodle("chispa", 170, 90, 120, -8) + doodle("chispa", 270, 190, 60, 10) + doodle("bombillo", 820, 70, 190, 8) +
    rayos(790, 110, 70, "izq") + rayos(980, 120, 70, "der") +
    '<div class="gancho"><h1 class="big">'
    '<span class="ul">La IA nunca más</span><br><span class="ul">va a cambiar</span><br>'
    '<span class="ul">tu cara después</span><br><span class="ul">de estos secretos</span></h1>'
    '<p class="pase">(desliza →)</p></div>' +
    doodle("estrella", 150, 1110, 95, -10) + doodle("chispa", 930, 1110, 70, 0) + rayos(240, 1120, 60, "der") + rayos(850, 1130, 60, "izq")
))

# 2. Hoja de referencia
def foto(src, cls="", style=""):
    return f'<img class="sk {cls}" src="foto/{src}" style="{style}" alt="">'


def hueco(texto):
    return f'<div class="hueco">{texto}</div>'


S.append(hoja(
    '<h2 class="tit2"><span class="ul">1. Crea una hoja de referencia real</span></h2>'
    '<div class="sheet">'
    '<div class="bx ficha"><b class="bt">PERSONAJE (TÚ)</b><div class="cols">'
    '<div><small>NOMBRE:</small>Jhei Trujillo</div><div><small>NICHO:</small>Estrategia digital</div>'
    '<div><small>PERSONALIDAD:</small>Directo, cercano</div><div><small>ESTILO:</small>Casual oscuro</div></div></div>'
    '<div class="bx paleta"><b class="bt">PALETA DE COLORES</b><div class="sw"><i></i><i></i><i></i><i></i><i></i></div></div>'
    '<div class="bx vistas"><b class="bt">VISTAS PRINCIPALES</b><div class="vrow">'
    f'<figure>{foto("jhei_boligrafo.png", "vfull")}<figcaption>FRENTE</figcaption></figure>'
    f'<figure>{hueco("tu foto<br>de 3/4")}<figcaption>3/4</figcaption></figure>'
    f'<figure>{hueco("tu foto<br>de perfil")}<figcaption>PERFIL</figcaption></figure></div></div>'
    '<div class="bx expr"><b class="bt">EXPRESIONES</b><div class="egrid">'
    f'<figure>{foto("c_retrato.png")}<figcaption>SONRISA</figcaption></figure>'
    f'<figure>{hueco("serio")}<figcaption>SERIO</figcaption></figure>'
    f'<figure>{hueco("pensativo")}<figcaption>PENSATIVO</figcaption></figure>'
    f'<figure>{hueco("sorpresa")}<figcaption>SORPRESA</figcaption></figure></div></div>'
    f'<div class="bx detalle"><b class="bt">RETRATO EN DETALLE</b>{foto("c_busto.png", "det")}'
    + doodle("corazon", 300, 8, 40, 10) + '</div>'
    '<div class="bx look"><b class="bt">DETALLES QUE NO CAMBIAN</b><div class="lgrid">'
    f'<figure>{foto("c_cabello.png")}<figcaption>CABELLO</figcaption></figure>'
    f'<figure>{foto("c_arete.png")}<figcaption>ARETE</figcaption></figure>'
    f'<figure>{foto("c_sonrisa.png")}<figcaption>BARBA</figcaption></figure>'
    f'<figure>{foto("c_camisa.png")}<figcaption>CAMISA</figcaption></figure>'
    f'<figure>{foto("c_tatuaje.png")}<figcaption>TATUAJE</figcaption></figure>'
    f'<figure>{hueco("tus<br>manos")}<figcaption>MANOS</figcaption></figure></div></div>'
    '</div>', "s2"))

# 3. Qué NO puede cambiar
S.append(hoja(
    rayos(150, 330, 90, "izq") + rayos(150, 560, 90, "izq") + rayos(905, 545, 90, "der") + rayos(290, 790, 70, "izq") + rayos(800, 790, 70, "der") +
    '<div class="centro"><h2 class="big b2">2. Dile lo que<br><span class="caps">NO</span> puede<br>cambiar</h2>'
    '<p class="sub">rostro • cabello<br>tono de piel • cuerpo<br>ropa base</p></div>'))

# 4. Misma foto base
S.append(hoja(
    rayos(130, 160, 90, "izq", 20) +
    '<div class="centro" style="top:170px"><h2 class="big b2" style="font-size:158px">3. Usa siempre<br>la misma<br><span class="ul">foto base</span></h2>'
    '<p class="sub">no cambies la foto<br>entre pruebas y escenas</p></div>' +
    rayos(230, 760, 70, "izq") + rayos(840, 760, 70, "der") +
    doodle("camara", 450, 960, 210, -3) + doodle("corazon", 680, 940, 56, 12) + rayos(370, 1010, 70, "izq") + rayos(680, 1020, 70, "der")))

# 5. Video: continuidad
S.append(hoja(
    doodle("claqueta", 140, 70, 230, -6) + rayos(360, 60, 60, "der") +
    doodle("flecha_curva", 460, 170, 200, 0) +
    '<div class="tripode"><div class="tel">' + foto("c_retrato.png", "telimg") + '</div><div class="pata"></div></div>' +
    rayos(740, 90, 70, "izq") +
    '<div class="centro" style="top:370px"><h2 class="big b2" style="font-size:146px">4. En video,<br>cuida la<br><span class="ul">continuidad</span></h2>'
    '<p class="sub">misma cara • voz<br>ropa • ángulo<br>primer cuadro fuerte</p></div>' +
    rayos(170, 870, 60, "izq") + rayos(880, 870, 60, "der") +
    foto("jhei_boligrafo.png", "abajo") + doodle("corazon", 105, 1035, 50, -12) +
    doodle("libreta", 870, 1060, 170, 0) + rayos(810, 1080, 50, "izq"), "s5"))

# 6. CTA
S.append(hoja(
    rayos(240, 180, 90, "izq", 30) + rayos(810, 180, 90, "der", -30) +
    '<div class="cta"><p class="comenta">Comenta</p><div class="kw">TALLER</div>'
    '<div class="kwul"></div>'
    '<p class="give">y te llevo a mi taller para<br>crear <span class="ul">tus fotos y contenido</span><br>con IA, sin que cambie tu cara.</p></div>' +
    rayos(80, 470, 90, "izq") + rayos(940, 470, 90, "der") +
    '<svg class="dd" style="left:120px;top:1010px;width:120px;height:150px" viewBox="0 0 100 130"><path d="M10 6 Q20 80 80 110"/><path d="M58 112 L82 112 L74 90"/></svg>'
    '<svg class="dd" style="left:860px;top:1010px;width:120px;height:150px;transform:scaleX(-1)" viewBox="0 0 100 130"><path d="M10 6 Q20 80 80 110"/><path d="M58 112 L82 112 L74 90"/></svg>'))

CSS = r"""
:root{--paper:#efebe3;--paper2:#e3ddd2;--ink:#14279a;--rule:#9fb5cf;--margin:#d9534f;
  --f:'Patrick Hand',cursive;--f2:'Gochi Hand',cursive}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#777;display:flex;flex-direction:column;gap:40px;align-items:center;padding:40px 0}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--ink);font-family:var(--f);
  background:radial-gradient(ellipse at 60% 40%,#f4f1ea 30%,var(--paper) 70%,var(--paper2) 100%)}
.lines{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,transparent 0 41px,var(--rule) 41px 42.4px);background-position:0 30px;opacity:.75;filter:url(#temblor)}
.margin{position:absolute;top:0;bottom:0;left:74px;width:1.6px;background:var(--margin);opacity:.75;filter:url(#temblor)}
.hole{position:absolute;left:20px;width:34px;height:34px;border-radius:50%;background:radial-gradient(circle at 50% 55%,#fbfaf7 0 50%,#d6d0c5 68%,#b7afa3 100%);box-shadow:inset 2px 3px 4px rgba(0,0,0,.28)}
.grain{position:absolute;inset:0;pointer-events:none;mix-blend-mode:multiply;opacity:.32;z-index:9;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.012' numOctaves='4' seed='5'/><feDiffuseLighting lighting-color='white' surfaceScale='2.2'><feDistantLight azimuth='225' elevation='55'/></feDiffuseLighting></filter><rect width='400' height='400' filter='url(%23n)'/></svg>");background-size:1080px 1350px}
svg.dd{position:absolute;z-index:2;fill:none;stroke:var(--ink);stroke-width:4.2;stroke-linecap:round;stroke-linejoin:round;overflow:visible;filter:url(#rough)}
.hdl{position:absolute;z-index:3;left:50%;bottom:44px;transform:translateX(-50%);font-size:46px;white-space:nowrap;-webkit-text-stroke:1.5px var(--ink)}
.hdl svg.dd{width:60px;height:60px;stroke-width:5}
.ink{filter:url(#pulso)}
.big{font-family:var(--f);font-weight:400;line-height:1.08;-webkit-text-stroke:9px var(--ink);paint-order:stroke fill;letter-spacing:1px;filter:url(#pulso);
  text-shadow:3px 2px 0 var(--ink),-2px 3px 0 var(--ink),1px -2px 0 var(--ink)}
.ul{background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 20' preserveAspectRatio='none'><path d='M1 6 Q30 2 60 5 T99 4' fill='none' stroke='%2314279a' stroke-width='2.4' stroke-linecap='round'/><path d='M4 14 Q35 10 62 13 T97 12' fill='none' stroke='%2314279a' stroke-width='1.6' stroke-linecap='round'/></svg>") left 100%/100% 18px no-repeat;padding-bottom:12px}
.gancho{position:absolute;z-index:3;left:100px;right:20px;top:285px;text-align:center}
.gancho .big{font-size:136px;line-height:1.2}
.pase{font-size:76px;margin-top:36px;-webkit-text-stroke:2.5px var(--ink)}
.centro{position:absolute;z-index:3;left:100px;right:20px;top:250px;text-align:center}
.b2{font-size:172px;line-height:1.1}
.caps{letter-spacing:4px}
.sub{font-size:86px;line-height:1.2;margin-top:60px;-webkit-text-stroke:3px var(--ink)}
/* hoja de referencia */
.tit2{position:absolute;z-index:3;left:96px;right:20px;top:58px;text-align:center;font-size:68px;line-height:1.1;white-space:nowrap;-webkit-text-stroke:5px var(--ink);paint-order:stroke fill;filter:url(#pulso);font-weight:400}
.sheet{position:absolute;z-index:3;left:100px;right:36px;top:165px;bottom:120px;display:grid;grid-template-columns:1.55fr 1fr;grid-template-rows:auto 1fr auto;gap:14px}
.bx{position:relative;border:2.5px solid var(--ink);padding:10px 14px;filter:url(#rough);background:rgba(255,255,255,.08)}
.bt{display:block;font-weight:400;font-size:26px;letter-spacing:1px;margin-bottom:6px;-webkit-text-stroke:.5px var(--ink)}
.bt::after{content:" ≡";font-size:22px}
.ficha .cols{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;font-size:23px;line-height:1.05}
.ficha small{display:block;font-size:17px;opacity:.85}
.paleta .sw{display:flex;gap:8px;margin-top:6px}
.paleta i{width:44px;height:44px;border:2px solid var(--ink);background:repeating-linear-gradient(45deg,var(--ink) 0 2px,transparent 2px 6px)}
.paleta i:nth-child(1){background:var(--ink)}.paleta i:nth-child(3){background:repeating-linear-gradient(45deg,var(--ink) 0 1.5px,transparent 1.5px 10px)}
.paleta i:nth-child(4){background:#1c1c3a}.paleta i:nth-child(5){background:transparent}
.vistas{grid-row:2}.vrow{display:flex;gap:10px;height:calc(100% - 40px)}
.vrow figure{flex:1;display:flex;flex-direction:column;align-items:center;min-width:0}
.vrow img,.vrow .hueco{flex:1;width:100%;min-height:0;object-fit:cover;object-position:52% 0}
.vrow figure:first-child{flex:1.6}
figure{margin:0}figcaption{font-size:20px;letter-spacing:1px;text-align:center;margin-top:4px}
.hueco{border:2px dashed var(--ink);display:flex;align-items:center;justify-content:center;text-align:center;font-size:20px;line-height:1.05;opacity:.75;padding:4px}
.expr{grid-row:1/2;grid-column:2}
.egrid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.egrid img,.egrid .hueco{width:100%;height:70px;object-fit:cover;object-position:50% 20%;border:1.5px solid var(--ink)}
.egrid figcaption{font-size:15px}
.paleta{display:none}
.detalle{grid-row:2;grid-column:2}
.detalle img.det{width:100%;height:calc(100% - 44px);object-fit:cover;object-position:50% 20%}
.detalle{overflow:hidden}
.look{grid-column:1/3;grid-row:3}
.lgrid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.lgrid img,.lgrid .hueco{width:100%;height:118px;object-fit:cover;border:1.5px solid var(--ink)}
.ficha{grid-column:1;grid-row:1}
img.sk{display:block}
.s2 .hdl{bottom:34px;font-size:38px}
/* slide 5 */
.tripode{position:absolute;z-index:2;left:770px;top:70px;filter:url(#rough)}
.tel{width:170px;height:290px;border:4px solid var(--ink);border-radius:24px;padding:12px 8px;background:rgba(255,255,255,.15);transform:rotate(4deg)}
.tel .telimg{width:100%;height:100%;object-fit:cover;object-position:50% 25%;border-radius:10px}
.pata{position:relative;width:5px;height:110px;background:var(--ink);margin:-4px auto 0}
.pata::before,.pata::after{content:'';position:absolute;bottom:-40px;width:5px;height:60px;background:var(--ink)}
.pata::before{left:-14px;transform:rotate(25deg)}.pata::after{left:14px;transform:rotate(-25deg)}
.abajo{position:absolute;z-index:2;left:40px;bottom:-40px;width:360px}
.s5 .sub{margin-top:34px;font-size:68px;padding:0 170px 0 150px}
/* CTA */
.cta{position:absolute;z-index:3;left:96px;right:20px;top:170px;text-align:center}
.comenta{font-size:140px;-webkit-text-stroke:8px var(--ink);paint-order:stroke fill;filter:url(#pulso)}
.kw{font-family:var(--f);font-size:310px;line-height:1;letter-spacing:4px;margin-top:0;color:transparent;-webkit-text-stroke:10px var(--ink);
  background:repeating-linear-gradient(68deg,var(--ink) 0 4px,transparent 4px 8px),repeating-linear-gradient(-22deg,var(--ink) 0 3px,transparent 3px 10px);
  -webkit-background-clip:text;background-clip:text;filter:url(#rough)}
.kwul{height:24px;margin:6px 40px 0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 20' preserveAspectRatio='none'><path d='M1 5 Q30 1 60 4 T99 3' fill='none' stroke='%2314279a' stroke-width='3' stroke-linecap='round'/><path d='M3 14 Q35 10 62 13 T98 11' fill='none' stroke='%2314279a' stroke-width='2' stroke-linecap='round'/></svg>") center/100% 100% no-repeat}
.give{font-size:72px;line-height:1.22;margin-top:50px;padding:0 60px;-webkit-text-stroke:2.5px var(--ink)}
"""

JS = r"""
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
function jitter(el){[...el.childNodes].forEach(n=>{
  if(n.nodeType===3){const f=document.createDocumentFragment();
    n.textContent.split(/(\s+)/).forEach(p=>{if(!p)return;if(/^\s+$/.test(p)){f.append(document.createTextNode(' '));return}
      const w=document.createElement('span');w.style.cssText='display:inline-block;white-space:nowrap';
      [...p].forEach(c=>{const s=document.createElement('span');s.textContent=c;s.style.display='inline-block';
        s.style.transform=`translateY(${(rnd()-.5)*5}px) rotate(${(rnd()-.5)*5}deg) scale(${.96+rnd()*.08})`;w.append(s)});f.append(w)});
    n.replaceWith(f)} else if(n.nodeType===1&&!['svg','IMG','BR'].includes(n.tagName)&&!n.classList.contains('kw'))jitter(n)})}
document.fonts.ready.then(()=>document.querySelectorAll('.big,.sub,.pase,.give,.comenta,.tit2').forEach(jitter));
"""

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Carrusel cara con IA</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Gochi+Hand&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<svg width="0" height="0" style="position:absolute">
 <filter id="rough" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="3"/></filter>
 <filter id="pulso" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="9"/><feDisplacementMap in="SourceGraphic" scale="2.4"/></filter>
 <filter id="temblor"><feTurbulence type="fractalNoise" baseFrequency="0.006 0.002" numOctaves="1" seed="7"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter>
</svg>
{''.join(S)}
<script>{JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("carrusel.html").write_text(html, encoding="utf-8")
print("ok")
