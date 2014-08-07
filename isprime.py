import sys

def isPrime(n):
  '''print a list of numbers, indicating primes, 1 thru n'''
  print "1\n2"
  for i in range(2,n+1):
    for j in range(2,i):
      if i % j == 0:
        print (i)
        break
      if j==(i-1):
        print (str(i) + ' is prime!')

def main():
  isPrime(int(sys.argv[1]))


if __name__=="__main__":
  main()
