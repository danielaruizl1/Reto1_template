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


def newActor (name, movie_id, dir_name):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':'', 'movie_id':'', "dir_name": ""}
    actor ['name'] = name
    actor ['movie_id'] = movie_id
    actor ["dir_name"] = dir_name
    return actor

def addActor (catalog, actor):

    """
    Adiciona un actor a la lista de actores
    """
    a= newActor(actor['actor1_name'], actor['id'], actor["director_name"])
    lt.addLast (catalog['actors'], a)
    a= newActor(actor['actor1_name'], actor['id'], actor["director_name"])
    lt.addLast (catalog['actors'], a)
    a= newActor(actor['actor1_name'], actor['id'], actor["director_name"])
    lt.addLast (catalog['actors'], a)
    a= newActor(actor['actor1_name'], actor['id'], actor["director_name"])
    lt.addLast (catalog['actors'], a) 
    a= newActor(actor['actor1_name'], actor['id'], actor["director_name"])
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
    directors = catalog['directors']
    movies= catalog['movies']

    for elemento in directors['elements'] :
        if dir_name.lower() in elemento["name"].lower(): #filtrar por palabra clave 
            for elemento2 in movies['elements']:
                if elemento['movie_id']==elemento2['id'] and float(elemento2['vote_average'])>=6:
                    counter+=1

    return print("el número de películas con votación positiva para el director seleccionado es: ",counter)

def getMoviesByDirector (catalog, dir_name):
    """
    Retorna las peliculas a partir del nombre del director
    """
    
    directors = catalog['directors']
    movies= catalog['movies']
    suma=0
    contador=0

    for elemento in directors['elements']:
        if dir_name.lower() in elemento['name'].lower():
            contador+=1
            for elemento2 in movies['elements']:
                if elemento['movie_id']==elemento2['id'].lower():
                    suma+=float(elemento2['vote_average'])

    if contador!=0:
        promedio=round(suma/(contador),2)
    else:
        promedio=contador
    
    print('El número de películas del director es: ',contador,'y su promedio de votos es: ',promedio)

def getMoviesByActor (catalog, act_name):

<<<<<<< HEAD
    """iterator = it.newIterator(catalog['actors'])
=======
    iterator = catalog['actors']
    iterator2 = catalog['movies']
    iterator3= catalog["directors"]
    suma=0
    contador=0

    for elemento in iterator['elements']:
        directores=0 
        director= ""
        if act_name.lower() in elemento['name'].lower():

            contador+=1
            for elemento2 in iterator2['elements']:
                if elemento['movie_id']==elemento2['id'].lower():
                    suma+=float(elemento2['vote_average'])

            for elemento3 in iterator3['elements']:
                directorescontador=0
                if elemento['dir_name']==elemento3['name'].lower():
                    directorescontador+=1
            if directorescontador> directores:
                director== elemento["dir_name"]
                directores= directorescontador

    if contador!=0:
        promedio=round(suma/(contador),2)
    else:
        promedio=contador
    
    
    print('El número de películas del actor es: ',contador,', su promedio de votos es: ',promedio,\
    "y el director que más lo ha dirigido es: ", director )

    """
    iterator = it.newIterator(catalog['actors'])
>>>>>>> c193015b1054b2fdf885d8d814c3954c9caf5546
    ids=lt.newList()

    while  it.hasNext(iterator):

        element = it.next(iterator)

        if act_name.lower() in element['name'].lower() and act_name not in "   none       ":


            if lt.isPresent(ids, act_name, comparefunction)!=0 :
                ids["movie_id"]= lt.addLast(ids["movie_id"],element["movie_id"])
            else: 
                
                lt.addLast(ids,element['movie_id'])"""

    actores = catalog['actors']
    

    print(catalog['actors'])
    """contador=0

    for elemento in actores['elements']:
        if act_name.lower() in elemento['name'].lower():
            contador+=1
            for elemento2 in 
            suma+=float(elemento['vote_average'])"""
    
<<<<<<< HEAD
=======
    return ids
    """
>>>>>>> c193015b1054b2fdf885d8d814c3954c9caf5546

def getMoviesByGenres (catalog, genre_name):
    
    movies = catalog['movies']
    suma=0
    contador=0

    for elemento in movies['elements']:
        if genre_name.lower() in elemento['genres'].lower():
            contador+=1
            suma+=float(elemento['vote_average'])
    
    if contador!=0:
        promedio=round(suma/(contador),2)
    else:
        promedio=contador
    return print('El número de películas de este género es: ',contador, ' y el promedio de su votación es: ',promedio)
