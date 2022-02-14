#Ejercicio 1: Creación de un bucle "while"

new_planet = ''
planets = []


while new_planet.lower() != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Ingrese un nuevo planeta: ")

#Ejercicio 2: Creación de un ciclo "for"
print("Los planetas ingresados son: ")
print("-"*len(max(planets)))
for planets in planets:
    print(planets)