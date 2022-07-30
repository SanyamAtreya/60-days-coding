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