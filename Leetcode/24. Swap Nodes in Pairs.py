# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: list[ListNode]) -> list[ListNode]:
        
        if not head or head.next is None:
            return head

        firstNode = head
        secondNode = firstNode.next
        thirdNode = secondNode.next if secondNode.next else None

        secondNode.next = firstNode
        firstNode.next = self.swapPairs(thirdNode) if thirdNode else None

        return secondNode