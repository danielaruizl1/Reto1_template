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
import config 
from Sorting import shellsort as sort
from DataStructures import listiterator as it
from ADT import list as slt


class shellSortTest (unittest.TestCase):

    list_type = 'ARRAY_LIST'
    #list_type = 'SINGLE_LINKED_LIST'

    def setUp (self):
        self.movie1 = {'movie_id':'1', 'movie_title':'Title 1', 'author':'author 1'}
        self.movie2 = {'movie_id':'2', 'movie_title':'Title 2', 'author':'author 2'}
        self.movie3 = {'movie_id':'3', 'movie_title':'Title 3', 'author':'author 3'}
        self.movie4 = {'movie_id':'4', 'movie_title':'Title 4', 'author':'author 4'}
        self.movie5 = {'movie_id':'5', 'movie_title':'Title 5', 'author':'author 5'}
        self.movie6 = {'movie_id':'6', 'movie_title':'Title 6', 'author':'author 6'}

    def tearDown (self):
        pass

    def less( self, element1, element2):
        if int(element1['movie_id']) <  int(element2['movie_id']):
            return True
        return False

    def greater( self, element1, element2):
        if int(element1['movie_id']) > int(element2['movie_id']):
            return True
        return False

    def test_randomElements (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie1)
        slt.addFirst (self.lst, self.movie2)

     
        print ("Random list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_randomElements_greater (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie1)
        slt.addFirst (self.lst, self.movie2)

     
        print ("Random list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.greater)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)


    def test_invertedElements (self):
        """
        Lista ordenada inversamente
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie1)
        slt.addFirst (self.lst, self.movie2)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie6)

        print ("Inverted list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_invertedElements_greater (self):
        """
        Lista ordenada inversamente
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie1)
        slt.addFirst (self.lst, self.movie2)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie6)

        print ("Inverted list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.greater)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_orderedElements (self):
        """
        Lista ordenada
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie2)
        slt.addFirst (self.lst, self.movie1)

        print ("ordered list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_orderedElements_greater (self):
        """
        Lista ordenada
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie2)
        slt.addFirst (self.lst, self.movie1)

        print ("ordered list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.greater)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_oneElement (self):
        """
        Un elemento
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie1)

        print ("one element:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_oneElement_greater (self):
        """
        Un elemento
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie1)

        print ("one element:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.greater)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_repeatedElements (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie1)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie2)
        slt.addFirst (self.lst, self.movie4)


        print ("Repeated elements:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)

    def test_repeatedElements_greater (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.movie5)
        slt.addFirst (self.lst, self.movie4)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie3)
        slt.addFirst (self.lst, self.movie1)
        slt.addFirst (self.lst, self.movie6)
        slt.addFirst (self.lst, self.movie2)
        slt.addFirst (self.lst, self.movie4)


        print ("Repeated elements:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.shellSort (self.lst, self.greater)
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)





if __name__ == "__main__":
    unittest.main()
