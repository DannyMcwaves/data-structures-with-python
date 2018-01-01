
__all__ = ['Stack']

from structs import LinkedList


class Stack:

    top = -1

    def __init__(self):
        """
        This is the stack that is implemented using linked_list.
        """
        self.__container = LinkedList()

    def __repr__(self):
        return '{} len={} peek={}'.format(self.__class__.__name__, self.top, self.peek())

    def pop(self):
        """
        :return:
        """
        if self.top < 0:
            raise IndexError('stack index out or range')
        head = self.__container.head.data if self.__container.head is not None else None
        del self.__container[0]
        self.top -= 1
        return head

    def peek(self):
        return self.__container.head.data if self.__container.head is not None else None

    def push(self, other):
        """
        :return:
        """
        self.__container.prepend(other)
        self.top += 1

    def isEmpty(self):
        if self.top < 0:
            return True
        return False
