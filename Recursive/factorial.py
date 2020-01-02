# Recursive Function to excute n!
def Fact(n):
    if n == 0: 
        return 1
    else:
        return n * Fact(n-1)

def main():
    print("0! = ", Fact(0))
    print("1! = ", Fact(1))
    print("2! = ", Fact(2))
    print("3! = ", Fact(3))
    print("4! = ", Fact(4))
    print("5! = ", Fact(5))

if __name__ == '__main__':
    main()