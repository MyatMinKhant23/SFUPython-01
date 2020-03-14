def say_hello():
	print('Hello World')




say_hello()


#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b,'is maximum')

print_max(3,4)

def KFC():
	sale = 30000
	tax = 5 / 100
	total_tax = sale * tax
	total_price = sale + total_tax
	print(total_price)

#Local Variables

def func(x):
	print('x is', x)
	x = 2
	print('Changed local x to', x)

x = 50 
func(x)
print('x is still', x)

x = 30
def func(x):
	x = 2

def func(x)
	x = 10

#Global Statement

def func():
	global x

	print('x is ',x)
	x = 2
	print('Change global x to', x)

x = 50
func()
print('Value of x is',x)

def say(massage, time=1):
	print(message * times)

say('Hello')
say('World', 5)
say('Goodbye')



#Keyword Agrument

def func(a, b=5, c=10):
	print('a is ', a, 'and b is', b, 'and c is', c)

func(3, 8)
func(24, c=26)
func(c=29, a = 39)


#VarArgs parameters
#function_VArArgs.py

def total(a=5, *number, **phonebook):
	print('a',a)

	for single_item in numbers:
		print('single_item',single_item)

	for first_part,second_part in phonebook.items():
		print(first_part,second_part)

total(10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)

def maximum(x, y)
	if x > y:
		return x
	elif x == y:
		return 'The nubers are equal'
	else:
		return y

print(maximum(3,8))

print(maximum(20,10))

#DocString (Documentation Strings)

def mx(x):
	x = 50
	return x

x = 20
max(x)
pritn(max(x))


def print_max(x, y):
	'''Prints the maximum of two numbers 
		The Two Values must be integers.
	'''

	x = int(x)
	y = int(y)

	if x > y:
		print(x, 'is maximum')

	elif x < y:
		print(y, 'is maximum')
	else:
		print(x,'&',y,'is equal')

print_max(5,9)

print(print_max.__doc__)

def paper():
	'''1. There will e situatiiion where your 
	program has to interact with the user.
	For example, you would want to take input 
	from the user and then print some results 
	back. We can achieve thsi using the input()
	function and print function respectively.'''

	'''2. There will e situatiiion where your 
	program has to interact with the user.
	For example, you would want to take input 
	from the user and then print some results 
	back. We can achieve thsi using the input()
	function and print function respectively.'''

	print(paper.__doc__)