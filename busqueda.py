def buscarLibors(biblioteca):
    busqueda = input("Introduce el nombre de un libro o un autor: ")
    libros = []
    for libro in biblioteca:
        for i in libro.values():
            if busqueda.lower() in i.lower():
                libros.append(libro)
    return libros
