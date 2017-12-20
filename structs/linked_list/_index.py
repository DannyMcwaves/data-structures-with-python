__all__ = ['Node', 'LinkedList']

from ._node import Node
from ._iter import LinkedListIterator, LinkedListIteratorData


class LinkedList:
    
    head: type(Node) = None
    length: int = 0
    
    def __init__(self):
        """just initialize and pass"""
    
    def __iadd__(self, other):
        """
        time complexity of 0(1) best case scenario.
        average
        :param other:
        :return:
        """
        other = Node(other)
        if self.head is None:
            self.head = other
            self.length += 1
            return self
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current += other
        self.length += 1
        return self

    def __iter__(self):
        yield from self.traverse_data()

    def __getiter__(self):
        yield from self.traverse()
    
    def __repr__(self):
        return str(self.head)

    def __len__(self):
        """
        changing the code for len from 0(n) time to 0(1)
        :return: int
        """
        return self.length

    def __getitem__(self, item):
        """
        :param item: the index to pick from.
        :return: the value at that index in the list.
        """
        length = len(self)

        if item < 0 or item > length - 1:
            raise IndexError('list assignment out of range')

        if item == 0:
            return self.head.data

        count = 0
        for i in self:
            if count == item:
                return i
            count += 1

    def __get(self, item):
        """
        :param item: the index to pick from.
        :return: the value at that index in the list.
        """
        length = len(self)

        if item < 0 or item > length - 1:
            raise IndexError('list assignment out of range')

        if item == 0:
            return self.head

        count = 0
        for i in self.__getiter__():
            if count == item:
                return i
            count += 1

    def __setitem__(self, key, value):
        """
        :param key: this is the index that that value needs to be set.
        :param value: the value to insert at the new
        :return: bool. true is inserted and false it not inserted.

        if an index index is greater than the length of the list it throws an error.
        """
        _prev, _next = self.__chain(key)
        node = Node(value)
        if _next is not None:
            node.link = _next

        if _prev is None:
            self.head = node
        else:
            _prev.link = node

    def __chain(self, key):
        """
        :param key: the number to return.
        :return: the chain
        """
        _prev = self.__get(key - 1) if 0 < key < len(self) else None
        _next = self.__get(key + 1) if key < len(self) - 1 else None
        return _prev, _next

    def __contains__(self, item):
        """
        :param item: items in the list.
        :return: bool
        """
        for i in self:
            if i == item:
                return True
        return False

    def prepend(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    def insert(self, index, data):
        """
        :param index:
        :param data:
        :return:
        """
        if index == 0:
            self.prepend(data)
            return

        if index > len(self):
            raise IndexError('linked list index out of range')

        node = Node(data)

        _prev, _next = self.__chain(index)
        _this = self.__get(index)

        _prev.link = node
        if _this is not None:
            node.link = _this
        self.length += 1

    def __delitem__(self, key):
        """
        :param key:
        :return:
        """
        if key == 0:
            self.head = self.head.link if self.head.link is not None else None
            self.length -= 1
            return
        _prev, _next = self.__chain(key)
        if _next is not None:
            _prev.link = _next
            self.length -= 1
            return
        if _prev is None:
            raise IndexError('list index out of range')
        _prev.link = None
        self.length -= 1

    def add(self, data):
        return self.__iadd__(data)

    def traverse(self):
        return LinkedListIterator(self.head)

    def traverse_data(self):
        return LinkedListIteratorData(self.head)
