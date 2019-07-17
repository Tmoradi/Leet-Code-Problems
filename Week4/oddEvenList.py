# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        
        if head == None: return None  
        
        odd = head ; evenHead = head.next; even = evenHead
        
        while even !=None and even.next !=None:
            # the next value of odd is going to come from even.next 
            odd.next = even.next 
            odd = odd.next 
            # the next value of odd is going to be from odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        return head 
                