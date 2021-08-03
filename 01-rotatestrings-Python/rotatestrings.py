# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def rotate(s,d):
	tmp = s[d:] + s[0:d]
	return tmp

def fun_rotatestrings(s, n):
	if n==0:
		return s
	elif n<0:
		n = abs(n)
		d = len(s) -n
		return rotate(s,len(s)-n)


	elif n > len(s):
		
		return rotate(s, n-5)
	else:
		return rotate(s,n)

	

