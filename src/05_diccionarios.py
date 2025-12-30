"""Archivo asociado al notebook 05_diccionarios.ipynb.
Incluye ejemplos y funciones que manipulan diccionarios.
"""


def obtener_claves(dic):
    return list(dic.keys())


def actualizar_valor(dic, clave, valor):
    dic[clave] = valor
    return dic
