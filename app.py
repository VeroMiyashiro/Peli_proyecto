from models import*
opcion = None
nombre_catalogo = input("¡Bienvenido! Ingresa el nombre del catálogo: ")
catalogo = CatalogoPelicula(nombre_catalogo)

while opcion != 4:
    print("\nOpciones:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")
    
    opcion = int(input("Escribe una opción de 1 al 4: "))
    
    if opcion == 1:
        nombre_pelicula = input("Ingrese el nombre de la película: ")
        pelicula = Pelicula(nombre_pelicula)
        catalogo.agregar_pelicula(pelicula)
    elif opcion == 2:
        catalogo.listar_peliculas()
    elif opcion == 3:
        catalogo.eliminar_peliculas()
    elif opcion == 4:
        print("Programa terminado.")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
