import sympy

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
n = int(input("Ingrese el valor de n: "))


x = Symbol('x')
expresion = (a*x + b)
solucion = sympy.expand(expresion)**n

if a == 1:
    solucion = (x + b)**n
elif a == -1
    solucion = (-x + b)**n
else:
    solucion = sympy.expand(expresion)**n



print(solucion)


