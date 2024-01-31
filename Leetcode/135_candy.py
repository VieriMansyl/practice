def candy(ratings: list[int]) -> int:
  n = len(ratings)
  ret = [1] * n

  for i in range(1, n):
    if ratings[i - 1] < ratings[i]:
      ret[i] = ret[i - 1] + 1

  for r in range(n - 2, -1, -1):
    if ratings[r] > ratings[r + 1]:
      ret[r] = max(ret[r], ret[r + 1] + 1)

  return sum(ret)