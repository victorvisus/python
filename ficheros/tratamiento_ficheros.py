import json

"""
cargamos un json en txt en formato de diccionario de python, y lo guardamos en un nuevo json.
"""
dataFile = "./data/countries-data.txt"
dataJson = "./data/new-countries-data.json"

try:
    with open(dataFile, "r", encoding="utf-8") as fichero:
        contenido = (
            fichero.read()
        )  # Lee todo el contenido del archivo como una cadena de texto
        dataCountries = json.loads(
            contenido
        )  # Convierte la cadena de texto en un objeto de Python (lista de diccionarios)

        print(f"El número de países es: {len(dataCountries)}")
        print(f"El primer país es: {dataCountries[0]['name']}")

    with open(dataJson, "w", encoding="utf-8") as ficheroExit:
        json.dump(
            dataCountries, ficheroExit, ensure_ascii=False, indent=4
        )  # Escribe el objeto de Python en un archivo JSON con formato legible

    print("El archivo se ha guardado correctamente.")

except FileNotFoundError:
    print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")
except json.JSONDecodeError:
    print("El archivo no es un JSON válido. Verifica su contenido.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
