
__all__ = ['DoubleNode']
from ._node import Node
from .validator import LinkValidator


class DoubleNode(Node):
    """
    this is the double of the node.
    """

    prev = LinkValidator()

    def __init__(self, data, link):
        super(DoubleNode, self).__init__(data)
        self.prev = None

    def __iadd__(self, other):
        """
        :param other: the other node to add to this node.
        :return: self.
        """
        if isinstance(other, type(self)):
            other.prev = self
            self.link = other
        return self

    def __repr__(self):
        return 'data: {0}, prev: {1}, next: {2}'.format(self.data, self.prev, self.__class__.__name__ if self.link else None)
