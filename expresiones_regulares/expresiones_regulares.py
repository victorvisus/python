"""
Expresiones regulares
Las expresiones regulares (RegEx) son cadenas de texto especiales que ayudan a encontrar patrones en los datos. RegEx se puede usar para comprobar la existencia de ciertos patrones en diferentes tipos de datos. Para usar RegEx en Python debemos importar el módulo llamado re.

Métodos en el módulo re
Para buscar patrones usamos diferentes conjuntos de caracteres y funciones de re, que permiten buscar coincidencias dentro de una cadena.

    re.match(): busca solo al inicio de la cadena; devuelve un objeto Match si hay coincidencia, sino None.
    re.search: busca en cualquier parte de la cadena (incluyendo textos multilínea); devuelve el primer objeto Match encontrado o None.
    re.findall: devuelve una lista con todas las coincidencias.
    re.split: acepta una cadena y la divide en los puntos donde hay coincidencia, devolviendo una lista.
    re.sub: reemplaza una o más coincidencias en una cadena.
"""

# https://regex101.com/

import re

# Ejemplo con re.match() ######
print(
    "\nEjemplo con re.match() ------------------------------------------------------- \n"
)

txt = "I love to teach python and javaScript"

# Devuelve un objeto Match con span y match
encontrado = re.match("I love to teach", txt, re.I)
if encontrado == None:
    raise AttributeError("No se encontro ninguna coincidencia")

print(encontrado)  # <re.Match object; span=(0, 15), match='I love to teach'>

# Podemos usar span para obtener la posición inicial y final como tupla
posiciones = (0, 0)
if encontrado:
    posiciones = encontrado.span()
print(posiciones)  # (0, 15)

# Tomamos inicio y fin desde span
ini, fin = posiciones
print(ini, fin)  # 0, 15
subCadena = txt[ini:fin]
print(subCadena)  # I love to teach


# Ejemplo con re.search() ######
print(
    "\nEjemplo con re.search() ------------------------------------------------------- \n"
)
txt = """Python is the most first beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# Devuelve un objeto Match con span y match
encontrado = re.search("first", txt, re.I)
print(encontrado)  # <re.Match object; span=(100, 105), match='first'>

# Podemos usar span para obtener inicio y fin como tupla
if encontrado:
    posiciones = encontrado.span()
print(posiciones)  # (100, 105)

# Tomamos inicio y fin
ini, fin = posiciones
print(ini, fin)  # 100 105
subCadena = txt[ini:fin]
print(subCadena, "\nSolo te doy la primera aparicion de ", subCadena)  # first


# Buscar todas las coincidencias con findall ######
print(
    "\nEjemplo con re.findall() ------------------------------------------------------- \n"
)
txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# Devuelve una lista
matches = re.findall("language", txt, re.I)
print(matches)  # ['language', 'language']


# Reemplazar subcadenas ########
print(
    "\nEjemplo con re.sub() ------------------------------------------------------- \n"
)
txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

match_replaced = re.sub("Python|python", "JavaScript", txt, re.I)
print(
    match_replaced
)  # JavaScript is the most beautiful language that a human being has ever created.
# o bien
match_replaced = re.sub("[Pp]ython", "JavaScript", txt, re.I)
print(
    match_replaced
)  # JavaScript is the most beautiful language that a human being has ever created.

# Usar RegEx para dividir el texto #####
print(
    "\nEjemplo con re.split() ------------------------------------------------------- \n"
)
txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

lines = re.split("\n", txt)
print(lines)
