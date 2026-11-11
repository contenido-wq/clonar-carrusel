# Cómo instalar la skill `clonar-carrusel`

Elige el camino según cómo usas Claude. Si no sabes cuál, empieza por la **Opción A**.

| Opción | Para quién | Dificultad | Captura sola el carrusel de Instagram |
|---|---|---|---|
| **A. Claude.ai** (web, escritorio o celular) | cualquier persona | fácil | depende del acceso a internet de tu cuenta; si no, subes capturas de pantalla |
| **B. Claude Code en tu computadora** | si ya usas la terminal | media | sí |
| **C. Claude Code en la nube** (claude.ai/code) | si ya usas Claude Code web | media | sí, después de permitir Instagram |

---

## Opción A: Claude.ai (sin programar)

### 1. Descarga la skill
1. Descarga **[clonar-carrusel.zip](https://github.com/contenido-wq/clonar-carrusel/raw/main/dist/clonar-carrusel.zip)** (se baja directo al tocar el enlace).
2. No lo descomprimas: Claude lo necesita tal cual.

> Si el enlace no funciona, entra a la carpeta [`dist/`](https://github.com/contenido-wq/clonar-carrusel/tree/main/dist), abre `clonar-carrusel.zip` y toca el botón de descarga (⬇️).

### 2. Activa lo necesario en Claude
1. Abre [claude.ai](https://claude.ai) y entra a **Configuración** (Settings).
2. Busca la sección de **Capacidades** (Capabilities) y activa **ejecución de código y creación de archivos** (Code execution and file creation). La skill la necesita para armar las imágenes.
3. Si ves la opción de **acceso a internet** para la ejecución de código, actívala. Así la skill puede bajar el carrusel desde el link.

> Los nombres exactos de los menús pueden cambiar con las actualizaciones de Claude. Si no los encuentras, busca "Skills" dentro de Configuración.

### 3. Sube la skill
1. En **Configuración → Capacidades**, ve a la sección **Skills**.
2. Toca **Subir skill** (Upload skill) y elige el `clonar-carrusel.zip` que descargaste.
3. Verifica que aparezca **clonar-carrusel** en la lista y que esté activada.

> Tu plan de Claude tiene que permitir skills. Si no ves la sección, revisa tu plan o pregúntale al administrador de tu organización.

### 4. Úsala
Abre un chat nuevo y escribe:

> ¿Qué estilos de carrusel tienes?

Claude te manda el catálogo con los 11 estilos incluidos. Elige uno y dile tu tema, tu @ y tu palabra clave. También puedes pasarle un link:

> Quiero modelar este carrusel para mi cuenta: https://www.instagram.com/p/XXXX/

Claude te va a hacer una entrevista corta (máximo 10 preguntas) y luego arma tu carrusel.

### 5. Guarda tus propios estilos
En Claude.ai cada chat empieza desde cero, así que un estilo guardado solo dura ese chat, a menos que lo metas en tu skill:

1. Cuando termines un carrusel que te guste, di **"Guárdalo como estilo y empaqueta la skill con mis estilos"**.
2. Claude te entrega un `clonar-carrusel.zip` nuevo.
3. En **Configuración → Capacidades → Skills**, elimina la versión anterior de **clonar-carrusel** y sube el ZIP nuevo.

Desde ahí tu estilo aparece en el catálogo en cualquier chat. Ese mismo ZIP sirve para compartir tus estilos con tu equipo.

### Actualizar a la última versión
Descarga otra vez el ZIP del paso 1 y súbelo en lugar del anterior. Si tenías estilos propios, primero pídele a Claude, en un chat, que empaquete la skill con tus estilos, para no perderlos.

**Si te dice que no puede abrir Instagram:** haz capturas de pantalla de cada slide del carrusel (en orden) y súbelas al chat. La skill sigue igual con esas imágenes.

---

## Opción B: Claude Code en tu computadora

### 1. Requisitos (una sola vez)
Necesitas tener instalado:
- [Claude Code](https://code.claude.com)
- [Node.js](https://nodejs.org) (versión 18 o superior)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### 2. Instala la skill y lo que necesita
Abre la terminal y copia estos comandos, uno por uno:

```bash
# 1. Descarga la skill en tu carpeta de skills
git clone https://github.com/contenido-wq/clonar-carrusel ~/.claude/skills/clonar-carrusel

# 2. Instala el navegador que usa para capturar y renderizar
cd ~/.claude/skills/clonar-carrusel
npm install playwright
npx playwright install chromium

# 3. Instala la librería de imágenes de Python
pip install pillow
```

> En Windows, usa `%USERPROFILE%\.claude\skills\clonar-carrusel` en lugar de `~/.claude/skills/clonar-carrusel`, y si `pip` no funciona prueba con `py -m pip install pillow`.

### 3. Pruébala
Abre Claude Code en la carpeta donde quieras guardar tus carruseles y escribe:

> Quiero modelar este carrusel: https://www.instagram.com/p/XXXX/

Los resultados quedan en la carpeta `carruseles/` de donde abriste Claude Code. Los 11 estilos incluidos vienen con la skill, y los que guardes quedan en `carruseles/estilos/` sin hacer nada más. Para ver el catálogo, pregunta: *"¿Qué estilos de carrusel tienes?"*

### Actualizar a la última versión
```bash
cd ~/.claude/skills/clonar-carrusel && git pull
```

---

## Opción C: Claude Code en la nube (claude.ai/code)

1. En tu entorno de la nube, abre la configuración del entorno (el menú del entorno en la barra superior de la sesión → **Editar**).
2. En **Acceso de red** (Network access), agrega estos dominios permitidos:
   - `instagram.com`
   - `cdninstagram.com`
   - `fonts.googleapis.com`
   - `fonts.gstatic.com`
3. Agrega el repositorio `contenido-wq/clonar-carrusel` a tu sesión, o clónalo dentro de `.claude/skills/` de tu proyecto.
4. Playwright y Chromium ya vienen instalados en ese entorno, así que no tienes que instalar nada más.

Guía oficial de acceso de red: https://code.claude.com/docs/en/cloud-environments#network-access

---

## Problemas comunes

| Lo que ves | Qué hacer |
|---|---|
| "No puedo abrir Instagram" o `ERR_TUNNEL_CONNECTION_FAILED` | Tu entorno no tiene permiso para entrar a Instagram. Sube capturas de pantalla de los slides o permite `instagram.com` y `cdninstagram.com` (Opción C). |
| `Cannot find module 'playwright'` | Ejecuta `npm install playwright` dentro de la carpeta de la skill (Opción B, paso 2). |
| `ModuleNotFoundError: No module named 'PIL'` | Ejecuta `pip install pillow`. |
| Las letras salen con una fuente rara | No cargó Google Fonts. Revisa tu conexión o permite `fonts.googleapis.com` y `fonts.gstatic.com`. |
| El ZIP no sube a Claude.ai | Revisa que lo subiste sin descomprimir. Si con tus estilos propios pesa mucho, pídele a Claude que guarde menos muestras o quita estilos que ya no uses. |
| Claude no usa la skill | Menciona algo como "modela este carrusel" o "clona este carrusel" junto al link. En Claude.ai, revisa que la skill esté activada. |
| Solo capturó algunos slides | Instagram a veces muestra menos slides en su versión embebida. Sube capturas de los que faltan. |

---

¿Dudas o sugerencias? Abre un [issue](https://github.com/contenido-wq/clonar-carrusel/issues) o escríbele a [@jheitrujillob](https://instagram.com/jheitrujillob).
