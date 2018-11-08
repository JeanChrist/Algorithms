"""
>>> two_sum = Solution().twoSum

>>> two_sum([1,2,3,5], 5)
[1, 2]

>>> two_sum([1,2,3], 3)
[0, 1]

>>> two_sum([2, 7, 11, 15], 9)
[0, 1]

>>> two_sum([2, 7, 11, 15], 22)
[1, 3]

>>> two_sum([7, 11], 18)
[0, 1]

>>> two_sum([7, 0, 11], 11)
[1, 2]

>>> two_sum([7, -9, 11], 2)
[1, 2]

>>> two_sum([3,2,4], 6)
[1, 2]

>>> two_sum([3,3], 6)
[0, 1]

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}

        for i, v in enumerate(nums):

            val = target - v
            if val in dic:
                return [dic[val], i]
            else:
                dic[v] = i

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for i, v in enumerate(nums):

            if v not in dic:
                dic[v] = [i]
            else:
                dic[v].append(i)

        for i, v in enumerate(nums):
            val = target - v
            if val in dic:
                for j in dic[val]:
                    if i != j:
                        return [i, j]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            try:
                j = nums.index(target - nums[i])
                if j != i:
                    return [i, j]
            except ValueError:
                continue

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        range_nums = range(len(nums))

        for i in range_nums:
            val = target - nums[i]
            if val in nums:
                j = nums.index(val)
                if j != i:
                    return [i, j]



if __name__ == '__main__':
    import doctest
    doctest.testmod()
