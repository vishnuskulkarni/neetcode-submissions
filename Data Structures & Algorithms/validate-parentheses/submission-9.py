class Solution:
    def isValid(self, s: str) -> bool:

        mapp = {'(' : ')', 
                '[' : ']',
                '{' : '}'}
        stack = []

        for i in s:
            if i in mapp:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i != mapp[stack.pop()]:
                    return False
        
        return not stack

        