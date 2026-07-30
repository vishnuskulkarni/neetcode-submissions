class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        c = 0

        for h, e in zip(heights, exp):
            if h!=e:
                c+=1 
        return c
        