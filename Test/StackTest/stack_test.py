import unittest
from inspect import stack

from src.Stack.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.mystack = Stack()
    def test_that_stack_is_empty(self):
        self.assertTrue(self.mystack.is_empty())

    def test_that_when_i_add_element_to_my_stack_it_does_not_remain_empty(self):
        self.mystack.push("name")
        self.assertFalse(self.mystack.is_empty())

    def test_that_when_i_add_element_to_my_stack_when_i_pop_i_get_the_last_element(self ):
        self.mystack.push("name")
        self.mystack.push(1)
        self.assertEqual(self.mystack.pop(),1)

    def test_that_when_my_stack_is_empty_and_i_remove_it_raise_error(self):
        with self.assertRaises(IndexError):
            self.mystack.pop()

    def test_that_when_i_add_two_elements_and_i_pop_twice_it_return_the_element_on_the_stack(self):
        self.mystack.push("name")
        self.mystack.push("banana")
        self.assertEqual(self.mystack.pop(),"banana")
        self.assertEqual(self.mystack.pop(),"name")

    def test_that_if_stack_if_full_i_cannot_add(self):
        self.mystack.push("name")
        self.mystack.push("banana")
        self.mystack.push("orange")
        self.mystack.push("apple")
        self.mystack.push("yam")
        with self.assertRaises(IndexError):
            self.mystack.push("cow")

    def test_that_when_i_pop_out_everthing_from_my_stack_it_becomes_empty(self):
        self.mystack.push("name")
        self.mystack.push("banana")
        self.mystack.push("orange")
        self.mystack.push("apple")
        self.mystack.push("yam")
        self.mystack.pop()
        self.mystack.pop()
        self.mystack.pop()
        self.mystack.pop()
        self.mystack.pop()
        self.assertTrue(self.mystack.is_empty())

    def test_that_i_can_peek_on_my_get_the_current_eleemnt_on_the_stack(self):
        self.mystack.push("name")
        self.mystack.push("banana")
        self.mystack.push("orange")
        self.mystack.push("apple")
        self.mystack.push("yam")
        self.assertTrue(self.mystack.peek(),"yam")

    def test_that_i_search_for_element_in_my_stack_i_returns_the_element(self):
        self.mystack.push("name")
        self.mystack.push("banana")
        self.mystack.push("orange")
        self.assertEqual(self.mystack.search("banana"),2)
    def test_all_stack_behavoiur(self):
        self.assertTrue(self.mystack.is_empty())
        self.mystack.push("name")
        self.mystack.push("banana")
        self.mystack.push("orange")
        self.assertFalse(self.mystack.is_empty())
        self.assertEqual(self.mystack.pop(),"orange")
        self.assertEqual(self.mystack.peek(),"banana")
        self.assertEqual(self.mystack.search("banana"),2)





