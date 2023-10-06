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

def chequeraParticular(chequeraGen, dni, tipo, estado, rangoFechas):
    c = 0

chequeraGen = chequeraGeneral(sys.argv[1])
for 
print(list(chequeraGen['DNI']).index('55555555'))
# print(chequeraGen[tuple(chequeraGen.keys())[0]][9])
