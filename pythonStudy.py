print '\n'*20

print '\n\n___________________________  lists'
x = [1, 2, 3]
x.append([4, 5]) # [1, 2, 3, [4, 5]]

y = [1, 2, 3]
y.extend([4, 5]) # [1, 2, 3, 4, 5]


print '\n\n___________________________  stack (with list)'
l = []
l.append(1)
l.append(2)
l.append(3)
print l  # [1, 2, 3]
print l.pop()  # 3, (last in)


print "\n\n___________________________ linked list (with list)"
l.insert(1, 1.5)  # [1, 1.5, 2]
print l
l.remove(1.5)  # [1, 2]
print l


print '\n\n___________________________   queue'
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print q.popleft()  # 'a',  (first in)


print '\n\n___________________________  dicts '
d = {'a':1, 'b':2, 'c':3}
d.update({'c':-1, 'd':4})   # {'a': 1, 'c': -1, 'b': 2, 'd': 4}

d = dict([('a',1), ('b',2)])  
print d # {'a':1, 'b':2}
print d.items() # [('a', 1), ('b', 2)]   # creates a tuple of items in memory!
print [(k, v) for k,v in d.iteritems()] # [('a', 1), ('b', 2)]   # uses a generator so may be cheaper!
print d.values() # [1, 2]


print '\n___________________________ functional methods'
print reduce(lambda x,y: x+y, [1,2,3,4,5,6,7,8,9,10])  # 55 
print map(int, ['1','2','3'])  # [1,2,3]
print filter(lambda x: x%2==0, range(10))  # [0, 2, 4, 6, 8]


print '\n\n___________________________ range vs xrange'
from timeit import timeit

# range has to create a list in memory which might be expensive!
print 'range took %s' % timeit('[i for i in  range(10000000) if False]', number=3) # 1.5s

# xrange evaluates lazily like a generator (isnt actually a generator)
print 'xrange took %s' %timeit('[i for i in xrange(10000000) if False]', number=3) # 1.0s



print '\n\n___________________________  Sorting'
from operator import itemgetter, attrgetter 

print sorted([('a',2), ('b', 1)], key=itemgetter(0))  # [('a', 2), ('b', 1)]
print sorted([('a',2), ('b', 1)], key=itemgetter(1))  # [('b', 1), ('a', 2)]


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
            return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('dave', 'B', 10),
    Student('jane', 'B', 12),
]

print sorted(student_objects, key=attrgetter('age'))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]



print '\n\n___________________________  staticmethod, classmethod and abstract methods'
import abc

class A(object):
	__metaclass__ = abc.ABCMeta

	def meth1(self):     # instance methods must have self instance as first arg
		print 'meth1'

	@staticmethod
	def meth2():         # @staticmethods can have no args at all
		print 'meth2'

	@classmethod
	def meth3(cls):    	 # @classmethod must have the class-object as first arg
		print cls == A 	 # True
		print cls == A() # False
		print 'meth3'

	@abc.abstractmethod
	def meth4(self):
		print 'meth4'


class B(A):

	def meth4(self, a):   # implementations of abstractmethods can change the argument list
		print 'meth4 overridden'

	def meth5(self):
		print 'meth5'

	@staticmethod
	def meth6():
		print 'meth6'

B().meth4(1)

class Third(B):
	def meth5(self):
		print 'meth5 overridden'



print '\n\n___________________________  multi arguments'

def meth7(**kargs):
	print isinstance(kargs, dict) # True
	print kargs['b']

meth7(a=1, b=2)  # 2

def meth8(*args):
	print isinstance(args, tuple) # True
	print args[1]

meth8(1,2)  # 2



print '\n\n___________________________  unpacking args'
def getThem(a,b,c,d,e):
   print a,b,c,d,e

mList = ['uno','dos','tres','cuatro','cinco']
getThem(*mList) # note the '*' to split the list in to arguments



print '\n\n___________________________  Iterators'
i = iter([1,2,3])

try:
	print i.next(), i.next(), i.next(), i.next()
except StopIteration:
	print 'iterator finished'


i2 = iter([1,2,3])
a,b,c = i2 # unpacking
print a,b,c 


class C(object):
	l = [1,2,3]
	def __init__(self):
		self.counter = 0

	def next(self):    # must be __next__ in python3
		if self.counter == len(C.l):
			raise StopIteration

		ans = C.l[self.counter]
		self.counter += 1
		return ans 

	def __iter__(self):
		return self


print '\n\n___________________________  list, tuple, dict, set can all take finite iterators'
print list(C())
print tuple(C())
print dict(zip(C(), C())) # {1: 1, 2: 2, 3: 3}
print set(C())

for i in C():   # note 'for' halts on StopIteration without errors
	print i

print [str(i) for i in C()] # List Comprehension - returns a list - ['1', '2', '3']

