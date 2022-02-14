#Ejercicio1 - Utilizar operadores aritméticos

Tierra=149597870
Jupiter=778547200

distancia=(abs(Jupiter-Tierra))
distancia_millas = distancia*0.621

print("La distancia entre la Tierra y Jupiter (en Km) es de", distancia,"Km")
print("La distancia entre la Tierra y Jupiter (en Mi) es de",distancia_millas, "Mi\n")

#Ejercicio 2: convierte cadenas en números y usa valores absolutos
Planeta1="Marte"
Planeta2="Urano"
entrada= "Ingrese la distancia de {planeta} al Sol en Km: \n"
Marte= int(input(entrada.format(planeta=Planeta1)))
Urano = int(input(entrada.format(planeta=Planeta2)))
Distancia=(abs(Marte-Urano))

print("La distancia entre {} y {} es de:".format(Planeta1,Planeta2), Distancia )