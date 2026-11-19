def anadir_libro(biblioteca):
    titulo = input("Introduce el título: ")
    autor = input("Introduce el autor: ")
    anio = input("Introduce el año: ")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "anio": anio
    }

    biblioteca.append(libro)
    print("Libro añadido correctamente.")


def listar_libros(biblioteca):
    if len(biblioteca) == 0:
        print("No hay libros en la biblioteca.")
    else:
        print("\nListado de libros:")
        for i, libro in enumerate(biblioteca, start=1):
            print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['anio']})")