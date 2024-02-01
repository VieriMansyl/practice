from itertools import product 

numToAlph = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z'],
}

def letterCombinations(digits: str) -> list[str]:
  combinations = set()

  if len(digits) == 0:
    return combinations
  elif len(digits) == 1:
    return numToAlph[digits]
  else:
    all_list = [numToAlph[d] for d in digits]
    print(all_list)
    combinations = [''.join(c) for c in product(*all_list)]
    return combinations


print(letterCombinations('23'))
