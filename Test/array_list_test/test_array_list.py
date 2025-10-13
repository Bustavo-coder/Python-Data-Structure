import unittest
from src.ArrayList.array_list import ArrayList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.array_list = ArrayList()

    def test_that_list_is_empty(self):
            self.assertTrue(self.array_list.is_empty())

    def test_that_when_to_my_list_it_is_not_empty(self):
        self.array_list.append("yam")
        self.assertFalse(self.array_list.is_empty())


    def test_that_when_i_add_more_elements_to_my_list_the_size_increase(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.assertEqual(self.array_list.size(),2)

    def test_that_when_i_clear_all_elements_my_size_reduce_and_my_array_is_empty(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.array_list.clear()
        self.assertEqual(self.array_list.size(),0)
        self.assertTrue(self.array_list.is_empty())

    def test_that_when_i_remove_from_my_list_it_return_the_elements_removed(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.assertEqual(self.array_list.pop(),"Fish")

    def test_that_when_i_remove_mutiple_elements_in_my_list_it_return_last_element(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.assertEqual(self.array_list.pop(),"Fish")
        self.assertEqual(self.array_list.pop(),"yam")

    def test_that_when_my_array_is_empty_it_raise_error_if_i_Want_to_pop(self):
       with self.assertRaises(IndexError):
           self.array_list.pop()

    def test_that_when_i_add_elements_my_list_contains_element(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.assertTrue(self.array_list.contains("Fish"))

    def test_that_when_i_search_for_element_not_in_my_list(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.assertFalse(self.array_list.contains("cow"))

    def test_that_i_can_keep_adding_to_my_list(self):
        my_list = ArrayList(2)
        my_list.append("yam")
        my_list.append("Fish")
        my_list.append("yam")
        my_list.append("cow")

    def test_that_when_i_add_element_i_can_get_index_of_first_occurance(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.array_list.append("Goat")
        self.array_list.append("yam")
        self.assertEqual(self.array_list.index("yam"),0)

    def test_that_when_i_search_for_element_not_in_my_list(self):
        self.array_list.append("yam")
        self.assertEqual(self.array_list.index("fish"),-1)

    def test_that_when_i_add_element_i_can_get_index_of_(self):
        self.array_list.append("Fish")
        self.array_list.append("Goat")
        self.array_list.append("yam")
        self.assertEqual(self.array_list.index("yam"),2)

    def test_that_when_i_remove_the_first_occurence(self):
        self.array_list.append("yam")
        self.array_list.append("fish")
        self.array_list.append("Cow")
        self.array_list.append("hen")
        self.array_list.remove("yam")
        self.assertFalse(self.array_list.contains("yam"))

    def test_that_when_i_want_to_remove_a_wrong_element(self):
        self.array_list.append("yam")
        self.array_list.append("fish")
        self.array_list.append("Cow")
        self.array_list.append("hen")
        self.array_list.remove("yam")
        with self.assertRaises(ValueError):
            self.array_list.remove("2")

    def test_that_when_i_insert_element_in_my_list(self):
        self.array_list.append("yam")
        self.array_list.append("Fish")
        self.array_list.append("cow")
        self.array_list.append("hen")
        self.array_list.insert(2,"cat")
        self.assertTrue(self.array_list.contains("cat"))

    def test_when_index_is_higher_than_array_list(self):
        with self.assertRaises(IndexError):
            self.array_list.insert(0,"yame")




