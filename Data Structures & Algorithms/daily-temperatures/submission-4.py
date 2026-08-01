class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack w/o tuples
        temps = temperatures[:]
        res = [0] * len(temps)
        stack = [] #indices

        for i in range(len(temperatures)):
            while stack and temps[i] > temps[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res


        