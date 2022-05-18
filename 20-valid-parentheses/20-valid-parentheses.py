class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for b in s:
            if not stack:
                if b not in pair:
                    return False
                stack.append(b)
            else:
                if b not in pair and pair[stack[-1]] != b:
                    return False
                if b == pair[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(b)
        return not stack