"""
>>> longest_common_prefix = Solution().longestCommonPrefix

>>> longest_common_prefix(["dog","racecar","car"])
''

>>> longest_common_prefix(["flower","flow","flight"])
'fl'

>>> longest_common_prefix(["f2ower","flow","flight"])
'f'

>>> longest_common_prefix(["aca","cba"])
''
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res, index = '', 0

        for t in zip(*strs):
            if self.check_all_same(t):
                res += t[0]
            else:
                break
        return res

    @staticmethod
    def check_all_same(li):

        for i in range(1, len(li)):
            if li[i] != li[i-1]:
                return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
