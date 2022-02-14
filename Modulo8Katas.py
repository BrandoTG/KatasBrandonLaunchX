#Ejercicio 1: Creación de diccionarios de Python
planeta={
    'nombre':'Marte',
    'lunas': 2
}

print(f'{planeta["nombre"]} tiene {planeta["lunas"]} lunas\n')

planeta["circunferencia en Km"]={
    "polar":6752,
    "equatorial":6792
}

print(f'{planeta["nombre"]} tiene {planeta["lunas"]} lunas, también tiene una circunferencia polar de {planeta["circunferencia en Km"]["polar"]}km y circunferencia ecuatorial de {planeta["circunferencia en Km"]["equatorial"]}km')

#Ejercicio 2: Programación dinámica con diccionarios

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons=planet_moons.values()
planets=len(planet_moons.keys())

suma_moons=0
suma_planetas=0

for moon in moons:
    suma_moons=suma_moons+moon

promedio_lunas=suma_moons/planets

print("En el sistema solar existe un promedio de: ",promedio_lunas," por cada planeta")
    
    