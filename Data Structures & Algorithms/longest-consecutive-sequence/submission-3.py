class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we need to check if value - 1 is in the array.if not then that is the start of the array
        # we then move into the loop and find the + 1 till we can. and store the len.
        # we do this till we reach end of the array/
        num_set = set(nums)  
        res = 0

        for num in num_set:
            if (num - 1) not in num_set:  # start of sequence
                length = 1
                while (num + length) in num_set:
                    length += 1
                res = max(res, length)
        return res
