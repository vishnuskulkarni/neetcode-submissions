class Solution:
    def scoreOfString(self, s: str) -> int:
        #zip solution

        score = 0
        for a, b in zip(s, s[1:]):
            score += abs(ord(b) - ord(a))

        return score

        