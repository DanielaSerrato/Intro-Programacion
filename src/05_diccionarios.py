"""Archivo asociado al notebook 05_diccionarios.ipynb.
Incluye ejemplos y funciones que manipulan diccionarios.

Concepto clave:
- Un diccionario guarda pares clave–valor para acceder rápido a datos.
"""


def obtener_claves(dic):
    return list(dic.keys())


def actualizar_valor(dic, clave, valor):
    dic[clave] = valor
    return dic
