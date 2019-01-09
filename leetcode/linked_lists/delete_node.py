"""
>>> linked_list = LinkedList.create([1, 4, 5, 2])
>>> delete_node = Solution().deleteNode

>>> delete_node(linked_list.next.next)
>>> list(linked_list)
[1, 4, 2]

>>> linked_list = LinkedList.create([1, 4, 5, 2])
>>> delete_node(linked_list.next)
>>> list(linked_list)
[1, 5, 2]
"""
from leetcode.linked_lists import LinkedList


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':

    import doctest
    doctest.testmod()
