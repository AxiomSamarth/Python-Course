#		This program demonstrates the way of reading a matrix!

m = []

for i in range(0,3):
	
	l = []				# every row is a list
	
	for j in range(0,3):
		
		print 'm[',i,']','[',j,'] : '
		
		l.append(int(input()))
		
	m.append(l)			#append the list to the main list
		
print m		
	


# 		thus forming a list of list !
