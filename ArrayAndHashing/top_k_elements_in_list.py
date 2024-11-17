import sys
sys.path.append("..")
#import utilities
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

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def printLinkedList(firstNode: Node):
    if firstNode is None:
        print("Linked List: []")
        return

    current = firstNode
    message = "Linked List: ["
    while current is not None:
        message += str(current.data)  + ", "
        current = current.next

    if message != "Linked List: [":
        message = message[:-2]
    
    print(message + "]")
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        elementHash = {}

        for num in nums:
            elementHash[num] = elementHash.get(num, 0) + 1

        beforeFirst = None
        size = 0

        for num, count in elementHash.items():
            if beforeFirst is None:
                beforeFirst = Node(-1)
                beforeFirst.next = Node(num)
                size += 1
                continue
                        
            #print("> Step num:", num, " | count:", count)
            printLinkedList(beforeFirst.next)
            #print("Size ", size)
            
            added = False
            current = beforeFirst
            #print("Beginning with ", current.next.data)
            #print("placing ", num, " count: ", count, "...")
            for i in range(0, min(size, k)):
                #print(current.next.data)
                if count > elementHash[current.next.data]:
                    newNode = Node(num)

                    temp = current.next
                    current.next = newNode
                    newNode.next = temp                    

                    added = True
                    size += 1
                    break
                else:
                    current = current.next

            if size < k and not added:
                current.next = Node(num)
                size += 1
        
        res = []
        current = beforeFirst.next
        for i in range(0, min(size, k)):
            res.append(current.data)
            current = current.next

        return res
    
nums=[4,1,-1,2,-1,2,3]
k=2
res = Solution.topKFrequent({}, nums, k)
print("Result is ", res)