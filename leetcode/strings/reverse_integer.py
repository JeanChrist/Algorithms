"""
>>> reverse = Solution().reverse

>>> reverse(123)
321

>>> reverse(-123)
-321

>>> reverse(0)
0

>>> reverse(1)
1

>>> reverse(1534236469)
0
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int('-' + str(-x)[::-1])

        if res > 2**31 - 1 or res < -2 ** 31:
            return 0

        return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()