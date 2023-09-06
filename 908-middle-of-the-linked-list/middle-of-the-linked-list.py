# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        x = []
        while head:
            x.append(head)
            head = head.next
        return x[len(x)//2]
        