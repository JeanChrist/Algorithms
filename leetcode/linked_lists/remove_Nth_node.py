class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def _count(_node):
            index, node_cp = 0, 1
            while node_cp:
                node_cp = node_cp.next
                index += 1

            return index - n

        i, node = _count(head), head
        while i > 0:
            node = node.next
            i -= 1

        return node
