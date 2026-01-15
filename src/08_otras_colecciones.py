"""Archivo asociado al notebook 08_otras_colecciones.ipynb.

Ejemplos básicos de tuplas y sets.
"""


def crear_tupla(nombre, edad, ciudad):
    """Crea una tupla con tres datos."""
    return (nombre, edad, ciudad)


def eliminar_duplicados(lista):
    """Devuelve un set con elementos únicos."""
    return set(lista)


if __name__ == "__main__":
    print(crear_tupla("Ana", 20, "Cali"))
