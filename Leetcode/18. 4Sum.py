def fourSum(nums: list[int], target: int) -> list[list[int]]:
  nums.sort()
  n = len(nums)

  res = set()

  for i in range(n):
    for j in range(i+1, n):
      leftP = j + 1
      rightP = n - 1
      while leftP < rightP:
        sum = nums[i] + nums[j] + nums[leftP] + nums[rightP]
        if sum == target:
          res.add((nums[i], nums[j], nums[leftP], nums[rightP]))
          leftP += 1
          rightP -= 1
        elif sum < target:
          leftP += 1
        else:
          rightP -= 1

  return res

  

print(fourSum([1,0,-1,0,-2,2], 0))
print(fourSum([2,2,2,2,2], 8))



''' N-sum'''
def findNsum(nums, target, leftP, rightP, N, result, results: list[list[int]]):
  # early termination
  if (rightP-leftP + 1 < N) or (N < 2) or (target < nums[leftP] * N) or (target > nums[rightP] * N):
    return
  
  # two pointers solve sorted 2-sum problem
  if N == 2:
    while leftP < rightP:
      s = nums[leftP] + nums[rightP]
      if s == target:
        results.append(result + [nums[leftP], nums[rightP]])
        leftP += 1
        while leftP < rightP and nums[leftP] == nums[leftP - 1]:
          leftP += 1
      elif s < target:
        leftP += 1
      else:
        rightP -= 1
  
  # recursively reduce N
  else: 
    for i in range(leftP, rightP+1):
      if i == leftP or (i > leftP and nums[i-1] != nums[i]):
        findNsum(i+1, rightP, target-nums[i], N-1, result+[nums[i]], results)