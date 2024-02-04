def generateParenthesis(n: int) -> list[str]:
  combinations = []

  def permute(comb = '', left = 0, right = 0):
    if len(comb) == 2*n:
      combinations.append(comb)
      return

    if left < n:
      permute(comb + '(', left + 1, right)

    if left > right:
      permute(comb + ')', left, right + 1)
  
  permute()
  
  return combinations

n = 3
print(generateParenthesis(n))