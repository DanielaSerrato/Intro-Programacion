"""Archivo asociado al notebook 02_variables.ipynb.

Ejemplos de variables y tipos básicos.
"""


def crear_ficha(nombre, edad, ciudad):
    """Devuelve una frase con datos básicos."""
    return f"{nombre} tiene {edad} años y vive en {ciudad}."


def incrementar_edad(edad):
    """Suma 1 a la edad recibida."""
    return edad + 1


if __name__ == "__main__":
    print(crear_ficha("Ana", 20, "Lima"))
