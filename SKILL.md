---
name: clonar-carrusel
description: Modela un carrusel viral de Instagram adaptándolo a la marca, la voz y la oferta de una persona. Empieza con una entrevista corta (máximo 10 preguntas, por texto o nota de voz), captura los slides del post original, saca su ADN (gancho, estructura, diseño), reescribe el copy y renderiza PNG de 1080x1350 con hoja de comparación y caption listo. También guarda estilos en una biblioteca con catálogo visual y replica el estilo que la persona elija con temas nuevos, sin necesidad de un link (registrar métricas es opcional). Úsala siempre que alguien pase un link de instagram.com/p/… y pida "modelar", "clonar", "hacer uno igual", "adaptar este carrusel", "algo así para mi marca", o quiera crear un carrusel viral para ganar seguidores o llevar gente a un curso, taller, mentoría o producto, o pida "guardar este estilo", "usa mi estilo de…", "hazme otro como el de cuaderno", "qué estilos tengo guardados", aunque no diga "skill" ni "clonar".
---

# Clonar / modelar carruseles virales

El flujo toma un carrusel que ya funcionó y lo convierte en uno propio: misma estructura, ritmo y estética, pero con el tema, la voz, las pruebas y la oferta de la persona. El valor no está en copiar, sino en entender **por qué** funcionó el original y ponerlo al servicio de lo que la persona quiere lograr. Por eso empieza con una entrevista.

## Qué modo usar

| La persona… | Modo |
|---|---|
| pasa un link y quiere su versión | **Modelar**: pasos 0 a 6 |
| sube uno o varios carruseles "para guardarlos" | **Guardar estilos**: pasos 1, 2 y 4 por cada uno, y luego guardar (ver `references/estilos.md`) |
| pide un tema "con el estilo X" o "con uno de mis estilos" | **Replicar**: entrevista corta (solo tema, objetivo y CTA), el estilo lo elige la persona (§2: catálogo si no dijo cuál), luego `references/estilos.md` §4 y los pasos 3 a 6 |
| pregunta qué estilos tiene | **Catálogo**: `estilos.py catalogo` y mándale la imagen |
| pasa métricas por su cuenta (opcional) | **Rendimiento**: `references/estilos.md` §3; no las pidas |

Si la persona ya tiene estilos guardados (`carruseles/estilos/`) y pide un carrusel nuevo sin link, pregúntale en la entrevista si quiere modelar uno nuevo o usar uno de sus estilos. Mándale el catálogo visual.

## Paso 0: entrevista

Lee `references/entrevista.md` y haz la entrevista **antes de capturar nada**: máximo 10 preguntas, todas en un mensaje, que se puedan contestar por texto o nota de voz. Si ya existe `perfil.json` de esta persona, muestra el resumen y pregunta solo lo que cambia para este carrusel.

Si la persona dice "arranca sin preguntas" o ya dio todo el contexto, no la frenes: usa supuestos, márcalos como `[SUPUESTO]` y sigue.

Si mandan una nota de voz y no puedes transcribirla en este entorno, pídele que use el dictado del teléfono y pegue el texto.

## Paso 1: capturar

```bash
node scripts/capturar.js "<url del post>" carruseles/<codigo>/original
```

Usa la ruta absoluta de `scripts/` dentro de esta skill. Playwright y Chromium deben estar instalados (`node -e "require('playwright')"`).

Lo que ya sabemos que puede pasar:
- **`ERR_TUNNEL_CONNECTION_FAILED` o 403**: el acceso de red del entorno no permite instagram.com ni cdninstagram.com. Dile a la persona cómo habilitarlos y detente; no inventes slides.
- **El embed puede traer menos slides que el post.** Compara con la numeración visible: si la portada dice "01/08" y las demás "/10", la portada manda (el "/10" sobra de un borrador). Si de verdad faltan slides, dilo en vez de rellenar.
- **El script ya resuelve** el JSON con doble escape (`\\u0026`, `\\/`) y el proxy: el navegador se lanza con `HTTPS_PROXY`. Si cambias el script, conserva ambas cosas.
- El caption original queda en `caption_original.txt`. Ahí suele estar el CTA cuando no aparece en las slides.

## Paso 2: ADN (`adn.json`)

Mira **cada** slide con la herramienta de imágenes. Saca:
- el texto de cada slide y su número de palabras,
- la paleta en hex (muestréala con PIL, no la adivines),
- el fondo, las tipografías y la Google Font más parecida, la jerarquía de tamaños, los márgenes y los recursos que se repiten.

En la narrativa, anota:
- el tipo de carrusel,
- la **fórmula del gancho**,
- el rol de cada slide,
- cómo se engancha cada slide con la siguiente,
- el tipo de CTA,
- de 3 a 5 razones de por qué funciona.

