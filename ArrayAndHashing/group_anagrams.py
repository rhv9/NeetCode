import sys
sys.path.append("..")
import utilities
from typing import List
import random

# Time complexity
#   Best case    : 
#   Average case : 
#   Worst case   : 

# Memory complexity
#   Best case    : 
#   Average case : 
#   Worst case   : 

class SolutionIterative:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagramList = []

        for str in strs:
            strDict = {}
            strLen = len(str)
            for c in str:
                strDict[c] = strDict.get(c, 0) + 1
            
            found = False
            for anagramTuple in anagramList:
                foundAnagram = False

                if anagramTuple[1] == strLen: 
                    anagramMatches = True
                    for c, count in strDict.items():
                        if anagramTuple[0].get(c, 0) != count:
                            anagramMatches = False
                            break

                    if anagramMatches:
                        foundAnagram = True
                        
                if foundAnagram:
                    # Found the anagram
                    outputPointer = anagramTuple[2]
                    output[outputPointer].append(str)
                    found = True
                    break
            
            if not found:
                # add as sublist
                sublist = [str]
                output.append(sublist)
                newAnagramTuple = (strDict, strLen, len(output) - 1)
                anagramList.append(newAnagramTuple)
                
        return output

strs=["act","pots","tops","cat","stop","hat"]

solution = SolutionIterative.groupAnagrams({}, strs)
print("Solution: ", solution)