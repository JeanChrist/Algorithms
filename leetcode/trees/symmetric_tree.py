"""
>>> is_symmetric = Solution().isSymmetric

>>> is_symmetric1 = Solution().isSymmetric1

>>> is_symmetric(BinaryTree(5))
True
>>> is_symmetric1(BinaryTree(5))
True

>>> is_symmetric(BinaryTree(5, BinaryTree(5)))
False
>>> is_symmetric1(BinaryTree(5, BinaryTree(5)))
False

>>> tree = BinaryTree(1, BinaryTree(2, BinaryTree(3), BinaryTree(4)), BinaryTree(2, BinaryTree(4), BinaryTree(3)))

>>> is_symmetric(tree)
True

>>> is_symmetric1(tree)
True
"""
from leetcode.trees import BinaryTree


class Solution(object):
    def isSymmetric(self, root):
        """
        Recursively
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        if not left or not right:
            return not left and not right

        if left.val != right.val:
            return False

        return self.is_mirror(left.left, right.right) and self.is_mirror(right.left, left.right)

    def isSymmetric1(self, root):
        """
        Iteratively
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        li = [root.right, root.left]

        while li:

            left, right = li.pop(), li.pop()

            if not left and not right:
                continue

            if not left or not right:
                return False
            elif left.val != right.val:
                return False

            li.extend([left.left, right.right, left.right, right.left])

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
