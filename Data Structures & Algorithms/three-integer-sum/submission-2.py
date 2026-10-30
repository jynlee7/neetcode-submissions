class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        #   l                r
        nums.sort()
        res = []
        prev = None
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if prev == nums[i]:
                continue
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                if summ > 0:
                    r -= 1
                if summ < 0:
                    l += 1
            prev = nums[i]
        return res

