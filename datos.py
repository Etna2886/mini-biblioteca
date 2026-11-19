def guardar_libros(biblioteca):
    """Guarda la lista de libros en un archivo de texto llamado libros.txt."""
    try:
        with open("libros.txt", "w", encoding="utf-8") as archivo:
            for libro in biblioteca:
                archivo.write(f"{libro.get('titulo')},{libro.get('autor')},{libro.get('anio')}\n")
    except Exception as e:
        print(f"Error al guardar los libros: {e}")
def guardar_libros(biblioteca):
    """Guarda la lista de libros en un archivo de texto llamado libros.txt."""
    try:
        with open("libros.txt", "w", encoding="utf-8") as archivo:
            for libro in biblioteca:
                archivo.write(f"{libro.get('titulo')},{libro.get('autor')},{libro.get('anio')}\n")
    except Exception as e:
        print(f"Error al guardar los libros: {e}")

def cargar_libros():
    """Lee libros.txt y devuelve la lista de libros. Si no existe, devuelve una lista vacía."""
    biblioteca = []
    try:
        with open("libros.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    libro = {
                        "titulo": partes[0],
                        "autor": partes[1],
                        "anio": partes[2]
                    }
                    biblioteca.append(libro)
    except FileNotFoundError:
        pass
    return biblioteca
