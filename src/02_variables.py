"""Archivo asociado al notebook 02_variables.ipynb.
Incluye ejemplos y funciones básicas que usan variables.

Concepto clave:
- Una variable es un nombre que guarda un valor para reutilizarlo.
"""


def resumen_personal(nombre, edad, ciudad):
    """Devuelve un texto descriptivo usando variables."""
    return f"{nombre} tiene {edad} años y vive en {ciudad}."


def cambiar_estado(estado_actual):
    """Invierte un valor booleano."""
    return not estado_actual
