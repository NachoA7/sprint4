import sys
import csv

def chequeraGeneral(rutaArch):
    chequera = {}
    with open(f'{rutaArch}.csv', 'r') as cheques:
        lector_csv = tuple(csv.reader(cheques))
        for index in range(0, len(lector_csv[0])):
            columna = []
            for linea in lector_csv:
                columna.append(linea[index])
            columna.remove(columna[0])
            chequera[lector_csv[0][index]] = columna
    return chequera

def chequeraParticular(chequeraGen, dni = '55555555', tipo = 'emitido', estado = 'pendiente', rangoFechas = 0):
    indices = []
    for indice, elemento in enumerate(chequeraGen['DNI']):
        if elemento == dni:
            if tuple(chequeraGen['TipoCheque'])[indice] == tipo:
                indices.append(indice)
                if estado != 0 and tuple(chequeraGen['Estado'])[indice] == estado:
                    continue
                else:
                    indices.pop()
    print(indices)

chequeraGen = chequeraGeneral(sys.argv[1])
chequeraParticular(chequeraGen)
# print(chequeraGen[tuple(chequeraGen.keys())[0]][9])
