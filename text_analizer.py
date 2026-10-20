# modules/text_analyzer.py
import string
import os
from collections import Counter
import matplotlib.pyplot as plt
from modules.utils import imprimir_titulo, imprimir_error, imprimir_exito, VERDE, AZUL, AMARILLO, RESET

def analizar_texto(ruta_archivo):


    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    try:

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
        if not lineas:
            imprimir_error("El archivo está vacío. No hay nada que analizar.")
            return

        imprimir_titulo("RESUMEN ESTADÍSTICO DEL TEXTO")
        

        total_lineas = len(lineas)
        texto_completo = "".join(lineas)
        total_caracteres = len(texto_completo)

        total_caracteres_sin_espacios = len(texto_completo.replace(" ", "").replace("\n", ""))
        
     
        texto_limpio = texto_completo.lower().translate(str.maketrans('', '', string.punctuation))
        palabras = texto_limpio.split()
        total_palabras = len(palabras)
        
        print(f"Total de líneas: {AZUL}{total_lineas}{RESET}")
        print(f"Total de palabras: {AZUL}{total_palabras}{RESET}")
        print(f"Total de caracteres (con espacios): {AZUL}{total_caracteres}{RESET}")
        print(f"Total de caracteres (sin espacios): {AZUL}{total_caracteres_sin_espacios}{RESET}")
        
 
        conectores = {'el', 'la', 'los', 'las', 'un', 'una', 'de', 'del', 'y', 'o', 'en', 'a', 'por', 'para', 'con', 'que', 'es', 'al', 'se', 'su', 'lo'}
        
        palabras_filtradas = [p for p in palabras if p not in conectores and p != '']
        
        
        contador_palabras = Counter(palabras_filtradas)
        top_10 = contador_palabras.most_common(10)
        
        print(f"\n{AMARILLO}Top 5 palabras más repetidas:{RESET}")
        for i, (palabra, frecuencia) in enumerate(top_10[:5], 1):
            print(f"{i}. {palabra}: {frecuencia} veces")

        
        errores_404 = texto_completo.count("404")
        errores_generales = texto_completo.count("ERROR")
        
        print(f"\n{AMARILLO}Extracción de Patrones (Logs):{RESET}")
        print(f"Apariciones de 'ERROR': {errores_generales}")
        print(f"Apariciones de '404': {errores_404}")

        palabras_grafico = [item[0] for item in top_10]
        frecuencias_grafico = [item[1] for item in top_10]

        plt.figure(figsize=(10, 6)) 
        plt.style.use('ggplot')       
        plt.barh(palabras_grafico[::-1], frecuencias_grafico[::-1], color='skyblue') 
        plt.title('Top 10 Palabras más Frecuentes', fontsize=14, fontweight='bold')
        plt.xlabel('Frecuencia')
        plt.ylabel('Palabras')
        plt.tight_layout() 
        plt.savefig('outputs/grafico_1_palabras.png', dpi=300)
        plt.close() 
        longitudes = [len(linea) for linea in lineas]
        
        plt.figure(figsize=(8, 5))
        plt.style.use('ggplot')

        max_long = max(longitudes) if longitudes else 100
        bins = range(0, max_long + 50, 50) 
        
        plt.hist(longitudes, bins=bins, color='coral', edgecolor='black')
        plt.title('Distribución de Longitud de Líneas', fontsize=14, fontweight='bold')
        plt.xlabel('Cantidad de caracteres por línea')
        plt.ylabel('Cantidad de líneas')
        plt.tight_layout()
        plt.savefig('outputs/grafico_2_longitud_lineas.png', dpi=300)
        plt.close()

        imprimir_exito("¡Análisis completado! Revisa la carpeta /outputs para ver los gráficos.")

    except FileNotFoundError:
        imprimir_error(f"No se encontró el archivo en la ruta: {ruta_archivo}")
    except Exception as e:
        imprimir_error(f"Ocurrió un error inesperado al procesar el texto: {e}")