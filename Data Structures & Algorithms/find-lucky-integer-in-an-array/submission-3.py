class Solution:
    def findLucky(self, arr: List[int]) -> int:
        store = {}
        luck = []
        for v in arr:
            store[v] = store.get(v, 0) + 1

        for k, v in store.items():
            if k == v:
                luck.append(k)
            
        if luck:
            return max(luck)
        else:
            return -1

            
        