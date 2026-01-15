"""Archivo asociado al notebook 09_repaso.ipynb.

Ejercicios de integración de conceptos del curso.
"""


def promedio(numeros):
    """Calcula el promedio de una lista de números."""
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)


def filtrar_mayores(personas):
    """Devuelve nombres de personas con edad >= 18."""
    mayores = []
    for persona in personas:
        if persona["edad"] >= 18:
            mayores.append(persona["nombre"])
    return mayores


if __name__ == "__main__":
    print(promedio([2, 4, 6]))
