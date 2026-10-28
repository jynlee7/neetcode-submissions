class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = {}
        tTable = {}
        for l in s:
            if l in sTable:
                sTable[l] += 1
            else:
                sTable[l] = 1
        for l in t:
            if l in tTable:
                tTable[l] += 1
            else:
                tTable[l] = 1
        return sTable == tTable