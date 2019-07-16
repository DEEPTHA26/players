din,de=map(str,input().split())
din=list(din)
de=list(de)
kow=0
for f in range(0,len(din)):
        if(din[f]!=de[f]):
            kow=kow+1
if(kow==1):
    print("yes")
else:
    print("no")
