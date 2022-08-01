class Solution(object):
    def productExceptSelf(self, nums):
        left = [0]*len(nums)
        left[0] = nums[0]
        for i in range(1,len(nums)):
            left[i] = nums[i] * left[i-2]

        p = nums[-1]
        nums[-1] = left[(len(left) - 2)]
        j = len(nums)-2
        while j>0:
            k = nums[j]
            nums[j] = left[j-1]*p
            p = p*k
            j -= 1
        nums[0] = p
        return nums