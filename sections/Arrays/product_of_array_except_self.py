
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.



from typing import List          #List data type import
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)           #the length of the array
        pre_fix = 1             #prefixing from left to right , product of underlying left indices
        post_fix = 1
        result = [0] * n        #result output formulated to populate possible outcomes
        for i in range(n):
            result[i] = pre_fix           #prefix , which is multiplied by predeccessor
            pre_fix*=nums[i]

        for i in range(n-1,-1,-1):
            result[i] *= post_fix         #post_fix taking the numbers from the right except the present index
            post_fix *= nums[i]

        return result


ab  = Solution()
print(ab.productExceptSelf([1,2,3,4,5]))