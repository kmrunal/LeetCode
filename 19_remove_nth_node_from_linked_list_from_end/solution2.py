# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head

        dummy = ListNode(0)
        l = self.length(head)


        dummy.next = head
        head = dummy
        cnt = l - n
        while (cnt):
            dummy = dummy.next
            cnt -= 1
        dummy.next = dummy.next.next

        return head.next

        
