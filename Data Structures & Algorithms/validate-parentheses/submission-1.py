class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {")": "(", "]":"[", "}": "{"}
        for c in s:
            stack.append(c)
            if c in h:
                stack.pop()
                stack.pop()
        return not stack
