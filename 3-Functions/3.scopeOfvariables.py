#	This program will show you different scope of variables  

def function():
	
	a = 10
	
	print 'Value of variable \'a\' in function is',a
	
a = 100

function()

print '\nValue of variable \'a\' in function is',a



#	********************************************************************

#		The variable inside the function is local to the function and is 
#		not accessed outside the function. 

#		The variable outside the function is called global variable and
#		is visible throughout the program.

#		Inorder to access that variable within the function then
#		we must prefix the variable with the keyword 'global' as
#		'global a'

#	********************************************************************
