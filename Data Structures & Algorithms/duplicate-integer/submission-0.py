class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                next = nums[j]
                if curr == next:
                    return True
        return False
            
