class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        for c in s:
            if c in hashmap_s:
                hashmap_s[c] += 1
            else:
                hashmap_s[c] = 1
        for c in t:
            if c in hashmap_t:
                hashmap_t[c] += 1
            else:
                hashmap_t[c] = 1
        for c in hashmap_s:
            if c not in hashmap_t:
                return False
            if hashmap_s[c] != hashmap_t[c]:
                return False
        for c in hashmap_t:
            if c not in hashmap_s:
                return False
            if hashmap_s[c] != hashmap_t[c]:
                return False
        return True
