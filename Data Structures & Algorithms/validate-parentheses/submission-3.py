class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {'(' : ')', 
                '[' : ']',
                '{' : '}'}

        stack = []

        for i in s:
            if i in mapp.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                elif mapp[stack.pop()] != i:
                    return False
            
        return not stack

        