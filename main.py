from libros import anadir_libro, listar_libros
# --- Aquí cada persona añade el import de su módulo ---
import busqueda

def mostrar_menu():
    print("\n=== MINI BIBLIOTECA ===")
    # --- Aquí cada persona añade su opción del menú ---
    print("1. Añadir libro")
    print("2. Listar libros")

    print("0. Salir")
    print("3. Buscar libor.")
def main():
    biblioteca = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        elif opcion == "1":
            anadir_libro(biblioteca)

        elif opcion == "2":
            listar_libros(biblioteca)
        # --- Aquí cada persona añade su elif ---
        elif opcion == "3":
            print(busqueda.buscarLibors(biblioteca))
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
 main()