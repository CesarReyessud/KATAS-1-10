from datetime import date, datetime

from numpy import product

print("----------------------------------------------------------------------")
print("fechas")
print("hoy es " + str(date.today()))
print("\n")

print("----------------------------------------------------------------------")
print("sumas de numeros")
sum = 1 + 2
print ("el resultado de la suma es ")
print(sum)
print ("el resultado de la suma es " + str(sum))
print("\n")

print("----------------------------------------------------------------------")
print("usar variables")
suma = 1 + 2 # 3
product = sum * 2
print ("el resultado de la multiplicacion es ")
print(product)
print ("el resultado de la multiplicacion es " + str(product))
print("\n")

print("----------------------------------------------------------------------")
print("impresion de valores asignados a una variable")
distancia_a_alfa_centauri = 4.367
type(distancia_a_alfa_centauri)
print("la distancia a alfa centauri es ")
print(distancia_a_alfa_centauri)

print("----------------------------------------------------------------------")
print("entrada de datos")
print("Bienvenido al programa de bienvenida")
name = input("ingresa tu nombre")
print("saludos: " + name)

print("----------------------------------------------------------------------")
print("calculadora")
first_number = input("primer numero: ")
second_number = input("segundo numero: ")
print(int(first_number) + int(second_number))











