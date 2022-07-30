class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = [["".join(sorted(list(strs[i]))),strs[i]] for i in range(len(strs))]
        dic = {}
        for i in L:
            if i[0] in dic.keys():
                dic[i[0]].append(i[1])
            else:
                dic[i[0]] = [i[1]]
        ans = []
        for i in dic.keys():
            ans.append(dic[i])
        return ans




# -------------------------------------------------------------------
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        final = []
        
        for i in strs:
            ans.append(''.join(sorted(i)))
            
        h = {}
        n = len(ans)
        
        for i in range(n):
            if ans[i] not in h:
                h[ans[i]] = [i]
            else:
                h[ans[i]] += [i]
            
        idx = []
        
        for i in h:
            idx.append(h[i])
        
        res = []
        
        for i in idx:
            temp = []
            for j in i:
                temp.append(strs[j])
            res.append(temp)
        
        return res