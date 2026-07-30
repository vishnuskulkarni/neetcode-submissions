class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count, t_count = {}, {}

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            s_count[s[c]] = s_count.get(s[c], 0) + 1
            t_count[t[c]] = t_count.get(t[c], 0) + 1

        for c in s_count:
            if s_count[c] != t_count.get(c, 0):
                return False

        return True
        