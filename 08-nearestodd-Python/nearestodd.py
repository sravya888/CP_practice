# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.


import math
def fun_nearestodd(n):
	n=math.ceil(n)
	if n%2!=0:
		return (n)
	else:
		return (n-1)

	


