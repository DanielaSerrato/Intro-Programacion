"""Archivo asociado al notebook 07_loops.ipynb.

Ejemplos básicos de ciclos for y while.
"""


def sumar_lista(numeros):
    """Suma los elementos de una lista usando un acumulador."""
    total = 0
    for numero in numeros:
        total += numero
    return total


def contar_hasta(limite):
    """Devuelve una lista con números del 1 al limite usando while."""
    resultado = []
    contador = 1
    while contador <= limite:
        resultado.append(contador)
        contador += 1
    return resultado


if __name__ == "__main__":
    print(sumar_lista([1, 2, 3]))
