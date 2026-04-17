# Proyecto Aprendizaje de maquina 1
Juan José Rodríguez y Fabian Sneyder Moya


## Descripción del proyecto:
Este proyecto tiene como objetivo analizar los factores asociados a la depresión en estudiantes y desarrollar un modelo de clasificación capaz de predecir la variable depression, a partir de variables académicas, personales y de estilo de vida.

Se sigue la metodología CRISP-DM, abordando el problema desde la comprensión del negocio hasta la comunicación de resultados mediante un dashboard.


## Objetivos

### Objetivo general:
Desarrollar un modelo de aprendizaje de máquina que permita identificar patrones asociados a la depresión en estudiantes.

### Objetivos específicos:
1. Analizar la calidad y estructura de los datos
2. Identificar relaciones entre variables
3. Preparar y transformar los datos para modelado
3. Entrenar y comparar modelos de clasificación
4. Evaluar el desempeño mediante métricas adecuadas
5. Comunicar resultados mediante visualizaciones y dashboard


## Descripción de carpetas

### config/:Contiene archivos de configuración del proyecto.
- paths.yaml → rutas de archivos
- model_config.yaml → parámetros de modelos
Permite centralizar configuraciones sin modificar código.


### data/: Contiene los datos en diferentes etapas:
- raw/ → datos originales (raw.csv)
- interim/ → datos parcialmente procesados
- processed/ → datos listos para modelado (train/test)


### models/: Almacena los modelos entrenados:
- pipelines (.joblib)
- métricas (.json)
- variables del modelo
Aquí se guardan los modelos listos para despliegue.


### notebooks/: Contiene el desarrollo del proyecto por fases CRISP-DM:
1. 01_entendimiento_negocio.ipynb
2. 02_eda.ipynb
3. 03_preparacion.ipynb
4. 04_modelado.ipynb
5. 05_evaluacion.ipynb
6. 06_dashboard.ipynb


### reports/: Contiene resultados finales:
- dashboard/ → archivos para Power BI o Tableau
- figures/ → gráficas
- presentation/ → diapositivas
- informe.md → conclusiones


### src/: Código reutilizable del proyecto:
- data/ → carga y limpieza
- features/ → ingeniería de variables
- modeling/ → entrenamiento y evaluación
- visualization/ → gráficas
Permite separar lógica del análisis en notebooks.


## Modelos utilizados
Se entrenaron cuatro modelos de clasificación:
1. Regresión Logística
2. Árbol de Decisión
3. Random Forest
4. K-Nearest Neighbors (KNN)

Se evaluaron con:
1. Accuracy
2. Precision
3. Recall
4. F1-score
5. ROC-AUC
6. Matriz de confusión


## Consideraciones éticas sobre el uso de Inteligencia Artificial: Durante el desarrollo de este proyecto se utilizó inteligencia artificial como una herramienta de apoyo para fortalecer el proceso de aprendizaje y mejorar la calidad técnica del trabajo. Su uso se realizó de manera responsable, crítica y complementaria, sin sustituir el rol activo de los estudiantes en la construcción del conocimiento.

### Uso de la inteligencia artificial en el proyecto: La inteligencia artificial fue utilizada principalmente como:
- herramienta de apoyo en la estructuración del proyecto bajo la metodología CRISP-DM
- guía para la organización de carpetas y arquitectura del repositorio
- asistencia en la escritura y optimización de código
- ayuda en la gestión de rutas y manejo eficiente de archivos dentro del proyecto
- apoyo en la redacción de algunos apartados técnicos

Es importante resaltar que la IA no tomó decisiones autónomas sobre el desarrollo del proyecto. Su uso estuvo siempre mediado por la interpretación, validación y criterio de los estudiantes.


### Rol de los estudiantes
Nosotros como estudiantes tuvimos un papel central y activo en todo el proceso, incluyendo:
- la comprensión del problema de negocio
- el análisis exploratorio de los datos (EDA)
- la identificación de problemas de calidad de datos
- la toma de decisiones sobre limpieza, transformación y selección de variables
- el diseño del flujo del proyecto
- la selección, entrenamiento y evaluación de los modelos
- la interpretación de resultados y generación de conclusiones

Además, fuimos responsables de:
- proporcionar a la IA el contexto necesario (archivos, datos, instrucciones)
- validar cada sugerencia antes de implementarla
- adaptar el código a las necesidades específicas del proyecto
- garantizar la coherencia metodológica del trabajo


### Relación entre estudiantes e inteligencia artificial
El uso de la IA se dio como una herramienta colaborativa, donde:
- los estudiantes definieron el problema y los objetivos
- la IA ofreció sugerencias técnicas y estructurales
- los estudiantes evaluaron, ajustaron y decidieron qué implementar

En ningún momento se utilizó la IA como sustituto del aprendizaje, sino como un medio para:
- mejorar la eficiencia
- reducir errores técnicos
- fortalecer la organización del proyecto
- explorar buenas prácticas en desarrollo de proyectos de ciencia de datos


### Consideración final
El uso de inteligencia artificial en este proyecto se enmarca dentro de un enfoque ético y académico, donde:
- no se delegó la responsabilidad del aprendizaje
- no se automatizó la toma de decisiones críticas
- se mantuvo el control humano sobre todo el proceso

En este sentido, la IA fue utilizada como una herramienta de apoyo para potenciar el aprendizaje, sin reemplazar el análisis, la interpretación y el juicio profesional de los estudiantes.