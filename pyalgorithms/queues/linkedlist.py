from .interfaces import IQueue


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class FIFOQueue(IQueue):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        if self._size == 0:
            # if the queue is empty, initialize both
            # head and tail to the item
            self._head = Node(
                value=item
            )
            self._tail = self._head
        else:
            # append the item at the end of the queue
            # i.e. put the item in line (FIFO)
            self._tail.next = Node(
                value=item
            )
            self._tail = self._tail.next

        # always increment size
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError # TODO

        # get the current head i.e. the FIRST in
        node = self._head
        # set the head to the next in line
        self._head = self._head.next

        self._size -= 1

        if self._size == 0:
            # set the tail
            self._tail = None

        # return the first value
        return node.value

    def peek(self):
        if self._size == 0:
            raise IndexError
        return self._head.value

    def size(self):
        return self._size


