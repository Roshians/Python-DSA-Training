# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        count = 0
        pend = p2end = p3start = p2start = None
        if left == right:
            return head
        
        while temp:
            if count == (left - 2):
                pend = temp
                p2start = temp.next
            elif count == (right - 1):
                p2end = temp
                p3start = temp.next
                p2end.next = None
                break
            temp = temp.next
            count += 1
        
        start = end = None

        if left == 1:
            p2start = head
        while p2start:
            temp = p2start
            p2start = p2start.next
            if end == None:
                start = end = temp
                end.next = None
            else:
                temp.next = start
                start = temp
        if pend:
            pend.next = start
        else:
            head = start
        end.next = p3start

        return head