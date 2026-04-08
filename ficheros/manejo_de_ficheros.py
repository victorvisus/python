"""# sintaxis
open('filename', mode) # mode(r, a, w, x, t, b) puede ser lectura, escritura o actualización

"r" - lectura - valor por defecto. Abre el archivo solo para lectura; si no existe genera un error.
"a" - append (añadir) - abre el archivo para agregar contenido al final; crea el archivo si no existe.
"w" - escritura - abre el archivo para escribir, sobrescribe si existe; crea el archivo si no existe.
"x" - crear - crea el archivo; si existe genera un error.
"t" - texto - valor por defecto. Modo texto.
"b" - binario - modo binario (por ejemplo para imágenes).
"""

import os

"""
Abrir un archivo para lectura
El modo por defecto de open es lectura, así que no es necesario especificar 'r' o 'rt'. He creado un archivo llamado reading_file_example.txt en el directorio files. Veamos:
"""
f = open("./files/reading_file_example.txt")
print(
    f
)  # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

"""
Como en el ejemplo, al imprimir el objeto archivo obtenemos información sobre él. Un archivo abierto permite distintos métodos de lectura: read(), readline, readlines. Debemos cerrar el archivo con close() cuando terminemos.

read(): lee todo el texto como una cadena. Podemos limitar el número de caracteres pasando un entero a read(number).
"""
print("-- Imprimimos todo --------------------------------------")

f = open("./files/reading_file_example.txt", "rt")
txt = f.read()
print(type(txt), " es un string")
print(txt)
f.close()

# NOTA: con with open(), en vez de open(), no hace falta hacer el close() del archivo

# En lugar de imprimir todo el texto, podemos leer solamente los primeros 10 caracteres:
print("-- Imprimimos los 10 primeros caracteres -------------------------------")
f = open("./files/reading_file_example.txt")
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# arrelgamos la codificacion

print("-- Imprimimos todo con la codificacion correcta ------------------------")

with open("./files/reading_file_example.txt", "rt", encoding="utf-8") as f:
    txt = f.read()
    print(type(txt), " es un string")
    print(txt)


# readlines(): lee todo el texto línea por línea y devuelve una lista de líneas
print("-- Imprimimos todo con readlines() -------------------------------------")

with open("./files/reading_file_example.txt", "rt", encoding="utf-8") as f:
    txt = f.readlines()
    print(type(txt), " es una lista")
    print(txt)

# read().splitlines() lee todo el texto y lo divide en una lista de sin los saltos de linea \n
print("-- Imprimimos todo con read().splitlines() -----------------------------")

with open("./files/reading_file_example.txt", "rt", encoding="utf-8") as f:
    txt = f.read().splitlines()
    print(type(txt), " es una lista")
    print(txt)

"""
Abrir un archivo para escritura y actualización
Para escribir en un archivo hay que pasar el modo a open():

    "a" - append - añade al final; crea el archivo si no existe.
    "w" - write - sobrescribe el contenido; crea el archivo si no existe.
Añadamos texto al archivo que hemos estado leyendo:
"""
print("-- Escribo al final del fichero ----------------------------------------")
with open("./files/reading_file_example.txt", "a", encoding="utf-8") as f:
    f.write("\nEste texto debe añadirse al final")

print("-- Sobreescribo al final del fichero -----------------------------------")
with open("./files/reading_file_example2.txt", "w", encoding="utf-8") as f:
    f.write("\nNuevo archivo para sobreescribir")


"""
Eliminar archivos
"""
print("-- Eliminar el fichero -------------------------------------------------")
NOMBRE_FICHERO = "./files/reading_file_example2.txt"
# time.sleep(2)
if os.path.exists(NOMBRE_FICHERO):
    os.remove(NOMBRE_FICHERO)
    print("Archivo eliminado")

else:
    print("El archivo no existe")
