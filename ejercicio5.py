

x = input("Secuencia: ")
y = int(input("Filas: "))

lista = [[" " for i in len(x)] for j in range(y)]

fila = 0
columna = 0

for i in range(len(x)):
    lista[fila][i] = x[i]
    if fila == 0:
        columna = 0
    elif fila == y - 1:
        columna = 1
        if columna == 0:
            fila = fila + 1
        else:

for i in range(y):
    print("".join(lista[i]))
