class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # res = max(res, nums[l])
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res