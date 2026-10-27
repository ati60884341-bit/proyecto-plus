# appplus.py - Version Base v1.0 (Alejandro Rioja en VS Code)
tareas = []
def mostrar_menu():
    print("\n--- GESTOR DE TAREAS PROYECTO PLUS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")
    
def agregar_tarea():
    titulo = input("Ingrese la descripción de la tarea: ").strip()
    if not titulo:
        print("¡La descripción no puede estar vacía!")
        return

    prioridad = input("Prioridad (Alta/Media/Baja) [Media]: ").strip().capitalize()
    if prioridad not in ["Alta", "Media", "Baja"]:
        prioridad = "Media"

    tareas.append({
        "titulo": titulo,
        "prioridad": prioridad,
        "completada": False
    })
    print(f"✓ Tarea '{titulo}' agregada con prioridad {prioridad}.")
 
def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n--- LISTA DE TAREAS ---")
    for idx, t in enumerate(tareas, 1):
        print(f"{idx}. [ ] {t['titulo']} (Prioridad: {t['prioridad']})")
        

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
