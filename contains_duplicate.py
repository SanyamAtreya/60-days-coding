class Solution(object):
    def containsDuplicate(nums):
        if len(nums) != len(set(nums)):
            return True
        else:
            return False

    nums=[1,3,4,5,6,24,56,1]
    print(containsDuplicate(nums))
    