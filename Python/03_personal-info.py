#Crear un script que pregunte por el nombre, el apellido, el teléfono, la ciudad, y la edad.
#Cada valor ha de ser guardado en una variable diferente.

def informacion(nombre="Introduce tu nombre",apellidos="Introduce tu apellido", telefono="Numero de telefono",ciudad="ciudad",edad="edad"):
    print("La informacion es","nombre: "+ nombre, "apellidos: " + apellidos,"tlf: "+ telefono,"ciudad: " + ciudad,"edad: " + edad)


informacion("Paola","Martin","655652951","Sevilla","21")

