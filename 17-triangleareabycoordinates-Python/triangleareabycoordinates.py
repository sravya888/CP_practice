# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	a=((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))
	a = a**0.5
	b=((x2-x3)**2)+((y2-y3)**2)
	c=((x3-x1)**2)+((y3-y1)**2)
	b = b**0.5
	c = c**0.5
	s=(a+b+c)/2
	area=(s*(s-a)*(s-b)*(s-c))**0.5
	return area