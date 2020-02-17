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
from DataStructures import listiterator as it
from DataStructures import liststructure as lt


class insertionSortTest (unittest.TestCase):

    def setUp (self):
        self.movie1 = {'movie_id':'1', 'movie_title':'Title 1', 'author':'author 1'}
        self.movie2 = {'movie_id':'2', 'movie_title':'Title 2', 'author':'author 2'}
        self.movie3 = {'movie_id':'3', 'movie_title':'Title 3', 'author':'author 3'}
        self.movie4 = {'movie_id':'4', 'movie_title':'Title 4', 'author':'author 4'}
        self.movie5 = {'movie_id':'5', 'movie_title':'Title 5', 'author':'author 5'}
        self.movie6 = {'movie_id':'6', 'movie_title':'Title 6', 'author':'author 6'}

    def tearDown (self):
        pass


    def test_randomElements (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.alst = lt.newList('ARRAY_LIST')
        lt.addFirst (self.alst, self.movie3)
        lt.addFirst (self.alst, self.movie1)
        lt.addFirst (self.alst, self.movie2)
        print (self.alst)
        print('-----')
        self.slst = lt.newList()
        lt.addFirst (self.slst, self.movie5)
        lt.addFirst (self.slst, self.movie4)
        lt.addFirst (self.slst, self.movie6)

        print (self.slst)


if __name__ == "__main__":
    unittest.main()
