"""
>>> intersect = Solution().intersect

>>> intersect([1,2,2,1], [2,2])
[2, 2]

>>> intersect([4,9,5], [9,4,9,8,4])
[9, 4]

>>> intersect([1,2,2,1], [2])
[2]

>>> intersect([], [])
[]

>>> intersect([3,1,2], [1,1])
[1]

>>> intersect([1], [])
[]

>>> intersect([], [2])
[]

>>> intersect([1,2,3], [4,5,6])
[]
"""


class Solution:

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic, res = {}, []
        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in nums2:
            if i in dic and dic[i] > 0:
                res.append(i)
                dic[i] -= 1

        return res

    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        res = []
        while nums1:
            i1 = nums1.pop()
            while nums2:
                i2 = nums2.pop()

                if i1 > i2:
                    nums2.append(i2)
                    break

                if i1 == i2:
                    res.append(i1)
                    break
        return res

    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter_nums = []
        while nums1 and nums2:
            item = nums1.pop()
            if item in nums2:
                inter_nums.append(item)
                nums2.remove(item)
        return inter_nums


if __name__ == '__main__':
    from doctest import testmod
    testmod()
