"""
>>> str_to_int = Solution().myAtoi

>>> str_to_int("42")
42

>>> str_to_int("42 hello")
42

>>> str_to_int("-54378 world")
-54378

>>> str_to_int("words and 987")
0

>>> str_to_int("-91283472332")
-2147483648

>>> str_to_int("   -42")
-42

>>> str_to_int(" ")
0

>>> str_to_int("")
0

>>> str_to_int("3.14159")
3

>>> str_to_int("+")
0

>>> str_to_int("+-2")
-2

>>> str_to_int("0-1")
-1
"""


class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = ''

        for cell in s:

            if cell == ' ' or cell == '+':
                continue
            if cell.isdigit() or cell == '-':
                res += cell
            else:
                break
        ret, split_s = 0, res.split()
        if len(split_s) > 1:
            if split_s[0] == '':
                ret = -int(split_s[1])
        elif len(split_s) > 2:

            for i in split_s[2]:

                ret -= i
        print(ret)
        return self.cut_overflow(res) if res and res != '+' and res != '-' else 0

    @staticmethod
    def cut_overflow(num):
        num = int(num)
        max_num, min_num = 2**31 - 1, -2**31
        if num > max_num:
            return max_num
        if num < min_num:
            return min_num
        return num
        # return


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    Solution().myAtoi('0-1')