from typing import List
import random
import time

# Time complexity
#   Best case    : 
#   Average case : O(n^2)
#   Worst case   : O(n^2)

# Memory complexity
#   Best case    : O(1)
#   Average case : O(1)
#   Worst case   : O(1)

# brute force solution
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]


# jumpy solution
class SolutionJumpy:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort
        numsTuple = [(nums[i], i) for i in range(len(nums))]
        numsTuple = sorted(numsTuple,key=lambda tup: tup[0])

        initialJump = 1024*64
        print("Initial jump = ", initialJump)
        for i in range(len(numsTuple)):
            jump = initialJump
            j = i+1
            while j < len(numsTuple):
                sum = numsTuple[i][0] + numsTuple[j][0]

                numi = numsTuple[i][0]
                numj = numsTuple[j][0]

                if sum == target:
                    return [numsTuple[i][1], numsTuple[j][1]]
                elif sum < target:
                    j += jump
                else:
                    if jump == 1:
                        break
                    j -= jump
                    jump = round(jump / 2)

                # if the next jump is going over nums array, then iterate normally
                while j + jump >= len(numsTuple) and jump != 1:
                    jump = round(jump / 2)

        return [-1, -1]
    
class SolutionOnePass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i in range(len(nums)):
            firstNum = nums[i]
            secondNum = target - firstNum

            if secondNum in hashMap:
                return [i, hashMap[secondNum]]
            else:
                hashMap[firstNum] = i

        return [-1, -1]

print(random.seed())

size = 100000
print("Size of array is ", size)
nums = [random.randint(-10000000, 10000000) for _ in range(size)]

i = random.randint(0, size-1)
j = random.randint(0, size-1)
while (j == i):
    j = random.randint(0, size-1)

target = nums[i] + nums[j]
print("Target: ", target)
print("i: ", i) 
print("j: ", j) 

print("Brute force")
t = time.process_time_ns()
solution = SolutionBruteForce.twoSum({}, nums, target)
print((time.process_time_ns() - t)/1000000.0)
print("nums[", solution[0], "] + nums[", solution[1], "] == ", nums[solution[0]] + nums[solution[1]])

print("Jumpy")
t = time.process_time_ns()
solution = SolutionJumpy.twoSum({}, nums, target)
print((time.process_time_ns() - t)/1000000.0)
print("nums[", solution[0], "] + nums[", solution[1], "] == ", nums[solution[0]] + nums[solution[1]])

print("Onepass")
t = time.process_time_ns()
solution = SolutionOnePass.twoSum({}, nums, target)
print((time.process_time_ns() - t)/1000000.0)
print("nums[", solution[0], "] + nums[", solution[1], "] == ", nums[solution[0]] + nums[solution[1]])


