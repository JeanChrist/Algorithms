"""
>>> contain = Solution().containsDuplicate

>>> contain([])
False

>>> contain([1])
False

>>> contain([1,2,5,3,4])
False

>>> contain([1,1])
True

>>> contain([1,2,3,4,2])
True

>>> contain([1,2,3,4,5,5,3])
True

>>> contain([1,1,1,3,3,4,3,2,4,2])
True
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        k = None
        for i in nums:
            if i == k:
                return True
            k = i

        return False


if __name__ == '__main__':
    from doctest import testmod
    testmod()
