"""
>>> delete_node = Solution().deleteNode
#
# >>> li = [1, 4, 5, 2]
# >>> delete_node(5)
# >>> li
# [1, 4, 2]
#
# >>> li = [1, 4, 5, 2]
# >>> delete_node(5)
# >>> li
# [1, 4, 2]
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next
        node.next = node.next.next
