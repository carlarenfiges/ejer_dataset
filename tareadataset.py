import csv
archivo = open("C:/Users/Carla/Desktop/FACU/PYTHON/actividad1/appstore_games.csv","r")
csvreader = csv.reader(archivo, delimiter= ',')
encabezado = next(csvreader)

"""
 listar los juegos gratuitos disponibles en español
"""

lista_valores=[]
for linea in csvreader:
    if linea[7] == "O" and linea[12] == "ES":
        print(linea[2]) # imprimo los nombres
    lista_valores.append(linea[6])
archivo.close()

lista_valores.sort(reverse=True)
for pos in range(10):
    print(lista_valores[pos])
