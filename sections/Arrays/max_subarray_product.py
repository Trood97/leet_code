

class Solution():
	def maxProduct(self,nums:list):
		n = len(nums)
		result = nums[0]
		max_product,min_product = result,result

		for i in range(1,n):

			if nums[i]<0:
				max_product,min_product = min_product,max_product

			max_product = max(nums[i]*max_product,max_product)
			min_product = min(nums[i]*min_product,min_product)

			result = max(result, max_product)

		return result
