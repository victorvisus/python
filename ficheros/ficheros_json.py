import json

"""
usa el archivo countries-data.py.
    - ¿Cuántos idiomas distintos hay en los datos?
    - ¿Cuál es el idioma usado por más países?
    - Encuentra los diez países con mayor población.
"""
dataJson = "./data/countries-data.json"

try:
    with open(dataJson, "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)

    # cuantos elementos tiene el diccionario de paises
    print(f"El número de países es: {len(paises)}")

    # 1. ¿Cuántos idiomas distintos hay en los datos?
    idiomas = set()  # un set no permite elementos duplicados, así que es ideal para contar idiomas distintos
    for pais in paises:
        for idioma in pais["languages"]:
            idiomas.add(idioma)
    print(f"El número de idiomas distintos es: {len(idiomas)}")

    # 2. ¿Cuál es el idioma usado por más países?

    # 3. Encuentra los diez países con mayor población.


except FileNotFoundError:
    print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")
except json.JSONDecodeError:
    print("El archivo no es un JSON válido. Verifica su contenido.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
