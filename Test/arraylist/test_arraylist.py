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
from DataStructures import liststructure as slt

class ListTest (unittest.TestCase):

    def setUp (self):
        self.movie1 = {'movie_id':'1', 'movie_title':'Title 1', 'author':'author 1'}
        self.movie2 = {'movie_id':'2', 'movie_title':'Title 2', 'author':'author 2'}
        self.movie3 = {'movie_id':'3', 'movie_title':'Title 3', 'author':'author 3'}
        self.movie4 = {'movie_id':'4', 'movie_title':'Title 4', 'author':'author 4'}
        self.movie5 = {'movie_id':'5', 'movie_title':'Title 5', 'author':'author 5'}
        self.movie6 = {'movie_id':'6', 'movie_title':'Title 6', 'author':'author 6'}

    def tearDown (self):
        pass


    def test_empty (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)

    def test_addFirst (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addFirst (self.lst, self.movie1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addFirst (self.lst, self.movie2)
        self.assertEqual (slt.size(self.lst), 2)
        movie = slt.firstElement(self.lst)
        self.assertDictEqual (movie, self.movie2)


    def test_addLast (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.movie1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.movie2)
        self.assertEqual (slt.size(self.lst), 2)
        movie = slt.firstElement(self.lst)
        self.assertDictEqual (movie, self.movie1)
        movie = slt.lastElement(self.lst)
        self.assertDictEqual (movie, self.movie2)


    def test_getElement (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.movie1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.movie2)
        self.assertEqual (slt.size(self.lst), 2)
        movie = slt.getElement(self.lst, 1)
        self.assertDictEqual (movie, self.movie1)
        movie = slt.getElement(self.lst, 2)
        self.assertDictEqual (movie, self.movie2)

    def test_removeFirst (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.movie1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.movie2)
        self.assertEqual (slt.size(self.lst), 2)
        slt.removeFirst(self.lst)
        movie = slt.getElement(self.lst, 1)
        self.assertEqual (slt.isEmpty(self.lst), False)
        self.assertEqual (slt.size(self.lst), 1)
        self.assertDictEqual (movie, self.movie2)

    def test_removeLast (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.addLast (self.lst, self.movie1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.addLast (self.lst, self.movie2)
        self.assertEqual (slt.size(self.lst), 2)
        slt.removeLast(self.lst)
        movie = slt.getElement(self.lst, 1)
        self.assertEqual (slt.isEmpty(self.lst), False)
        self.assertEqual (slt.size(self.lst), 1)
        self.assertDictEqual (movie, self.movie1)

    def test_insertElement (self):
        self.lst = slt.newList('ARRAY_LIST')
        self.assertEqual (slt.isEmpty(self.lst), True)
        self.assertEqual (slt.size(self.lst), 0)
        slt.insertElement (self.lst, self.movie1, 1)
        self.assertEqual (slt.size(self.lst), 1)
        slt.insertElement (self.lst, self.movie2, 1)
        self.assertEqual (slt.size(self.lst), 2)
        movie = slt.getElement(self.lst, 1)
        self.assertDictEqual (movie, self.movie2)
        movie = slt.getElement(self.lst, 2)
        self.assertDictEqual (movie, self.movie1)



if __name__ == "__main__":
    unittest.main()