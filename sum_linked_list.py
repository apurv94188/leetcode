# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        prev1 = None
        prev2 = None
        while l1 != None or l2 != None:
            if l1 != None:
                nextNode = l1.next
                l1.next = prev1
                prev1 = l1
                l1 = nextNode
                
                
            if l2 != None:
                nextNode = l2.next
                l2.next = prev2
                prev2 = l2
                l2 = nextNode
            
        prev = None
        carry = 0
        not_first = True
        Top = None
        while prev1 != None or prev2 != None:
            head = ListNode(carry)
            if prev1 != None:
                head.val += prev1.val
                if head.val > 9:
                    head.val -= 10
                    carry = 1
                prev1 = prev1.next
                
            if prev2 != None:
                head.val += prev2.val
                if head.val > 9:
                    head.val -= 10
                    carry = 1
                prev2 = prev2.next
            
            if not_first:
                not_first = False
                prev = head
                Top = head
                
            else:
                prev.next = head
                prev = head
                
        return Top
    
