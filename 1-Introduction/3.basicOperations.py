#this python program will show the mathematical operations on variabbles

a = 10
b = 20

sum = a + b
diff = a - b
prod = a * b
quo = a / b
mod = a % b

print 'The sum is ', sum
print '\nThe difference is ',diff
print '\nThe product is ',prod
print '\nThe quotient is ',quo
print '\nThe remainder is',mod

#inline operations can also be done and printed like below demo

print '\nThis is to demo inline operation'
print '\nThe sum is ',a+b


#	large expressions are simplified based on precedence and associativity

result = 5*10 + 15 - (15/3) % 10

print '\nThe result of the above expression evaluated based on precedence and associativity is',result
