"""
>>> first_unique = Solution().firstUniqChar

>>> first_unique('leetcode')
0

>>> first_unique('loveleetcode')
2

>>> first_unique('hello world')
0

>>> first_unique('')
-1

>>> first_unique('ss')
-1
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic, min_index = {}, float('inf')

        for i, v in enumerate(s):

            if v in dic:
                
                dic[v] = ''
            else:
                dic[v] = i

        for v in dic.values():

            if v != '' and v < min_index:
                min_index = v
        if min_index == float('inf'):
            min_index = -1
        return min_index


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    Solution().firstUniqChar('leetcode')