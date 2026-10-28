class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(index, path, current_sum):
            if current_sum == target:
                res.append(path.copy())
                return

            if current_sum > target:
                return

            if index >= len(nums):
                return

            path.append(nums[index])
            backtrack(index, path, current_sum + nums[index])
            path.pop()
            backtrack(index + 1, path, current_sum)
        
        backtrack(0, [], 0)
        return res
