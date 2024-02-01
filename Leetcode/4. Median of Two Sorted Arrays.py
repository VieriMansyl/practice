class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if(len(nums3) % 2 == 0):
            med = len(nums3)//2 - 1
            return (nums3[med] + nums3[med+1])/2
        else:
            return nums3[len(nums3)//2]