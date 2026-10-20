import os
from modules.utils import (
    limpiar_pantalla, imprimir_titulo, imprimir_error,
    imprimir_exito, pausar, AZUL, VERDE, RESET
)


def explorar_directorio():
    imprimir_titulo("EXPLORADOR DE DIRECTORIOS")
    ruta = input("Ingresa la ruta (Presiona ENTER para usar 'data/'): ").strip()

    if not ruta:
        ruta = "data/"

    try:
        archivos = os.listdir(ruta)
        archivos_texto = [f for f in archivos if f.endswith(('.txt', '.log'))]
        archivos_csv = [f for f in archivos if f.endswith('.csv')]

        print(f"\nArchivos de Texto (.txt / .log) en '{ruta}':")
        for archivo in archivos_texto:
            print(f"  - {VERDE}{archivo}{RESET}")

        print(f"\nArchivos CSV (.csv) en '{ruta}':")
        for archivo in archivos_csv:
            print(f"  - {AZUL}{archivo}{RESET}")

    except FileNotFoundError:
        imprimir_error(f"La ruta '{ruta}' no existe.")


def menu_principal():
    while True:
        limpiar_pantalla()
        imprimir_titulo("EXPLORADOR CLI PARA ANÁLISIS DE DATOS")

        print(f"{AZUL}1.{RESET} Explorar directorio")
        print(f"{AZUL}2.{RESET} Procesar Textos (.txt / .log)")
        print(f"{AZUL}3.{RESET} Analizar Dataset (.csv)")
        print(f"{AZUL}4.{RESET} Salir")

        opcion = input(f"\nSelecciona una opción (1-4): ").strip()

        if opcion == "1":
            limpiar_pantalla()
            explorar_directorio()
            pausar()

        elif opcion == "2":
            imprimir_titulo("PROCESAMIENTO DE TEXTO")
            print("(Esta opción se conectará en el Paso 4)")
            pausar()

        elif opcion == "3":
            imprimir_titulo("ANÁLISIS DE CSV")
            print("(Esta opción se conectará en el Paso 5)")
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            imprimir_exito("Saliendo del programa... ¡Hasta pronto!")
            break

        else:
            imprimir_error("Opción inválida. Ingresa un número del 1 al 4.")
            pausar()


if __name__ == "__main__":
    menu_principal()