

#kadane method , to look before you leap


class Solution():
	def maxSubArray(self,nums:list):
		n = len(nums)                #length is neccessary
		arr= []                      # a list to track record
		arr.append(nums[0])          #the first element, what we have
		max_sum = nums[0]            #the ultimate price
		for i in range(1,n):
			arr.append(max(arr[i-1]+nums[i],nums[i]))           #maximum of existing value and current iterated one

			if arr[i] > max_sum:                                #if the dummy array list ith element is greater than max_sum
				max_sum = arr[i]                                #max sum has a new value now
		return max_sum                                         #return the prize

	def testing(self,nums:list):
		pass


ab = Solution()
print(ab.maxSubArray([1,2,3,4,2,3,4,]))
print(ab.testing([1,2,3,4,2,3,4,]))
