class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        count = 0

        for n in nums:
            if n == 1:
                count += 1
                best = max(best, count)
            else:
                count = 0
        return best
        
        