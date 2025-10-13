import unittest
from src.Set.myset import Set

class TestSetMethods(unittest.TestCase):
    def setUp(self):
        self.mySet = Set()
    def test_that_i_cannot_add_duplicate_values(self):
        self.mySet.add(2)
        with self.assertRaises(ValueError):
            self.mySet.add(2)

    def test_that_i_can_more_element_to_my_set(self):
        self.mySet.add(2)
        self.mySet.add(20)
        self.assertTrue(self.mySet.contains(20))