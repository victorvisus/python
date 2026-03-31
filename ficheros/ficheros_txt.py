try:
    with open("./data/countries-data.txt", "r", encoding="utf-8") as fichero:
        lineas = fichero.readlines()  # .strip() quita el salto de línea sobrante)
except FileNotFoundError:
    print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")

print(lineas[0])  # Accedes a la primera línea
