# Nombre del Proyecto

Este proyecto automatiza la gestión de un cronograma de empleados para una empresa de atmosféricos, utilizando Python y Excel. Permite agregar, actualizar y eliminar mercados asignados a fechas específicas, incluyendo la hora, el camión y los empleados responsables.

## Características

- **Agregar mercados**: Permite agregar nuevos mercados a una fecha específica.
- **Actualizar mercados**: Actualiza la hora, camión y empleados de un mercado existente.
- **Eliminar mercados**: Elimina uno o varios mercados en una fecha determinada.

## Requisitos

- Python 3.x
- Pandas (instalar con `pip install pandas`)
- Un archivo Excel (`cronograma_empleados.xlsx`) con las columnas `Fecha`, `Mercado/s`, `Hora`, `Camión`, `Empleado/s`.

## Uso

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias de Python: `pip install -r requirements.txt` (si tienes un archivo de dependencias).
3. Abre el archivo Excel `cronograma_empleados.xlsx` y comienza a trabajar con el cronograma.
4. Utiliza las funciones para agregar, actualizar o eliminar mercados en las fechas correspondientes.

## Funciones

- **agregar_mercado(fecha, mercado, hora, camion, empleado)**: Agrega un mercado a la fecha indicada.
- **eliminar_mercado(fecha, *mercados)**: Elimina uno o más mercados de una fecha específica.
- **actualizar_mercado(fecha, mercado, nueva_hora, nuevo_camion, nuevo_empleado)**: Actualiza los datos de un mercado existente.

## Notas

- Este proyecto se puede ampliar para incluir más características, como la integración con un bot de WhatsApp o la automatización en la nube.
- Para más detalles, revisa el código fuente en los archivos `.py`.
