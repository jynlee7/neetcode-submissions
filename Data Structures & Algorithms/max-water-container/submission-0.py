class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        for i in range(len(heights)):
            if heights[l] < heights[r]:
                l += 1
        
        return (r-l) * min(heights[l], heights[r])
            