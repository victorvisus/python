"""
Módulo sys
El módulo sys provee funciones y variables para interactuar con diferentes partes del entorno de ejecución de Python. La función sys.argv devuelve la lista de argumentos de la línea de comandos pasados al script de Python. El elemento en el índice 0 de esa lista es siempre el nombre del script, el índice 1 es el primer argumento pasado desde la línea de comandos.
"""

import sys

# print(sys.argv[0], argv[1],sys.argv[2])  # esta línea imprimirá: nombre_archivo argumento1 argumento2
print(
    "Bienvenido {} a la ejecución de {}, . Disfruta {}!".format(
        sys.argv[1], sys.argv[0], sys.argv[2]
    )
)
print("estas ejecutando con la versión de Python {}".format(sys.version))
print("donde el tamaño máximo de un entero es {}".format(sys.maxsize))
print("la ruta de módulos es {}".format(sys.path))

"""
# salir del script
sys.exit()
# conocer el tamaño máximo de un entero
sys.maxsize
# conocer la ruta de módulos
sys.path
# conocer la versión de Python en uso
sys.version
# conocer la versión de Python en uso
sys.version_info
"""
