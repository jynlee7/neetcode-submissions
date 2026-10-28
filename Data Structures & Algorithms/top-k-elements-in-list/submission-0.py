class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for n in nums:
            hashMap[n] += 1
        
        sortedMap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        res = []
        for n in sortedMap.keys():
            if k != 0:
                res.append(n)
                k -= 1
            else:
                break
        return res