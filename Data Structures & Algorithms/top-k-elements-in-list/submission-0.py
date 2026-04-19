from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums_count = Counter(nums)
        # nums.count.sort(key=lambda x:x[1], reverse = True)
        sorted_items = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)
        
        for key, value in sorted_items:
            if len(res)==k:
                break
            res.append(key)
        return res

