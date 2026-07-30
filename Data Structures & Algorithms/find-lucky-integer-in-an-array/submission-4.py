class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        count = []
        for k, v in c.items():
            if k == v:
                count.append(k)
        if count:
            return max(count)
        else:
            return -1

        