Dale a la persona un resumen de 5 a 8 líneas.

## Paso 3: copy (`copy.md`)

- **Fidelidad**: según la respuesta de la entrevista.
  - *Espejo*: conserva el gancho traducido y adaptado, y los mismos roles y recursos por slide.
  - *Inspirado*: propone 3 ángulos que encajen con la estructura y con el negocio, elige el más fuerte y explica por qué en una línea.
- En los dos modos, **el cuerpo, los nodos, los ejemplos y los datos se escriben desde cero** con la voz y el negocio de la persona. Traducir frase por frase el contenido de otro creador es copiarlo, se nota y le resta autoridad a quien lo publica.
- **Mismo número de slides y misma densidad** (±30% de palabras). Escribe 3 variantes de gancho con la misma fórmula y usa la mejor.
- **Solo pruebas reales**: cifras, casos y herramientas que la persona usa de verdad. Si la persona tiene un flujo o una skill propia relacionada, léela y describe ese proceso real en vez del proceso del original. Lo que falte va como `[DATO A CONFIRMAR]`.
- **Las capturas de UI con datos de ejemplo** (tiempos, nombres de archivo) avísalas como ilustrativas.
- **Voz**: la de la persona, con su trato (tú o usted), sin jerga corporativa. Si la persona tiene una skill de voz propia, úsala. Si sus reglas de voz chocan con el pedido (por ejemplo "sin hashtags" o "sin promesas de ingreso" frente a un gancho de "imprimen dinero"), avisa del choque, recomienda una opción y deja la decisión a la persona.
- **CTA**: la palabra clave y la oferta de la entrevista ("Comenta PALABRA y te ___"). Ponlo en la última slide aunque el modelo lo tenga solo en el caption.
- Guarda en `copy.md`:
  - una tabla (slide | rol | original | nuevo),
  - las variantes de gancho,
  - el caption (gancho, de 3 a 5 líneas de valor y el CTA),
  - los pendientes.

## Paso 4: diseño (`carrusel.html` → PNG)

- Usa un `<section class="slide">` de 1080x1350 por slide, con los tokens en `:root` y Google Fonts.
- Replica la composición de cada slide del modelo. Pon el handle de la persona donde el modelo pone el suyo.
- **Fotos**: si la persona dio una foto, cópiala a la carpeta del proyecto y úsala. Encuádrala para que ningún texto ni tarjeta le tape la cara, y funde el borde con `mask-image` si queda un corte visible. Si no hay foto, deja un recuadro punteado con la descripción de la foto que debe tomar.
- **Logos de marcas ajenas**: no los dibujes. Usa íconos genéricos más el nombre.
- **Títulos que deben caber en una línea**: un script que reduzca el `font-size` hasta que `scrollWidth` quepa (render.js espera 400 ms a que corra).
- Si el diseño se repite slide a slide (mapas, íconos), genera el HTML con un pequeño script en Python, así cada ajuste se aplica a todas las slides a la vez.

```bash
node scripts/render.js carrusel.html final/
```

Si alguna línea sale con `⚠ texto desbordado`, corrige y vuelve a renderizar.

## Paso 5: control de calidad

```bash
python3 -I scripts/comparar.py original/ final/ comparacion.png
```

Mira la hoja de comparación y después las slides más densas a tamaño completo. Revisa:
- que el estilo se reconozca a primera vista,
- que el texto se lea en el celular,
- que nada quede cortado, encimado ni le tape la cara a nadie,
- que no haya frases copiadas.

Corrige hasta que pase. Los problemas típicos son títulos que se parten encima del cuerpo, contornos de texto feos (usa `text-shadow` en vez de `-webkit-text-stroke` en letra pequeña) y mucho espacio vacío frente al original.

## Paso 6: entrega

1. Envía `comparacion.png` y los PNG finales.
2. Pega en el chat el caption listo para copiar y 2 ganchos alternativos.
3. Lista los `[DATO A CONFIRMAR]` y los pendientes: fotos, datos de la oferta, auto-DM activo.
4. Cierra con una recomendación estratégica de una línea, conectada con su objetivo.

Al final, ofrece en una línea guardar el carrusel como estilo en su biblioteca para reutilizarlo con otros temas.

Para cambios posteriores, edita el HTML o el script que lo genera, vuelve a renderizar y reenvía solo lo que cambió.

## Estructura de carpetas

```
carruseles/
├── perfil.json                 # respuestas de la entrevista (se reutiliza)
├── estilos/                    # biblioteca de estilos (ver references/estilos.md)
└── <codigo_del_post>/
    ├── original/               # slides capturados + caption_original.txt
    ├── adn.json
    ├── copy.md
    ├── carrusel.html (+ build.py si lo generas por script)
    ├── final/                  # PNG 1080x1350
    └── comparacion.png
```
