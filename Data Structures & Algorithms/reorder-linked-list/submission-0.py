# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the middle node
        slow = head
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half excluding the middle element(slow)
        prev = None
        curr = slow.next #it shoud be slow.next or middle node also gets included in the reversed 2nd list
        slow.next = None
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        #merging the 2 halves
        head1 , head2 = head , prev #was slow
        while(head1 != None and head2 != None):
            tmp1 , tmp2 = head1.next , head2.next
            head1.next  = head2
            head2.next = tmp1
            head1,head2 = tmp1,tmp2
        
        

            