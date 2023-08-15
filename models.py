 import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre

class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.__nombre = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"
        self.__peliculas = []

        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    pelicula = Pelicula(linea.strip())
                    self.__peliculas.append(pelicula)

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula}\n')

        self.__peliculas.append(pelicula)
        print("Película agregada.")

    def listar_peliculas(self):
        if self.__peliculas:
            print("\nPelículas en el catálogo:")
            for pelicula in self.__peliculas:
                print(pelicula)
        else:
            print("No hay películas en el catálogo.")

    def eliminar_peliculas(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            self.__peliculas = []
            print(f"El archivo se ha eliminado: {self.ruta_archivo}")
        else:
            print("El archivo no existe.")
