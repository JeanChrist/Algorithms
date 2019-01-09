"""
>>> merge_two_lists = Solution().mergeTwoLists

>>> l1, l2 = LinkedList.create([1,3,5]), LinkedList.create([2,4,6])
>>> new_list = merge_two_lists(l1, l2)
>>> list(new_list)
[1, 2, 3, 4, 5, 6]
>>> l1, l2 = LinkedList.create([1,3,5,7,9]), LinkedList.create([2,4,6])
>>> new_list = merge_two_lists(l1, l2)
>>> list(new_list)
[1, 2, 3, 4, 5, 6, 7, 9]
>>> l1, l2 = LinkedList.create([1,3,5]), LinkedList.create([2,4,6,8,9])
>>> new_list = merge_two_lists(l1, l2)
>>> list(new_list)
[1, 2, 3, 4, 5, 6, 8, 9]
>>> l1, l2 = None, LinkedList.create([0])
>>> new_list = merge_two_lists(l1, l2)
>>> list(new_list)
[0]
>>> l1, l2 = LinkedList.create([2]), LinkedList.create([1])
>>> new_list = merge_two_lists(l1, l2)
>>> list(new_list)
[1, 2]
>>> l1, l2 = LinkedList.create([1,2,4]), LinkedList.create([5])
>>> new_list = merge_two_lists(l1, l2)
>>> list(new_list)
[1, 2, 4, 5]
"""
from leetcode.linked_lists import LinkedList


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1:
        #     return l2
        new_list = l1 or l2

        while l2 and l1:

            if l1.val > l2.val:
                l1.val, l2.val = l2.val, l1.val
                l1.next, l2.next = l2.next, l1.next

            l1.next, l2 = l2, l1.next
            l1 = l1.next

        return new_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # merge_two_lists = Solution().mergeTwoLists
    # l1, l2 = LinkedList.create([1,2,4]), LinkedList.create([5])
    # print(list(merge_two_lists(l1, l2)))
