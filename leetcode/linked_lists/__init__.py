"""
>>> linked_list = LinkedList(1, LinkedList(2, LinkedList(3)))
>>> list(linked_list)
[1, 2, 3]
>>> linked_list.val
1
>>> linked_list.next.val
2
>>> linked_list.next.val
2
>>> list(LinkedList.create([1,2,3]))
[1, 2, 3]

>>> head = LinkedList.create([1,2,3])
>>> head.get_final_node() is head.next.next
True

>>> LinkedList(1, LinkedList(2, LinkedList(3, None))).__repr__()
'LinkedList(1, LinkedList(2, LinkedList(3, None)))'
"""


class LinkedList:
    def __init__(self, v, _next=None):
        self.val = v
        self.next = _next

    def __iter__(self):
        yield self.val

        if self.next:
            yield from self.next

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val!r}, {self.next!r})'

    def __str__(self):
        return f'node:[val:{self.val}, next:{self.next.val if self.next else None}]'

    def get_final_node(self):
        last = self
        while last.next:
            last = last.next
        return last

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
    print(LinkedList.create([1, 2, 3]).__repr__())