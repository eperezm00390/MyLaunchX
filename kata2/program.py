from datetime import date

#program.py
sum = 1 + 2
print(sum)

#Impresion en pantalla
print("Hola desde la consola")

sum = 1 + 2 # 3
product = sum * 2
print(product)

planetas_en_el_sistema_solar = 8 
distancia_a_alfa_centauri = 4.367 
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" 

distancia_a_alfa_centauri = 4.367

type(distancia_a_alfa_centauri)

left_side = 10
right_side = 5
left_side / right_side


# Fechas

print(date.today())
print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Calc.py
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))