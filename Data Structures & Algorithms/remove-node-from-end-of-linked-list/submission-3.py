# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #kth node from end of list means n-k th node from the beginning
        dummy = head
        main_head = head
        length = 1
        
        while head.next !=  None:
            head = head.next
            length = length + 1 
        
        if n == length:
            return dummy.next
        req = length - n
        
        while req > 0:
            prev = dummy
            dummy = dummy.next
            req -= 1
        prev.next = dummy.next
        return main_head