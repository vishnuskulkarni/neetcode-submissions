class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip().split()
        last = string[-1]
        return len(last)
        