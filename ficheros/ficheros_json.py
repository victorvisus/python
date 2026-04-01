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
    """
    Cramos un diccionario para contar cuántos países hablan cada idioma. Luego, encontramos el idioma con el conteo máximo.
    con una clave => idioma y valor => número de países que lo hablan, luego iteramos sobre el diccionario para encontrar el idioma con el conteo máximo.
    """
    conteo_idiomas = (
        dict()
    )  # las claves vienen del set() de idioma, que lo convertimos a list()
    lista_idiomas = list(
        idiomas
    )  # convertimos el set de idiomas a una lista para iterar sobre ella

    for idioma in lista_idiomas:
        for pais in paises:
            if idioma in pais["languages"]:
                if (
                    idioma in conteo_idiomas
                ):  # si está ese idioma en el diccionario de conteo, le sumamos 1 al conteo
                    conteo_idiomas[idioma] = conteo_idiomas[idioma] + 1
                else:
                    conteo_idiomas[idioma] = 1
    # ya tengo el dicionario conteo_idiomas con el número de países que hablan cada idioma, ahora busco el idioma con el conteo máximo

    # print(list(conteo_idiomas.keys())[0])
    # itero en la lista de idiomas para encontrar el idioma con el conteo máximo
    idioma_mas_hablado = (
        0  # inicializo el conteo máximo con el conteo del primer idioma
    )

    idioma_mas_hablado_nombre = (
        ""  # inicializo el idioma más hablado con el primer idioma
    )
    for idioma in lista_idiomas:
        if conteo_idiomas[idioma] > idioma_mas_hablado:
            idioma_mas_hablado = conteo_idiomas[idioma]
            idioma_mas_hablado_nombre = idioma
    print(
        f"El idioma más hablado es: {idioma_mas_hablado_nombre} con {idioma_mas_hablado} países que lo hablan."
    )
    # Otra manera de encontrar el idioma más hablado es iterando directamente sobre el diccionario de conteo_idiomas con .items(), que devuelve una tupla (clave, valor) para cada elemento del diccionario, así no tenemos que convertir el set de idiomas a una lista para iterar sobre ella.
    for idioma, conteo in conteo_idiomas.items():
        if conteo > idioma_mas_hablado:
            idioma_mas_hablado = conteo
            idioma_mas_hablado_nombre = idioma
    print(
        f"El idioma más hablado es (con .item()): {idioma_mas_hablado_nombre} con {idioma_mas_hablado} países que lo hablan."
    )

    # 3. Encuentra los diez países con mayor población.


except FileNotFoundError:
    print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")
except json.JSONDecodeError:
    print("El archivo no es un JSON válido. Verifica su contenido.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
