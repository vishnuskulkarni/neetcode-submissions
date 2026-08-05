class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        used = set()
        out = []

        for i in range(len(strs)):
            if i in used:
                continue
            
            med = [strs[i]]
            used.add(i)

            for s in range(i+1, len(strs)):
                if s not in used and Counter(strs[i]) == Counter(strs[s]):
                    med.append(strs[s])
                    used.add(s)
            
            out.append(med)

        return out


