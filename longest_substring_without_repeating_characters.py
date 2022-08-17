class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = j = 0
        hset = set()
        res = 0

        while j < len(s):
            if s[j] in hset:
                hset.remove(s[i])
                i += 1
            else:
                hset.add(s[j])
                j += 1
                res = max(res, j - i)
        return res