def numberOfBeams(bank: list[str]) -> int:
  beams = []
  for row in bank:
    beams.append(row.count('1'))
  
  p, nexRow, res = 0, 0, 0
  while nexRow < len(beams):
    if p != nexRow and beams[nexRow] != 0:
      res += beams[p] * beams[nexRow]
      p = nexRow
    nexRow += 1
  
  return res
      

test = list(["011001","000000","010100","001000"])
test = list(["000","111", "000"])
print(numberOfBeams(test))