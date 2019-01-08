"""
1.     1
2.     11
3.     21
4.     1211
5.     111221

>>> count_and_say = Solution().countAndSay

>>> count_and_say(1)
'1'

>>> count_and_say(2)
'11'

>>> count_and_say(3)
'21'

>>> count_and_say(4)
'1211'

>>> count_and_say(5)
'111221'

>>> count_and_say(6)
'312211'
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(1, n):
            s = self.say(s)
        return s

    @staticmethod
    def say(s):
        res, step = '', 0
        len_s = len(s)

        for i in range(len_s):

            next_i = i + 1
            if len_s == next_i or s[i] != s[next_i]:
                res = res + str(next_i - step) + s[i]
                step = next_i

        return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # count_and_say = Solution().countAndSay
    # print(count_and_say(30))
