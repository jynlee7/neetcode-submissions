class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0
        for n in nums:
            # check if its the start ofa sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, streak)
        return streak