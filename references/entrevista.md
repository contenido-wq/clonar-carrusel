# Entrevista inicial (máximo 10 preguntas)

El objetivo es entender a la persona antes de tocar el carrusel: quién es, a quién le habla, y qué tiene que pasar después de que alguien lo vea. Un carrusel viral que no lleva a ningún lado solo da vanidad; uno que conecta con una oferta da clientes.

## Cómo hacerla

- Manda **todas las preguntas en un solo mensaje**, numeradas, para que la persona las conteste de una vez. No hagas una pregunta por turno: cansa y se pierde el impulso.
- Ofrece responder **por texto o por nota de voz**. Por voz casi siempre sale más contexto real (cómo habla, qué le importa) y eso sirve también para capturar su voz.
- Antes de preguntar, revisa lo que ya sabes: la conversación, el archivo `perfil.json` si ya trabajaste con esta persona, o lo que dijo en su pedido. **No preguntes lo que ya está respondido**. Si tienes el perfil guardado, muéstrale un resumen y pregúntale solo qué cambió y lo específico de este carrusel (preguntas 4 a 8), en **máximo 5 preguntas**. Si falta algo más (foto, pruebas nuevas), mételo dentro de una de esas 5 en vez de agregar una sexta. La persona vuelve porque quiere ir rápido, y con "igual que la vez pasada" debería bastar.
- Si solo responde parte, sigue con lo que tengas, usa supuestos razonables y márcalos como `[SUPUESTO]` en el copy. No la persigas con más preguntas.

## Las 10 preguntas (plantilla para enviar)

> Antes de arrancar, necesito entenderte para que este carrusel no solo tenga likes, sino que te traiga lo que buscas. Responde por texto o mándame una nota de voz, como te quede más fácil:
>
> 1. **¿Cuál es tu Instagram?** (@usuario)
> 2. **¿A qué te dedicas y qué vendes?** Tu producto o servicio en una frase y, si puedes, el precio aproximado.
> 3. **¿Quién es tu cliente ideal?** ¿Qué problema tiene, qué le frustra y qué dice cuando te escribe?
> 4. **¿Para qué es este carrusel?** Elige el principal: ganar seguidores, ganar autoridad (que lo guarden y lo compartan), conseguir mensajes o leads, o vender algo concreto.
> 5. **¿Lo quieres llevar a algo?** Curso, taller, mentoría, servicio, producto, lista de espera o recurso gratis. Cuéntame qué es, cómo se llama, si es gratis o pagado, la fecha y el link.
> 6. **¿Qué palabra quieres que comenten?** ¿Y qué le llega a quien la comente? ¿Tienes respuesta automática por DM (ManyChat u otra)?
> 7. **¿Cuál es el carrusel modelo y qué te gustó de él?** El link, y si fue el gancho, el diseño, el tema o el formato.
> 8. **¿Qué tan parecido lo quieres?** "Espejo" (mismo gancho y estructura, adaptado a ti) o "inspirado" (misma estructura con tu propio ángulo y tema).
> 9. **¿Qué pruebas reales tienes?** Años de experiencia, número de clientes, resultados, casos o testimonios. Solo lo que puedas demostrar: no invento cifras.
> 10. **¿Cómo hablas y cómo se ve tu marca?** ¿Tuteas o hablas de usted? ¿De qué país es tu audiencia? Palabras que nunca dirías, tus colores y tipografías, y si tienes una foto tuya que pueda usar.

## Qué hacer con las respuestas

Guárdalas en `perfil.json`, en la carpeta del cliente (por ejemplo `carruseles/perfil.json`), para reutilizarlas la próxima vez:

```json
{
  "instagram": "@usuario",
  "negocio": "qué hace y qué vende",
  "precio_referencia": "",
  "cliente_ideal": {"quien": "", "dolor": "", "frases_que_dice": []},
  "objetivo_carrusel": "seguidores | autoridad | leads | venta",
  "oferta": {"tipo": "curso | taller | mentoría | servicio | producto | recurso", "nombre": "", "gratis_o_pago": "", "fecha": "", "link": ""},
  "cta": {"palabra": "", "entrega": "", "auto_dm": true},
  "modelo": {"url": "", "que_le_gusto": ""},
  "fidelidad": "espejo | inspirado",
  "autoridad_verificable": [],
  "voz": {"trato": "tú | usted", "pais_audiencia": "", "prohibido": [], "notas": ""},
  "marca": {"colores": [], "fuentes": [], "foto": ""},
  "pendientes": ["lo que quedó sin responder"]
}
```

## Cómo cambian el trabajo las respuestas

- **Objetivo seguidores**: gancho polémico o curioso y contenido muy compartible. El CTA puede ser "sígueme para más" o "compártelo con alguien que…".
- **Objetivo autoridad**: carrusel tipo marco o checklist que dé ganas de guardarlo. El CTA invita a guardar.
- **Objetivo leads o venta**: el carrusel resuelve una parte del problema y la oferta resuelve el resto. El CTA usa la palabra clave y nombra la oferta tal como es ("Comenta TALLER y te llevo a mi taller de…"). Pon el CTA también en la última slide, aunque el modelo lo tenga solo en el caption: quien llega al final es quien más comenta.
- **Sin auto-DM**: avísale que debe activarlo antes de publicar. Si no, los comentarios quedan sin respuesta y pierde el pico de alcance.
- **Sin pruebas reales**: no inventes números. Marca el hueco como `[DATO A CONFIRMAR]` y sugiere qué medir.
- **Con foto**: úsala en las slides donde el modelo muestra a una persona (teléfonos, miniaturas). Asegúrate de que nada le tape la cara.
