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
import csv
from ADT import queue as q
from  DataStructures import listiterator as it


def loadCSVFile (file, queue):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        q.enqueue(queue,row)

def printQueue (queue):
    iterator = it.newIterator(queue)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        print (element)
print ('Creating movies queue')
lst_movies= q.newQueue()

print ('Creating movies casting queue')
lst_movie_casting= q.newQueue()


print ('Loading movies')
moviesfile = cf.data_dir + 'themoviesdb/SmallMoviesDetailsCleaned.csv'
loadCSVFile (moviesfile, lst_movies)
print (lst_movies['size'])
printQueue (lst_movies)


print ('Loading tags')
moviecastingfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'
loadCSVFile (moviecastingfile, lst_tags)
print (lst_movie_casting['size'])
printQueue (lst_movie_casting)
