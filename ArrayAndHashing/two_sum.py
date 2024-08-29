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
        nums = sorted(nums)

        initialJump = 16
        for i in range(len(nums)):
            jump = initialJump
            j = i+1
            while j < len(nums):
                sum = nums[i] + nums[j]

                numi = nums[i]
                numj = nums[j]

                if sum == target:
                    return [i, j]
                elif sum < target:
                    j += jump
                else:
                    if jump == 1:
                        break
                    j -= jump
                    jump = 1

                # if the next jump is going over nums array, then iterate normally
                if j + jump >= len(nums):
                    jump = 1

        return [-1, -1]


random.seed(0)

size = 100000
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


