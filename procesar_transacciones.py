import csv

def procesar_transacciones():
    """
    Procesa un archivo CSV llamado "archivo.csv" y genera un reporte de transacciones bancarias.
    
    Reporte generado:
    - Balance final de las transacciones.
    - Transacción con el mayor monto.
    - Conteo total de transacciones de tipo "Crédito" y "Débito".
    """
    archivo_csv = "archivo.csv"
    balance = 0
    max_monto = 0  # Inicializamos con el menor valor posible 0
    max_id = None
    creditos = 0
    debitos = 0
    
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                monto = float(row['monto'])
                tipo = row['tipo'].strip().lower()  # Normalizar el tipo de transacción a letras minúsculas
                
                if tipo == 'crédito': #Si encuentra un credito  lo suma en el balance y tambien el count de créditos
                    balance += monto
                    creditos += 1
                elif tipo == 'débito': # Lo mismo en débito
                    balance -= monto
                    debitos += 1
                
                if monto > max_monto:
                    max_monto = monto
                    max_id = row['id']
        
        print("Balance Final:", round(balance, 2))
        print("Mayor Transacción: ID", max_id, "Monto", round(max_monto, 2))
        print("Créditos:", creditos, "Débitos:", debitos)
    # Manejo algunos errores como archivo no encontrado,s i el csv no tiene la correcta estrucutra o si los datos estan mal.
    except FileNotFoundError:
        print("Error: El archivo", archivo_csv, "no se encontró.")
    except KeyError:
        print("Error: El archivo CSV no contiene las columnas esperadas.")
    except ValueError:
        print("Error: Datos inválidos en el archivo CSV.")

if __name__ == "__main__":
    procesar_transacciones()

