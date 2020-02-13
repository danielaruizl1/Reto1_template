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
    actor = {'name':'', 'movie_id':lt.newList, "dir_name":lt.newList}
    actor ['name'] = name
    actor ['movie_id'] = movie_id
    actor ["dir_name"] = dir_name
    return actor

def addActor (catalog, actor):

    """
    Adiciona un actor a la lista de actores
    """
    if actor["actor1_name"]!= "None": 

        a= newActor(actor['actor1_name'], actor['id'], actor["director_name"])
        lt.addLast (catalog['actors'], a)

def AddActor1(actor, actor_name, catalog):
    actores= catalog["actors"]
    if actor[actor_name].lower() not in  "   none    ":
        if it.isPresent(actores["elements"], actor_name, ct.compareratingpeople):
            UpdateeActor(catalog, )
        else: 
            a= newActor(actor[actor_name], actor['id'], actor["director_name"])
            lt.addLast (catalog['actors'], a)




def UpdateActor(catalog,  ):


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

    if contador!=0:
        promedio=round(suma/(contador),2)
    else:
        promedio=contador
    
    print('El número de películas del director es: ',contador,'y su promedio de votos es: ',promedio)

def getMoviesByActor (catalog, act_name):

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
    ids=lt.newList()

    while  it.hasNext(iterator):

        element = it.next(iterator)

        if act_name.lower() in element['name'].lower() and act_name not in "   none       ":


            if lt.isPresent(ids, act_name, comparefunction)!=0 :
                ids["movie_id"]= lt.addLast(ids["movie_id"],element["movie_id"])
            else: 
                
                lt.addLast(ids,element['movie_id'])
    
    return ids
    """

def getMoviesByGenres (catalog, genre_name):
    
    iterator = it.newIterator(catalog['movies'])
    suma=0
    contador=0

    while  it.hasNext(iterator):
  
        element = it.next(iterator)

        if genre_name.lower() in element['genres'].lower():
            contador+=1
            suma+=float(element['vote_average'])
    
    if contador!=0:
        promedio=round(suma/(contador),2)
    else:
        promedio=contador
    return print('El número de películas de este género es: ',contador, ' y el promedio de su votación es: ',promedio)
