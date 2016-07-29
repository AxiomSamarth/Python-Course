#		This program will teach how to create a file

f = open('./files/fileCreated.txt','w')		#this will create a file named fileCreated

f.write('Lorem Ipsum and some randome text') #this will add content to it

f.close()


#	******************************************************************

#		If you use another f.write()  then the content will be overridden
#		and the previous content will be lost.

#		To avoid such a situation we use append mode to open file!			

#	******************************************************************
