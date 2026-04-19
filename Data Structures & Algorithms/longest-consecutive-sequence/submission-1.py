class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we need to check if value - 1 is in the array.if not then that is the start of the array
        # we then move into the loop and find the + 1 till we can. and store the len.
        # we do this till we reach end of the array/
        if not nums:
            return 0

        res = 0
        store = {}

        i = 0
        while (i < len(nums)):
            if (nums[i] - 1) not in nums: # meaning nums[i] is the start of the sequence
                val = nums[i]+1
                total = 0
                while i < len(nums) and val in nums:
                    val += 1
                    total += 1
                res = max(res, total)
            i+=1
        return res + 1
