import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__))
import sys;sys.path.insert(0,_D);from md_es import MD
skills=[
("Frontend Design","La skill oficial de Anthropic: páginas con dirección visual clara, que no se ven hechas con IA","frontend-design","anthropics/skills › frontend-design"),
("Canvas Design","Pósters y piezas gráficas en PNG o PDF, a partir de una idea de diseño","canvas-design","anthropics/skills › canvas-design"),
("PPTX","Crea y edita presentaciones y pitch decks en PowerPoint","pptx","anthropics/skills › pptx"),
("XLSX","Hojas de cálculo con fórmulas y gráficos, o limpia las que ya tienes","xlsx","anthropics/skills › xlsx"),
("DOCX","Propuestas, contratos y documentos en Word con formato profesional","docx","anthropics/skills › docx"),
("PDF","Lee, une, separa y llena PDFs, y saca tablas y texto de ellos","pdf","anthropics/skills › pdf"),
("Theme Factory","10 temas de colores y fuentes listos para tus slides, documentos y páginas","theme-factory","anthropics/skills › theme-factory"),
("Brand Guidelines","Aplica colores y tipografías de marca. Trae la de Anthropic: úsala de molde para la tuya","brand-guidelines","anthropics/skills › brand-guidelines"),
("Skill Creator","Crea tus propias skills, pruébalas y mejóralas","skill-creator","anthropics/skills › skill-creator"),
("Clonar Carrusel","La mía: modela un carrusel viral con tu tema, tu voz y tu oferta. Exclusiva de mi taller","clonar-carrusel","EXCLUSIVA"),
]
LINK='<svg viewBox="0 0 24 24" width="30" height="30"><path d="M10 14a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1 1M14 10a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1-1" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/></svg>'
foot=lambda link:(f'<div class="foot"><span class="hw">Link<br>directo ↘</span><span class="pill">{LINK}{link}</span></div><div class="sw">DESLIZA ⟳</div>' if link!='EXCLUSIVA' else '<div class="foot"><span class="hw">Link en<br>mi perfil ↘</span><span class="pill" style="background:#f2541b;border-color:#f2541b">Solo en mi Taller</span></div><div class="sw">DESLIZA ⟳</div>')
WM='<div class="wm">@jheitrujillob</div>'
def inner(f):
    if f=='clonar-carrusel': return '<div class="shot lock" style="background-image:url(shots/md_clonar-carrusel.jpg)"></div><div class="lk2"><svg viewBox="0 0 24 24" width="86" height="86"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="#f2541b"/><path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="#f2541b" stroke-width="2.4"/></svg><p>Solo para alumnos del<br><b>Taller de contenido que vende con IA</b></p></div>'
    if f not in MD: return f'<div class="shot" style="background-image:url(shots/md_{f}.png)"></div>'
    m=MD[f]
    return f'''<div class="gh"><div class="crumb"><span class="lk">skills</span> / <span class="lk">skills</span> / <span class="lk">{f}</span> / <b>SKILL.md</b></div><div class="md"><table class="fm"><tr><th>nombre</th><td>{f}</td></tr><tr><th>descripción</th><td>{m["desc"]}</td></tr><tr><th>licencia</th><td>{m["lic"]}</td></tr></table>{m["body"]}</div></div>'''
out=[]
out.append(f'''<section class="slide cover"><img class="bg" src="cover_pixel.png">{WM}
<div class="cc"><p class="hw g" style="font-size:66px">Selección de</p><p class="ct">10 skills<br>de Claude</p><p class="hw g" style="font-size:66px">para tu negocio · Parte 1</p></div></section>''')
for i,(t,d,f,link) in enumerate(skills,1):
    out.append(f'''<section class="slide sk">{WM}<div class="num">{i:02d}/10</div>
<h2>{t}</h2><p class="sub">{d}</p>
<div class="win"><div class="bar"><i></i><i></i><i></i></div>{inner(f)}</div>
{foot(link)}</section>''')
out.append(f'''<section class="slide promo">{WM}<div class="pc">
<p class="pk">¿No sabes por dónde empezar?</p>
<p class="pt">Taller de contenido que vende con IA</p>
<p class="pd">Te enseño a usar Claude para crear el contenido de tu negocio: estrategia, guiones, carruseles y más.</p>
<p class="hw" style="font-size:64px;margin-top:40px">Link en <span class="bio">MI PERFIL</span></p></div></section>''')
out.append(f'''<section class="slide cta">{WM}<div class="ccx">
<p class="q">¿Quieres los links?</p>
<p class="hw" style="font-size:72px;margin-top:70px">Comenta ↘</p>
<p class="kw">SKILLS</p>
<p class="hw" style="font-size:64px;line-height:1.15">y te los envío<br>por mensaje directo</p></div>
<div class="sfoot"><span>SÍGUEME PARA LA PARTE 2</span><span>DESLIZA ⟳</span></div></section>''')
out.append(f'''<section class="slide quote">{WM}<p class="qt">El diseño no es solo cómo se ve. El diseño es cómo funciona.</p><p class="qa hw">Steve Jobs</p>
<div class="sfoot" style="color:#5a3c3a"><span>SÍGUEME PARA MÁS</span><span>GUARDA ESTE POST ▮</span></div></section>''')
head=open(_os.path.join(_D, 'head.html')).read()
open(_os.path.join(_D, 'carrusel.html'),'w').write(head+'\n'.join(out)+'</body></html>')
