# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(a, b, c):
	s=(a+b+c)/2
	area=((s-a)*(s-b)*(s-c)*s)**0.5
	return area

