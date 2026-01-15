import json
import os
JSON_FILE = os.path.join(os.path.dirname(__file__), "inventario_carros.json")
# Inicializar inventario para evitar NameError cuando no existe el archivo
inventario_carros = []

def cargar_datos():
    """Carga los datos del archivo JSON al iniciar el programa."""
    global inventario_carros
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                inventario_carros = json.load(f)
            print(f"--- Datos cargados correctamente ({len(inventario_carros)} registros) ---")
        except (json.JSONDecodeError, IOError):
            print("Error al leer el archivo de persistencia. Iniciando con inventario vacío.")
            inventario_carros = []
    else:
        print("No se encontró archivo previo. Se creará uno nuevo al guardar.")

def guardar_datos():
    """Guarda la lista de carros actual en el archivo JSON."""
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(inventario_carros, f, indent=4, ensure_ascii=False)
        print(">>> Cambios guardados en el archivo JSON.")
    except IOError as e:
        print(f"Error al guardar los datos: {e}")