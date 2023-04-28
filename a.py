#Construye un programa que al recibir como dato el radio de una esfera, calcule e imprima el area y su volumen
#Dato: RAD (variable de tipo real que representa el radio de la esfera).

#El area de una esfera la calculamos de la siguiente forma:
#area=4*pi*radio^2
#El volumen de una esfera se calcula asi:
#Volumen=1/3*pi*radio^3

import math as ma
radio=float(input("Ingrese el radio de la esfera: "))
area=4*ma.pi*pow(radio,2)
volumen=1/3*ma.pi*pow(radio,3)
print("El area de la esfera es: ",area)
print("El volumen de una esfera es: ",volumen)