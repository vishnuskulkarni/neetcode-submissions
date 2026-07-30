class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        index = 0
        indices = []
        for h, e in zip(heights, expected):
            if h!=e:
                indices.append(index)
            index += 1

        return len(indices)
                
        