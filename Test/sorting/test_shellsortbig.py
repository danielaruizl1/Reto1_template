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


import unittest 
import config as cf
from Sorting import shellsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv


class shellSortTest (unittest.TestCase):
    list_type = 'ARRAY_LIST'
    #list_type = 'SINGLE_LINKED_LIST'
    
    lst_movies = lt.newList(list_type)
    moviesfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'

    def setUp (self):
        print ('Loading movies')
        self.loadCSVFile (self.moviesfile, self.lst_movies)
        print (self.lst_movies['size'])


    def tearDown (self):
        pass

    def loadCSVFile (self, file, lst):
        input_file = csv.DictReader(open(file))
        for row in input_file:  
            lt.addLast(lst,row)


    def printList (self, lst):
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            print (element ['id'])


    def less( self, element1, element2):
        if int(element1['id']) >  int(element2['id']):
            return True
        return False

    def greater( self, element1, element2):
        if int(element1['id']) >  int(element2['id']):
            return True
        return False


    def test_sort_mayor_a_menor (self):
        """
         Lista con elementos en orden aleatorio
        """
        print ("sorting ....")
        sort.shellSort (self.lst_movies, self.less)
        self.printList (self.lst_movies)

    def test_sort_menor_a_mayor (self):
        """
         Lista con elementos en orden aleatorio
        """
        print ("sorting ....")
        sort.shellSort (self.lst_movies, self.grater)
        self.printList (self.lst_movies)


if __name__ == "__main__":
    unittest.main()
