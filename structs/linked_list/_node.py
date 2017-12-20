
from .validator import NodeValidator, LinkValidator


class Node:

    data = NodeValidator()
    link = LinkValidator()

    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    def __iadd__(self, other):
        """
        :param other:
        :return:
        """
        if isinstance(other, type(self)):
            self.link = other
        return self

    def __repr__(self):
        return 'data: {0}, link: {1}'.format(self.data, self.__class__.__name__ if self.link else None)
