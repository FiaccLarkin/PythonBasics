

##################################################################
def quicksort(l):
	# O(nlog(n)) best/average but O(n^2) worst,  O(n) worse space
	if len(l) < 2: 		# Base case
		return l

	newL = l[1:]		# copy new list minus the pivot

	left = [x for x in newL if x   > l[0]]	 # find all items that should be on the left(right). 
	right  = [x for x in newL if x  <= l[0]]  #  NOTE '<='  # sorts decending

	return quicksort(left) + [l[0]] + quicksort(right) # recurse each side


##################################################################
class mergesort(object):
	# best/average/worse cases all O(nlog(n))
	# O(n) worse space 
	# lends itself well to parallelisation and has good locality of reference (good for memory access)
	# mergesort is stable unlike quick and heap sorts
	@staticmethod
	def mergesort(lst):
		if len(lst) < 2:
			return lst

		middle = len(lst) // 2
		left = mergesort.mergesort( lst[:middle] )
		right = mergesort.mergesort( lst[middle:] )

		return mergesort.merge(left, right)

	@staticmethod
	def merge(left, right):
		
		result = []

		lIx, rIx = 0,0
		while lIx < len(left) and rIx < len(right):
			
			if left[lIx] > right[rIx]:
				result.append(left[lIx])
				lIx += 1	
			else:
				result.append(right[rIx])
				rIx += 1

		if left:
			result.extend(left[lIx:])

		if right:
			result.extend(right[rIx:])
		return result


##################################################################
class heapsort(object):
	# Animation: cs.usfca.edu/~galles/visualization/HeapSort.html
	#
	# O(nlogn) complexity and O(1) space in all cases because its inplace. 
	# has better stats than quick/merge sorts with the tradeoff being heapsort
	# is a more complicated algorithm.
	#
	# Used for priority queues.
	#
	# A heap is an array used with the convention that left child of n is 2n+1,
	# right child is 2n+2 and both children are always less than the parent in value.
	# left and right children are not compared unlike a binary search tree.
	#
	# pythons supplied implementation is 'heapq' which unlike this implementation
	# is a min-heap (min at root)

	@staticmethod
	def heapsort(l):
		# First reheap all parents starting from the bottom of the tree
		lastParentIx = (len(l)-2)/2 # note the integer division which gives the floor
		for parentIx in range(lastParentIx, -1, -1):  # must include the root node 0 as an iteration 
			heapsort.siftDown(l, parentIx, len(l)-1)

		# Then we have to make another full pass 
		for ix in range(len(l)-1, 0, -1): # dont need to inlude the zero index this time
			l[ix], l[0] = l[0], l[ix]
			heapsort.siftDown(l, 0, ix-1)

		return l

	@staticmethod
	def siftDown(l, startIx, endIx):

		rootIx = startIx
		while True:

			childIx = 2*rootIx + 1 

			if childIx > endIx: break # base case

			if ((childIx+1) <= endIx) and (l[childIx+1] < l[childIx]):  
				childIx += 1  # use the larger child

			if l[childIx] < l[rootIx]: 
				l[childIx], l[rootIx] = l[rootIx], l[childIx]  
				rootIx = childIx # swap them and keep going
			else:
				break # otherwise rootIx has reached its spot





##################################################################
##################################################################
def tester(sortMethod):
	print sortMethod.__name__
	correct = list(reversed(range(10) + [9])) # [9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	jumbled  =  list(reversed(correct))       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
	assert sortMethod(jumbled) == correct, (sortMethod(jumbled), correct)
	assert sortMethod([]) == []
	assert sortMethod([1]) == [1]


tester(quicksort)
tester(heapsort.heapsort)
tester(mergesort.mergesort)


print "all passed"


