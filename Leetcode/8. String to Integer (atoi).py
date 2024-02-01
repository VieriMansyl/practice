def myAtoi(s: str) -> int:

  op = ''
  res = '0'

  for i in range(len(s)):
    if (s[i] == ' ' and len(res) == 1 and op == ''):
      continue
    
    elif (s[i].isdigit()):
      res += s[i]
    
    elif (s[i] in ['-', '+'] and len(res) == 1):
      if (op == ''):
        op = s[i]
      else:
        return 0
    
    else:
      break

  print(f"ini res: {res}")
  return max(min(int(res) * (-1 if op == '-' else 1), 2**31 - 1), -2**31)

# Test cases
print(myAtoi("words and 987"))
print(myAtoi("3.1123"))
print(myAtoi("    -42"))
print(myAtoi("+-12"))
print(myAtoi("-+12"))
print(myAtoi("-91283472332"))
print(myAtoi("00000-42a1234"))