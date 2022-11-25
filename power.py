def power(n, p):
	if (p >= 1):
		i = n * power(n, p-1)
	elif (p == 0):
		i = 1
	return (i)

