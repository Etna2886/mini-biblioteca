def guardar_libros(biblioteca):
    """Guarda la lista de libros en un archivo de texto llamado libros.txt."""
    try:
        with open("libros.txt", "w", encoding="utf-8") as archivo:
            for libro in biblioteca:
                archivo.write(f"{libro.get('titulo')},{libro.get('autor')},{libro.get('anio')}\n")
    except Exception as e:
        print(f"Error al guardar los libros: {e}")
