from CatalogoDePeliculas.dominio.Pelicula import Pelicula
from servicios.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar catalogo')
        print('4. Salir:')
        opcion = int(input('Escribe tu opcion (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        if opcion ==2:
            cp.listar_peliculas()
        if opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Saliendo del programa')
