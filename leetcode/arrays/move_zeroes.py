"""
>>> move_0 = Solution().moveZeroes

>>> li = [1,0,1]
>>> move_0(li)
>>> li
[1, 1, 0]

>>> li = []
>>> move_0(li)
>>> li
[]

>>> li = [0,1,0,3,12]
>>> move_0(li)
>>> li
[1, 3, 12, 0, 0]

>>> li = [0]
>>> move_0(li)
>>> li
[0]

>>> li = [1, 2, 3]
>>> move_0(li)
>>> li
[1, 2, 3]

>>> li = [1, 0, 1, 0]
>>> move_0(li)
>>> li
[1, 1, 0, 0]

>>> li = [0,0,1]
>>> move_0(li)
>>> li
[1, 0, 0]

"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index, length = 0, len(nums)
        while length > 0:
            length -= 1
            if nums[index] == 0:
                nums.append(nums.pop(index))
            else:
                index += 1

    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for _ in range(len(nums)):
            if nums[index] == 0:
                nums.append(nums.pop(index))
            else:
                index += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
