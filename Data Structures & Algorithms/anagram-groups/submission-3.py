class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for s in strs:
            sig = ''.join(sorted(s))
            store[sig].append(s)
        return list(store.values())

        