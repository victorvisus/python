"""Expandir en Python
Al igual que en JavaScript, Python permite expandir listas usando el operador *. Veámoslo:"""

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

""" Enumerar (enumerate)
Si necesitamos los índices de una lista, usamos la función integrada enumerate. """
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(countries):
    print("hola")
    if i == "Finland":
        print(f"El país {i} está en el índice {index}")

""" Zip
A veces necesitamos combinar listas. Observa el ejemplo: """
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fruit": f, "veg": v})

print(fruits_and_veges)

""" Unir listas usando el operador + """
""" fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_veges = fruits + vegetables
print(fruits_and_veges) """
