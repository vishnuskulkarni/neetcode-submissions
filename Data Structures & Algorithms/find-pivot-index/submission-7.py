class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        suml = 0

        for i in range(len(nums)):
            
            sumr = total - suml - nums[i]

            if sumr == suml:
                return i

            suml += nums[i]

        return -1 