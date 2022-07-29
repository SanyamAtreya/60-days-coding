class Solution(object):
    def twoSum(self, nums, target):
        
        hashmap = {}
        
            
        for index, value in enumerate(nums):
            
            difference = target - value
            
            if difference in hashmap:
                return [index, hashmap[difference]]
            
            hashmap[value] = index
            