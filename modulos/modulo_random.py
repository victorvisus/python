"""
Módulo random
Ahora que sabes importar módulos, familiaricémonos con random. El módulo random nos da números aleatorios entre 0 y 0.9999. El módulo tiene muchas funciones; aquí usamos random y randint.
"""

from random import randint, random

print(random())  # no necesita parámetros; devuelve un valor entre 0 y 0.9999
print(randint(5, 20))  # devuelve un entero aleatorio en [5, 20] (inclusive)
