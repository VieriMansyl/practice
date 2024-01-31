def reverse(x: int) -> int:
  res = ''
  toStr = str(abs(x))
  for i in range(len(toStr)):
    res += (toStr[len(toStr) - i - 1])
    if not (-1* 2**31) <= int(res) <= (2**31):
      return 0
  
  if x >= 0:
    res = int(res)
  elif x < 0:
    res = -1 * int(res.replace('-',''))

  return res