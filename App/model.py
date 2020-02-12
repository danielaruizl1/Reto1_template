"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'movies':None, 'directors':None, 'actors': None}
    catalog['movies'] = lt.newList('ARRAY_LIST')
    catalog['directors'] = lt.newList('ARRAY_LIST')
    catalog['actors'] = lt.newList('ARRAY_LIST')
    return catalog


def newActor (name, movie_id):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':'', 'movie_id':''}
    actor ['name'] = name
    actor ['movie_id'] = movie_id
    return actor

def addActor (catalog, actor):

    """
    Adiciona un actor a la lista de actores
    """
    a= newActor(actor['actor1_name'], actor['id'])
    a= newActor(actor['actor2_name'], actor['id'])
    a= newActor(actor['actor3_name'], actor['id'])
    a= newActor(actor['actor4_name'], actor['id'])
    a= newActor(actor['actor5_name'], actor['id'])
    lt.addLast (catalog['actors'], a)


def newDirector (name, movie_id):
    """
    Esta estructura almacena los directores de una pelicula.
    """
    director = {'name':'', 'movie_id':''}
    director ['name'] = name
    director ['movie_id'] = movie_id
    return director


def addDirector (catalog, director):
    """
    Adiciona un director a la lista de directores
    """
    d = newDirector (director['director_name'], director['id'])
    lt.addLast (catalog['directors'], d)

# Funciones de consulta
def getMoviesPositiveVotacionDirector (catalog, dir_name):
    """
    Retorna las películas con votación postiva (>= 6) de un determinado director"
    """
    counter=0
    iterator = catalog['directors']
    iterator2 = catalog['movies']

    for elemento in iterator['elements'] :
        if dir_name.lower() in elemento["name"].lower(): #filtrar por palabra clave 
            for elemento2 in iterator2['elements']:
                if elemento['movie_id']==elemento2['id'] and float(elemento2['vote_average'])>=6:
                    counter+=1

    return print("el número de películas con votación positiva para el director seleccionado es: ",counter)

def getMoviesByDirector (catalog, dir_name):
    """
    Retorna las peliculas a partir del nombre del director
    """
    
    iterator = catalog['directors']
    iterator2 = catalog['movies']
    suma=0
    contador=0

    for elemento in iterator['elements']:
        if dir_name.lower() in elemento['name'].lower():
            contador+=1
            for elemento2 in iterator2['elements']:
                if elemento['movie_id']==elemento2['id'].lower():
                    suma+=float(elemento2['vote_average'])

    promedio=suma/contador
    
    print('El número de películas del director es: ',contador,'y su promedio de votos es: ',promedio)

def getMoviesByActor (catalog, act_name):

    iterator = it.newIterator(catalog['actors'])
    ids=lt.newList()

    while  it.hasNext(iterator):

        element = it.next(iterator)

        if act_name.lower() in element['name'].lower() and act_name not in "   none       ":


            if lt.isPresent(ids, act_name, comparefunction)!=0 :
                ids["movie_id"]= lt.addLast(ids["movie_id"],element["movie_id"])
            else: 
                
                lt.addLast(ids,element['movie_id'])
    
    return ids

def getMoviesByGenres (catalog, genre_name):
    
    iterator = it.newIterator(catalog['movies'])
    suma=0
    contador=0

    while  it.hasNext(iterator):
  
        element = it.next(iterator)

        if genre_name.lower() in element['genres'].lower():
            contador+=1
            suma+=float(element['vote_average'])
    
    promedio=round((suma/contador),2)

    return print('El número de películas de este género es: ',contador, ' y el promedio de su votación es: ',promedio)


