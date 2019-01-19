"""
>>> is_palindrome = Solution().isPalindrome

>>> is_palindrome(LinkedList.create([1,2]))
False

>>> is_palindrome(LinkedList.create([1,2,2,1]))
True

>>> is_palindrome(LinkedList.create([1,2,1]))
True

>>> is_palindrome(LinkedList.create([1,2,3,4,3,2,1]))
True

>>> is_palindrome(LinkedList.create([1,2,3,5,3,2,1]))
True

>>> is_palindrome(LinkedList.create([1,3,3,4,3,2,1]))
False
"""
from leetcode.linked_lists import LinkedList


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = middle = head
        reverse = None

        # find the middle node and reverse node before middle
        while fast and fast.next:
            fast = fast.next.next
            current, middle = middle, middle.next
            current.next, reverse = reverse, current

        if fast:  # mean list has odd count nodes, need change to next.
            middle = middle.next

        # check the reverse equal the middle
        while reverse:
            if reverse.val != middle.val:
                return False
            reverse = reverse.next
            middle = middle.next

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # is_palindrome = Solution().isPalindrome
    # is_palindrome(LinkedList.create([1, 2, 2, 1]))
    #
    # # is_palindrome(LinkedList.create([1, 2, 1]))
    # is_palindrome(LinkedList.create([1, 2, 3, 4, 3, 2, 1]))
    #
    # is_palindrome(LinkedList.create([1, 3, 5, 4, 3, 2, 1]))
