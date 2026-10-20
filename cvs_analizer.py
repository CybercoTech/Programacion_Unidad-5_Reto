# modules/csv_analyzer.py
import csv
import statistics
import os
from collections import Counter
import matplotlib.pyplot as plt
from modules.utils import (
    imprimir_titulo, imprimir_error, imprimir_exito,
    pausar, AZUL, AMARILLO, CIAN, RESET
)


def leer_csv(ruta_archivo):
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = list(lector)
            return datos, lector.fieldnames
    except FileNotFoundError:
        imprimir_error(f"No se encontró el archivo: {ruta_archivo}")
        return None, None
    except Exception as e:
        imprimir_error(f"Error al leer el CSV: {e}")
        return None, None


def mostrar_vista_previa(datos, columnas):
    imprimir_titulo("VISTA PREVIA DE DATOS")
    print(f"Columnas detectadas: {CIAN}{', '.join(columnas)}{RESET}\n")

    print(f"{AMARILLO}--- PRIMERAS 10 FILAS ---{RESET}")
    for fila in datos[:10]:
        print(fila)

    print(f"\n{AMARILLO}--- ÚLTIMAS 5 FILAS ---{RESET}")
    for fila in datos[-5:]:
        print(fila)


def calcular_estadisticas(datos):
    imprimir_titulo("ESTADÍSTICAS DESCRIPTIVAS")
    columna = input("Ingresa el nombre EXACTO de la columna numérica (ej. ventas, precio): ").strip()

    datos_numericos = []
    for fila in datos:
        valor = fila.get(columna)
        if valor and valor.strip() != "" and valor.lower() != "null" and valor.lower() != "nan":
            try:
                datos_numericos.append(float(valor))
            except ValueError:
                continue

    if not datos_numericos:
        imprimir_error(f"No se encontraron datos numéricos válidos en la columna '{columna}'.")
        return

    print(f"\nAnálisis de la columna: {columna}")
    print(f"Total de registros válidos: {AZUL}{len(datos_numericos)}{RESET}")
    print(f"Promedio (Media): {AZUL}{statistics.mean(datos_numericos):.2f}{RESET}")
    print(f"Mediana: {AZUL}{statistics.median(datos_numericos):.2f}{RESET}")
    print(f"Valor Máximo: {AZUL}{max(datos_numericos)}{RESET}")
    print(f"Valor Mínimo: {AZUL}{min(datos_numericos)}{RESET}")


def generar_grafico_tendencia(datos):
    imprimir_titulo("GRÁFICO 3: EVOLUCIÓN TEMPORAL")
    col_x = input("Columna para el Eje X (ej. fecha, mes): ").strip()
    col_y = input("Columna para el Eje Y (ej. ventas, temperatura): ").strip()

    x_valores = []
    y_valores = []

    try:
        for fila in datos:
            if fila.get(col_x) and fila.get(col_y):
                x_valores.append(fila[col_x])
                y_valores.append(float(fila[col_y]))

        plt.figure(figsize=(10, 5))
        plt.style.use('ggplot')
        plt.plot(x_valores, y_valores, marker='o', color='blue', linestyle='-')
        plt.title(f'Tendencia: {col_y} vs {col_x}', fontweight='bold')
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('outputs/grafico_3_tendencia.png', dpi=300)
        plt.close()
        imprimir_exito("Gráfico de tendencia generado en /outputs.")
    except ValueError:
        imprimir_error("El eje Y debe contener datos numéricos.")


def generar_grafico_pastel(datos):
    imprimir_titulo("GRÁFICO 4: COMPARACIÓN CATEGÓRICA")
    columna = input("Ingresa la columna categórica (ej. ciudad, categoria): ").strip()

    valores = [fila[columna] for fila in datos if fila.get(columna)]

    if not valores:
        imprimir_error("Columna no encontrada o vacía.")
        return

    conteo = Counter(valores)
    etiquetas = list(conteo.keys())
    tamanos = list(conteo.values())

    plt.figure(figsize=(8, 8))
    plt.style.use('ggplot')
    plt.pie(tamanos, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f'Distribución por {columna}', fontweight='bold')
    plt.tight_layout()
    plt.savefig('outputs/grafico_4_pastel.png', dpi=300)
    plt.close()
    imprimir_exito("Gráfico de pastel generado en /outputs.")


def generar_grafico_dispersion(datos):
    imprimir_titulo("GRÁFICO 5: CORRELACIÓN DE VARIABLES")
    col_x = input("Primera columna numérica (Eje X): ").strip()
    col_y = input("Segunda columna numérica (Eje Y): ").strip()

    x_valores = []
    y_valores = []

    try:
        for fila in datos:
            if fila.get(col_x) and fila.get(col_y):
                x_valores.append(float(fila[col_x]))
                y_valores.append(float(fila[col_y]))

        plt.figure(figsize=(8, 6))
        plt.style.use('ggplot')
        plt.scatter(x_valores, y_valores, color='green', alpha=0.7)
        plt.title(f'Correlación: {col_y} vs {col_x}', fontweight='bold')
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.tight_layout()
        plt.savefig('outputs/grafico_5_dispersion.png', dpi=300)
        plt.close()
        imprimir_exito("Gráfico de dispersión generado en /outputs.")
    except ValueError:
        imprimir_error("Ambas columnas deben contener datos numéricos.")


def analizar_csv(ruta_archivo):
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    datos, columnas = leer_csv(ruta_archivo)
    if datos is None:
        return

    if not datos:
        imprimir_error("El archivo CSV está vacío.")
        return

    mostrar_vista_previa(datos, columnas)
    pausar()

    while True:
        imprimir_titulo("OPCIONES DE ANÁLISIS CSV")
        print("1. Calcular Estadísticas Descriptivas")
        print("2. Generar Gráfico 3 (Tendencia)")
        print("3. Generar Gráfico 4 (Pastel)")
        print("4. Generar Gráfico 5 (Dispersión)")
        print("5. Volver al menú principal")

        opcion = input("\nSelecciona una opción (1-5): ").strip()

        if opcion == "1":
            calcular_estadisticas(datos)
            pausar()
        elif opcion == "2":
            generar_grafico_tendencia(datos)
            pausar()
        elif opcion == "3":
            generar_grafico_pastel(datos)
            pausar()
        elif opcion == "4":
            generar_grafico_dispersion(datos)
            pausar()
        elif opcion == "5":
            break
        else:
            imprimir_error("Opción inválida.")
            pausar()