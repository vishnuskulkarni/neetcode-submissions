class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = all(a <= b for a, b in zip(nums, nums[1:]))
        dec = all(a >= b for a, b in zip(nums, nums[1:]))
        return inc or dec

        