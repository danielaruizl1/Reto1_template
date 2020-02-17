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
from ADT import stack as st


class stackTest (unittest.TestCase):

    list_type = 'ARRAY_LIST'
    #list_type = 'SINGLE_LINKED_LIST'

    def setUp (self):
        self.movie1 = {'movie_id':'1', 'movie_title':'Title 1', 'author':'author 1'}
        self.movie2 = {'movie_id':'2', 'movie_title':'Title 2', 'author':'author 2'}
        self.movie3 = {'movie_id':'3', 'movie_title':'Title 3', 'author':'author 3'}
        self.movie4 = {'movie_id':'4', 'movie_title':'Title 4', 'author':'author 4'}
        self.movie5 = {'movie_id':'5', 'movie_title':'Title 5', 'author':'author 5'}
        self.movie6 = {'movie_id':'6', 'movie_title':'Title 6', 'author':'author 6'}
        self.movie7 = {'movie_id':'7', 'movie_title':'Title 7', 'author':'author 7'}
        self.movie8 = {'movie_id':'8', 'movie_title':'Title 8', 'author':'author 8'}
        self.movie9 = {'movie_id':'9', 'movie_title':'Title 9', 'author':'author 9'}
        self.movie10 = {'movie_id':'10', 'movie_title':'Title 10', 'author':'author 10'}

    def tearDown (self):
        pass

    def less( self, element1, element2):
        if int(element1['book_id']) <  int(element2['book_id']):
            return True
        return False

    def test_pushElements (self):
        """
        """
        self.stack = st.newStack(self.list_type)

        st.push   (self.stack, self.movie5)
        st.push   (self.stack, self.movie6)
        st.push   (self.stack, self.movie3)
        st.push   (self.stack, self.movie10)
        st.push   (self.stack, self.movie1)
        st.push   (self.stack, self.movie2)
        st.push   (self.stack, self.movie8)
        st.push   (self.stack, self.movie4)
        st.push   (self.stack, self.movie7)
        st.push   (self.stack, self.movie9)

        iterator = it.newIterator(self.stack)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)


    def test_sizeStack (self):
        """
        """
        self.stack = st.newStack(self.list_type)
        self.assertEqual (st.size(self.stack), 0)
        self.assertTrue (st.isEmpty(self.stack))
        st.push   (self.stack, self.movie5)
        st.push   (self.stack, self.movie6)
        st.push   (self.stack, self.movie3)
        st.push   (self.stack, self.movie10)
        st.push   (self.stack, self.movie1)
        st.push   (self.stack, self.movie2)
        st.push   (self.stack, self.movie8)
        st.push   (self.stack, self.movie4)
        st.push   (self.stack, self.movie7)
        st.push   (self.stack, self.movie9)
        self.assertEqual (st.size(self.stack), 10)


    def test_infoElements (self):
        """
        """
        self.stack = st.newStack(self.list_type)
        self.assertEqual (st.size(self.stack), 0)
        self.assertTrue (st.isEmpty(self.stack))
        st.push   (self.stack, self.movie5)
        st.push   (self.stack, self.movie6)
        st.push   (self.stack, self.movie3)
        st.push   (self.stack, self.movie10)
        st.push   (self.stack, self.movie1)
        st.push   (self.stack, self.movie2)
        st.push   (self.stack, self.movie8)
        st.push   (self.stack, self.movie4)
        st.push   (self.stack, self.movie7)
        st.push   (self.stack, self.movie9)
        
        elem = st.top (self.stack)
        self.assertEqual (st.size(self.stack), 10)
        self.assertDictEqual (elem, self.movie9)
        
        elem = st.pop (self.stack)
        self.assertEqual (st.size(self.stack), 9)
        self.assertDictEqual (elem, self.movie9)

        elem = st.pop (self.stack)
        self.assertEqual (st.size(self.stack), 8)
        self.assertDictEqual (elem, self.movie7)

        elem = st.top (self.stack)
        self.assertEqual (st.size(self.stack), 8)
        self.assertDictEqual (elem, self.movie4)

        st.push  (self.stack, self.movie9)
        self.assertEqual (st.size(self.stack), 9)
        elem = st.top (self.stack)
        self.assertDictEqual (elem, self.movie9)

if __name__ == "__main__":
    unittest.main()