print (str(i) for i in C()) # Generator Expression - very different! returns a generator object - <generator object <genexpr> at 0x100697870>
print (str(i) for i in C()).next() # returns 1


print '\n\n___________________________  cartesian product'
seq1 = 'abc'
seq2 = (1,2,3)
print [(x, y) for x in seq1 for y in seq2]  


print '\n\n___________________________  Generators, (simple iterators using yield)'

def my_gen():
	for i in range(3):
		yield i

print my_gen().next() # note the generator returns the iterator, it is not an iterator itself
print list(my_gen())

Third().meth5()

def fibonoci_generator(n):
   a, b = 0, 1
   for i in range(n):
      yield a
      a, b = b, a+b

for item in fibonoci_generator(10):
   print item,   # 0 1 1 2 3 5 8 13 21 34 


print '\n\n___________________________  print types'
def f(): 
   pass
print type(f()) # <type 'NoneType'>
print type(1J) # <type 'Complex'>
print 1j*1j # (-1+0j)
print type(lambda:None) # <type 'function'>

def f():
    yield
def g():
    return
print f() # <generator object f at 0x100797910>
print g() # None


print '\n\n___________________________  dictionary comprehension'
print dict((k,k**3) for k in range(5))  # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print {k:k**3 for k in range(5)}  # same as above


print '\n\n___________________________  floor '
print 5//2 # 2


print '\n\n___________________________  id '
a = 'blah'
print id(a)  # 4302972800   , memory address
print hex(id(a))  # '0x1007a2780'  
print len(hex(id(a)).strip('0x')) * 16   # 128  , bits in the address space


print '\n\n___________________________  os.path'
import os
print os.path.isdir( os.listdir('.')[0] )  # True


print '\n\n___________________________  running shell commands'
import subprocess
subprocess.call(['uname', '-a'])  # note the i) the list, ii) does not return anything 


print '\n\n___________________________  logic precidence (1: Not, 2: And, 3: Or)'
print True or False and False # True
print not True or False or not False and True  # becomes - False or False or True and True = True


print '\n\n___________________________  custom decorators'
def tag(fn):
	def new(*args):
		return '{{' + fn(*args) + '}}'

	return new  # note returning method

@tag
def meth(s):
	return str(s)

print meth('asdf')


def doubleit(fn):
	def doubleit_inside(*args):
		return fn(*args )*2
	return doubleit_inside  # note returning method

@doubleit
def meth2(arg):
	return arg+1

print meth2(2)


print '\n\n___________________________  "with" manager '

with open('asdf.txt', 'w') as o:
	o.write('blah\nblah\nblah')

with open('asdf.txt', 'r') as o:
	text = o.readlines()
	for i in text:
		print i


print '\n\n___________________________  Pickle'
import pickle  # poor mans db

class Blah(object):
	def __init__(self, _amount):
		self.amount = _amount

b = Blah(700)
f = open('archive.pk', 'w')
pickle.dump(b, f)
f.close()

f = open('archive.pk', 'r')
r = pickle.load(f)
f.close()
print r.amount


print '\n\n___________________________  __dict__  get attributes by name and create new ones'
b.__dict__['total'] = 100
print b.__dict__ # {'amount': 700, 'total': 100}
print b.total # 100, note total was not defined in the original Blah class


print '\n\n___________________________  collections'
import collections
a = [10,30,50,70,70,30,40,30,10]
b = collections.Counter(a) # Counter({30: 3, 10: 2, 70: 2, 40: 1, 50: 1})
print b[30]  # 3 , occurances of 30
print b.most_common()[0] # (30, 3)


print '\n\n___________________________  defaultdict'
import collections
s = [('yellow', 1), ('yellow', 3), ('blue', 2), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
     d[k].append(v)  # no need to initialize a new value with a list
print d.items() # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]



print "\n\n___________________________ 2d Matrix of lists"

def matrix_build_and_print(listA, listB):
	width = len(listA)
	height = len(listB)

	m = [[col + row*width for col in range(width)] for row in range(height)]

	print m[0][0], m[height-1][width-1]
	print

	for row in range(height):
		for col in range(width):
			print m[row][col], 
		print


dates = range(1, 15) 
costs = [2, 7, 25]

matrix_build_and_print(dates, costs)


print '\n\n___________________________ list grouping'

from collections import defaultdict
d = defaultdict(list)
ll = [[1]]

for i in [2,3,4,5,11,12,25]:

    if i == ll[-1][-1] + 1:
        ll[-1].append(i)

    else:
        ll.append([i])

print ll



print '\n\n___________________________  threading'
""" the GIL makes this useless for CPU bound tasks!!! 
	useful for IO bound tasks.
	Consider the mutiprocessor library instead 
"""

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"

