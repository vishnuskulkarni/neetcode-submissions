class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ""

        for c in s:
            if c.isalnum():
                new+=c.lower()

        
        l = 0
        r = len(new) - 1

        while l<r:
            if new[l] != new[r]:
                return False
            else:
                l+=1
                r-=1
        
        return True
            
        