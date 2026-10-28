# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removing the ith node
        So essentially cutting off the pointer from the prev and the next node

        1 -> 2 -> 3 -> 4    n = 2
        iterate n % len(head) = 2 % 4 = 2
        so then we are at 2
        create a pointer at 3
        p = iterated.next
        iterated.next = iterated.next.next
        p.next = None

        edge cases:
        when a list is empty
        or list.next is empty return None
        """
        if not head or not head.next:
            return None
        
        # iterate = n % len(head)
        nth_start = head
        while n > 0:
            nth_start = nth_start.next
            n -= 1
        
        curr, prev = head, None

        while nth_start != None:
            nth_start = nth_start.next
            prev = curr
            curr = curr.next

        if (prev == None):
            return head.next
        
        prev.next = prev.next.next
        return head
