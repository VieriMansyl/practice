def threeSum(nums: list[int]) -> list[list[int]]:
  
  res = set()

  nums = sorted(nums)

  for i in range(len(nums)):
    p1 = i + 1
    p2 = len(nums) - 1
    
    if p1 > len(nums) - 1:  # break if p1 exceeds the length of nums
      break

    while p1 < p2:
      sum = nums[i] + nums[p1] + nums[p2]

      if sum == 0:
        res.add((nums[i], nums[p1], nums[p2]))
        p1 += 1
        p2 -= 1
      elif sum < 0:
        p1 += 1
      else:
        p2 -= 1

  return res


arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))