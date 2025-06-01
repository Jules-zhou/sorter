import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from src import Sorter

class TestSorter(unittest.TestCase):
    def setUp(self):
        self.sorter = Sorter()

    def test_bubblesort_new_true(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = self.sorter.bubblesort(arr, new=True)
        self.assertEqual(sorted_arr, sorted(arr))
        self.assertNotEqual(arr, sorted_arr)

    def test_bubblesort_new_false(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        original_arr = arr[:]
        self.sorter.bubblesort(arr, new=False)
        self.assertEqual(arr, sorted(original_arr))
        
    def test_selectsort_new_true(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = self.sorter.selectsort(arr, new=True)
        self.assertEqual(sorted_arr, sorted(arr))
        self.assertNotEqual(arr, sorted_arr)

    def test_selectsort_new_false(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        original_arr = arr[:]
        self.sorter.selectsort(arr, new=False)
        self.assertEqual(arr, sorted(original_arr))

    def test_insertsort_new_true(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = self.sorter.insertsort(arr, new=True)
        self.assertEqual(sorted_arr, sorted(arr))
        self.assertNotEqual(arr, sorted_arr)

    def test_insertsort_new_false(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        original_arr = arr[:]
        self.sorter.insertsort(arr, new=False)
        self.assertEqual(arr, sorted(original_arr))

    def test_quicksort_new_true(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = self.sorter.quicksort(arr, new=True)
        self.assertEqual(sorted_arr, sorted(arr))
        self.assertNotEqual(arr, sorted_arr)

    def test_quicksort_new_false(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        original_arr = arr[:]
        self.sorter.quicksort(arr, new=False)
        self.assertEqual(arr, sorted(original_arr))

if __name__ == '__main__':
    unittest.main()
