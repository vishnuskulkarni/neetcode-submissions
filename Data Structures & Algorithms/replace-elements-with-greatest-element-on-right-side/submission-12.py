class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        mv = -1
        ans = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            ans[i] = mv
            mv = max(mv, arr[i])

        return ans
            
        