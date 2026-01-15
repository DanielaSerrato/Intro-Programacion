"""Archivo asociado al notebook 05_diccionarios.ipynb.

Ejemplos básicos de diccionarios y acceso por clave.
"""


def crear_persona(nombre, edad):
    """Crea un diccionario con datos de una persona."""
    return {"nombre": nombre, "edad": edad}


def agregar_ciudad(persona, ciudad):
    """Agrega la ciudad al diccionario de persona."""
    persona["ciudad"] = ciudad
    return persona


if __name__ == "__main__":
    print(crear_persona("Ana", 20))
