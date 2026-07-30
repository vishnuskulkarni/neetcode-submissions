class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        store = {}

        for v in nums:
            store[v] = store.get(v, 0) + 1

        for i in nums:
            if store[i] > 1:
                return True
        
        return False

        
        