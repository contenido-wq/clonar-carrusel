import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__))
# Iconos en línea blanca: componentes SVG simples
S='stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"'
def box(x,y,w,h,r=8): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" {S}/>'
def lines(x,y,w,n=3,gap=14): return ''.join(f'<line x1="{x}" y1="{y+i*gap}" x2="{x+w*(1 if i<n-1 else .6)}" y2="{y+i*gap}" {S}/>' for i in range(n))
def arrow(x1,y1,x2,y2): 
    import math;a=math.atan2(y2-y1,x2-x1);l=10
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {S}/><polyline points="{x2-l*math.cos(a-.5)},{y2-l*math.sin(a-.5)} {x2},{y2} {x2-l*math.cos(a+.5)},{y2-l*math.sin(a+.5)}" {S}/>'
def env(x,y,w=70,h=48): return box(x,y,w,h,5)+f'<polyline points="{x},{y} {x+w/2},{y+h*.55} {x+w},{y}" {S}/>'
def doc(x,y,w=80,h=104): return box(x,y,w,h,6)+lines(x+14,y+22,w-28,5,15)
def wave(x,y,w=110,h=70):
    import random;random.seed(3);o='';n=22
    for i in range(n):
        hh=h*(.15+.85*abs(__import__('math').sin(i*.55))*random.uniform(.5,1));xx=x+i*w/n
        o+=f'<line x1="{xx}" y1="{y+h/2-hh/2}" x2="{xx}" y2="{y+h/2+hh/2}" {S}/>'
    return o
def chat(x,y,w=90,h=56): return box(x,y,w,h,10)+f'<polyline points="{x+18},{y+h} {x+12},{y+h+14} {x+34},{y+h}" {S}/>'+''.join(f'<circle cx="{x+w/2+d}" cy="{y+h/2}" r="3" fill="#fff"/>' for d in (-16,0,16))
def win(x,y,w,h): return box(x,y,w,h,8)+f'<line x1="{x}" y1="{y+20}" x2="{x+w}" y2="{y+20}" {S}/>'+''.join(f'<circle cx="{x+12+i*12}" cy="{y+10}" r="2.5" fill="#fff"/>' for i in range(3))
def person(cx,cy,r=16): return f'<circle cx="{cx}" cy="{cy}" r="{r}" {S}/><path d="M{cx-r*1.8} {cy+r*3} Q{cx} {cy+r*1.2} {cx+r*1.8} {cy+r*3}" {S}/>'
def cal(x,y,w=80,h=80): return box(x,y,w,h,8)+f'<line x1="{x}" y1="{y+22}" x2="{x+w}" y2="{y+22}" {S}/>'+''.join(f'<rect x="{x+12+(i%3)*22}" y="{y+32+(i//3)*20}" width="12" height="10" rx="2" {S}/>' for i in range(6))
def clip(x,y): return f'<rect x="{x}" y="{y}" width="64" height="40" rx="6" {S}/><polygon points="{x+26},{y+10} {x+42},{y+20} {x+26},{y+30}" fill="#fff"/>'
def sparkle(cx,cy,r=14): return f'<path d="M{cx} {cy-r} L{cx+r*.25} {cy-r*.25} L{cx+r} {cy} L{cx+r*.25} {cy+r*.25} L{cx} {cy+r} L{cx-r*.25} {cy+r*.25} L{cx-r} {cy} L{cx-r*.25} {cy-r*.25}Z" {S}/>'
def svg(inner,w=760,h=420): return f'<svg class="dg" viewBox="0 0 {w} {h}" width="{int(w*1.24)}" height="{int(h*1.24)}">{inner}</svg>'

D={}
# 1 voz: wave -> brain/skill -> 4 outputs
D[1]=svg(wave(40,175)+arrow(170,210,250,210)+box(260,150,170,120,14)+'<text x="345" y="205" fill="#fff" font-family="Instrument Serif" font-size="30" text-anchor="middle">mi voz</text><text x="345" y="240" fill="#fff" font-family="Instrument Serif" font-size="22" text-anchor="middle" opacity=".7">skill</text>'
 +''.join(arrow(430,210,540,60+i*100) for i in range(4))+chat(560,30)+box(560,128,140,56,8)+lines(575,148,110,2,16)+env(565,232)+doc(580,320,60,80))
