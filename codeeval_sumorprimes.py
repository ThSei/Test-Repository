'''
def is_Prime(n):
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
'''
def is_Prime(x):
	if x<2:
		return False
	if x==2:
		return True
	if x%2==0:
		return False
	for i in range(3,int(round(x**0.5))+1,2):
		if x%i==0:
			return False
	else:
		return True
'''
sum = 0    
for num in range(0, 1001):
    if is_Prime(num):
        sum += num
print sum
'''


def main():
 
    # Frage den Benutzer nach einer Obergrenze bis zu der gesucht werden soll
    while True:
        try:
            obergrenze = int(raw_input('Bitte geben Sie eine Obergrenze ein: '))
            break
 
        except ValueError:
            print 'Dies ist keine gueltige Obergrenze. Bitte verwenden Sie eine Ganzzahl!'
 
    # Jede Zahl zwischen 1 und obergrenze wird zuerst als prim angenommen
    zahlen = [True]*(obergrenze+1)
    # Da 0 und 1 keine Primzahlen sind, werden sie auf False gesetzt
    zahlen[0] = False
    zahlen[1] = False
 
    i = 2
 
    while i*i <= obergrenze:
        if zahlen[i] == True: # Die Zahl i ist als prim markiert
            # Streiche alle Vielfachen von i
            for k in range(i*i,obergrenze+1,i):
                zahlen[k] = False
 
        i = i+1
	count = 0
	# Der Denkfehler beim Stoppwert 1001 ist folgender: bis 1001 habe ich noch keine 1000 Primzahlen erreicht
	# Ich muesste also wissen welches die 1000ste Primzahl ist -> mindestens bis 7920
	s = 0
	#for i in range(3,2000001,2):
	
	for i in range(0,7921,1):
		if is_Prime(i) == True:
			s += i
	print s
	
    # Ausgabe aller gefundenen Zahlen
    for i, v in enumerate(zahlen):
        if v == True:
			count = count + 1
			#print i, 'ist prim.'
			#print count
			s += i
	print s
	
    return 0
 
if __name__ == '__main__':
    main()
