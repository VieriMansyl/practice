def isPowerOfTwo(n: int) -> bool:
  if n <= 0: return False

  while n % 2 == 0:
    n /= 2

  return n == 1


# alternative
def isPowerOfTwo(n: int) -> bool:
  return n and not (n & n - 1)