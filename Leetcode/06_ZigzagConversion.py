def convert(s: str, numRows: int) -> str:
  if numRows <= 1 or numRows >= len(s):
    return s
  
  max_gap = 2 * (numRows - 1)
  res = ""

  for i in range(numRows):
    '''
    * Initialize pointer to the first character of the row and gap between characters.
    * The gap is calculated as the difference between the max gap and the current row.
    '''
    p, gap = i, max_gap - 2*i if (max_gap - 2*i) != 0 else max_gap

    while p < len(s):
      res += s[p]
      p += gap
      gap = abs(max_gap - gap) or max_gap

  return res

print(convert("PAYPALISHIRING", 5))