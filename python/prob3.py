# https://projecteuler.net/problem=3
# Largest prime factor
# every integer greater than 1 either is prime itself or is the product of
# prime numbers, and that this product is unique

def compute():
    # type set to keep it unique
    factors = set()
    N = 600851475143
    d = 2
    while N > 1:
        while N % d == 0:
            N = N / d
            factors.add(d)
        # O(sqrt(n))
        d = d + 1
        # careful of the break position
        if d * d > N:
            if N > 1:
                factors.add(N)
            break
    return (factors)
    #return (str(max(factors)))


if __name__ == "__main__":
    print(compute())
