
'''A more efficient approach is to use a hash table (unordered_map in C++). We can iterate through the array once,
and for each element, check if the target minus the current element exists in the hash table. If it does,
we have found a valid pair of numbers. If not, we add the current element to the hash table. '''

'''Approach using a hash table:

Create an empty hash table to store elements and their indices.
Iterate through the array from left to right.
For each element nums[i], calculate the complement by subtracting it from the target: complement = target - nums[i].
Check if the complement exists in the hash table. If it does, we have found a solution.
If the complement does not exist in the hash table, add the current element nums[i] to the hash table with its index as the value.
Repeat steps 3-5 until we find a solution or reach the end of the array.
If no solution is found, return an empty array or an appropriate indicator.'''

"Time complexity = O(n)"
from typing import List

#Two pass Hash-map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found

class my_solution:
    def method_hash(self,num:List[int],target:int)->List[int]:
        n = len(num)
        numMap = {}
        for i in range(n):
            numMap[num[i]] = i

        for i in range(n):
            complement = target - num[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []

# obj = my_solution()
# print(obj.method_hash([1,2,3,4],4))  #it works

#One pass Hash-Map
class Solution_onepass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found

class my_solution_onepass:
    def method_onepass(self,nums:List[int],target:int)-> List[int]:
        n = len(nums)
        numMap = {}
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]] = i

        return []

# obj2 = my_solution_onepass()
# print(obj2.method_onepass([1,2,3,4,5],800))  #it is working