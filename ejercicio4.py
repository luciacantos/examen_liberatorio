termino = int(input("Ingrese el valor de n: "))

n1 = 0
n2 = 1

contador = 0

if termino <= 0:
    print("Ingresar un número mayor a 0")
elif termino == 1:
    print("Serie de Fibonacci hasta el valor: ", termino)
    print(n1)
else:
    print("Serie de Fibonacci: ")
    while contador < termino:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        contador = contador + 1
