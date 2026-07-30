class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        if len(pattern) != len(s.split()):
            return False

        chars = pattern
        words = s.split()

        c2w = {}
        w2c = {}

        for c, w in zip(chars, words):
            if c not in c2w:
                c2w[c] = w

            else:
                if c2w[c] != w:
                    return False

        for w, c in zip(words, chars):
            if w not in w2c:
                w2c[w] = c

            else:
                if w2c[w] != c:
                    return False
        
        return True

        