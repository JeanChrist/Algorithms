"""
>>> remove_node_from_end = Solution().removeNthFromEnd

>>> head = LinkedList.create([1, 4, 5, 2])
>>> res = remove_node_from_end(head, 2)
>>> list(res)
[1, 4, 2]

>>> head = LinkedList.create([1, 4, 5, 2])
>>> res = remove_node_from_end(head, 3)
>>> list(res)
[1, 5, 2]

>>> head = LinkedList.create([1, 4, 5, 2])
>>> res = remove_node_from_end(head, 1)
>>> list(res)
[1, 4, 5]

>>> head = LinkedList.create([1, 2])
>>> res = remove_node_from_end(head, 2)
>>> list(res)
[2]

>>> head = LinkedList.create([1])
>>> res = remove_node_from_end(head)
>>> list(res)
[2]
"""
from leetcode.linked_lists import LinkedList


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        while n > 1:
            node = node.next
            n -= 1
        r_node, l_node = node, head
        # print(l_node, r_node)
        if not r_node.next:
            return l_node.next
        while r_node.next.next:
            l_node = l_node.next
            r_node = r_node.next

        l_node.next = l_node.next.next
        return head


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # remove_node_from_end = Solution().removeNthFromEnd
    # head = LinkedList.create([1, 4, 5, 2])
    #
    # head = remove_node_from_end(head, 1)
    # print(list(head))
    #
    # head = LinkedList.create([1, 2])
    #
    # head = remove_node_from_end(head, 2)
    # print(list(head))
