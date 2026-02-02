# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 3 parts
        # dummy node at start
        # firs tmove to the left side
        # second is reverse the middle
        # last is clean up pointer

        dummyNode = ListNode(0, head)

        prevLeft, curr = dummyNode, head
        for i in range(left - 1):
            prevLeft = curr
            curr = curr.next
        
        prev = None # node that is the one before the swaps
        # we want to break that link into the reverrse part
        for i in range(right - left + 1):
            tempNode = curr.next
            curr.next = prev
            prev = curr
            curr = tempNode
        
        prevLeft.next.next = curr
        prevLeft.next = prev

        return dummyNode.next

