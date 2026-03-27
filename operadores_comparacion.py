print(3 > 2)  # True, porque 3 es mayor que 2
print(3 >= 2)  # True, porque 3 es mayor o igual que 2
print(3 < 2)  # False,  porque 3 no es menor que 2
print(2 < 3)  # True, porque 2 es menor que 3
print(2 <= 3)  # True, porque 2 es menor o igual que 3
print(3 == 2)  # False, porque 3 no es igual a 2
print(3 != 2)  # True, porque 3 no es igual a 2
print(len("mango") == len("avocado"))  # False
print(len("mango") != len("avocado"))  # True
print(len("mango") < len("avocado"))  # True
print(len("milk") != len("meat"))  # False
print(len("milk") == len("meat"))  # True
print(len("tomato") == len("potato"))  # True
print(len("python") > len("dragon"))  # False

# Las comparaciones devuelven True o False
print("True == True: ", True == True)
print("True == False: ", True == False)
print("False == False:", False == False)


"""
Además de los operadores de comparación anteriores, Python también utiliza los siguientes operadores:
-is: devuelve True si los objetos son idénticos (x is y)
-is not: devuelve True si los objetos no son idénticos (x is not y)
-in: devuelve True si un elemento está en una secuencia (x in y)
-not in: devuelve True si un elemento no está en una secuencia (x not in y)
"""
print("1 is 1", 1 is 1)  # True - porque los objetos son idénticos
print("1 is not 2", 1 is not 2)  # True - porque los objetos no son idénticos
print("A in Asabeneh", "A" in "Asabeneh")  # True - la cadena contiene 'A'
print("B in Asabeneh", "B" in "Asabeneh")  # False - no hay 'B' mayúscula
print("coding" in "coding for all")  # True - 'coding' está en 'coding for all'
print("a in an:", "a" in "an")  # True
print("4 is 2 ** 2:", 4 is 2**2)  # True
print("4 is not 2 ** 2:", 4 is not 2**2)  # False
