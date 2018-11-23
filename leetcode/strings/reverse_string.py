"""
>>> reverse_s = Solution().reverseString

>>> reverse_s('reverse')
'esrever'

>>> reverse_s("A man, a plan, a canal: Panama")
'amanaP :lanac a ,nalp a ,nam A'

>>> reverse_s('hello')
'olleh'
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):

            res += s[~i]
        return res

    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # reverse_s = Solution().reverseString
    # reverse_s('reverse')