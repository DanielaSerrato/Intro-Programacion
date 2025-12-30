"""Archivo asociado al notebook 03_condicionales.ipynb.
Incluye ejemplos y funciones que utilizan condicionales.
"""


def clasificar_edad(edad):
    """Devuelve un mensaje según si la persona es mayor de edad."""
    if edad >= 18:
        return "Mayor de edad"
    return "Menor de edad"


def par_o_impar(numero):
    """Devuelve si un número es par o impar."""
    return "Par" if numero % 2 == 0 else "Impar"


def clasificar_temperatura(temp):
    """Clasifica temperatura en frío, templado o caliente."""
    if temp < 15:
        return "Frío"
    elif temp <= 25:
        return "Templado"
    else:
        return "Caliente"
