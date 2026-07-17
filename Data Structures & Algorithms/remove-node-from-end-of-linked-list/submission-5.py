# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        
        #count length
        while head:
            count += 1
            head = head.next
        
        #remove
        curr = dummy
        for i in range(count - n):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next