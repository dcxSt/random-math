import math

# counts number of entries not divisible by 7 in nth (or n+1th) row
def rho(n):
	j=0
	for k in range(0,n+1):
		if math.comb(n,k)%7!=0:
			j+=1
	return j
