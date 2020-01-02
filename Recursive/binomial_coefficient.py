# Recursive Function to execute C(n,k)
# C(n,k) is recursively defined as follow:
#   C(n,0) = 1, C(n,n) = 1,             with n>= 0
#   C(n,k) = C(n-1,k-1) + C(n-1,k),     0<k<n

def C(n,k):
    if k==0 or k==n: 
        return 1
    else:
        return C(n-1,k-1) + C(n-1,k)

def main():
    n = int(input("Choose n: "))
    k = int(input("Choose k (k must less than n): "))
    if (n<k): 
        print("Error! I warned you!")
        return
    else:
        print("C(n,k) = ", C(n,k))

if __name__ == '__main__':
    main()