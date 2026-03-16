cantidad_personas = int(input("Ingrese la cantidad de personas que va a ingresar: "))
contador = 0
personas = []
suma = 0

while contador < cantidad_personas:
    persona = []
    persona.append(input("Ingrese el nombre de la persona: "))
    persona.append(int(input("Ingrese la edad de la persona: ")))
    persona.append(int(input("Ingrese la nota de la persona: ")))
    personas.append(persona)
    contador += 1

print("Lista de personas (en el orden que fueron ingresadas): ")
for persona in personas:
    print(persona)

print("Lista de personas en la fila 0, columna 0 (nombre): ")
print(personas[0][0])

# reverse=True = invierte el orden, en este caso, de mayor a menor
# key=lambda x: x[2] = permite ordenar por la clave en la posición 2, en este caso, por nota
print("Personas ordenas por nota de mayor a menor: ")
ordenados = sorted(personas, key=lambda x: x[2], reverse=True)
for persona in ordenados:
    print(persona)

for persona in personas:
    suma = suma + persona[2]

print(f"La suma de las notas de las personas es: {suma}")

promedio = suma / cantidad_personas
print(f"El promedio de las notas de las personas es: {promedio}")