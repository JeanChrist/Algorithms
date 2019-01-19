"""

"""


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
