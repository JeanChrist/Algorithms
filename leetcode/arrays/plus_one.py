"""
>>> plus_one = Solution().plusOne

>>> plus_one([1,2,3])
[1, 2, 4]

>>> plus_one([1])
[2]

>>> plus_one([1,2,9])
[1, 3, 0]

>>> plus_one([1,2,5])
[1, 2, 6]

>>> plus_one([0])
[1]

>>> plus_one([9,9])
[1, 0, 0]
"""


class Solution:

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = -1
        while True:
            try:
                item = digits[index]
            except IndexError:
                digits.insert(0, 1)
                break
            if item != 9:
                digits[index] = 1 + item
                break
            digits[index] = 0
            index -= 1

        return digits

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if not digits:
            return [1]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        return self.plusOne(digits[:-1]) + [0]

    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        res = 0
        mul_factor = len(digits)
        for i in digits:
            mul_factor -= 1
            res += i * 10 ** mul_factor

        res += 1

        return list(map(int, str(res)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
