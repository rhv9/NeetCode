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



class SolutionCountHashed:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagramHash = {}

        for str in strs:
            strDict = {}
            for c in str:
                strDict[c] = strDict.get(c, 0) + 1
            
            found = False

            anagramList = anagramHash.get(len(str), [])

            for anagramTuple in anagramList:
                anagramMatches = True
                for c, count in strDict.items():
                    if anagramTuple[0].get(c, 0) != count:
                        anagramMatches = False
                        break

                if anagramMatches:
                    # Found the anagram
                    outputPointer = anagramTuple[1]
                    output[outputPointer].append(str)
                    found = True
                    break
            
            if not found:
                # add as sublist
                outputSublist = [str]
                output.append(outputSublist)
                newAnagramTuple = (strDict, len(output) - 1)

                if len(str) in anagramHash:
                    anagramHash[len(str)].append(newAnagramTuple)
                else:
                    anagramHash[len(str)] = [newAnagramTuple]
                
        return output
    
class SolutionArrayHash:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for str in strs:
            arrayDict = [0]*26

            for c in str:
                arrayDict[ord(c) - ord('a')] += 1
            
            tup = tuple(arrayDict)
            if tup in output:
                output[tup].append(str)
            else:
                output[tup] = [str]
            
        return output.values()



strs=["act","pots","tops","cat","stop","hat"]

solution = SolutionArrayHash.groupAnagrams({}, strs)
print("Solution: ", solution)