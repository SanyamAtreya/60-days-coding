class Solution(object):
    def topKFrequent(self, nums, k):
        res={}
        lst=[]
        len_nums = len(nums)
        for i in range(len_nums):
            count=0
            for j in range(len_nums):
                

                if nums[i] == nums[j]:
                    
                    count+=1

            if nums[i] not in res:
                
                res[nums[i]]=count
        sort_data = sorted(res.items(), key=lambda x: x[1], reverse=True)
        
        for i in sort_data:
            
            if len(lst) < k:
                lst.append(i[0])

        return lst