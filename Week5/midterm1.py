PYTHON

How the class statement works.
	#inheritance
	class Scary:
		def __init__(self, name):
			self.__name = name
		def getName(self):
			return self.__name

	class Alive(Scary):
		def __init__(self, name, aliveness):
			Scary.__init__(self, name)
			self.__aliveness = aliveness
			def getAliveness(self):
				return self.__aliveness

	class Dead(Scary):
		def __init__(self, name, deadness):
			Scary.__init__(self, name)
			self.__deadness = deadness
			def getDeadness(self):
				return self.__deadness

	#multiple inheritance
	class AliveAndDead(Alive, Dead): #order of parameters matters
		def __init__(self, name, aliveness, deadness):
			Alive.__init__(self, name, aliveness)
			Dead.__init__(self, name, deadness)

How the def statement works (with functions and methods).

How the for statement works (with lists, strings, and tuples).

	for letter in 'Python':     # First Example
	   print('Current Letter :', letter)


How the if–elif–else statement works.

How the import statement works.
	If you have a file called file.py, you can call
		import file
	to import the file.

How the while statement works.
	while b < n:
        print(b, end=' ')
        a, b = b, a+b

How the raise statement works.
	raise Exception('An error occured.')

How the return statement works.

How Booleans, dictionaries, integers, lists, reals, strings, and tuples work.
	
	#dictionary
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

	dict['Age'] = 8; # update existing entry
	dict['School'] = "DPS School"; # Add new entry


	print "dict['Age']: ", dict['Age']
	print "dict['School']: ", dict['School']

	#another dictionary
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

	del dict['Name']; # remove entry with key 'Name'
	dict.clear();     # remove all entries in dict
	del dict ;        # delete entire dictionary

	print "dict['Age']: ", dict['Age']
	print "dict['School']: ", dict['School']

	#tuples
	tup1 = ()
	tup1 = (50,)
	tup1 = ('physics', 'chemistry', 1997, 2000);
	tup2 = (1, 2, 3, 4, 5, 6, 7 );

	print "tup1[0]: ", tup1[0]
	print "tup2[1:5]: ", tup2[1:5]
		Which outputs:
		tup1[0]:  physics
		tup2[1:5]:  [2, 3, 4, 5]


How the constants None, False, and True work.

How to make lists with [].

How to make tuples with ().

How to make dictionaries with {}.

How the arithmetic operators +, −, *, and / work.

How the boolean operators and, not, and or work.

How the relational operators ==, !=, <, >, <=, and >= work.

How the functions len and str work.

How the assignment operator = works.

How to call functions and methods.

How to write a method that returns a value.

How to write a method that does not return a value.

How lambda expressions work. / How the higher-order functions filter, map, and reduce work.
	names = ['Tarzan', 'Peter Pan', 'Prince', 'Adam Smith']
	oneNamed = filter((lambda name: not(' ' in name)), names)
	print(oneNamed)
	howMany = len(oneNamed)
	lengths = map((lambda name: len(name)), oneNamed)
	sumOfLengths = reduce((lambda first, rest: first + rest), lengths, 0)
	average = sumOfLengths / howMany

	MAP: applies a function to all the items in an input_list.
	items = [1, 2, 3, 4, 5]
	squared = list(map(lambda x: x**2, items)) 
	//returns [1, 4, 9, 16, 25]

	FILTER: creates a list of elements for which a function returns true. 
	number_list = range(-5, 5)
	less_than_zero = list(filter(lambda x: x < 0, number_list))
	print(less_than_zero) 
	# Output: [-5, -4, -3, -2, -1]

	REDUCE:
	from functools import reduce
	product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
	# Output: 24


How to access dictionaries, lists, strings, and tuples with [].

How the . (dot) operator works with class instances.
	monster = Alive("Frankenstien's Monster", 85)
	wolfman = Alive("Wolfman", 100)
	monster.getName()
	monster.getAliveness()
	ghost = Dead('Casper', 100)
	mummy = Dead('Imhotep', 50)
	mummy.getName()
	mummy.getDeadness()
	vampire = AliveAndDead('Dracula', 50, 50)
	vampire.getAliveness()
	vampire.getDeadness()

