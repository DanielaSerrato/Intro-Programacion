"""Funciones de práctica general antes del proyecto final.
"""


def sumar_lista(lista):
    return sum(lista)


def saludar(nombre):
    return f"Hola {nombre}, bienvenido al repaso."


def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for c in texto if c in vocales)
