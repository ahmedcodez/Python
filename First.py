# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:47:52 2019

@author: moizuddin
"""
print('Hello world'); #Print is a function in python 

#Comment --single line by #
"""
"Code tells you how, comments should tell you why."
Multi line comment like this 

"""

#Literal Constant 

#Only two types of number in python integer (int) and float 

a = 5
print (type(a))

b = 5.5
print(type(b))

#Strings -Sequence of characters

str1 = 'This is one way to specify' 
print(str1)

str2 = "The other way to specify "
print(str2)

str3 = '''This is a  third way or  multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.( when you have inner inverted commas)
He said "Bond, James Bond."
'''
print(str3)

#STRINGS ARE IMMUTABLE

#Example 

first_Name = 'BOND'
print(first_Name)
print (id(first_Name))

#Scenario 1
#first_Name[0] = 'D' 
#print(first_Name)


#Scenario 2

first_Name = 'JAMES'
print(first_Name)
print (id(first_Name))

first_Name = 'MY NAME IS' + ' ' + first_Name #Concatenation
print(first_Name)
print (id(first_Name))

'''
Uncomment to know strings are immuatble i.e you cant change once created.

But How does scenrio  works if strings are immutable ????

So, its variable pointing in different location(SEE ID() OF ALL THREE).
The value is not changing here,variable is changing.

'''
#USING PRINT AND FORMAT

empID = 554545
empName = 'JOHN SNOW'

#Multiple ways of printing

print (str(empID) + ' ' +'is the id of' +' '+ empName) 

'''Type conversion from int to str by str(int).
TypeError: unsupported operand type(s) for +: 'int' and 'str' 
'''

#Format method substitute the values with agrs given to it
print('{} is the id of {}'.format(empID,empName))

print('{0} is the id of {1}'.format(empID,empName))

print('{empID} is the id of {empName}'.format(empID= empID,empName=empName))

#Python3 version

print(f'{empID} is the id of {empName}')

#PRINT FACTS

print('apple') #ends with a newline character

print('mango',end=' ')
print('apple',end=' ')
print('banana',end=' \n')

#ESCAPE SEQUENCE

#print('what's your name?')

'''
Uncomment above line to know the problem
to use (') inside a print statement  so as to not to confuse python
A slash (\) is used and double slash (\\) '''

print('what\'s your name?')
print("what\\'s your name?")

print("Im done with strings.\nlets practice some variables and data types \t cool")


















