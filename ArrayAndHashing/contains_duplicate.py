from typing import List

# O(n*m)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foundSet = set();

        i = 0
        for x in nums:
            i+=1
            foundSet.add(x) # O(m) where m is size of foundSet
            if len(foundSet) != i:
                return True

        return False;

Solution.hasDuplicate({}, [1,2,3,4]);