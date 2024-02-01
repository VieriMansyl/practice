# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def __init__(self):
    self.maxDepth = 0
  
  def amountOfTime(self, root, start):
    self.traverse(root, start)
    return self.maxDepth
  
  def traverse(self, root, start):
    depth = 0

    if root is None:
      return depth
    
    # traverse both children node
    left = self.traverse(root.left, start)
    right = self.traverse(root.right, start)

    if root.val == start:
      self.maxDepth = max(self.maxDepth, max(left, right))
      depth = -1
    elif left >= 0 and right >= 0:
      depth = 1 + max(left, right)
    else:
      distance = abs(left) + abs(right)
      self.maxDepth = max(self.maxDepth, distance)
      depth = min(left, right) - 1
    
    return depth