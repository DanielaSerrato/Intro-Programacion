# Plan de clases 7–10: SQL

## Clase 7: SQL básico (SELECT, WHERE, ORDER BY, GROUP BY, tipos)

**Objetivo:** introducir la sintaxis base de SQL para consultar datos, filtrar resultados, ordenar y agrupar, con foco en tipos de datos comunes.

**Agenda (180 min)**
1. **Bienvenida y objetivos (10 min)**
2. **Contexto y repaso de bases de datos relacionales (25 min)**
3. **SELECT y FROM: lectura básica de tablas (35 min)**
4. **Pausa breve (15 min)**
5. **WHERE y operadores básicos (30 min)**
6. **ORDER BY y LIMIT: ordenar y acotar resultados (25 min)**
7. **GROUP BY + agregaciones y tipos de datos (30 min)**
8. **Quiz de cierre (10 min)**

**Quiz (auto-evaluación)**
1. ¿Qué diferencia hay entre `WHERE` y `HAVING` y en qué casos usarías cada uno?
2. Escribe una consulta que devuelva nombres y edades ordenadas de mayor a menor.
3. ¿Para qué sirve `GROUP BY` y qué funciones de agregación conoces?
4. ¿Qué tipos de datos usarías para almacenar fechas y números decimales?
5. ¿Qué hace la cláusula `LIMIT`?

---

## Clase 8: JOINS multi-tabla con ejercicios de integración

**Objetivo:** combinar información de varias tablas usando joins y resolver ejercicios de integración con claves primarias y foráneas.

**Agenda (180 min)**
1. **Bienvenida y objetivos (10 min)**
2. **Modelo relacional y llaves (PK/FK) (20 min)**
3. **INNER JOIN: sintaxis y casos típicos (35 min)**
4. **LEFT JOIN y manejo de nulos (30 min)**
5. **Pausa breve (15 min)**
6. **RIGHT/FULL JOIN (conceptual) y buenas prácticas (20 min)**
7. **Ejercicios integradores multi-tabla (40 min)**
8. **Quiz de cierre (10 min)**

**Quiz (auto-evaluación)**
1. ¿Cuándo usarías un `LEFT JOIN` en lugar de un `INNER JOIN`?
2. ¿Qué sucede con los registros sin coincidencia en cada tipo de join?
3. Dibuja un ejemplo simple de PK/FK entre dos tablas.
4. ¿Qué columna conviene usar en la condición del join y por qué?
5. ¿Qué problema resuelve un join en un modelo normalizado?

---

## Clase 9: CRUD y calidad en contexto (nulos, duplicados)

**Objetivo:** ejecutar operaciones CRUD y evaluar calidad de datos, con foco en nulos, duplicados y validaciones básicas.

**Agenda (180 min)**
1. **Bienvenida y objetivos (10 min)**
2. **CREATE/INSERT: carga básica de datos (30 min)**
3. **READ: consultas con filtros y validaciones (25 min)**
4. **Pausa breve (15 min)**
5. **UPDATE/DELETE: cambios controlados (30 min)**
6. **Calidad de datos: nulos, duplicados y reglas simples (35 min)**
7. **Ejercicios prácticos de CRUD + limpieza (25 min)**
8. **Quiz de cierre (10 min)**

**Quiz (auto-evaluación)**
1. ¿Qué diferencia hay entre `DELETE` y `TRUNCATE`?
2. ¿Cómo identificarías registros duplicados en una tabla?
3. ¿Qué cuidado extra tendrías antes de ejecutar un `UPDATE` masivo?
4. ¿Qué significa `NULL` y cómo se filtra correctamente?
5. ¿Qué prácticas ayudan a mejorar la calidad de datos en una base?

---

## Clase 10: CTEs y vistas (nivel básico)

**Objetivo:** introducir CTEs y vistas como herramientas para modularizar consultas y reutilizar lógica, sin usar funciones de ventana.

**Agenda (180 min)**
1. **Bienvenida y objetivos (10 min)**
2. **Motivación: por qué modularizar consultas (15 min)**
3. **CTEs básicos (`WITH`) con ejemplos (35 min)**
4. **Pausa breve (15 min)**
5. **Vistas: creación, uso y limitaciones (35 min)**
6. **Comparación CTE vs vista y criterios de uso (20 min)**
7. **Ejercicios guiados (40 min)**
8. **Quiz de cierre (10 min)**

**Quiz (auto-evaluación)**
1. ¿Qué ventaja ofrece un CTE frente a una subconsulta anidada?
2. ¿Cuándo preferirías una vista sobre un CTE?
3. Escribe un ejemplo mínimo de `WITH` con un alias.
4. ¿Una vista almacena datos o solo una definición de consulta?
5. ¿Qué cuidados considerarías al crear vistas compartidas?
