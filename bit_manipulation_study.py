

print bin(16)  # '0b10000'   dec -> bin
print int(bin(16), 2)  # 16    bin -> dec

print hex(43981)  # '0xabcd'   dec -> hex
print int(hex(43981), 16)  # 43981   hex -> dec

print '\n________________iterative binary conversion'
def my_bin(n):
	i = 1<<7
	while i>0:
		print '1' if (i&n==i) else '0', 
		i >>= 1
	print '\n'

my_bin(11)  # 0 0 0 0 1 0 1 1 
my_bin(-3)  # 1 1 1 1 1 1 0 1  # works correctly for negatives!

print '\n________________recursive binary conversion 1'
def my_bin(dec_int):
	return str(dec_int) if dec_int <= 1 else my_bin(dec_int>>1) + str(dec_int & 1)

# doesn't work on negatives !
print my_bin(15)  # 1111
print '0b' + my_bin(15) == bin(15) #  True

print '\n________________recursive binary conversion 2'
# doesn't work on negatives !
def my_bin(n):
    if n > 1:
        my_bin(n/2)
 
    print "%d"% (n % 2.0), 

my_bin(11)


print '\n________________O(N) length of bit sequence,  use (n).bit_length()'
def counter(dec_int):
	count = 0 
	while(dec_int > 0):
		count += 1
		dec_int >>= 1

	return count

print counter(9)  # 4

import timeit
print "counter method takes %s" % timeit.timeit('counter(10)', 'from __main__ import counter')  # 0.4 seconds
print "bit_length method takes %s" % timeit.timeit('(10).bit_length()')  # 0.06 seconds


print '\n________________sub O(n) number of bits set'
def bits_set(dec_int):
	count = 0
	while(dec_int > 0):
		dec_int &= dec_int - 1
		count += 1

	return count

print bits_set(9)


print '\n________________bits count odd'
print 43 & 1 == 1# & with 1 to check if any number is odd
print bits_set(9) & 1  # 0
print bits_set(7) & 1  # 1


print '\n________________bit flipping'
i = 9
bin((i ^ (2 ** (i.bit_length()+1) - 1)))[3:]


print '\n________________get only the rightmost set bit'
print bin(14 & -14)  # '0b10'

def lowestSetIndex(int_type):
    low = (int_type & -int_type)
    lowBit = -1
    while (low):
        low >>= 1
        lowBit += 1
    return(lowBit)

print 'lowbit %s' % lowestSetIndex(8)



# testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
def testBit(int_type, offset):
    mask = 1 << offset
    return (int_type & mask)==mask

# setBit() returns an integer with the bit at 'offset' set to 1.
def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

# clearBit() returns an integer with the bit at 'offset' cleared.
def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

# getting the inverse of a mask
# dec 4   = 0100 
# ~4 = -5 = 1011    
# not python's bin wont show this, only 1s comp


# toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)


print testBit(10, 0)  # False
print testBit(10, 1)  # True
print bin(setBit(8, 0))  # 0b1001
print bin(clearBit(15, 3))  # 0b111
print bin(toggleBit(3, 0))  # 0b10


print "\n________________twos complement, the complement is alway one larger when comparing absolutes"
# signed ranges go from -128 -> 127
# 2s comp allows for addition/subtractions with mix signs naturally 
print  ~5 == -6  # True
print -8 == ~7  # True


print "\n________________prefilled numbers"
bin(int('aaaaaaaa', 16))  # '0b10101010101010101010101010101010'  # can be ANDed to give even values
bin(int('55555555', 16))  # '0b1010101010101010101010101010101  # can be ANDed to give odd values


print "\n________________ get binary number of all 1's"
print bin((1 << 5) -1 )  # gives 11111 (note there are 5 not 4)


print "\n________________find the only single occuring element"
def find(lst):
    ones = 0
    twos = 0
    for x in lst:
        twos |= ones & x
        ones ^= x
        not_threes = ~(ones & twos)
        ones &= not_threes
        twos &= not_threes
    return ones
print find([2,1,4,5,1,4,2,2,4,1])



print "\n________________ rotation shifts"

def rotateLeft(n, d, int_bit):
	int_bit_mask = (1<<int_bit)-1  # use to cut off overflow
	left = (n << d) & int_bit_mask
	right = (n >> (int_bit - d)) & int_bit_mask
	return bin(left | right)

print rotateLeft(11, 3, 4)


print "\n________________ find the next 'sparse' number (no consequtive digits)"

# cascade any grouped pairs by adding one to that pair
# you may have to repeat the process if the cascade caused another pair of adjacent 1's

"""
0000000  0
0000001  1
0000010  2
0000011  3  *
0000100  4
0000101  5
0000110  6  *
0000111  7  *
0001000  8
0001001  9
0001010  10
0001011  11 *
0001100  12 *
0001101  13 *
0001110  14 *
0001111  15 *
0010000  16
0010001  17
0010010  18
0010011  19 *
0010100  20
0010101  21
0010110  22 *
0010111  23 *
0011000  24 *
0011001  25 *
0011010  26 *
0011011  27 *
0011100  28 *
0011101  29 *
0011110  30 *
"""
