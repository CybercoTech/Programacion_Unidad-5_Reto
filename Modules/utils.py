# modules/utils.py
import os

VERDE = '\033[92m'
AZUL = '\033[94m'
CIAN = '\033[96m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
RESET = '\033[0m' 

def limpiar_pantalla():
 
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    
    input(f"\n{AMARILLO}Presiona ENTER para continuar...{RESET}")

def imprimir_titulo(texto):
    
    ancho = 60 # Ancho de la línea
    print(f"{CIAN}" + "=" * ancho)
    print(f"{CIAN}{texto.center(ancho)}")
    print(f"{CIAN}" + "=" * ancho + f"{RESET}")

def imprimir_error(texto):
    
    print(f"{ROJO}[ERROR] {texto}{RESET}")

def imprimir_exito(texto):
    
    print(f"{VERDE}[ÉXITO] {texto}{RESET}")
