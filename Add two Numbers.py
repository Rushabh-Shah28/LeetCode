# Definition for singly-linked list.

#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        start = None
        end = None
        carry = 0
        
        while l1 or l2 or carry :
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
                
            value += carry
            carry = 0
            
            if value >= 10:
                carry = value // 10
                value = value % 10
            
            if not start:
                start = ListNode(value)
                end = start
            else:
                end.next = ListNode(value)
                end = end.next
            
        return start