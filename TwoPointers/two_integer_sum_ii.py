import sys
sys.path.append("..")
from typing import List
import random

# Time complexity
#   Worst case :  O(n^2)

# Memory complexity
#   Worst case :  O(1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(0, len(numbers)):
            
            for j in range(0, i):
                if numbers[i] == numbers[j]:
                        return [j+1, i+1]
            
            numbers[i] = target - numbers[i]
        
        return [-1, -1]


# Time complexity
#   Worst case :  O(n^2)

# Memory complexity
#   Worst case :  O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1
        
        while left != right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]







# [1,2,3,4,5,6,7,8,9,10]
# [1,1,2,3,3,5,7,10,21]
# target = 12