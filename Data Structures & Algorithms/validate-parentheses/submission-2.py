class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {")": "(", "]":"[", "}": "{"}
        for c in s:
            # stack.append(c)
            if c in h:
                if stack and stack[-1] == h[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
