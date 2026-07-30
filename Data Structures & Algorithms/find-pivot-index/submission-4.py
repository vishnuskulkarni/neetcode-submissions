class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        for i in range(len(nums)):
            suml, sumr = 0, 0

            for n in range(i):
                suml += nums[n]

            for n in range(i+1, len(nums)):
                sumr += nums[n]

            if sumr == suml:
                return i

        return -1
        
        