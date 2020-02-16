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
from App import controller as ct
from Sorting import mergesort as ms



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
    actor = {'name':'', 'movie_id':lt.newList("ARRAY_LIST"), "dir_name":lt.newList("ARRAY_LIST")}
    actor ['name'] = name
    lt.addLast(actor["movie_id"], movie_id)
    lt.addLast(actor["dir_name"], dir_name)
    return actor

def addActor (catalog, actor):

    """
    Adiciona un actor a la lista de actores
    """

    AddActor1( actor, "actor1_name", catalog)
    AddActor1( actor, "actor2_name", catalog)
    AddActor1( actor, "actor3_name", catalog)
    AddActor1( actor, "actor4_name", catalog)
    AddActor1( actor, "actor5_name", catalog)

def AddActor1(actor, actor_name, catalog):
    """
    Revisa si el recuadro es none, si ya estaba presente el actor en la lista actualiza
    su informacióm, en caso contrario crea el actor


    """
    if actor[actor_name].lower() !=  "none":
        
        if lt.isPresent(catalog["actors"], actor[actor_name], ct.comparepeople) != 0:
            UpdateActor(catalog, actor, actor[actor_name] )
        else: 
            a= newActor(actor[actor_name], actor['id'], actor["director_name"])
            lt.addLast (catalog['actors'], a)

 


def UpdateActor(catalog, actor, actor_name):
    """
    Actualiza info actor

    """
    #posicion= catalog["actors"]["elements"].get(actor_name) No funciona :(

    iterator=it.newIterator(catalog['actors'])
    while  it.hasNext(iterator):

        element = it.next(iterator)

        if actor_name in element["name"]:
            lt.addLast(element["movie_id"], actor["id"])
            lt.addLast(element["dir_name"], actor["director_name"])
            if it.hasNext(iterator):
                iterator['iterable_lst'] == []







    """
    print(catalog["actors"]["elements"][n]["name"])
    
    cada_actor= True
    while cada_actor:
        if actor_name in catalog["actors"]["elements"][n]["name"]:
            catalog["actors"]["elements"][n]["movie_id"]= lt.addLast(catalog["actors"]["elements"][n]["movie_id"], actor["id"])
            catalog["actors"]["elements"][n]["dir_name"]= lt.addLast(catalog["actors"]["elements"][n]["dir_name"], actor["director_name"])
            cada_actor== False 
        else: 
            n+=1

    """

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
def getBestMovies (catalog, number):
    movies = catalog['movies']
    bestmovies = lt.newList()
    for cont in range (1, number+1):
        movie = lt.getElement (movies, cont)
        lt.addLast (bestmovies, movie)
    return bestmovies

def getWorstMovies (catalog, number):
    movies = catalog['movies']
    worstmovies = lt.newList()
    size=lt.size(movies)
    for cont in range (size-number, size):
        movie = lt.getElement (movies, cont)
        lt.addLast (worstmovies, movie)
    return worstmovies

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

    print("El número de películas con votación positiva para el director seleccionado es: ",counter)

def getMoviesByDirector (catalog, dir_name):
    """
    Retorna las peliculas a partir del nombre del director
    """
    peliculas= lt.newList("ARRAY_LIST")
    directors = catalog['directors']
    movies= catalog['movies']
    suma=0
    contador=0

    for elemento in directors['elements']:
        if dir_name.lower() in elemento['name'].lower():
            contador+=1
            for elemento2 in movies['elements']:
                if elemento['movie_id']==elemento2['id'].lower():
                    lt.addLast(peliculas, elemento2)
                    suma+=float(elemento2['vote_average'])

    if contador!=0:
        promedio=round(suma/(contador),2)
    else:
        promedio=contador
    
    print('El número de películas del director es: ',contador,'y su promedio de votos es: ',promedio)

    return peliculas

def getMoviesByActor (catalog, act_name):
    """
    Esta función retorna el primer actor con el nombre indicado

    """
    iterator = it.newIterator(catalog['actors'])
    iterator = catalog['actors']
    iterator2 = catalog['movies']
    suma=0
    peliculas= lt.newList("ARRAY_LIST")
    director=""
    numdirector=-1
    posicion= lt.isPresent(iterator, act_name, ct.comparepeople)
    if posicion != 0:
        actor = lt.getElement(iterator, posicion)
        for pelicula in actor["movie_id"]["elements"]:
            for element in iterator2["elements"]:
                if element["id"]==pelicula: 
                    lt.addLast(peliculas, element)
                    suma+= float(element["vote_average"])
        for direc in actor["dir_name"]["elements"]:
            cont = actor["dir_name"]["elements"].count(direc)
            if numdirector < cont:
                numdirector = cont
                director = direc

        contador=lt.size(actor["movie_id"])
        promedio=round(suma/(contador),2)


        print('El número de películas del actor es: ',contador,',\nSu promedio de votos es: ',promedio,\
            "\nel director que más lo ha dirigido es: ", director )

    else: 
        print("El actor ingresado no se encuentra en la lista")

    return peliculas
    """
    for elemento in iterator['elements']:
        directores=0 
        director= ""
        if act_name.lower() in elemento['name'].lower():
            for elemento2 in iterator2['elements']:
                if elemento['movie_id']["elements"]==elemento2['id']:
                    suma+=float(elemento2['vote_average'])

            for elemento3 in iterator3['elements']:
                directorescontador=0
                if elemento['dir_name']==elemento3['name'].lower():
                    directorescontador+=1
            if directorescontador> directores:
                director== elemento["dir_name"]
                directores= directorescontador
    """
    """
    iterator = it.newIterator(catalog['actors'])
    ids=lt.newList()

    while  it.hasNext(iterator):

        element = it.next(iterator)

        if act_name.lower() in element['name'].lower() and act_name not in "   none       ":


            if lt.isPresent(ids, act_name, comparefunction)!=0 :
                ids["movie_id"]= lt.addLast(ids["movie_id"],element["movie_id"])
            else: 
                lt.addLast(ids,element['movie_id'])"
    
    return ids
    """

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
    print('El número de películas de este género es: ',contador, ' y el promedio de su votación es: ',promedio)
