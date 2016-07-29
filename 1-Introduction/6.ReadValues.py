#this program will demonstrate how to input a value from the terminal




a = raw_input('Enter the value of varible a :')

print '\nThe value of a as entered is',a

b = input('\nEnter the value of b :')

print '\nThe value of b is ',b




#	********************************************************************

#		the raw_input() takes the input in the form of strings  
#		but input() function takes 
#		only numbers as input from the terminal

#		it is a good practice to typecast the input functions 
#		at the time of input like below

#	********************************************************************

c = int(input('\nEnter the integer value for c : '))
print '\nThe value of c is',c

d = str(raw_input('\nEnter the string :')) #note that raw_input() is used
print '\nThe string is',d


