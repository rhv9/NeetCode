class Solution:
    def FirstSolution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCharCount = {}
        for l in s:
            if l in sCharCount:
                sCharCount[l]+=1
            else:
                sCharCount[l] = 0
        
        tCharCount = {}
        for l in t:
            if l in tCharCount:
                tCharCount[l]+=1
            else:
                tCharCount[l] = 0

        return sCharCount == tCharCount
    