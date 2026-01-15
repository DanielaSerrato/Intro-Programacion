"""Archivo asociado al notebook 03_condicionales.ipynb.

Ejemplos de decisiones con if, elif y else.
"""


def clasificar_numero(numero):
    """Devuelve un mensaje indicando si el número es positivo, negativo o cero."""
    if numero > 0:
        return "El número es positivo"
    if numero < 0:
        return "El número es negativo"
    return "El número es cero"


def es_par(numero):
    """Devuelve True si el número es par."""
    return numero % 2 == 0


if __name__ == "__main__":
    print(clasificar_numero(3))
