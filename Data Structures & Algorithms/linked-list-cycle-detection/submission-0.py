# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            if head not in visited:
                visited[head] = 1
                head = head.next
            else:
                return True
            #if visited[head] > 1:
                #return True
            
        return False


