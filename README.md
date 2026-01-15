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

## Ruta recomendada del curso en Google Colab (sin instalaciones)

### ¿Por qué usar Google Colab?
Google Colab te permite abrir y ejecutar los notebooks sin instalar nada. Solo necesitas una cuenta de Google y un navegador. Es ideal si estás comenzando y quieres concentrarte en aprender sin preocuparte por configurar tu computador.

### Reglas generales de uso
1. Sigue los notebooks en orden (00 → 10).
2. Ejecuta las celdas de arriba hacia abajo, sin saltar.
3. Haz una copia en tu Google Drive antes de escribir tus respuestas:
   - En Colab: Archivo → Guardar una copia en Drive.
4. No te preocupes si no entiendes todo de inmediato: la práctica hará que las ideas se vuelvan claras.

### Ruta sugerida (en orden)

1. **00 Introducción**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/00_introduccion.ipynb
2. **01 Algoritmos**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/01_algoritmos.ipynb
3. **02 Variables**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/02_variables.ipynb
4. **03 Condicionales**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/03_condicionales.ipynb
5. **04 Listas**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/04_listas.ipynb
6. **05 Diccionarios**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/05_diccionarios.ipynb
7. **06 Funciones**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/06_funciones.ipynb
8. **07 Loops**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/07_loops.ipynb
9. **08 Otras colecciones**  
   https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/08_otras_colecciones.ipynb
10. **09 Repaso**  
    https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/09_repaso.ipynb
11. **10 Proyecto final**  
    https://colab.research.google.com/github/DanielaSerrato/Intro-Programacion/blob/main/notebooks/10_proyecto_final.ipynb


## Uso de los módulos en `src/`

Cada notebook tiene un archivo asociado en `src/` con funciones de apoyo y ejemplos reutilizables.
Puedes importarlos desde los notebooks o desde scripts locales para practicar:

```python
from src.05_diccionarios import obtener_claves
```
