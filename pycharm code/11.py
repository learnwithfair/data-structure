# Program for 0-1 Knapsack problem
def knapSack(W, wt, val, n):
	dp = [0 for i in range(W+1)] # Making the dp array

	for i in range(1, n+1): # taking first i elements
		for w in range(W, 0, -1): # starting from back,so that we also have data of
								# previous computation when taking i-1 items
			if wt[i-1] <= w:
				# finding the maximum value
				dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])

	return dp[W]


# Driver code
P = [15, 25, 13, 23]
wt = [2, 6, 12, 9]
C = 20
n = len(P)
print("Maximum Profit for 0/1 Knapsack Using Dynamic Programing is : ", knapSack(C,wt,P,n))
