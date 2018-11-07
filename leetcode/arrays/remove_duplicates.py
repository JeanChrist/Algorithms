"""
>>> remove_duplicate = Solution().removeDuplicates

>>> li = []
>>> k = remove_duplicate(li)
>>> k
0
>>> li[:k]
[]

>>> li = [1]
>>> k = remove_duplicate(li)
>>> k
1
>>> li[:k]
[1]

>>> li = [1, 1, 2]
>>> k = remove_duplicate(li)
>>> k
2
>>> li[:k]
[1, 2]

>>> li = [1, 1, 2, 3, 4, 4]
>>> k = remove_duplicate(li)
>>> k
4
>>> li[:k]
[1, 2, 3, 4]
"""
from unittest import TestCase


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0

        for i in nums:

            if i != nums[k]:
                k += 1
                nums[k] = i

        return k + 1 if nums else k


if __name__ == '__main__':
    import doctest
    doctest.testmod()
