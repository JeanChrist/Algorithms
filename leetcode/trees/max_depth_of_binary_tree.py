"""
>>> max_depth = Solution().maxDepth
>>> max_depth(BinaryTree(6, BinaryTree(5), BinaryTree(7)))
2
>>> max_depth(BinaryTree(6))
1
>>> max_depth(BinaryTree(6))
1

>>> max_depth(BinaryTree(6, BinaryTree(5, BinaryTree(4)), BinaryTree(8, BinaryTree(7), BinaryTree(9))))
3
>>> max_depth(BinaryTree(3, BinaryTree(9), BinaryTree(20, BinaryTree(15), BinaryTree(7))))
3
"""
from leetcode.trees import BinaryTree


class Solution(object):
    def maxDepth(self, root, index=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return index
        index += 1

        return max(self.maxDepth(root.left, index), self.maxDepth(root.right, index))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
