def removeElement(nums: list[int], val: int) -> int:
  index = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[index] = nums[i]
      index += 1
  return index

# arr = [3,2,2,3]
arr = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(arr, val))