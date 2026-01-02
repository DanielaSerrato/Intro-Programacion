"""Archivo asociado al notebook 06_funciones.ipynb.
Incluye funciones básicas usadas como ejemplos en el curso.

Concepto clave:
- Una función es un bloque reutilizable que puede recibir datos y devolver resultados.
"""


def saludo(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"


def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2


def contar_elementos(lista):
    """Cuenta elementos de una lista."""
    return len(lista)


def es_par(n):
    """Retorna True si n es par."""
    return n % 2 == 0
