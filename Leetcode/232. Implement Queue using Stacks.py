class MyQueue:

  def __init__(self):
    self.head = []

  def push(self, x: int) -> None:
    self.head.append(x)

  def pop(self) -> int:
    head = self.head.pop(0)
    return head
      
  def peek(self) -> int:
    return self.head[0]

  def empty(self) -> bool:
    return len(self.head) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()