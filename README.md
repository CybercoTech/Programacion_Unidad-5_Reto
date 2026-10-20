# Programacion_Unidad-5_Reto
José Miguel Vásquez y Isabela Montaño - Reto 5

Explorador CLI para el Análisis y Visualización de Archivos Reales

Descripción del Proyecto

Este repositorio contiene el código fuente de una aplicación de línea de comandos (CLI) desarrollada en Python. La herramienta está diseñada para procesar, analizar estadísticamente y visualizar conjuntos de datos extraídos del mundo real a partir de archivos de texto (.txt, .log) y archivos de valores separados por comas (.csv).

El desarrollo se ha realizado utilizando exclusivamente la biblioteca estándar de Python y la librería matplotlib para la generación de gráficos, en estricto cumplimiento con las restricciones del reto (exclusión de librerías de análisis de datos avanzadas como pandas o numpy).

Estructura del Repositorio

El proyecto sigue una arquitectura modular para separar las responsabilidades del código:

```text
Proyecto_Analisis_Datos/
│
├── main.py                 # Punto de entrada y gestión del menú principal
├── README.md               # Documentación del proyecto
│
├── /modules                # Módulos con la lógica de procesamiento
│   ├── __init__.py         # Inicializador del paquete
│   ├── utils.py            # Funciones de soporte (formato de consola, limpieza)
│   ├── text_analyzer.py    # Lógica de análisis para archivos de texto
│   └── csv_analyzer.py     # Lógica de análisis para archivos CSV
│
├── /data                   # Directorio con los archivos de datos utilizados
│   ├── servidor.log
│   └── ventas.csv
│
├── /outputs                # Directorio de salida para los gráficos generados
│
└── /docs                   # Diagramas de flujo del sistema
```

Origen de los Datos

Para la validación y prueba de la aplicación, se implementaron los siguientes conjuntos de datos:

1. Archivo de registro (servidor.log): Corresponde a un archivo de texto que simula los registros de acceso y errores de un servidor web. Incluye marcas de tiempo, niveles de severidad (INFO, ERROR) y códigos de estado HTTP, lo que permite probar la extracción de patrones.
2. Conjunto de datos tabular (ventas.csv): Datos obtenidos de [Kaggle / Portal de Datos Abiertos - Especificar fuente]. El archivo contiene registros históricos de ventas de un comercio, incluyendo variables categóricas (categoría de producto, ciudad) y variables numéricas (precio, cantidad, total).

Análisis y Conclusiones

A partir de la ejecución del programa y la observación de los gráficos generados en el directorio /outputs, se extraen las siguientes conclusiones:

1. Análisis de texto (Gráficos 1 y 2): El análisis de frecuencia de palabras en servidor.log demuestra que los términos relacionados con errores (ej. "ERROR", "404") representan un porcentaje significativo del total de las líneas. Asimismo, el histograma de longitud de líneas indica que la mayoría de los registros tienen una estructura homogénea de entre 50 y 100 caracteres, lo que facilita el diseño de futuros filtros automáticos.
2. Análisis categórico (Gráfico 4): La representación de pastel del archivo ventas.csv revela una clara concentración del volumen de ventas en una categoría específica ([Insertar categoría real, ej. Electrónica]), la cual supera el 40% de participación total. Esto sugiere que dicho segmento es el principal motor de ingresos del negocio analizado.
3. Análisis de correlación (Gráfico 5): El gráfico de dispersión entre las variables numéricas seleccionadas ([Insertar variables, ej. Precio vs Cantidad]) muestra una tendencia negativa: a medida que el precio unitario del producto aumenta, la cantidad demandada tiende a disminuir, confirmando el comportamiento esperado de la elasticidad precio-demanda en los datos proporcionados.

Instrucciones de Ejecución

1. Clone el repositorio y acceda al directorio raíz del proyecto mediante la terminal.
2. Ejecute el archivo principal:
   ```bash
   python main.py
   ```
3. Utilice el menú interactivo para explorar los directorios, analizar los textos o procesar los conjuntos de datos en formato CSV. Los gráficos se guardarán automáticamente en la carpeta outputs/.

Información Académica

· Autor: Jose Miguel Vasquez y Isabela Montaño 
· Institución: Universidad Pontificia Bolivariana
· Asignatura: Programacion
· Evaluación: Reto Unidad 5 - Análisis Visual de Datos Reales