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
import model 
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)



def compareratings (movie1, movie2):
    return ( float(movie1['vote_average']) > float(movie2['vote_average']))
    
def compareratingpeople(actor1, actor2):
    return (actor1["name"]) == (actor2['name']))



# Funciones para la carga de datos 

def loadMovies (catalog):
    """
    Carga las peliculas del archivo.  Por cada libro se cargan sus directores
    
    """
    t1_start = process_time() #tiempo inicial
    moviesfile = cf.data_dir + 'themoviesdb/SmallMoviesDetailsCleaned.csv'
    
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(moviesfile, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lt.addLast (catalog['movies'], row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga peliculas",t1_stop-t1_start," segundos")



def loadDirectors(catalog):
    """
    Carga todos los directores
    """
    t1_start = process_time() #tiempo inicial
    castingfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'
    
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(castingfile, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            model.addDirector (catalog, row)
    t1_stop = process_time() #tiempo inicial
    print("Tiempo de ejecución carga directores",t1_stop-t1_start," segundos")


def loadActors(catalog):
    """
    Carga todos los actores
    """
    t1_start = process_time() #tiempo inicial
    castingfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'
    
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(castingfile, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            model.addActor (catalog, row)
    t1_stop = process_time() #tiempo inicial
    print("Tiempo de ejecución carga directores",t1_stop-t1_start," segundos")


def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



def loadData (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadMovies(catalog)
    sort.sort(catalog['movies'], compareratings)
    loadDirectors(catalog)
    loadActors(catalog)
    

# Funciones llamadas desde la vista y enviadas al modelo
def getMoviesPositiveVotacionDirector (catalog, dir_name):
    return model.getMoviesPositiveVotacionDirector(catalog, dir_name)

def getBestMovies (catalog, number):
    return model.getBestMovies(catalog, number)

def getWorstMovies (catalog, number):
    return model.getWorstMovies(catalog, number)

def getMoviesByDirector (catalog, dir_name):
    return model.getMoviesByDirector(catalog, dir_name)

def getMoviesByActor(catalog, act_name):
    return model.getMoviesByActor(catalog, act_name)

def getMoviesByGenres (catalog, genre_name):
    return model.getMoviesByGenres(catalog, genre_name)


