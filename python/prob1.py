# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def compute():
    """
    Returns sum of all number within 1 million that can be divided by 3 or 5.
    """
    ans = sum(x for x in range(1000000) if x % 3 == 0 or x % 5 == 0)
    return(ans)

def SumDivisibleBy(n, target=100000000-1):
    """
    https://projecteuler.net/overview=001
    """
    p = target // n
    return (n * p * (p+1) / 2)

if __name__ == "__main__":
	# print(str(compute()))
    print(str(SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)))
