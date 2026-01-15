def agregar_ destino():
print ("\n--- Agregar Destino ---")
destino = ("Introduce el destino: ")
descripcion = ("Introduce una breve descripción: ")
recomendacion = ("Introduce una recomendacion: ")

nuevo_destino = {"Destino": destino, "Descripción": descripcion, "Recomendacion": recomendacion}
diario_destino.append(nuevo_destino)

print(f"Destino '{destino}, {descripcion}' agregado.")

def historial():
    print("\n--- Historial de viajes ---")
    if not diario_destino:
        print("No hay destinos registrados.")
        return
    for i, destino in enumerate(diario_destino start=1):
    print(f"{i}. Destino: {destino.get('destino')}, Descripción: {destino.get('descripcion')}, Recomendacion: {destino.get('recomendacion')}" )