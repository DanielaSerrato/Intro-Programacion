# Auditoría pedagógica del repositorio

## 1) Mapa de contenidos (orden actual, objetivos y prerequisitos)

**Ruta principal del curso (00 → 10):**

1. **00_introduccion.ipynb**  
   - **Objetivo:** presentar Python, el entorno de trabajo (Colab), `print()`, variables/tipos básicos y una primera función.  
   - **Prerequisitos implícitos:** ninguno.
2. **01_algoritmos.ipynb**  
   - **Objetivo:** definir algoritmos como pasos ordenados antes de programar.  
   - **Prerequisitos implícitos:** `print()` y variables básicas.
3. **02_variables.ipynb**  
   - **Objetivo:** crear y usar variables de distintos tipos.  
   - **Prerequisitos implícitos:** `print()`.
4. **03_condicionales.ipynb**  
   - **Objetivo:** tomar decisiones con `if/elif/else` y operadores de comparación.  
   - **Prerequisitos implícitos:** variables, tipos y operadores básicos.
5. **04_listas.ipynb**  
   - **Objetivo:** crear y manipular listas con índices y métodos simples.  
   - **Prerequisitos implícitos:** variables y tipos.
6. **05_diccionarios.ipynb**  
   - **Objetivo:** crear y usar diccionarios con claves y valores.  
   - **Prerequisitos implícitos:** variables y tipos.
7. **06_funciones.ipynb**  
   - **Objetivo:** definir funciones con parámetros y `return`.  
   - **Prerequisitos implícitos:** variables y operadores básicos.
8. **07_loops.ipynb**  
   - **Objetivo:** repetir instrucciones con `for` y `while`.  
   - **Prerequisitos implícitos:** listas y condicionales.
9. **08_otras_colecciones.ipynb**  
   - **Objetivo:** conocer tuplas y sets, y cuándo usarlos.  
   - **Prerequisitos implícitos:** listas.
10. **09_repaso.ipynb**  
    - **Objetivo:** integrar variables, condicionales, listas, diccionarios, funciones y loops.  
    - **Prerequisitos implícitos:** capítulos 00–08.
11. **10_proyecto_final.ipynb**  
    - **Objetivo:** aplicar todo lo aprendido en un mini-sistema de gestión de usuarios.  
    - **Prerequisitos implícitos:** capítulos 00–09.

---

## 2) Secuencia oficial de conceptos del curso

**Secuencia definida (basada en el orden real del repo):**
1. Qué es Python y para qué sirve
2. Google Colab (Markdown vs código, ejecutar, guardar)
3. `print()` como primer output
4. Variables y tipos básicos (`str`, `int`, `float`, `bool`)
5. Algoritmos como pasos ordenados
6. Operadores y comparaciones básicas
7. Condicionales (`if`, `elif`, `else`, `and`, `or`)
8. Listas (crear, índices, `append`, `remove`, `len`)
9. Diccionarios (claves, valores, `get`)
10. Funciones (`def`, parámetros, `return`)
11. Loops (`for`, `while`, `range`)
12. Tuplas y sets
13. Integración (repaso)
14. Proyecto final

---

## 3) Auditoría por archivo (problemas y acciones)

