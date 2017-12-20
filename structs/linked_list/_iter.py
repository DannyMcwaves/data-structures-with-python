
from ._node import Node

_all_ = ['LinkedListIterator', 'LinkedListIteratorData']


class LinkedListIterator:

    def __init__(self, head):
        """
        :param head:
        """
        self.head = head
        self.index = Node(None, self.head)

    def __next__(self):
        """
        :return: traverse the
        """
        if self.index.link is not None:
            self.index = self.index.link
            return self.index
        else:
            self.index = Node(None, self.head)
            raise StopIteration()

    def __iter__(self):
        return self


class LinkedListIteratorData:

    def __init__(self, head):
        """
        :param head:
        """
        self.head = head
        self.index = Node(None, self.head)

    def __next__(self):
        """
        :return: traverse the
        """
        if self.index.link is not None:
            self.index = self.index.link
            return self.index.data
        else:
            self.index = Node(None, self.head)
            raise StopIteration()

    def __iter__(self):
        return self
