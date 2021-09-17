# Infraestructuras Virtuales

## Sobre el proyecto

La mayoría de las aplicaciones de *TODO-list* no funcionan. Requieren tiempo de gestión, que accedas continuamente a ellas, y que organices correctamente tus objetivos. Al final, todas acaban sin usarse.

En mi caso, acabo poniendo recordatorios en Telegram mediante mensajes programados. Tanto en mis mensajes guardados como en un grupo privado que tengo de la universidad.

Aquí entra **Guorbu**.

Guorbu es un bot de telegram escrito en Rust. Permite enviarle mensajes en lenguaje natural, con los que después te los recordará. Su fuerte es la simplicidad.

Por ejemplo, si queremos recordanos coger el *workbook* mañana por la mañana, podemoes escribir:

```
mañana 8:00 universidad; coger workbook
```

El bot guarda el mensaje, y te lo mostrará en ese momento.

### Sintaxis

La sintaxis es la siguiente:

```
[hora] [dia] [tag]; [mensaje]
```

- `[hora]`: formato `hh:mm`.
- `[dia]`: admite `mañana`, `pasado`, y día específico en formato `día-de-la-semana`, `[número] de [mes]`, `dia/mes`.
- `[tag]`: permite clasificar el tipo de tarea. Por defecto: `varios`.
- `[Contenido]`: descripción de la tarea.

Las 3 etiquetas que preceden al punto y coma pueden ser cambiadas de orden.

### Features

- Producto mínimo:
  - Añadir tareas.
  - Eliminar tareas.
  - Listar las tareas guardadas.
  - Recordatorios del día en específico.
- Planeadas (si fuera posible):
  - Recordatorios de las tareas en el día que se envían.
  - Tareas sin hora o día fijo.
  - Recordatorios cada cierto tiempo.