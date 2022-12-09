from sympy import Symbol, expand

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
n = int(input("Ingrese el valor de n: "))


x = Symbol('x')
expresion = (a*x + b)**n


if a == 1:
    solucion = (x + b)**n
elif a == (-1)
    solucion = solucion.replace("x", "-x")
else:
    solucion = (x + b)**n



print(solucion)


