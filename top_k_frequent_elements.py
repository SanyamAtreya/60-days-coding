class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)            
        h = []
        for i in c:
            heappush(h, (-c[i],i))
        res = []
        for i in range(k):
            kv = heappop(h)
            res.append(kv[1])
        return res