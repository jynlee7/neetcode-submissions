class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0
        for n in num_set:
            # check if its the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                streak = max(length, streak)
        return streak