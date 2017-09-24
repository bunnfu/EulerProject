# https://projecteuler.net/problem=2
# Even Fibonacci numbers

def compute():
    """
    Returns the largest even Fibonacci number that does not exceed 4 million.
    """
    ans = 0
    x,y = 1,2
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
        x, y = y, x+y
    return(str(ans))

if __name__ == "__main__":
    print(compute())
