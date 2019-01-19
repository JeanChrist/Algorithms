"""
>>> BinaryTree(6, BinaryTree(5), BinaryTree(7)).__repr__()
'BinaryTree(6, BinaryTree(5, None, None), BinaryTree(7, None, None))'

>>> list(BinaryTree(6, BinaryTree(5, BinaryTree(4)), BinaryTree(8, BinaryTree(7), BinaryTree(9))))
[6, 5, 8, 4, None, 7, 9]
>>> BinaryTree.create([6,5,7]).__repr__()
'BinaryTree(6, BinaryTree(5, None, None), BinaryTree(7, None, None))'
"""


class BinaryTree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val!r}, {self.left!r}, {self.right!r})'

    # @classmethod
    # def create(cls, iterator, level=1):
    #     i = 0
    #     try:
    #         item = iterator[i]
    #     except IndexError:
    #         return None
    #     cls(item, cls.create(iterator, level), cls.create(iterator, level))
    #     return cls.create(iterator[3:])

    # def __iter__(self):
    #
    #     yield self.val
    #
    #     if self.left:
    #         yield from self.left
    #
    #     if self.right:
    #         yield from self.right



if __name__ == '__main__':
    import doctest
    doctest.testmod()
