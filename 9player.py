dvi= []
def drime(o):
    s = 0
    for x in range(2,o-1):
        if o%x == 0:
            s =1
            break
    if not s:
        dvi.append(o)

d ,mt = map(int,input().split())

for e in range(d,mt+1):
    drime(e)
print(len(dvi))
