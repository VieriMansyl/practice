class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    for bracket in s:
      if stack:
        if stack[-1] == "(" and bracket == ")":
          stack.pop()
        elif stack[-1] == "{" and bracket == "}":
          stack.pop()
        elif stack[-1] == "[" and bracket == "]":
          stack.pop()
        else:
          stack.append(bracket)
      else:
        stack.append(bracket)

    return not stack