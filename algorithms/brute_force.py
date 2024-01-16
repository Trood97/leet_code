from typing import List

''' One brute force approach is to consider every pair of elements and check if their sum equals the target. This can
be done using nested loops, where the outer loop iterates from the first element to the second-to-last element,
and the inner loop iterates from the next element to the last element. However, this approach has a time complexity
of O(n^2). '''

"time complexity = O(n^2)"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found


class my_solution:
    def method_1(self,num:List[int],target:int)-> List[int]:
        for i in range(len(num)-1):
            for j in (range(i+1,len(num))):
                if num[i] + num[j] == target:
                    return [i,j]
        else:
            return []


# obj = my_solution()
# print(obj.method_1([1,2,3,4],4))

