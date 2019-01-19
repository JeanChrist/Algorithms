"""
>>> is_valid_BST = Solution().isValidBST

>>> is_valid_BST(BinaryTree(6, BinaryTree(5, BinaryTree(4)), BinaryTree(8, BinaryTree(7), BinaryTree(9))))
True
>>> is_valid_BST(BinaryTree(3, BinaryTree(9), BinaryTree(20, BinaryTree(15), BinaryTree(7))))
False
>>> is_valid_BST(BinaryTree(1, BinaryTree(1)))
False
>>> is_valid_BST(BinaryTree(10, BinaryTree(5), BinaryTree(15, BinaryTree(6), BinaryTree(20))))
False
"""
from leetcode.trees import BinaryTree


class Solution(object):
    def isValidBST(self, root, less=float('-inf'), larger=float('inf')):
        """
        :param root: TreeNode
        :param less: float. The node.val should less than
        :param larger: float. The node.val should large than
        :return: bool
        """

        if not root:
            return True
        if less >= root.val:
            return False
        if larger <= root.val:
            return False

        return all((
            self.isValidBST(root.left, less, min(larger, root.val)),
            self.isValidBST(root.right, max(less, root.val), larger)
        ))



if __name__ == '__main__':
    import doctest
    doctest.testmod()
