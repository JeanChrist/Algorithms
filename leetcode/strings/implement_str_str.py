"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "hello", needle = "ll"
Output: 2

>>> str_str = Solution().strStr

>>> str_str('hello', 'll')
2

>>> str_str('aaaa', 'bb')
-1


>>> str_str("", "")
0

>>> str_str("", "a")
-1

>>> str_str("a", "")
0

>>> str_str("a", "a")
0

>>> str_str('aaaa', 'ab')
-1

>>> str_str('mississippi', 'issip')
4
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        index = 0
        len_haystack = len(haystack)
        len_needle = len(needle)

        while index <= len_haystack - len_needle:
            if haystack[index:].startswith(needle):
                return index

            index += 1
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # str_str = Solution().strStr
    # print(str_str('mississippi', 'issip'))
    # print(str_str('aaaa', 'bb'))
