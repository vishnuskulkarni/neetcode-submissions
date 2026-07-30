class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0

        for l in range(len(nums)):
            if nums[l] != 0:
                nums[r] = nums[l]
                r += 1

        while r < len(nums):
            nums[r] = 0
            r += 1
            


        