"""
>>> sorted_array_to_BST = Solution().sortedArrayToBST

>>> sorted_array_to_BST([-10,-3,0,5,9])
BinaryTree(0, BinaryTree(-3, BinaryTree(-10, None, None), None), BinaryTree(9, BinaryTree(5, None, None), None))
"""
from leetcode.trees import BinaryTree as TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)

        if length == 0:
            return None

        middle_index = length // 2
        left_nums, right_nums = nums[:middle_index], nums[middle_index+1:]

        tree = TreeNode(nums[middle_index])
        tree.left, tree.right = self.sortedArrayToBST(left_nums), self.sortedArrayToBST(right_nums)

        return tree


if __name__ == '__main__':
    import doctest
    doctest.testmod()
