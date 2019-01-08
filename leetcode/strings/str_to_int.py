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
0

>>> str_to_int("0-1")
0

>>> str_to_int("502")
502

>>> str_to_int("-5-")
-5

>>> str_to_int("+1")
1

>>> str_to_int("   +0 123")
0

>>> str_to_int("-+1")
0

>>> str_to_int("-13+8")
-13

>>> str_to_int(" ++1")
0

>>> str_to_int(" --2")
0
"""


class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        sign, res = 1, 0

        if not s or s.startswith('+-') or s.startswith('-+')\
                or s.startswith('--') or s.startswith('++')\
                or s.startswith('0-'):
            return res

        for cell in s:
            # print(f'cell:{cell}')
            if cell.isdigit():
                res = 10*res + int(cell)
            elif cell == '-' and res == 0:
                sign = -sign
                continue
            elif cell == '+' and res == 0:
                continue
            else:
                break

        return self.cut_overflow(sign*res)

    @staticmethod
    def cut_overflow(num):
        max_num, min_num = 2**31 - 1, -2**31
        if num > max_num:
            return max_num
        if num < min_num:
            return min_num
        return num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Solution().myAtoi("   +0 123")