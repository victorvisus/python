"""
Empaquetado
A veces no sabemos cuántos argumentos nos pasarán a una función. Podemos usar empaquetado para aceptar un número variable de argumentos.
"""


# Empaquetar listas
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# Empaquetar diccionarios
def packing_person_info(**kwargs):
    # comprobar el tipo de kwargs: es un dict
    print(type(kwargs))
    # imprimir los pares clave-valor
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

newDict = {"name": "jjjjj", "country": "Finland", "city": "Helsinki", "age": 250}
print(
    packing_person_info(**newDict)
)  # para pasarle un diccionario, hay que ponerlo los ** delante
