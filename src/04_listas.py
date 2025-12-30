"""Archivo asociado al notebook 04_listas.ipynb.
Incluye ejemplos y funciones útiles que manipulan listas.
"""


def obtener_primero_y_ultimo(lista):
    if not lista:
        return None, None
    return lista[0], lista[-1]


def agregar_y_ordenar(lista, elemento):
    lista.append(elemento)
    return sorted(lista)
