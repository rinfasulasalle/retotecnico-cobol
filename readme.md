# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción
Esta es una aplicación de línea de comandos (CLI) en Python que procesa un archivo CSV con transacciones bancarias y genera un reporte con la siguiente información:
- **Balance Final**: Suma de los montos de transacciones de tipo "Crédito" menos la suma de los montos de tipo "Débito".
- **Transacción de Mayor Monto**: ID y monto de la transacción más alta.
- **Conteo de Transacciones**: Número total de transacciones de cada tipo ("Crédito" y "Débito").

## Instrucciones de Ejecución
1. Asegúrate de tener el archivo `archivo.csv` en la misma carpeta que el script.
2. Ejecuta el script con el siguiente comando:
   ```
   python procesar_transacciones.py archivo.csv
   ```
3. El resultado se mostrará en la terminal con el balance final, la transacción más alta y el conteo de transacciones.

## Enfoque y Solución
- Se utiliza la biblioteca estándar `csv` para leer el archivo de transacciones.
- Se recorre el archivo sumando y clasificando las transacciones en "Crédito" o "Débito".
- Se determina la transacción con el monto más alto y se imprime el resumen final.

## Estructura del Proyecto
```
/
│── procesar_transacciones.py  # Script principal
│── archivo.csv  # Archivo de entrada con transacciones bancarias
```

