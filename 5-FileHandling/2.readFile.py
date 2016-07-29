#		This program will teach you how to read file !

f = open('./files/fileCreated.txt','r')

text = f.read()

print text

f.close()

#	******************************************************************

#		File handling is simple. Create the file object and open it
#		in required format and then access it using write(), read() methods		

#	******************************************************************