How variables work with classes, functions, and methods.

How self works with classes and their methods.




Lab 1:
{
	import types
def left(e):
    return e[0]

def op(e):
    return e[1]

def right(e):
    return e[2]

def isInside(v, e):
    if v==e:
        return True
    elif type(e)!=types.TupleType:
        return False
    elif isInside(v, left(e)):
        return True
    elif isInside(v, right(e)):
        return True
    else:
        return False

def solvingAdd(v, q):
    if isInside(v, left(left(q))):
        return solving(v, (left(left(q)), '=', (right(q), '-', right(left(q)))))
    else:
        return solving(v,(right(left(q)), '=', (right(q), '-', left(left(q)))))

def solvingSubtract(v, q):
    if isInside(v, left(left(q))):
        return solving(v, (left(left(q)), '=', (right(q), '+', right(left(q)))))
    else:
        return solving(v,(right(left(q)), '=', left(left(q)), '-', right(q)))

def solvingMulitply(v, q):
    if isInside(v, left(left(q))):
        return solving(v, (left(left(q)), '=', (right(q), '/', right(left(q)))))
    else:
        return solving(v,(right(left(q)), '=', (right(q), '/', left(left(q)))))

def solvingDivide(v, q):
    if isInside(v, left(left(q))):
        return solving(v, (left(left(q)), '=', (right(q), '*', right(left(q)))))
    else:
        return solving(v,(right(left(q)), '=', left(left(q)), '/', right(q)))



def solve(v, q):
    if isInside(v, left(q)):
        return solving(v, q)
    if isInside(v, right(q)):
        r = (right(q), op(q), left(q))
        return solving(v, r)
    else:
       return None

def solving(v, q):
    if left(q) == v:
        return q
    elif op(left(q)) == '+':
        return solvingAdd(v, q)
    elif op(left(q)) == '-':
        return solvingSubtract(v, q)
    elif op(left(q)) == '*':
        return solvingMulitply(v, q)
    else:
        return solvingDivide(v, q)

}






Lab 2:
{
	class Zillion:
	def __init__(self, digits):
		hasDigit = False
		badChar = False
		for d in digits:
			if d == '0' or d == '1' or d == '2' or d == '3' or d == '4' or d == '5' or d == '6' or d == '7' or d == '8' or d == '9':
				hasDigit = True
			else:
				if d != ' ' and d != ',':
					badChar = True
		if hasDigit == False or badChar == True:
			raise RuntimeError
		self.numList = []
		for d in digits:
			if d == '0' or d == '1' or d == '2' or d == '3' or d == '4' or d == '5' or d == '6' or d == '7' or d == '8' or d == '9':
				self.numList += [int(d)]
	def increment(self):
		n = 1
		while self.numList[len(self.numList)-n] == 9:
			self.numList[len(self.numList)-n] = 0
			n += 1
		if len(self.numList)-n >= 0:
			self.numList[len(self.numList)-n] += 1
		else:
			self.numList = [1] + self.numList
	def isZero(self):
		for d in self.numList:
			if d != 0:
				return False
		return True
	def toString(self):
		text = ''
		for d in self.numList:
			text += str(d)
		return text
}





Lab 3
{
	def sigma(F, B, E):
	if B > E:
		return 0
	return F(B) + sigma(F, B+1, E)

def numTrue(P, S):
	if S == []:
		return 0
	elif P(S[0]):
		return 1 + numTrue(P, S[1:len(S)])
	else:
		return numTrue(P, S[1:len(S)])

def numFalse(P, S):
	if S == []:
		return 0
	elif P(S[0]):
		return numFalse(P, S[1:len(S)])
	else:
		return 1 + numFalse(P, S[1:len(S)])

def most(P, S):
	if numTrue(P, S) > numFalse(P, S):
		return True
	else:
		return False
}