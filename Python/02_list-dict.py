#Crear una lista que contenga varios strings.
#Crear una lista que contenga varios integers.
#Crear una lista que contenga strings, integers y floats.

list= ["Hola", "Hi", "Aló"]
list2=[1,2,3]
list3=[1.2,1.3,1.4]

list1= ["Hola", "Hi", "Aló", 1,2,3, 3.1456]

#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.

print(list)
print(list2)
print(list3)
print(list1)

#Crear 3 sentencias para asignar, en cada una, el último valor
#de una lista diferente a una variable (es decir, habrá 3 variables, cada una con el último valor de una de las listas).

x="Aló"
y= 3
z=1.4

#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.
print("Los valores de las variables asignadas son:" + x, y, z)

#Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)

dict = {'Ariana Grande': 'Thanks, next','Justin Bieber': 'Baby','Rihanna': 'Umbrella'}

#Crear sentencia para imprimir por pantalla todo el diccionario.

print(dict)

#Crear sentencia para imprimir por pantalla sólo las claves del diccionario
for key, val in dict.items():
    print (key)
#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
for key, val in dict.items():
    print(val)
