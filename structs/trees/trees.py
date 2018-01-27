__all__ = ["Tree"]


class Tree:

    root = None
    left = None
    right = None
    val = None

    def __init__(self, root):
        """
        this is the realest.
        """
        self.val = root

    def __add__(self, number):
        """
        :param number: the new number to add
        :return: self.
        """
        return self

    def __iter__(self):
        """
        :return: yield the values in the tree
        """
        yield from self.__iter_help__(self.root);

    def __iter_help__(self, root):
        if root:
            yield root.val
            self.__iter_help__(root.left)
            self.__iter_help__(root.right)

    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count
