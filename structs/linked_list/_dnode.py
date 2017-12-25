
__all__ = ['DoubleNode']
from ._node import Node
from .validator import LinkValidator


class DoubleNode(Node):
    """
    this is the double of the node.
    """

    back = LinkValidator()

    def __init__(self, data, link):
        super(DoubleNode, self).__init__(data)
        self.back = None

    def __iadd__(self, other):
        """
        :param other: the other node to add to this node.
        :return: self.
        """
        if isinstance(other, type(self)):
            other.back = self
            self.link = other
        return self
