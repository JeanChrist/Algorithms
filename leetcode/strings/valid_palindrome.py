"""
>>> is_palindrome = Solution().isPalindrome

>>> is_palindrome("A man, a plan, a canal: Panama")
True

>>> is_palindrome("race a car")
False

>>> is_palindrome("a.")
True

>>> is_palindrome("..........a.     c....")
False

>>> is_palindrome(".,")
True

>>> is_palindrome("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
True
"""


class Solution:

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pre_index, end_index = 0, len(s)-1

        while pre_index < end_index:

            while pre_index < end_index and not s[end_index].isalnum():

                end_index -= 1
            while pre_index < end_index and not s[pre_index].isalnum():
                pre_index += 1

            if s[pre_index].lower() != s[end_index].lower():
                return False

            pre_index += 1
            end_index -= 1

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Solution().isPalindrome("A man, a plan, a canal: Panama")
    # Solution().isPalindrome("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
