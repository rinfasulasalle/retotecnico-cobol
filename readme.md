# Procesamiento de Transacciones Bancarias (CLI)

## Introducción
Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python que procesa un archivo CSV con transacciones bancarias. Su objetivo es generar un reporte con la siguiente información:
- **Balance Final**: Diferencia entre la suma de los montos de tipo "Crédito" y "Débito".
- **Transacción de Mayor Monto**: Identificar el ID y monto de la transacción más alta.
- **Conteo de Transacciones**: Número total de transacciones de cada tipo.

## Instrucciones de Ejecución
### Prerrequisitos
- Tener instalado **Python 3.x** en el sistema.
- Instalar las dependencias necesarias ejecutando:
  ```sh
  pip install -r requirements.txt
  ```

### Ejecución
Para procesar un archivo CSV, ejecutar el siguiente comando:
```sh
python procesar_transacciones.py archivo.csv
```
Donde `archivo.csv` es el archivo con las transacciones bancarias a procesar.

## Enfoque y Solución
La aplicación utiliza la biblioteca `csv` para leer los datos y realiza las siguientes operaciones:
1. **Lectura y validación de datos**: Se asegura que el archivo contiene las columnas necesarias.
2. **Cálculo del balance final**: Se suman los montos de las transacciones "Crédito" y se restan las de "Débito".
3. **Identificación de la transacción de mayor monto**: Se recorre el archivo buscando el valor más alto.
4. **Conteo de transacciones por tipo**: Se mantiene un registro del número total de cada tipo de transacción.

El diseño se centra en la eficiencia y simplicidad, permitiendo manejar archivos grandes con un consumo óptimo de memoria.

## Estructura del Proyecto
```
📂 transacciones-cli/
├── 📄 procesar_transacciones.py  # Script principal que procesa el CSV
├── 📄 requirements.txt           # Lista de dependencias necesarias
├── 📄 README.md                  # Documentación del proyecto
```

## Autor
Roger Infa Sánchez

