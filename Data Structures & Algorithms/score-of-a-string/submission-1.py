class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        x = [ord(i) for i in s]
        for i in range(len(x)-1):
            res += abs(x[i] - x[i+1])

        return res

        