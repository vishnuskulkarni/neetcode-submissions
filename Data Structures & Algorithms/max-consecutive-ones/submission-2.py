class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        maxc = 0

        for n in nums:
            if n == 1:
                c += 1
                maxc = max(c, maxc)
            else:
                c = 0
        return maxc
        