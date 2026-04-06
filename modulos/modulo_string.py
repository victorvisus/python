"""
Módulo string
El módulo string es muy útil. Los siguientes ejemplos muestran algunos usos.
"""

import string

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(
    string.capwords("hola mundo")
)  # Hola Mundo, convierte a mayúscula la primera letra de cada palabra
print(
    string.Template("Hola, $nombre!").substitute(nombre="Alice")
)  # Hola, Alice!, uso de plantillas para formatear cadenas
print(string.whitespace)  # \t\n\r\x0b\x0c, caracteres de espacio en blanco
print(
    string.printable
)  # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c, caracteres imprimibles
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
