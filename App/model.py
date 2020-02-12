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
    actor = {'name':'', 'movie_id': lt.newList }
    actor  ['name'] = name
    actor  ['movie_id'] = movie_id
    return actor

def addActor (catalog, actor):
<<<<<<< HEAD

    #a= newActor(actor['name'], actor['id'])
    #lt.addLast (catalog['actors'], a)
=======
>>>>>>> 62ec3c29b37ab3a7f8706973dd69ee7d347175a6
    """
    Adiciona un actor a la lista de actores
    """
    a= newActor(actor['actor1_name'], actor['id'])
    lt.addLast (catalog['actors'], a)


def newDirector (name, movie_id):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'director_name':'', 'movie_id':''}
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

def getMoviesByDirector (catalog, dir_name):
    """
    Retorna las peliculas a partir del nombre del director
    """
<<<<<<< HEAD
    
=======

    """
>>>>>>> 62ec3c29b37ab3a7f8706973dd69ee7d347175a6
    iterator = it.newIterator(catalog['directors'])
    iterator3 = it.newIterator(catalog['movies'])
    ids=lt.newList()
    suma=0
    contador=0

    while  it.hasNext(iterator):
  
        element = it.next(iterator)

        if dir_name in element['name']:
            lt.addLast(ids,element['movie_id'])

<<<<<<< HEAD
    iterator2 = it.newIterator(ids)

    while it.hasNext(iterator2):
        
        element2= it.next(iterator2)      

        while it.hasNext(iterator3):   
        
            element3= it.next(iterator3)

            if element2==element3['id']:
=======
 
    #return lt.size(ids)a
    #iterator2 = it.newIterator(catalog['movies'])
    
    #while 
    #print(catalog['movies'])
    """
    pass
def getMoviesByActor(catalog, act_name):


    iterator = it.newIterator(catalog['actors'])
    ids=lt.newList()

    while  it.hasNext(iterator):

        element = it.next(iterator)

        if act_name in element['name']and act_name not in "   none       ":


            if lt.isPresent(ids, act_name, comparefunction)!=0 :
                ids["movie_id"]= lt.addLast(ids["movie_id"],element["movie_id"])
            else: 
                
                lt.addLast(ids,element['movie_id'])
    
    print(ids)
    return ids
>>>>>>> 62ec3c29b37ab3a7f8706973dd69ee7d347175a6

                suma+=float(element3['vote_average'])
                contador+=1
                print(contador)
    
    promedio=suma/lt.size(ids)
    
    print('El número de películas del director es: ',contador,'y su promedio de votos es: ',promedio)

    


