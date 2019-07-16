def compute_gcd(n0,n2):   #compute the gcd
    while(n2):
        n0,n2=n2,n0%n2

    return n0

inp=list(map(int,input().split()))
print(compute_gcd(inp[0],inp[1]))



