Proyecto Aprendizaje de maquina 1
Juan José Rodríguez y Fabian Sneyder Moya


Descripción del proyecto:
Este proyecto tiene como objetivo analizar los factores asociados a la depresión en estudiantes y desarrollar un modelo de clasificación capaz de predecir la variable depression, a partir de variables académicas, personales y de estilo de vida.

Se sigue la metodología CRISP-DM, abordando el problema desde la comprensión del negocio hasta la comunicación de resultados mediante un dashboard.


Objetivos

Objetivo general:
Desarrollar un modelo de aprendizaje de máquina que permita identificar patrones asociados a la depresión en estudiantes.

Objetivos específicos:
1.Analizar la calidad y estructura de los datos
2.Identificar relaciones entre variables
3.Preparar y transformar los datos para modelado
3.Entrenar y comparar modelos de clasificación
4.Evaluar el desempeño mediante métricas adecuadas
5.Comunicar resultados mediante visualizaciones y dashboard


Descripción de carpetas

config/
Contiene archivos de configuración del proyecto.

paths.yaml → rutas de archivos

model_config.yaml → parámetros de modelos

Permite centralizar configuraciones sin modificar código.


data/
Contiene los datos en diferentes etapas:

raw/ → datos originales (raw.csv)

interim/ → datos parcialmente procesados

processed/ → datos listos para modelado (train/test)


models/
Almacena los modelos entrenados:

pipelines (.joblib)

métricas (.json)

variables del modelo

Aquí se guardan los modelos listos para despliegue.


notebooks/
Contiene el desarrollo del proyecto por fases CRISP-DM:

01_entendimiento_negocio.ipynb

02_eda.ipynb

03_preparacion.ipynb

04_modelado.ipynb

05_evaluacion.ipynb

06_dashboard.ipynb


reports/
Contiene resultados finales:

dashboard/ → archivos para Power BI o Tableau

figures/ → gráficas

presentation/ → diapositivas

informe.md → conclusiones


src/
Código reutilizable del proyecto:

data/ → carga y limpieza

features/ → ingeniería de variables

modeling/ → entrenamiento y evaluación

visualization/ → gráficas

Permite separar lógica del análisis en notebooks.


Modelos utilizados
Se entrenaron cuatro modelos de clasificación:
1.Regresión Logística
2.Árbol de Decisión
3.Random Forest
4.K-Nearest Neighbors (KNN)

Se evaluaron con:
1.Accuracy
2.Precision
3.Recall
4.F1-score
5.ROC-AUC
6.Matriz de confusión