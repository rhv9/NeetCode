# Time complexity
#   Best case    : 
#   Average case : 
#   Worst case   : O(s + t)

# Memory complexity
#   Best case    : 
#   Average case : 
#   Worst case   : O(s + t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict: dict = dict()
        tdict: dict = dict()

        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1

        for c in sdict.keys():
            if sdict[c] != tdict.get(c, 0):
                return False
            
        return True

# Time complexity
#   Best case    : 
#   Average case : O(n logn)
#   Worst case   : O(n logn)

# Memory complexity
#   Best case    : 
#   Average case : 
#   Worst case   : TODO: Does sorted use extra memory to sort or is it O(1). 
#                  Use O(1) memory complexity sorting algorithm to do such.
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

# This is equivalent and still as efficient as og Solution2 because of lazy boolean evaluation.
class Solution2OneLine:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)