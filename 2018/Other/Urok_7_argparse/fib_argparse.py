
import argparse

def fib(n):
	a,b = 0,1
	for i in range(n):
		a,b = b, a+b
		print ("a :{} and b :{}".format(a,b))
	return a

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num", help ="you need to write n ",type=int)

	args = parser.parse_args()

	result = fib(args.num)
	print ("The "+str(args.num)+ "th fib number is "+str(result))

if __name__ == '__main__': 
	Main()
