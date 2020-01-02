# Fibonacci Sequence are defined as follow: 
#   F(0) = 0, F(1) = 1;
#   F(n) = F(n-1) + F(n-2), n>=2

def FibRec(n):
    if n<=1:
        return n
    else:
        return FibRec(n-1) + FibRec(n-2)

def main():
    fib_seq = []
    n = int(input("Choose an integer: "))
    print("Fibonacci index from 0 to", n, "is:")
    for i in range(0,n+1):
        fib_seq.append(FibRec(i))
    print(fib_seq)

if __name__ == '__main__':
    main()