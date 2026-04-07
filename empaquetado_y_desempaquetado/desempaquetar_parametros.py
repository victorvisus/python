"""
Empacar y desempacar parámetros en Python
Usamos dos operadores:

    * para tuplas/listas
    ** para diccionarios
Veamos un ejemplo. Supongamos que una función acepta parámetros separados, pero nosotros tenemos una lista. Podemos desempaquetarla y convertirla en argumentos.
"""

# Desempaquetado
""" def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e' """

"""Al ejecutar lo anterior ocurre un error porque la función espera números separados, no una lista. Desempaquetemos la lista:"""


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

""" También podemos usar desempaquetado con range(), que acepta inicio y fin:"""
numbers = range(2, 7)  # llamada normal con parámetros separados
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # llamada usando los parámetros desempaquetados desde la lista
print(list(numbers))  # [2, 3, 4, 5, 6]

"""También podemos usar desempaquetado en asignaciones:"""
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  #  1 [2, 3, 4, 5, 6] 7


# Desempaquetar diccionarios
def unpacking_person_info(name, country, city, age):
    return f"{name} vive en {city}, {country}. Tiene {age} años."


dct = {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 250}
print(
    unpacking_person_info(**dct)
)  # Asabeneh vive en Helsinki, Finland. Tiene 250 años.
