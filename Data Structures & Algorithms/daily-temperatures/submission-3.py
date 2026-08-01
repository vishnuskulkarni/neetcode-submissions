class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack
        temps = temperatures[:]
        stack = []
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                s_t, s_i = stack.pop()
                res[s_i] = i - s_i

            stack.append((t, i))

        return res