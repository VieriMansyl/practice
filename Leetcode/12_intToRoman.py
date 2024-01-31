def intToRoman(num: int) -> str:
  romeNum = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  result = ''
  for symbol, value in reversed(romeNum.items()):
    while num >= value:
      result += symbol
      num -= value

      result = result\
                .replace("DCCCC", "CM")\
                .replace("CCCC", "CD")\
                .replace("LXXXX", "XC")\
                .replace("XXXX", "XL")\
                .replace("VIIII", "IX")\
                .replace("IIII", "IV")

  return result
  
print(intToRoman(999))