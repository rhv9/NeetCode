import sys
sys.path.append("..")
#import utilities
from typing import List
import random

# Time complexity
#   Best case    : 
#   Average case : 
#   Worst case   : O(n) where n is length of str

# Memory complexity
#   Best case    : 
#   Average case : 
#   Worst case   : 

def isAlpha(char):
    c = ord(char)
    return (c >= ord('0') and c <= ord('9') or 
            c >= ord('A') and c <= ord('Z') or 
            c >= ord('a') and c <= ord('z'))

def lower(char):
    c = ord(char)
    if c >= ord('A') and c <= ord('Z'):
        return chr(c + ord('a') - ord('A'))
    else:
        return char
    


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlpha(s[l]):
                l += 1

            while l < r and not isAlpha(s[r]):
                r += -1

            if lower(s[l]) != lower(s[r]):
                return False
            
            l += 1
            r += -1
        
        return True
    

sol = Solution.isPalindrome({}, ".,")
print(sol)
            

