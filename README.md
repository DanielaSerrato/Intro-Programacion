# Intro-Programacion

Curso universitario de introducción a la programación con Python para estudiantes de ingeniería en modalidad presencial/híbrida.

## Objetivos del curso

- Desarrollar pensamiento computacional y resolución de problemas.
- Aprender programación en Python desde cero.
- Dominar estructuras de datos básicas (listas, diccionarios, tuplas, sets).
- Usar condicionales, ciclos y funciones.
- Organizar código en módulos reutilizables.
- Integrar conceptos en un proyecto final.

## Estructura del repositorio

```
intro-programacion/
├── notebooks/
│   ├── 00_introduccion.ipynb
│   ├── 01_algoritmos.ipynb
│   ├── 02_variables.ipynb
│   ├── 03_condicionales.ipynb
│   ├── 04_listas.ipynb
│   ├── 05_diccionarios.ipynb
│   ├── 06_funciones.ipynb
│   ├── 07_loops.ipynb
│   ├── 08_otras_colecciones.ipynb
│   ├── 09_repaso.ipynb
│   └── 10_proyecto_final.ipynb
├── src/
│   ├── 00_introduccion.py
│   ├── 01_algoritmos.py
│   ├── 02_variables.py
│   ├── 03_condicionales.py
│   ├── 04_listas.py
│   ├── 05_diccionarios.py
│   ├── 06_funciones.py
│   ├── 07_loops.py
│   ├── 08_otras_colecciones.py
│   ├── 09_repaso.py
│   └── proyecto_final.py
├── styles/
│   └── pdf_style.css
├── pdf/
│   └── (vacío por ahora)
├── README.md
└── .gitignore
```

## Notebooks del curso (00–10)

- **00 Introducción**: propósito del curso, entorno y primeros pasos.
- **01 Algoritmos**: definición de algoritmos y traducción a pasos claros.
- **02 Variables**: creación y uso de variables y tipos básicos.
- **03 Condicionales**: decisiones con `if`, `elif` y `else`.
- **04 Listas**: listas, índices, modificación y recorridos.
- **05 Diccionarios**: pares clave–valor y operaciones básicas.
- **06 Funciones**: definición, parámetros, retorno y buenas prácticas.
- **07 Loops**: ciclos `for` y `while` con ejemplos aplicados.
- **08 Otras colecciones**: tuplas y sets.
- **09 Repaso**: integración de conceptos antes del proyecto final.
- **10 Proyecto final**: sistema de gestión de usuarios en consola.

## Cómo ejecutar los notebooks

### En VS Code

1. Instala la extensión de Python.
2. Abre la carpeta del proyecto en VS Code.
3. Abre el notebook deseado desde `notebooks/`.
4. Selecciona un kernel de Python.

### En Jupyter Notebook

1. Asegúrate de tener Jupyter instalado.
2. Ejecuta `jupyter notebook` en la raíz del proyecto.
3. Abre el notebook desde `notebooks/`.

### En Google Colab

1. Sube el repositorio a GitHub.
2. Abre el notebook usando el enlace:

```
https://colab.research.google.com/github/TU_USUARIO_DE_GITHUB/intro-programacion/notebooks/NOMBRE_DEL_NOTEBOOK.ipynb
```

## Uso de los módulos en `src/`

Cada notebook tiene un archivo asociado en `src/` con funciones de apoyo y ejemplos reutilizables.
Puedes importarlos desde los notebooks o desde scripts locales para practicar:

```python
from src.05_diccionarios import obtener_claves
```

## Generación de PDFs

La hoja de estilos `styles/pdf_style.css` está preparada para exportar notebooks a PDF con un formato consistente.
Para automatizar la generación, aplica este CSS al proceso de exportación (por ejemplo, usando nbconvert con HTML + CSS o una herramienta externa de conversión a PDF).
