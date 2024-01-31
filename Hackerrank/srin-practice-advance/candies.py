#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def candies(n, arr):
  ret = [1] * n

  for i in range(1, n):
    if arr[i - 1] < arr[i]:
      ret[i] = ret[i - 1] + 1

  for r in range(n - 2, -1, -1):
    if arr[r] > arr[r + 1]:
      ret[r] = max(ret[r], ret[r + 1] + 1)

  return sum(ret)

# print(candies(3, [1,2,2]))
# print(candies(10, [2,4,2,6,1,7,8,9,2,1]))
# print(candies(8, [2,4,3,5,2,6,4,5]))
# print(candies(3, [3,2,1]))
print(candies(3, [1,1,1]))