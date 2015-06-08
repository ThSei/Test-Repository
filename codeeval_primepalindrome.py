def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n < 2 or n % 2 == 0:
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		#print '\t', f
		if n % f == 0:
			return False
		if n % (f + 2) == 0:
			return False
		f += 6
	return True

# Addes ths comment, for using a test-branch
for num in range(1000, 3, -1):
#for num in range(100, 1001, 1):
#for num in range(1001):
	if str(num) == str(num)[::-1] and is_prime(num): 	#inverts the string
	#if str(num) == str(num)[::-1]: 	#inverts the string
		print num
		break;
