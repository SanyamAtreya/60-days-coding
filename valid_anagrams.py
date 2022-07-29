class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        
        count = collections.defaultdict(int)
        
        for val in s:
            count[val]+=1
        
        for val in t:
            count[val]-=1
            
        for item in count:
            if count[item] > 0:
                return False
            
        return True      
        