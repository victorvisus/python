# ===================================================================
# RESUMEN: EXPRESIONES REGULARES EN PYTHON - Día 18
# ===================================================================
# Las expresiones regulares (RegEx) son cadenas de texto especiales
# que ayudan a encontrar patrones en los datos.
# Para usar RegEx en Python: import re

import re

# ===================================================================
# 1. MÉTODOS PRINCIPALES DEL MÓDULO RE
# ===================================================================

# 1.1 re.match() - Busca solo al INICIO de la cadena
# Devuelve un objeto Match o None
txt = "I love to teach python and javaScript"
match = re.match("I love to teach", txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
if match:
    span = match.span()
print(span)  # (0, 15)
start, end = span
substring = txt[start:end]
print(substring)  # I love to teach

# Si no coincide al inicio, retorna None
match = re.match("I like to teach", txt, re.I)
print(match)  # None


# 1.2 re.search() - Busca en CUALQUIER PARTE de la cadena
# Devuelve el primer Match encontrado o None
txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

match = re.search("first", txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
if match:
    span = match.span()
print(span)  # (100, 105)


# 1.3 re.findall() - Devuelve una LISTA con todas las coincidencias
matches = re.findall("language", txt, re.I)
print(matches)  # ['language', 'language']

matches = re.findall("python", txt, re.I)
print(matches)  # ['Python', 'python']

# Alternancia: usar | (o)
matches = re.findall("Python|python", txt)
print(matches)  # ['Python', 'python']

# Usando corchetes [Pp]
matches = re.findall("[Pp]ython", txt)
print(matches)  # ['Python', 'python']


# 1.4 re.sub() - Reemplaza coincidencias en una cadena
match_replaced = re.sub("Python|python", "JavaScript", txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language...

# Reemplazar caracteres específicos
txt_dirty = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing."""
clean_txt = re.sub("%", "", txt_dirty)
print(clean_txt)  # I am teacher and I love teaching.


# 1.5 re.split() - Divide la cadena en puntos de coincidencia
txt = """I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people."""
lines = re.split("\n", txt)
print(lines)  # Divide por saltos de línea


# ===================================================================
# 2. CONSTRUIR PATRONES REGEX
# ===================================================================
# Usar cadenas raw: r'patrón'

# 2.1 CORCHETES [] - Conjunto de caracteres
regex_pattern = r"[Aa]pple"  # Apple o apple
txt = "Apple and banana are fruits. An apple a day"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# Rangos:
# [a-c]      -> a, b o c
# [a-z]      -> cualquier letra minúscula
# [A-Z]      -> cualquier letra mayúscula
# [0-9]      -> cualquier dígito
# [A-Za-z0-9] -> caracteres alfanuméricos

regex_pattern = r"[a-zA-Z0-9]"
matches = re.findall(regex_pattern, txt)
print(matches)  # Todos los caracteres alfanuméricos


# 2.2 METACARACTERES DE ESCAPE (\)
# \d -> dígito (0-9)
# \w -> carácter de palabra (a-z, A-Z, 0-9, _)
# \s -> espacio en blanco
# \ seguido de carácter especial -> el carácter literal

regex_pattern = r"\d"  # Busca dígitos
txt = "December 6, 2019 and revised on July 8, 2021"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

regex_pattern = r"\d+"  # \d+ -> uno o más dígitos
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']


# 2.3 CUANTIFICADORES
# +  -> Una o más veces
# *  -> Cero o más veces
# ?  -> Cero o una vez
# {n}   -> Exactamente n veces
# {n,m} -> Entre n y m veces

# Una o más veces (+)
regex_pattern = r"\d+"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

# Cero o más veces (*)
regex_pattern = r"[a].*"  # 'a' seguido de cualquier carácter cero o más veces
txt_text = "Apple and banana are fruits"
matches = re.findall(regex_pattern, txt_text)
print(matches)  # ['and banana are fruits']

# Cero o una vez (?)
txt_email = "email, e-mail, Email, E-mail"
regex_pattern = r"[Ee]-?mail"  # ? indica cero o una vez el guion
matches = re.findall(regex_pattern, txt_email)
print(matches)  # ['email', 'e-mail', 'Email', 'E-mail']

# Exactamente n dígitos y rango {n,m}
regex_pattern = r"\d{4}"  # Exactamente 4 dígitos
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

regex_pattern = r"\d{1,4}"  # Entre 1 y 4 dígitos
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']


# 2.4 PUNTO (.) - Cualquier carácter excepto nueva línea
regex_pattern = r"[a]."  # 'a' seguido de cualquier carácter
txt_text = "Apple and banana are fruits"
matches = re.findall(regex_pattern, txt_text)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r"[a].+"  # 'a' seguido de cualquier carácter una o más veces
matches = re.findall(regex_pattern, txt_text)
print(matches)  # ['and banana are fruits']


# 2.5 CIRCUNFLEJO (^) - Inicio de cadena / Negación
# ^ al inicio -> indica que empieza con ese patrón
# ^ dentro de [] -> negación

regex_pattern = r"^This"  # Cadena que comienza con 'This'
txt = "This is the beginning"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negación con ^
regex_pattern = r"[^A-Za-z ]+"  # NO es A-Z, a-z, o espacio
txt = "December 6, 2019 and revised on July 8, 2021"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8,', '2021']


# ===================================================================
# 3. APLICACIONES PRÁCTICAS
# ===================================================================

# 3.1 Validar nombre de variable en Python
# Las variables en Python: letras, números y guión bajo (_)
# No pueden empezar con número
regex_pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
variables = ["myVar", "_private", "123invalid", "var_name_2", "class"]
for var in variables:
    if re.match(regex_pattern, var):
        print(f"{var} es válido")
    else:
        print(f"{var} es inválido")


# 3.2 Validar correo electrónico
regex_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = ["user@example.com", "invalid.email", "test@domain.co.uk"]
for email in emails:
    if re.match(regex_pattern, email):
        print(f"{email} es válido")
    else:
        print(f"{email} es inválido")


# 3.3 Extraer fechas en formato DD-MM-YYYY
text = "Las fechas importantes: 12-01-2021, 25-12-2020, 01-05-2022"
regex_pattern = r"\d{2}-\d{2}-\d{4}"
dates = re.findall(regex_pattern, text)
print(dates)  # ['12-01-2021', '25-12-2020', '01-05-2022']


# 3.4 Encontrar verbos en tiempo -ing
text = "I am teaching, learning, and coding. She is teaching Python"
regex_pattern = r"\b\w+ing\b"
gerunds = re.findall(regex_pattern, text)
print(gerunds)  # ['teaching', 'learning', 'coding', 'teaching']


# ===================================================================
# 4. BANDERAS Y OPCIONES
# ===================================================================
# re.I o re.IGNORECASE -> Ignora mayúsculas/minúsculas
# re.M o re.MULTILINE -> ^ y $ son inicio/fin de línea
# re.S o re.DOTALL -> . coincide incluida nueva línea
# re.X o re.VERBOSE -> Permite espacios en blanco en el patrón

# Ignorar mayúsculas/minúsculas
txt = "Python python PYTHON"
matches = re.findall("python", txt, re.I)
print(matches)  # ['Python', 'python', 'PYTHON']


# ===================================================================
print("\n✅ Resumen de Expresiones Regulares completado")
# ===================================================================
