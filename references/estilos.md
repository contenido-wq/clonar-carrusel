# Biblioteca de estilos

Un **estilo** es un carrusel ya resuelto (diseño, estructura de slides, fórmula del gancho y plantilla que renderiza) guardado con nombre para reutilizarlo con otros temas. La biblioteca vive en `carruseles/estilos/`, una carpeta por estilo:

```
carruseles/estilos/<id>/
├── estilo.json      # nombre, modelo de origen, ADN completo, nota, rendimiento[]
├── plantilla.html   # el carrusel tal como quedó (renderiza solo)
├── build.py         # si el HTML se generó por script
├── muestras/        # los PNG finales, para comparar y para mostrar el estilo
└── fotos, fuentes   # recursos que usa la plantilla
```

Todo pasa por `scripts/estilos.py` (corre desde la carpeta del cliente o pasa `--bib`).

## 1. Guardar un estilo

**Cuándo:** al terminar un carrusel, ofrécelo en una línea ("¿Lo guardo como estilo para reutilizarlo con otros temas?"). También cuando la persona sube varios carruseles solo para guardarlos.

```bash
python3 -I scripts/estilos.py guardar carruseles/<codigo> "Nombre del estilo" --nota "para qué sirve"
# si el HTML o el build tienen otro nombre: --html carrusel_v2.html --build build_v2.py --final final_v2
```

- **El nombre** debe decir cómo se ve y para qué sirve ("Cuaderno mapas mentales", "Tutorial paso a paso UI"), no el tema del post. El tema cambia; el estilo es lo que se repite.
- **La nota** explica para qué contenido funciona ("marcos de 4 categorías", "mostrar un flujo con IA"). Así, al elegir estilo para un tema nuevo, se ve cuál encaja.
- **Si suben varios links solo para guardarlos:** por cada uno corre los pasos 1 (captura), 2 (ADN) y 4 (diseño) con un copy mínimo de la persona, y guarda el estilo. No hace falta el copy completo ni el caption, pero sí una plantilla que renderice, porque sin eso no se puede reutilizar. Si son muchos, hazlos uno por uno y confirma el nombre de cada uno en un solo mensaje al final.

## 2. Elegir qué estilo replicar

**La persona elige.** Ella conoce su audiencia y sabe qué le funcionó, así que no hace falta pedirle estadísticas para decidir.

```bash
python3 -I scripts/estilos.py catalogo carruseles/estilos/catalogo_estilos.png   # portada + 2 slides de cada estilo
python3 -I scripts/estilos.py listar                                             # versión en texto, con la nota de cada uno
```

- **Si nombró el estilo** ("con el de cuaderno", "el tutorial"), úsalo directamente. Si el nombre es ambiguo, toma el más parecido y dilo en una línea.
- **Si no dijo cuál** ("hazme uno sobre X con uno de mis estilos"), mándale el catálogo y pregúntale por número o por nombre. Puedes recomendar uno según qué tan bien encaje la estructura con el tema (por ejemplo, el de 4 categorías para un marco o el tutorial para mostrar un proceso), pero la decisión es suya.
- **Si el estilo que eligió no encaja bien con el tema** (por ejemplo, el tema trae 3 puntos y el estilo es de 4 categorías), adáptalo sin romper el estilo. Explica cómo lo resolviste y márcalo como `[SUPUESTO]`.

## 3. Rendimiento (opcional)

Solo si la persona lo pide o pasa sus números por iniciativa propia. **No le pidas estadísticas.** Sirve para quien quiere que el ranking le sugiera estilos con datos:

```bash
python3 -I scripts/estilos.py rendimiento "Nombre" --alcance 20000 --guardados 900 --palabra 180 ...
python3 -I scripts/estilos.py ranking --objetivo leads   # seguidores | autoridad | venta
```

- Todo se compara por cada 1.000 de alcance, así que el alcance es obligatorio.
- Solo se guardan los números que la persona da; nunca se inventan.
- Con 1 o 2 posts por estilo, el ranking es una pista, no una conclusión; dilo así.

## 4. Replicar un estilo con otro tema

**Cuándo:** "hazme uno sobre X con el estilo Y", "usa mi mejor estilo", "como el de la vez pasada pero de otro tema". No hace falta link ni captura.

1. Define el estilo como en §2. Lo elige la persona; si no dijo cuál, mándale el catálogo.
2. Lee `estilo.json` (`ver "Nombre"`): el ADN trae la fórmula del gancho, el rol de cada slide y la densidad de palabras. Esa es la estructura que se repite.
3. Copia la carpeta del estilo a un proyecto nuevo, `carruseles/<tema-AAAAMMDD>/`, y reescribe solo el contenido de la plantilla, o de `build.py` si existe, con el tema nuevo. Respeta el mismo número de slides, los mismos roles y la misma densidad. El copy sigue las reglas del Paso 3: voz de la persona, pruebas reales y `[DATO A CONFIRMAR]`.
4. Renderiza y compara contra las muestras del estilo: `comparar.py carruseles/estilos/<id>/muestras final/ comparacion.png`. Debe verse como el mismo estilo con otro tema.

**Aviso de fatiga:** si la persona usa el mismo estilo en varias publicaciones seguidas, recomiéndale alternarlo con otro. La audiencia se acostumbra a un formato y el rendimiento baja aunque el estilo sea bueno. Una buena regla es no repetir el mismo estilo en 2 posts seguidos del feed.
