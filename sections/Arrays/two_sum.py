from typing import List
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class two_sum:
	def brute_force(self,l:List[int],target:int) -> List[int]:
		n = len(l)                     #first step is to know the length of the string, handy data
		for i in range(n-1):           #range - follows the index number ruling
			for j in range(i+1,n):     #range - forcing the indexing from the next element to the last element , len(n) - autonomous
				if l[i] + l[j] == target:
					return [i,j]

		return []


	def two_pass_hash_table(self,l:List[int],target:int) -> List[int]:
		n = len(l)
		numMap = {}
		for i in range(n):
			numMap[l[i]] = i     #first create a hashmap for reference

		for i in range(n):
			compliment = target - l[i]             #simple algebra to find the remaining one out
			if compliment in numMap and numMap[compliment] !=i:           #if block to make sure and not pointing to the same index
				return [i,numMap[compliment]]
		return []


	def one_pass_hash_table(self,l:List[int],target:int)->List[int]:
		numMap = {}
		n = len(l)
		for i in range(n):                         #just one pass to settle the deal, just a mercedes thing
			compliment = target - l[i]
			if compliment in numMap:               #to check if the compliment is present
				return [numMap[compliment],i]
			numMap[l[i]] = i                       #add it to the hashmap!

		return []



# ab = two_sum()
# print(ab.brute_force([1,2,3,4,5],9))
# print(ab.two_pass_hash_table([1,2,3,4,5],9))
# print(ab.one_pass_hash_table([1,2,3,4,5],9))