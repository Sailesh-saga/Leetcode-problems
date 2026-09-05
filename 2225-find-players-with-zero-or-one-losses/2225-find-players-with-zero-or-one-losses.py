class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a=[]
        b=[]
        for i in range(len(matches)):
            a.append(matches[i][0])
        for i in range(len(matches)):
            b.append(matches[i][1])
        dict1={}
        dict2={}
        for i in a:
            dict1[i]=dict1.get(i,0)+1
        for i in b:
            dict2[i]=dict2.get(i,0)+1
        c=[]
        d=[]
        for i in dict1:
            if i not in dict2:
                c.append(i)
        c=sorted(c)
        for i in dict2:
            if dict2[i]==1:
                d.append(i)
        d=sorted(d)
        return [c,d]
        