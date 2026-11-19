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


