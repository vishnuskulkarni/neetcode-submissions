class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        store = {}
        for i, v in enumerate(nums):
            store[v] = store.get(v, 0) + 1

        for i in store.values():
            if i > 1:
                return True

        return False
        