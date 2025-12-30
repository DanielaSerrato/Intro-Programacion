"""Funciones de apoyo para el capítulo 08: tuplas y sets.
"""


def es_miembro(conjunto, elemento):
    return elemento in conjunto


def contar_unicos(lista):
    return len(set(lista))


def crear_coordenada(x, y):
    return (x, y)
