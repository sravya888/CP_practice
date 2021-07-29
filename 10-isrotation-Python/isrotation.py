# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	s=str(x)
	r=str(y)
	n=len(s)
	if s==r[::-1]:
		return True

	for i in range(n):
		x=s[i:n]+s[0:i]
		
		z=s[-i::]+s[:n-i]
		
		if x==r or z==r:


			return True
		
	return False
print(isrotation(12345,54321))

	
	
