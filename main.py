import csv
import random
from typing import List
import asyncio
from functools import reduce

# -------------------------
# Componente POO
# -------------------------

class Pelicula:
    """Clase básica para representar una película"""
    def __init__(self, id: str, titulo: str, genero: str, año: int, calificacion: float):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.año = año
        self.calificacion = calificacion
    
    def __str__(self):
        return f"{self.titulo} ({self.año}) - {self.genero} - Calificación: {self.calificacion:.1f}"

class RecomendadorPeliculas:
    """Sistema principal de recomendación"""
    def __init__(self):
        self.peliculas: List[Pelicula] = []
    
    def cargar_peliculas(self, nombre_archivo: str):
        """Carga películas desde un archivo CSV"""
        try:
            with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    try:
                        self.peliculas.append(
                            Pelicula(
                                id=fila['id'],
                                titulo=fila['title'],
                                genero=fila['genre'],
                                año=int(fila['year']),
                                calificacion=float(fila['rating'])
                            )
                        )
                    except (ValueError, KeyError) as e:
                        print(f"Error procesando fila: {fila}. Error: {e}")
                        continue
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {nombre_archivo}")
            print("Usando datos de ejemplo...")
            self.crear_datos_ejemplo()
    
    def crear_datos_ejemplo(self):
        """Crea datos de ejemplo si no se encuentra el archivo"""
        datos_ejemplo = [
            ("1", "Sueños de libertad", "Drama", 1994, 9.3),
            ("2", "El padrino", "Crimen", 1972, 9.2),
            ("3", "El caballero de la noche", "Acción", 2008, 9.0),
            ("4", "Tiempos violentos", "Crimen", 1994, 8.9),
            ("5", "Forrest Gump", "Drama", 1994, 8.8),
            ("6", "Origen", "Ciencia ficción", 2010, 8.8),
            ("7", "Matrix", "Ciencia ficción", 1999, 8.7),
            ("8", "Buenos muchachos", "Crimen", 1990, 8.7),
            ("9", "El silencio de los inocentes", "Suspenso", 1991, 8.6),
            ("10", "Interestelar", "Ciencia ficción", 2014, 8.6)
        ]
        for pelicula in datos_ejemplo:
            self.peliculas.append(Pelicula(*pelicula))
    
    def obtener_peliculas_aleatorias(self, n: int = 5) -> List[Pelicula]:
        """Devuelve n películas aleatorias"""
        return random.sample(self.peliculas, min(n, len(self.peliculas)))

# -------------------------
# Componente Funcional
# -------------------------

def filtrar_por_genero(peliculas: List[Pelicula], genero: str) -> List[Pelicula]:
    """Filtra películas por género (función pura)"""
    return [pelicula for pelicula in peliculas if pelicula.genero.lower() == genero.lower()]

def ordenar_por_calificacion(peliculas: List[Pelicula]) -> List[Pelicula]:
    """Ordena películas por calificación (función pura)"""
    return sorted(peliculas, key=lambda x: x.calificacion, reverse=True)

def obtener_top_n(peliculas: List[Pelicula], n: int = 5) -> List[Pelicula]:
    """Obtiene las N mejores películas"""
    return peliculas[:n]

def calcular_promedio_calificacion(peliculas: List[Pelicula]) -> float:
    """Calcula la calificación promedio usando reduce"""
    calificaciones = [pelicula.calificacion for pelicula in peliculas]
    return reduce(lambda a, b: a + b, calificaciones) / len(calificaciones) if calificaciones else 0

# -------------------------
# Componente Reactivo/Concurrente
# -------------------------

async def recomendar_por_genero(genero: str, peliculas: List[Pelicula]):
    """Recomendación asíncrona por género"""
    print(f"\nBuscando recomendaciones de {genero}...")
    await asyncio.sleep(1)
    
    filtradas = filtrar_por_genero(peliculas, genero)
    if not filtradas:
        print(f"\nNo se encontraron películas del género {genero}")
        return
    
    ordenadas = ordenar_por_calificacion(filtradas)
    mejores_peliculas = obtener_top_n(ordenadas, 3)
    
    print(f"\nTop 3 películas de {genero}:")
    for i, pelicula in enumerate(mejores_peliculas, 1):
        print(f"{i}. {pelicula}")

async def mostrar_recomendaciones_aleatorias(peliculas: List[Pelicula]):
    """Recomendaciones aleatorias async"""
    print("\nGenerando recomendaciones aleatorias...")
    await asyncio.sleep(0.5)
    
    aleatorias = random.sample(peliculas, min(3, len(peliculas)))
    print("\nPelículas aleatorias que podrías disfrutar:")
    for i, pelicula in enumerate(aleatorias, 1):
        print(f"{i}. {pelicula}")

# -------------------------
# Programa Principal
# -------------------------

async def main_async():
    recomendador = RecomendadorPeliculas()
    recomendador.cargar_peliculas('data/peliculas.csv')

    # Análisis funcional
    generos = {pelicula.genero for pelicula in recomendador.peliculas}
    print(f"\nGéneros disponibles: {', '.join(sorted(generos))}")
    
    promedio_calificacion = calcular_promedio_calificacion(recomendador.peliculas)
    print(f"\nCalificación promedio de todas las películas: {promedio_calificacion:.1f}")
    
    while True:
        genero_usuario = input("\n¿Que genero te interesa? (o 'salir' para terminar) ").strip()
        if genero_usuario.lower() == 'salir':
            break
        
        if genero_usuario not in generos:
            print(f"\nGenero no válido. Los generos disponibles son: {', '.join(sorted(generos))}")
            continue
        
        # Ejecutar las corrutinas
        await asyncio.gather(
            recomendar_por_genero(genero_usuario, recomendador.peliculas),
            mostrar_recomendaciones_aleatorias(recomendador.peliculas)
        )

def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()