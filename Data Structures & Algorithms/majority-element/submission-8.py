class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        store = {}
        maxcount, res = 0, 0

        for i in nums:
            store[i] = store.get(i, 0) + 1
            if store[i] > maxcount:
                maxcount = store[i]
                res = i

        return res


        

        