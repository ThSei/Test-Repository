import sys

#e.g. x = 3
x = input("Divisor 1: ")

#e.g. y = 5
y = input("Divisor 2: ")

#e. g. nums = 17
nums = input("Bis: ")
for i in range(1, nums):
	#if i % 15 == 0:
	if i % x  == 0 and i % y == 0:
		print 'FB'
	#elif i % 3 == 0:
	elif i % x == 0:
		print 'F'
	#elif i % 5 == 0:
	elif i % y == 0:
		print 'B'
	else:
		print i
