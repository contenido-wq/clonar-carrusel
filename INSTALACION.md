# Cómo instalar `clonar-carrusel`

Solo necesitas el link del repositorio: **`contenido-wq/clonar-carrusel`**. No hay nada que descargar ni descomprimir.

| Dónde usas Claude | Cómo se instala |
|---|---|
| **Claude.ai** (web o app de escritorio) | Plugins → agregar marketplace desde el repositorio |
| **Claude Code** | 2 comandos |

Los plugins están disponibles en los planes Pro, Max, Team y Enterprise.

---

## Claude.ai (sin programar)

1. Abre [claude.ai](https://claude.ai) y ve a **Personalizar** (Customize) → pestaña **Plugins**.
2. Toca **Agregar** (Add) → **Agregar marketplace** (Add marketplace) → **Desde un repositorio** (Add from a repository).
3. Pega esto y confirma:
   ```
   contenido-wq/clonar-carrusel
   ```
4. En la lista de plugins aparece **clonar-carrusel**. Instálalo y verifica que quede activado.
5. En **Configuración → Capacidades**, activa **ejecución de código y creación de archivos**. Si ves la opción de acceso a internet para el código, actívala también: así la skill puede bajar el carrusel desde el link.

> Los nombres de los menús pueden cambiar con las actualizaciones de Claude. Si tu organización restringe los marketplaces, pídele al administrador que permita este repositorio.

### Úsala
Abre un chat nuevo y escribe:

> ¿Qué estilos de carrusel tienes?

Claude te manda el catálogo con los 11 estilos. Elige uno y dile tu tema, tu @ y tu palabra clave. También puedes pasarle un link:

> Quiero modelar este carrusel para mi cuenta: https://www.instagram.com/p/XXXX/

Claude te hace una entrevista corta (máximo 10 preguntas) y te entrega los slides por separado, listos para subir.

**Si te dice que no puede abrir Instagram:** sube capturas de pantalla de cada slide, en orden. La skill sigue igual con esas imágenes.

---

## Claude Code

Requisitos: [Claude Code](https://code.claude.com), [Node.js](https://nodejs.org) 18 o superior y [Python 3](https://www.python.org/downloads/).

Dentro de Claude Code:

```
/plugin marketplace add contenido-wq/clonar-carrusel
/plugin install clonar-carrusel@jheitrujillob
```

Después, una sola vez en la terminal, instala el navegador y la librería de imágenes que usa:

```bash
npm install -g playwright && npx playwright install chromium
pip install pillow
```

En Claude Code en la nube (claude.ai/code) Playwright ya viene instalado; solo permite en el acceso de red del entorno `instagram.com`, `cdninstagram.com`, `fonts.googleapis.com` y `fonts.gstatic.com` ([guía oficial](https://code.claude.com/docs/en/cloud-environments#network-access)).

Tus carruseles y tus estilos quedan en la carpeta `carruseles/` de donde abriste Claude Code.

---

## Agregar tus propios estilos

Cuando termines un carrusel que te guste, di **"Guárdalo como estilo"**. Aparece en el catálogo junto a los 11 incluidos y lo puedes reutilizar: *"Hazme otro sobre X con mi estilo de …"*.

- **Claude Code:** queda guardado en `carruseles/estilos/`. No tienes que hacer nada más.
- **Claude.ai:** cada chat empieza desde cero, así que para tenerlo siempre usa tu propia copia del repositorio:
  1. En GitHub, abre este repositorio y toca **Fork**.
  2. Pídele a Claude: **"Prepara mi estilo para subirlo a GitHub"**. Te da la carpeta del estilo con sus archivos.
  3. En tu fork, entra a `skills/clonar-carrusel/estilos/`, toca **Add file → Upload files**, arrastra la carpeta y guarda.
  4. En Claude.ai agrega tu fork como marketplace (`tu-usuario/clonar-carrusel`) y usa esa versión.

  Así tu estilo aparece en todos tus chats, y cualquiera que instale tu fork lo tiene.

---

## Actualizar

Las mejoras se publican en este mismo repositorio. En Claude Code, activa la actualización automática en `/plugin` → Marketplaces → *Enable auto-update*, o corre `/plugin marketplace update jheitrujillob`. En Claude.ai, actualiza el marketplace desde la pestaña Plugins.

---

## Problemas comunes

| Lo que ves | Qué hacer |
|---|---|
| No encuentro la pestaña Plugins | Revisa que tu plan sea Pro, Max, Team o Enterprise. En organizaciones, el administrador puede tenerlos restringidos. |
| "No puedo abrir Instagram" o `ERR_TUNNEL_CONNECTION_FAILED` | Tu entorno no tiene permiso para entrar a Instagram. Sube capturas de los slides o permite `instagram.com` y `cdninstagram.com`. |
| `Cannot find module 'playwright'` | Instala Playwright (paso de Claude Code). |
| `ModuleNotFoundError: No module named 'PIL'` | Ejecuta `pip install pillow`. |
| Las letras salen con una fuente rara | No cargó Google Fonts. Permite `fonts.googleapis.com` y `fonts.gstatic.com`. |
| Claude no usa la skill | Di "modela este carrusel" o "¿qué estilos de carrusel tienes?". Revisa que el plugin esté activado. |
| Solo capturó algunos slides | Instagram a veces muestra menos slides en su versión embebida. Sube capturas de los que faltan. |

---

¿Dudas o sugerencias? Abre un [issue](https://github.com/contenido-wq/clonar-carrusel/issues) o escríbele a [@jheitrujillob](https://instagram.com/jheitrujillob).
