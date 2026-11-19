# --- Aquí cada persona añade el import de su módulo ---
def mostrar_menu():
    print("\n=== MINI BIBLIOTECA ===")
    # --- Aquí cada persona añade su opción del menú ---
    print("4. Guardar libros en archivo.")
    print("0. Salir")
def main():
    biblioteca = cargar_libros()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        # --- Aquí cada persona añade su elif ---
        elif opcion=="4":
            guardar_libros(biblioteca)
            print("Libros guardados correctamente.")
        else:
            print("Opción no válida")
if __name__ == "__main__":
    main()