# 2 clonar carrusel: phone carousel -> clone -> my carousel
D[2]=svg(box(40,90,150,240,18)+box(60,120,110,140,6)+lines(70,280,90,2,14)+arrow(200,210,290,210)+''.join(box(300+i*14,130+i*14,140,170,8) for i in range(3))+arrow(470,210,560,210)+box(570,90,150,240,18)+box(590,120,110,140,6)+sparkle(645,190,26)+lines(600,280,90,2,14))
# 3 reels: raw clip -> cuts -> subtitled
D[3]=svg(clip(40,180)+box(30,150,90,100,10)+arrow(130,200,220,200)+''.join(box(230+i*60,170,48,60,6) for i in range(4))+'<line x1="290" y1="160" x2="290" y2="240" stroke="#fff" stroke-width="2.4" stroke-dasharray="6 6"/>'+arrow(480,200,560,200)+box(570,60,150,280,18)+box(590,90,110,160,6)+'<rect x="600" y="262" width="90" height="16" rx="4" fill="#fff"/><rect x="615" y="286" width="60" height="12" rx="4" fill="#fff" opacity=".6"/>')
# 4 lead magnet: idea doc -> PDF pages stack -> DM
D[4]=svg(doc(40,150)+arrow(140,200,230,200)+''.join(box(240+i*26,110+i*12,150,200,8) for i in range(3))+lines(310,180,100,6,18)+arrow(460,210,550,210)+chat(570,150,130,80)+env(600,270,70,48))
# 5 AIVI estrategia: funnel 3 tiers
D[5]=svg('<polygon points="120,40 640,40 560,150 200,150" '+S+'/><polygon points="220,170 540,170 480,270 280,270" '+S+'/><polygon points="300,290 460,290 420,390 340,390" '+S+'/>'+''.join(person(260+i*80,90,12) for i in range(4))+chat(320,195,60,40)+chat(400,195,60,40)+env(345,315,70,45))
# 6 WhatsApp agente: message -> agent -> tags -> calendar
D[6]=svg(chat(40,170,100,64)+arrow(150,200,240,200)+box(250,120,170,170,16)+sparkle(335,190,34)+'<text x="335" y="265" fill="#fff" font-family="Instrument Serif" font-size="24" text-anchor="middle">agente</text>'+arrow(420,160,530,80)+arrow(420,205,530,205)+arrow(420,250,530,330)+box(540,55,170,50,25)+'<text x="625" y="88" fill="#fff" font-family="Inter" font-size="20" text-anchor="middle">lead caliente</text>'+box(540,180,170,50,25)+'<text x="625" y="213" fill="#fff" font-family="Inter" font-size="20" text-anchor="middle">cliente</text>'+cal(585,300))
# 7 biblioteca por cliente: folders grid
D[7]=svg(''.join(f'<path d="M{60+(i%3)*230} {60+(i//3)*170} h60 l14 16 h106 v110 h-180z" {S}/>'+person(150+(i%3)*230,130+(i//3)*170,12) for i in range(6)))
# 8 morning brief: mail, calendar, notion -> brief doc
D[8]=svg(env(40,60)+cal(40,170)+box(40,290,80,80,10)+'<text x="80" y="345" fill="#fff" font-family="Instrument Serif" font-size="48" text-anchor="middle">N</text>'+arrow(130,90,300,190)+arrow(130,210,300,210)+arrow(130,330,300,230)+box(310,110,180,210,14)+'<text x="400" y="155" fill="#fff" font-family="Instrument Serif" font-size="30" text-anchor="middle">brief</text>'+lines(335,190,130,6,18)+arrow(500,210,590,210)+person(650,180,26))

items=[
("Mi voz vive en una skill","Le hablo a Claude y todo sale sonando a mí.","Guiones, captions, correos y respuestas a clientes.|Le entrené mi tono una vez y ahora lo usa siempre.|No reescribo nada para que suene a mí."),
("Clono carruseles virales","Lo que funcionó, adaptado a mi tema y mi voz.","Paso el link de un carrusel que se volvió viral.|Claude saca su estructura y lo rehace con mi oferta.|Lo tengo listo para publicar el mismo día."),
("Edito reels sin abrir CapCut","Una skill corta silencios y tomas repetidas.","Subo el video crudo.|Me lo devuelve cortado, con subtítulos y animaciones.|Yo solo reviso y publico."),
("Mis lead magnets se diseñan solos","De la idea al PDF regalo en minutos.","Le doy el tema y Claude escribe la guía.|Otra skill la diseña con mi marca y mi foto.|La reparto por mensaje directo a quien comenta."),
("AIVI arma mi estrategia","Cada semana sé qué publicar y para qué.","Contenido para atraer gente nueva.|Contenido para conectar con mi comunidad.|Contenido para vender: el que pide que comenten."),
("Mi WhatsApp responde solo","Un agente de IA atiende y etiqueta a cada lead.","Responde las preguntas de siempre.|Etiqueta quién está listo para comprar.|Yo entro solo a las conversaciones que valen la pena."),
("Cada cliente tiene su biblioteca","Sus estilos guardados, su marca, sus reglas.","Marca de agua, colores y voz de cada cliente.|Las reglas que no se rompen, por ejemplo: cero azúcar.|Pido 'la parte 2' y sale igual a la parte 1."),
("Mi día empieza con un brief","Claude revisa mi correo, mi agenda y Notion.","Me dice qué es urgente y qué puede esperar.|Me prepara las reuniones del día.|Yo me enfoco en crear y en vender."),
]
WM='<div class="wm">@jheitrujillob</div>'
out=[f'''<section class="slide cover"><img class="bg" src="foto/cover.jpg"><div class="shade"></div>
<div class="ct"><p class="t1">8 sistemas aburridos<br>que mueven mi negocio</p><p class="t2">mientras voy en el ascensor</p></div>{WM}</section>''']
for i,(t,sub,body) in enumerate(items,1):
    ps=''.join(f'<p>{x}</p>' for x in body.split('|'))
    out.append(f'''<section class="slide"><img class="bg" src="foto/bg.jpg"><div class="num">( 0{i} )</div><h2>{t}</h2><p class="sub">{sub}</p><div class="dgw">{D[i]}</div><div class="bt">{ps}</div>{WM}</section>''')
out.append(f'''<section class="slide"><img class="bg" src="foto/bg.jpg"><h2 style="top:110px;font-size:84px">¿Quieres montar<br>estos sistemas?</h2>
<div class="stack">{''.join(f'<div class="pg" style="left:{i*70}px;top:{i*14}px"><span class="tag">TALLER · IA</span><b>Contenido que vende con IA</b><i></i><i></i><i></i><i class="s"></i><i></i><i class="s"></i></div>' for i in range(4))}</div>
<p class="cta">comenta <em>“TALLER”</em><br>y te llevo a mi taller</p>{WM}</section>''')
head=open(_os.path.join(_D, 'head.html')).read()
open(_os.path.join(_D, 'carrusel.html'),'w').write(head+'\n'.join(out)+'</body></html>')
