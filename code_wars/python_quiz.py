def q1():
	print("hello" * 5)

# hellohellohellohellohello

def q2():
	x, y = 4, 5
	y, x = x, y
	print(x)
	print(y)

# x= 5 y = 4

def q3():
	z = 9
	lst = [0] * z
	print(lst[:-1])

# [0, ...8 times]

def q4():
	def help(x):
		return x % 2 == 0

	lst = [i**2 for i in range(10)]
	lst = filter(help, lst)
	print(list(lst)[::2])
'''
25 lst = [0,1,4,9,16,25,36,49,64,81]
26 lst = [0,4,16,36,64]
27 [0,16,64]
'''


def q5():
	z = 0
	for i in range(1, 10):
		if (i + 1 // 2) % 7 == 0:
			break
		else:
			z += int(i % 2 == 0) #int(False) -> 0 int(True) -> 1
			print(z)
	else:
		print('end')

'''
// is the floor division operator. 9//2 would be 4 because 2*4 is 8 which is the last whole number before 9
the floor operator is going to be processed first. 1//2 = 0 so it was meant to through you off it could have been
written (i + (1//2)) so its really just i + 0 which is just i.  this means it will iterate until it gets to 7 then 
7%7 == 0. that will cause it to break and will not trigger the else in the for else syntax.

in for else if the for loop does not break else executes. however if it does break then it doesnt execute else

line 41 this is a bolean int statement. if the stament is true it adds 1 if it is false it adds 0.
output is 0, because 1, 1, 2, 2, 3 break
'''

def q6():
	import math

	for i in range(1, 100):
		if math.sqrt(i) == (i - 5)**2:
			print(i)
			break
	else:
		print('no')

'''
    there is not a number between 1 and 99 that meets the criteria of the if.
    ex->  sqrt of 9 is 3. 9-5 = 4 4**2 = 16
    this reaches the else and prints no
'''

def q7():
	class A:
		def __init__(self, x):
			self.x = x

		def __eq__(self, o):
			return self.x == o.x  #this is really a.__eq__(b) so is a == b


	a = A(2)
	b = A(2)
	print(a == b)
	print(a is b)
	print(b is a)
	print(a is a)
	print(a == a)

'''
the init method defines the attribute so x = 2 the eq method compares if they are equal so o = 2
it will compare is o is equal to x.
 a == b is true because 2 = 2
 a is b false because it is comparing memory locations so even though they have same numeric value they are different
 b is a false for same reason
 a is a true because they are held in the same memory location
 a == a true because they are same numeric value
'''

def q8():
	class A:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def print(self):
			print(self.x, self.y)

	class B(A):
		def print(self):
			print(self.y, self.x)

	class C(B):
		def __init__(self, x, y, z):
			super().__init__(x, y)
			self.z = z

	d = A(2, 4)
	e = B(4, 5)
	g = C( 3, 4, 7)
	g.x = g.z
	d.print()  #(2, 4)
	e.print()  #(5, 4)
	g.print()  #(4, 7)
'''
    on the last one the 3 is removed because it was overridden to z which is 7 which would make it print (7,4,7)
     c is only asking us to print x and y which is (7,4) but because B switches x and y to (y, x) it makes it (4,7)
'''

def q9():
	def x(z):
		def q(x, y):
			x = y + z + x
			print(x)

		return q

	for i in range(10):
		func = x(i)
		func(i, i-1)
'''
first iteration
0
func z = 0
func(x = 0, y = 0 -1)
x =-1 + 0 + 0  output 1

1
func = 1
func(x = 1, y = 1 - 1)
x = 0 + 1 + 1 output 2

'''

def q10():
	def d(f):
		def w(*args, **kwargs):
			r = f(*args, **kwargs)
			r += 1
			return r

		return w

	@d
	def a(x):
		return x + 1

	print(a(5))

'''
look up decorator function (denoted with @) its taking a function that returns another function
this was pretty complicated but at the end of the day function a takes an input x so 5
5+ 1 = 6 so that makes r = 6 and finally 6+1 = 7
'''

def q11():
	print(*list(map(lambda x: chr(ord(x) + 1), ["a", "b", "c"])))


def q12():
	x = 0.1
	y = 0.10000000000000001
	print(x == y)
'''
this actually returns true because even though they are different in python decimals get crazy so because they were the
same for so long it just rounds off the end so pyton processes .1 = .1 true
'''

def q13():
	x = [True, 1, "a", "b", "2"]
	print(any(x))

'''
any looks through a list and if anything is true it returns true and false if nothing returns true
'''

def q14():
	x = ["a", 1, 2, 3, 4]
	y = z = x
	z[1] = 7
	y[3] = 2
	x[2] = 9
	print(x)
	print(y)
	print(z)
'''
all three print statements will be ["a", 7, 9, 2, 4] 
y = z = x basically means we are all pointing to the same list so if we change one  element of one list it will change
for all three
'''

def q15():
	print(1 == True)
	print("1" == 1)
 '''
 the first one is true because it treats them as the same
 false because they are found in different memory slots
'''
def q16():
	x = b'1001'
	y = b'1010'
	z = x + y
	print(z)
'''
the difference is the b is before the' it means it is a byte string
this is saying they are byte strings so its concatonating both of them to "10011010"
'''

def q17():
	x = 0b1001 #this is 9 in binary
	y = 0b1010 #this is 10 in binary
	z = x + y
	print(z)
#output is 19