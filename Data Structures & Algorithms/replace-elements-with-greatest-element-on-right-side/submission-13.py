class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        mv = -1

        for i in range(len(arr) - 1, -1, -1):
            nm = max(mv, arr[i])
            arr[i] = mv
            mv = nm

        return arr
        