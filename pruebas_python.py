print("Hola mundo")
print("Mi nombre es: " + "Brenda")
print("Mi apellido es: " + "Pineda")

""" Reglas para nombres de variables en Python

El nombre de la variable debe comenzar con una letra o un guion bajo
El nombre de la variable no puede comenzar con un número
El nombre de la variable sólo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _)
Los nombres de variables distinguen mayúsculas de minúsculas (firstname, Firstname, FirstName y FIRSTNAME son variables diferentes)
A continuación algunos ejemplos de nombres válidos:
 """

# Variables en Python
first_name = "Asabeneh"
last_name = "Yetayeh"
country = "Finland"
city = "Helsinki"
age = 250
is_married = True
skills = ["HTML", "CSS", "JS", "React", "Python"]
person_info = {
    "firstname": "Angel",
    "lastname": "Yetayeh",
    "country": "Finland",
    "city": "Helsinki",
}

print("Hola ", first_name, " me interesa tu habilidad ", skills[2])
print("Hola ", person_info["firstname"], " eres de ", person_info["country"])
