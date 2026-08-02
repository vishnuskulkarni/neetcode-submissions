class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter

        counts = Counter(nums)

        return [num for num, count in counts.most_common(k)]

        