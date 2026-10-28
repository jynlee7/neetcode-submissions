class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])

        res = [intervals[0]]

        for start, end in intervals:
            prev_e = res[-1][1]
            if prev_e >= start:
                res[-1][1] = max(prev_e, end)
            else:
                res.append([start, end])
        return res
            
