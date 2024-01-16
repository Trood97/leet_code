

class Solution:
	def maxprofit(self,prices:list)->int:
		min_price = prices[0]       #initalising the initial price to compare and change
		max_profit = 0              #ultimate goal , setting 0 as a tradition
		for price in prices[1:]:
			max_profit = max(max_profit,price-min_price)          #maximum of current, anticipated
			min_price= min(min_price,price)                       #next minimum stock price

		return max_profit

