"""Archivo asociado al notebook 07_loops.ipynb.
Incluye funciones relacionadas con ciclos.

Concepto clave:
- Un loop repite acciones; `for` recorre y `while` repite según condición.
"""


def recorrer_lista(lista):
    """Imprime cada elemento de una lista."""
    for elemento in lista:
        print(elemento)


def sumar_lista(lista):
    """Suma todos los elementos de la lista."""
    return sum(lista)


def recorrer_diccionario(dic):
    """Imprime claves y valores."""
    for k, v in dic.items():
        print(k, v)
