class Solution(object):
    def isPalindrome(self, s):
        l2 = ''.join(ch for ch in s if ch.isalnum())
      
        l2=l2.lower()
        # s.replace('a', '')
        r=len(l2)-1
        l=0
        pala=True
        while(l<=r):
            if(l2[l]!=l2[r]):
                pala=False
            l=l+1
            r=r-1
        return pala

























