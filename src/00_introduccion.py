"""Resumen del capítulo 00 - Introducción.

Temas cubiertos:
- Qué es Python y para qué sirve.
- Uso básico de Google Colab (Markdown vs código, ejecutar, guardar).
- Primeros pasos con print().
- Variables y tipos básicos.
- Primera función con def y return.
"""


def saludo_basico(nombre):
    """Devuelve un saludo simple usando un f-string."""
    return f"Hola, {nombre}!"


if __name__ == "__main__":
    print(saludo_basico("Estudiante"))
