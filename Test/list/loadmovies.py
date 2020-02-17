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
from DataStructures import liststructure as lt
import csv

def loadCSVFile (file, lst):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        lt.addLast(lst,row)

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)


print ('Creating movies list')
lst_movies= lt.newList()

print ('Creating movies casting list')
lst_movies_casting=  lt.newList('ARRAY_LIST')

print ('Loading movies')
moviesfile = cf.data_dir + 'themoviesdb/SmallMoviesDetailsCleaned.csv'
loadCSVFile (moviesfile, lst_movies)
print (lst_movies['size'])
#printList (lst_movies)


print ('Loading movies casting')
moviescastingfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'
loadCSVFile (moviescastingfile, lst_movies_casting)
print (movies_casting['size'])
#printList (lst_tags)
