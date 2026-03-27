"""TIPOS DE DATOS"""
# Diferentes tipos de datos en Python
# Declaramos algunas variables con distintos tipos de datos

first_name = "Asabeneh"  # str
last_name = "Yetayeh"  # str
country = "Finland"  # str
city = "Helsinki"  # str
age = 250  # int, no se preocupe, esta no es mi edad real :)

# Printing out types
print(type("Asabeneh"))  # str
print(type(first_name))  # str
print(type(10))  # int
print(type(3.14))  # float
print(type(1 + 1j))  # complex
print(type(True))  # bool
print(type([1, 2, 3, 4]))  # list
print(type({"name": "Asabeneh", "age": 250, "is_married": 250}))  # dict
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))  # set
