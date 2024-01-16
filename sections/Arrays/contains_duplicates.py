

#contains duplicates:
from typing import List

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:      #bool return type lol
		numMap = {}                                      #a hashmap for items
		for i in nums:
			if i in numMap:
				return True
			else:
				numMap[i] = 1                            #accumulate unique elements
		return False