| Archivo | Conceptos introducidos | Prerequisitos | Problemas detectados | Acción tomada |
|---|---|---|---|---|
| README.md | Orden general del curso, uso de Colab | Ninguno | Había archivos extra en el repo que no aparecían en la ruta oficial. | Se mantuvo la ruta oficial y se eliminaron materiales duplicados/placeholder para evitar confusión. |
| notebooks/00_introduccion.ipynb | Colab, `print`, variables, tipos, primera función | Ninguno | Faltaban instrucciones de Colab y una progresión explícita hacia funciones. | Reestructuración completa con flujo pedagógico y ejercicios estandarizados. |
| notebooks/01_algoritmos.ipynb | Algoritmos como pasos | `print`, variables | Uso de listas/loops antes de introducirlos. | Sustituido por pasos en texto y ejercicios con variables simples. |
| notebooks/02_variables.ipynb | Variables y tipos | `print` | Ejercicios sin formato consistente. | Ejercicios estandarizados con scaffolding, pruebas y pistas. |
| notebooks/03_condicionales.ipynb | Condicionales | Variables y operadores | Ejercicios pedían `input` implícitamente y formato inconsistente. | Ejercicios con variables definidas y pruebas simples. |
| notebooks/04_listas.ipynb | Listas | Variables y tipos | Se mencionaban recorridos antes de enseñar loops. | Se enfocó en creación y métodos básicos sin loops. |
| notebooks/05_diccionarios.ipynb | Diccionarios | Variables y tipos | Ejercicios con recorridos no explicados. | Se limitaron a creación, acceso y `.get()`. |
| notebooks/06_funciones.ipynb | Funciones | Variables y operadores | Se usaban loops antes de presentarlos. | Ejercicios ajustados a operaciones simples y `return`. |
| notebooks/07_loops.ipynb | Loops `for`/`while` | Listas, condicionales | Ejercicios sin formato consistente. | Estandarización completa y ejemplos claros. |
| notebooks/08_otras_colecciones.ipynb | Tuplas y sets | Listas | Formato inconsistente. | Ejercicios estandarizados con ejemplos. |
| notebooks/09_repaso.ipynb | Integración | 00–08 | Ejercicios sin estructura uniforme. | Se reescribió la sección de ejercicios con plantilla común. |
| notebooks/10_proyecto_final.ipynb | Proyecto integrador | 00–09 | Código completo sin scaffolding ni pruebas. | Se convirtió en pasos guiados con funciones y asserts simples. |
| src/00_introduccion.py | Resumen del capítulo 00 | Ninguno | Resumen desactualizado respecto al notebook. | Actualizado al nuevo flujo de 00. |
| src/01_algoritmos.py | Algoritmos en texto | `print`, variables | Usaba listas antes de introducirlas. | Reemplazado por funciones que devuelven texto paso a paso. |
| src/02_variables.py | Variables y tipos | `print` | Ejemplos mínimos. | Se añadieron funciones simples coherentes con el notebook. |
| src/03_condicionales.py | Condicionales | Variables y operadores | Sin inconsistencias mayores. | Ajustado para alinear con los ejercicios del notebook. |
| src/04_listas.py | Listas | Variables | Sin inconsistencias mayores. | Ajustado a operaciones básicas sin loops. |
| src/05_diccionarios.py | Diccionarios | Variables | Sin inconsistencias mayores. | Ajustado a claves y valores básicos. |
| src/06_funciones.py | Funciones | Variables y operadores | Sin inconsistencias mayores. | Ajustado a funciones sencillas de retorno. |
| src/07_loops.py | Loops | Listas | Sin inconsistencias mayores. | Ajustado con ejemplos de acumuladores y while. |
| src/08_otras_colecciones.py | Tuplas y sets | Listas | Sin inconsistencias mayores. | Ajustado con ejemplos simples. |
| src/09_repaso.py | Integración | 00–08 | Sin inconsistencias mayores. | Actualizado con ejercicios de repaso. |
| src/proyecto_final.py | Proyecto final | 00–09 | Usaba list comprehension y `global` sin explicar. | Simplificado con loops explícitos y funciones coherentes. |
| notebooks/03_loops.ipynb | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| notebooks/04_diccionarios.ipynb | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| notebooks/04_otras_colecciones.ipynb | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| notebooks/05_funciones.ipynb | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| notebooks/05_funciones_aplicadas.ipynb | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| notebooks/06_proyecto_final.ipynb | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/algoritmos.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/condicionales.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/diccionarios.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/funciones.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/listas.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/loops.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/otras_colecciones.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/tipos.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |
| src/variables.py | Placeholder | — | Duplicado sin contenido real. | Eliminado para evitar confusión. |

---

## 4) Reglas de estilo del curso (convenciones)

1. **Títulos claros y consistentes:** usar `#` para el título del capítulo y `##` para secciones principales.
2. **Bienvenida estándar al inicio de cada notebook** (misma redacción en todos).
3. **Progresión pedagógica:** no usar un concepto antes de explicarlo.
4. **Formato de ejercicios obligatorio:**
   - Enunciado claro.
   - Celda de código con `# TU CÓDIGO AQUÍ`.
   - 1–2 pruebas simples (`assert`) o ejemplos de entrada/salida.
   - Pista breve opcional.
5. **Evitar `input()` hasta el proyecto final** (y solo como paso opcional).
6. **Lenguaje amigable y neutro**, sin tecnicismos innecesarios.

---

## 5) Recomendaciones de próximos pasos

- Agregar una **rúbrica breve** al proyecto final (criterios de evaluación claros).
- Incluir un **glosario** con definiciones simples de conceptos clave.
- Preparar un **mini-quizz** por capítulo (2–3 preguntas de autoevaluación).
- Agregar un **checklist de progreso** al inicio de cada notebook (por ejemplo, “Si ya sabes X, puedes avanzar a Y”).
