"""
>>> single = Solution().singleNumber

>>> single([1])
1

>>> single([1,2,1])
2

>>> single([1,2,2])
1

>>> single([4,1,2,1,2])
4

>>> single([1,1,2,2,3])
3

"""


class Solution:

    def singleNumber(self, nums):
        """
        It's the best answer, only O(n)
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        for i in range(0, length, 2):
            item = nums[i]
            if i == length - 1 or nums[i+1] != item:
                return item

            # if :
            #     return pre_item
            # except IndexError:
            #     return pre_item

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for index, value in enumerate(nums):
            pre_val = nums[index-1]
            if index % 2 != 0 and value != pre_val:
                return pre_val

        return nums[-1]

    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        while nums:
            i = nums.pop()
            try:
                nums.remove(i)
            except ValueError:
                return i


if __name__ == '__main__':
    from doctest import testmod
    testmod()
