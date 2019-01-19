"""
>>> has_cycle = Solution().hasCycle

>>> item1, item2 = LinkedList(5), LinkedList(6)
>>> item1.next = item2
>>> item2.next = item1
>>> has_cycle(item1)
True

>>> item = LinkedList(5, LinkedList(6, LinkedList(7)))
>>> item.get_final_node().next = item
>>> has_cycle(item1)
True

>>> has_cycle(LinkedList(5, LinkedList(6)))
False
"""
from leetcode.linked_lists import LinkedList


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # item1 = LinkedList(5)
    # item2 = LinkedList(6)
    # item1.next = item2
    # item2.next = item1
