import unittest

from src.Queue.queue import Queue

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.myqueue = Queue()
    def test_that_queue_is_empty(self):
        self.assertTrue(self.myqueue.is_empty())

    def test_that_when_i_add_to_my_queue_it_does_not_remain_empty(self):
        self.myqueue.add(1)
        self.myqueue.add(True)
        self.assertFalse(self.myqueue.is_empty())

    def test_that_i_can_not_add_none_to_my_queue(self):
        with self.assertRaises(TypeError):
            self.myqueue.add(None)
    def test_that_when_i_add_to_my_queues_i_can_get_the_first_element(self):
        self.myqueue.add(1)
        self.myqueue.add(True)
        self.assertEqual(self.myqueue.element(),True)

    def test_that_when_My_Queue_is_empty_it_raise_exceptions(self):
        with self.assertRaises(Exception):
            self.myqueue.element()


    def test_that_when_remove_from_my_queue_it_remove_the_element_on_queue(self):
        self.myqueue.add("Ade")
        self.assertEqual("Ade",self.myqueue.remove())
    def test_that_when_i_add_mutiple_elements_to_myques(self):
        self.myqueue.add(1)
        self.myqueue.add(True)
        self.myqueue.add("Ade")
        self.assertEqual(1,self.myqueue.remove())
        self.assertIs(True, self.myqueue.remove())
        self.assertEqual("Ade",self.myqueue.remove())

    def test_that_when_My_Queue_is_empty_it_raises_exceptions(self):
        with self.assertRaises(Exception):
            self.myqueue.remove()

    def test_that_when_my_queue_is_full_i_can_not_add_to_my_quueu(self):
        MyQueue = Queue(2)
        MyQueue.add(1)
        MyQueue.add(True)
        with self.assertRaises(Exception):
            MyQueue.add("Ade")

