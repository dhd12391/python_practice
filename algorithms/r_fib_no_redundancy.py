"""
fibonacci recursive algorithm using map to check for redundant calculations 
benchmarking it by comparing iterative fibonacci and usual recursive ways
"""

calculated_fib = {0:1,1:1}

def r_fib(x):
	"""Recursively calculate fibonacci using saved calculations."""	
	if x == 0 or x == 1:
		return calculated_fib[x]

	if x-1 not in calculated_fib:
		calculated_fib[x-1] = fib(x-1)
	if x-2 not in calculated_fib:
		calculated_fib[x-2] = fib(x-2)
	calculated_fib[x] = calculated_fib[x-1]+calculated_fib[x-2]
	return calculated_fib[x]

def i_fib(x):
	"""Iteratively calculate fibonacci."""
	f1 = 1
	f2 = 1
	i = 2

	if x == f1 or x == f2:
		return x
	while(i <= x):
		if i%2==0:
			f1 += f2
			if i==x:
				return f1
		else:
			f2 += f1
			if i==x:
				return f2
		i += 1
	return 0


if __name__=='__main__':
	i_count = 0
	r_count = 0
	
	for i in range(50):
		print "%(i)d: %(r_fib_i)d (%(r_count)d), %(i_fib_i)d" %\
			{"i": i, "r_fib_i": r_fib(i), "r_count": r_count,\
			"i_fib_i": i_fib(i)}
		r_count = 0
		i_count = 0

