class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        out = []

        for _ in range(2):
            for n in nums:
                out.append(n)

        return out
        