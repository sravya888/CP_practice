# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n,k,d):
	temp = 0
	if n < 0:
		temp = 1
	n = abs(n)
	n = str(n)
	n = n[::-1]
	d = str(d)
	p = n[:k]
	q = n[k+1:]
	z = p+d+q
	z = z[::-1]
	z = int(z)
	if temp == 1:
		return -z
	else:
		return z
