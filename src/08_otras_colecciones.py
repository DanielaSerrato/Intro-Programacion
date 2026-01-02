"""Funciones de apoyo para el capítulo 08: tuplas y sets.

Concepto clave:
- Las tuplas son inmutables; los sets eliminan duplicados.
"""


def es_miembro(conjunto, elemento):
    return elemento in conjunto


def contar_unicos(lista):
    return len(set(lista))


def crear_coordenada(x, y):
    return (x, y)
