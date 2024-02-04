def removeDuplicates(nums: list[int]) -> int:
  numSet = []
  idx = 0
  for num in nums:
    if num not in numSet:
      numSet.append(num)
      nums[idx] = num
      idx += 1
    else:
      continue
  print(nums)
  return len(nums)

# test
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))