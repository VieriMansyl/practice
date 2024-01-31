def longestCommonPrefix(strs: list[str]) -> str:
  res = ""

  maxLen = min([len(s) for s in strs])

  for i in range(maxLen):
    char = strs[0][i]

    for j in range(1, len(strs)):
      if (strs[j][i] != char):
        return res
    
    res += char

  return res

# Test cases
print(longestCommonPrefix(["flower","flow","flight"]))