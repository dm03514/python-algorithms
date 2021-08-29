from abc import ABC, abstractmethod


class IQueue(ABC):

    @abstractmethod
    def enqueue(self, item):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        raise NotImplementedError

    @abstractmethod
    def size(self):
        raise NotImplementedError

