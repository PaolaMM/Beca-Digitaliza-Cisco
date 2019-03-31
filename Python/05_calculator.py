#Crear las sentencias necesarias para recoger dos números a través del terminal
#Integrar funcionalidades de suma, multiplicación, división, y exponencial
import math

def sum():
    print(x+y)

def restar():
    print(x-y)

def dividir():
    print(x/y)

def multiplicar():
    print(x*y)


x= int(input("El valor de x: "))
y= int(input("El valor de y: "))
op=input("1 para sumar,2 para restar,3 para multiplicar,4 para dividir: ")

if op == 1:
    sum()
elif op == 2:
    restar()
elif op == 3:
    multiplicar()
elif op == 4:
    dividir()



