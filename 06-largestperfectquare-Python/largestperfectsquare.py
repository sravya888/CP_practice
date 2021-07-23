# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

def ismostlymagicsquare(arr):
    leftdiag=0
    rightdiag=0
    n=len(arr)
    for i in range(n):
        leftdiag +=arr[i][i]
        rightdiag+=arr[i][n-i-1]
    if leftdiag != rightdiag:
        return False
    
    
    for i in range(n):
        row=0
        col=0
        for j in range(n):
            row+=arr[i][i]
            col+=arr[j][i]
            
        if row!= leftdiag and col!=leftdiag:
            return False
    return True