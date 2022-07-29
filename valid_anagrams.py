class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        #Declaring dictionary to store count  
        count = collections.defaultdict(int)
        
        #Taking the count of the characters in the first string
        for val in s:
            count[val]+=1
        
        #Iterating the charaters from the second string and reducing the count
        for val in t:
            count[val]-=1
            
        #Iterating over dictionary
        for item in count:
            #If count is having non zero then return False
            if count[item] > 0:
                return False
            
        #All good, returning True
        return True      
        