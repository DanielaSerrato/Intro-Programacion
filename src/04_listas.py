"""Archivo asociado al notebook 04_listas.ipynb.

Ejemplos básicos de creación y manipulación de listas.
"""


def agregar_elemento(lista, elemento):
    """Agrega un elemento a la lista y devuelve la lista actualizada."""
    lista.append(elemento)
    return lista


def obtener_primero(lista):
    """Devuelve el primer elemento de la lista."""
    return lista[0]


if __name__ == "__main__":
    print(agregar_elemento(["perro"], "gato"))
