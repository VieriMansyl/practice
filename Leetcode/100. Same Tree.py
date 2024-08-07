# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
  if p is None and q is None:
    return True
  elif p is None or q is None:
    return False
  elif p.val != q.val:
    return False
  else:
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)