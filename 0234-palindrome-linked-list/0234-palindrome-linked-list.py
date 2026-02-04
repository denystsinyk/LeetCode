# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # inital thoughts
        # traverse list, check if top list is the same if so then pop if not then add
        # if the stack not empty then return False, else True or flip

        curr = head
        s = []

        # so what we can do is go backwards using the stack and forwards from ll
        # kinda acks as 2 pointers

        while curr:
            s.append(curr.val)
            curr = curr.next
        curr = head
        
        while curr and curr.val == s.pop():
            curr = curr.next

        if not s:
            return True
        return False
        
        