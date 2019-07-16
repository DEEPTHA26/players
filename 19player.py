u,l=map(int,input().split())
count=0
for i in range(u,l+1):
    c=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                c=1
                break
        if c==0:
            count+=1
print(count)
        
