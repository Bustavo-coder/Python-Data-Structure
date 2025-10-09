import unittest
from idlelib.debugobj import myrepr

from src.Array import array
from src.Array.array import Array


class TestArray(unittest.TestCase):
    def setUp(self):
        self.array = Array(10)
    def test_that_i_can_change_element_at_any_position(self):
        self.array.set_element(0,"fish")
        self.assertEqual(self.array.get_element(0), "fish")


    def test_that_it_raises_value_error_when_i_tried_getting_an_element_greater_than_size(self):
        self.array.set_element(0,"fish")
        with self.assertRaises(IndexError):
            self.array.get_element(10)


    def test_that_i_cannot_set_elemnt_at_element_greter_than_size(self):
        with self.assertRaises(IndexError):
            self.array.set_element(10,"fish")

    def test_that_i_can_get_size_of_my_array(self):
        self.assertEqual(self.array.size(), 10)

    def test_that_i_can_create_a_2d_array(self):
        array = Array(2)
        array2 = Array(2)
        for num in range(array.size()):
            array.set_element(num,array2)
            for number in range(array2.size()):
                array2.set_element(number,"Ade")
            print(array.get_element(num).__str__())