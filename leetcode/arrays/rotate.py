"""
>>> rotate = Solution().rotate

>>> li = [1,2,3,4,5,6,7]
>>> rotate(li, 3)

>>> li
[5, 6, 7, 1, 2, 3, 4]


>>> li = [-1,-100,3,99]
>>> rotate(li, 2)

>>> li
[3, 99, -1, -100]


>>> li = []
>>> rotate(li, 2)

>>> li
[]


>>> li = []
>>> rotate(li, 0)

>>> li
[]


>>> li = [1, 2, 3]
>>> rotate(li, 0)

>>> li
[1, 2, 3]


>>> li = [1, 2]
>>> rotate(li, 2)

>>> li
[1, 2]


>>> li = [1]
>>> rotate(li, 2)

>>> li
[1]

>>> li = [1,2]
>>> rotate(li, 3)

>>> li
[2, 1]
"""


class Solution:

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return

        k = k % length
        if k > 0:
            nums[:-k], nums[-k:] = nums[-k:], nums[:-k]

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:  # empty list
            return

        for _ in range(k):
            nums.insert(0, nums.pop())  # rotate last item to first place


if __name__ == '__main__':
    import doctest
    doctest.testmod()
