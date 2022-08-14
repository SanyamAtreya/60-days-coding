class Solution(object):
    def maxArea(self, height):
        ans = 0
        l=0
        r=len(height)-1
        
        while l < r:
            _h = min(height[l],height[r])
            _w = r-l
            ans = max(ans, _h * _w)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans