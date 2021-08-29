import unittest

from pyalgorithms.queues.linkedlist import FIFOQueue


class FIFOQueueLinkedListTestCase(unittest.TestCase):

    def test_enqueue_single_item(self):
        q = FIFOQueue()
        q.enqueue('hi')
        self.assertEqual(1, q._size)
        self.assertEqual('hi', q._head.value)
        self.assertEqual('hi', q._tail.value)
        self.assertEqual(q._head, q._tail)

    def test_enqueue_multiple_items(self):
        q = FIFOQueue()
        q.enqueue('first')
        q.enqueue('second')
        self.assertEqual(2, q._size)
        self.assertEqual('first', q._head.value)
        self.assertEqual('second', q._tail.value)
        self.assertEqual(q._head.next, q._tail)

    def test_dequeue_empty_queue_exception(self):
        q = FIFOQueue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_peek_empty_queue_exception(self):
        q = FIFOQueue()
        with self.assertRaises(IndexError):
            q.peek()

    def test_dequeue_single_queue_item(self):
        q = FIFOQueue()
        q.enqueue('hi')
        item = q.dequeue()
        self.assertEqual('hi', item)
        self.assertEqual(0, q._size)
        self.assertIsNone(q._head)
        self.assertIsNone(q._tail)

    def test_dequeue_multiple_items(self):
        q = FIFOQueue()
        q.enqueue('first')
        q.enqueue('second')
        val = q.dequeue()
        self.assertEqual('first', val)
        self.assertEqual(1, q._size)
        self.assertEqual('second', q._head.value)
        self.assertEqual('second', q._tail.value)
        self.assertEqual(q._head, q._tail)

    def test_size_empty(self):
        self.assertEqual(0, FIFOQueue().size())

    def test_size_single_item(self):
        q = FIFOQueue()
        q.enqueue('first')
        self.assertEqual(1, q.size())

    def test_size_multiple_items(self):
        q = FIFOQueue()
        q.enqueue('first')
        q.enqueue('second')
        q.enqueue('third')
        self.assertEqual(3, q.size())

    def test_size_multiple_items_enqueue_dequeue(self):
        q = FIFOQueue()
        q.enqueue('first')
        q.enqueue('second')
        q.enqueue('third')
        q.dequeue()
        q.dequeue()
        self.assertEqual(1, q.size())

    def test_peek_single_item(self):
        q = FIFOQueue()
        q.enqueue('first')
        item = q.peek()
        self.assertEqual('first', item)
        self.assertEqual(1, q.size())
