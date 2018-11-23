"""
>>> is_anagram = Solution().isAnagram

>>> is_anagram('cat', 'rat')
False

>>> is_anagram('anagram', 'nagaram')
True

>>> is_anagram('大笑', '笑大')
True

>>> is_anagram('s大笑', '笑大t')
False
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in t:
            if i not in dic:
                return False

            if dic[i] == 1:
                dic.pop(i)
            else:
                dic[i] -= 1

        return not dic

    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return sorted(s) == sorted(t)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
