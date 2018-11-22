
class Solution:
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            _next = head.next
            head.next = pre
            pre = head
            head = _next
        return pre

    def reverseList(self, head, pre=None):
        """
        :type head: ListNode
        :type pre: ListNode
        :rtype: ListNode
        """
        if not head:
            return pre

        _next = head.next
        head.next = pre

        return self.reverseList(_next, head)
