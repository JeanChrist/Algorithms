"""
>>> list(LinkedList(1, LinkedList(2, LinkedList(3))))
[1, 2, 3]

>>> list(LinkedList.create([1,2,3]))
[1, 2, 3]
"""


class LinkedList:
    def __init__(self, v, _next=None):
        self.val = v
        self.next = _next

    def __iter__(self):
        yield self.val

        if self.next:
            yield from self.next.__iter__()

    def __str__(self):
        return self.val

    @classmethod
    def create(cls, iterator, i=0):

        # length = len(iterator)
        # if not iterator:
        #     return None
        try:
            item = iterator[i]
        except IndexError:
            return None
        i += 1
        return cls(item, cls.create(iterator, i))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
