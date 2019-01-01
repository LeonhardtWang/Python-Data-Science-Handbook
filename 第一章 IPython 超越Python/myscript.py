#------------------------------------
# file: myscript.py

def square(x):
	"""求平方"""
	return x ** 2
	
for N in range(1,4):
	print(N, "squred is", square(N))