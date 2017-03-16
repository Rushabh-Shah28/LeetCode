# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        A, B = headA, headB
        while A != B:
            if not A:
                A = headB
            else:
                A = A.next
            if not B:
                B = headA
            else:
                B = B.next
             
        return A
            
        