#		This program will teach you how to read the list items using a 
#		for loop

l = []		#declare a list  as ' listname = [] '

for i in range(0,10):
	
	print 'l['+str(i)+'] : '
	
	l.append(int(input()))
	
print l
