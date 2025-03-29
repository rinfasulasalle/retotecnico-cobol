import csv

def procesar_transacciones():
    archivo_csv = "archivo.csv"
    balance = 0
    max_monto = 0
    max_id = None
    creditos = 0
    debitos = 0
    
    with open(archivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            monto = float(row['monto'])
            if row['tipo'] == 'Crédito':
                balance += monto
                creditos += 1
            else:
                balance -= monto
                debitos += 1
            if monto > max_monto:
                max_monto = monto
                max_id = row['id']
    
    print("Balance Final:", balance)
    print("Mayor Transacción: ID", max_id, "Monto", max_monto)
    print("Créditos:", creditos, "Débitos:", debitos)

if __name__ == "__main__":
    procesar_transacciones()
