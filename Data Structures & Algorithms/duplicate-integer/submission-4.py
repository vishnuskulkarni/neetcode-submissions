class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1

        # for x in d.values():
        #     if x > 1:
        #         return True

        # return False

        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)

        return False

        