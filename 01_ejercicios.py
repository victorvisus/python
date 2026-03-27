"""
Ejercicio: Nivel 2
1 Usa la función integrada type() para comprobar el tipo de las variables que declaraste
2 Usa la función len() para calcular la longitud de la variable first_name
3 Compara la longitud de las variables first_name y last_name
4 Declara las variables num_one = 5 y num_two = 4
---- Suma num_one y num_two y asigna el resultado a la variable total
---- Resta num_two de num_one y asigna el resultado a la variable diff
---- Multiplica num_one y num_two y asigna el resultado a la variable product
---- Divide num_one entre num_two y asigna el resultado a la variable division
---- Usa la operación módulo para obtener el resto de num_two dividido por num_one y asígnalo a remainder
---- Calcula num_one elevado a num_two y asigna el valor a exp
---- Calcula la división entera de num_one entre num_two (operación de floor division) y asigna el resultado a floor_division
5 El círculo tiene un radio de 30 metros.
---- Calcula el área del círculo y asígnala a la variable _area_of_circle_
---- Calcula la circunferencia del círculo y asígnala a la variable _circum_of_circle_
---- Pide el radio al usuario y calcula el área.
6 Usa la función integrada input() para obtener nombre, apellido, país y edad del usuario y almacena los valores en las variables correspondientes
7 Ejecuta help('keywords') en el intérprete de Python o en un archivo para comprobar las palabras reservadas (keywords) de Python
"""

# DIVISION DE MODULO
numero_uno = 85
numero_dos = 6

print("Division: ", numero_uno / numero_dos)  # division
print("El resto es: ", numero_uno % numero_dos)  # me da el resto, el resido
print("El cociente (modulo) es: ", numero_uno // numero_dos)  # me da el modulo


# Ejercicio 5.
print("\n-- Ejercicio 5 -------------------------------------------")
"""
5 El círculo tiene un radio de 30 metros.
---- Calcula el área del círculo y asígnala a la variable _area_of_circle_
---- Calcula la circunferencia del círculo y asígnala a la variable _circum_of_circle_
---- Pide el radio al usuario y calcula el área.
"""
radio = 30
diametro = radio * 2
piValor = 3.1416

_area_of_circle = piValor * radio**2
_circum_of_circle = piValor * diametro
print("El radio es: ", radio)
print("El area es: ", _area_of_circle)
print("La circunferencia es: ", _circum_of_circle)

usrRadio = float(input("¿Cuál es tu radio?\n"))
_area_of_circle = piValor * pow(float(usrRadio), 2)
_circum_of_circle = piValor * (usrRadio * 2)
print("El nuevo radio es: ", radio)
print("La nueva area es: ", _area_of_circle)
print("La nueva circunferencia es: ", _circum_of_circle)
