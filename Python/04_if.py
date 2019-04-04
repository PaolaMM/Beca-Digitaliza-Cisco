#Crear un script en el que guardéis en una variable un número
x= int(input("El valor de x: "))
#Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
#En cada uno de los casos imprimir por pantalla el número que se haya introducido.

if(x<=20):
    print(x, "Es menor que 20")

if (20<x<39):
    print(x, "Esta entre 20 y 39")

if (40 < x < 59):
    print(x, "Esta entre 40 y 59")

if (x > 60):
    print(x, "Es mayor que 60")




