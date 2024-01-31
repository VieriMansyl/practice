class Solution:
    def maxArea(self, height: list[int]) -> int:
        endLeft = 0
        endRight = len(height) - 1
        maks = 0

        while endLeft < endRight:
            area = min(height[endLeft], height[endRight]) * (endRight - endLeft)
            maks = max(maks, area)

            if height[endLeft] < height[endRight]:
                endLeft += 1
            else:
                endRight -= 1
        return maks