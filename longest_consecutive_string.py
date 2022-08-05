class Solution(object):
    def longestConsecutive(self, nums):  
        s = set(nums)
        long=0 # keeping track of longest sequence
        for i in nums:
            if (i-1) not in s:
                l = 0
                while (i+l) in s:
                    l+=1
                long = max(l,long)
        return long