"""
>>> level_order = Solution().levelOrder

>>> level_order(BinaryTree(3, BinaryTree(9), BinaryTree(20, BinaryTree(15), BinaryTree(7))))
[[3], [9, 20], [15, 7]]
"""
from leetcode.trees import BinaryTree


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        return self.travel([], root)

    def travel(self, li, *nodes):

        li_value, li_node = [], []

        for node in nodes:
            if node:
                li_value.append(node.val)

                li_node.extend((node.left, node.right))

        if not li_node:
            return li

        li.append(li_value)

        return self.travel(li, *li_node)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
