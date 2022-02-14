#Ejercicio 1: Crear y usar listas de Python

planetas=['Mercurio','Venus','Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

print("Existen un total de: ",len(planetas),"planetas")
print("Los planetas son: ",(planetas),"\n")

#Agrega a Plutón a la lista que creaste. Luego muestra tanto el número de planetas como el último planeta de la lista.

planetas.append('Pluton')
print("Ahora hay un total de: ",len(planetas),"planetas")
print(planetas)
print("El último planeta de la lista es: ", planetas[-1],"\n")

#Ejercicio 2: Trabajando con datos de una lista

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno','Urano', 'Neptuno']

usuario=input("Ingrese el nombre del planeta deseado (use mayúcsulas para la primer letra): ")
planetas_indice=planetas.index(usuario)
print(planetas_indice)
print("Los planetas más cercanos al sol que el planeta", usuario, "son:\n")
print(planetas[0:planetas_indice])

print("Los planetas más lejos del sol que el planeta", usuario, "son:")
print(planetas[planetas_indice:])
