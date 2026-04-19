from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # we want to save key as sorted X : [all values]

        for str in strs:
            key =  "".join(sorted(str))
            res[key].append(str)
        
        return list(res.values())