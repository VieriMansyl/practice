# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  dummy = ListNode()
  dummy.next = head
  prev = dummy
  length = 1

  while head:
    length += 1
    head = head.next

  head = dummy
  for _ in range(length - n):
    prev = head
    head = head.next
  prev.next = head.next

  return dummy.next

# test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head = ListNode(1)
n = 1
removeNthFromEnd(head, n)