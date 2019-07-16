dvi=list(input())
dd=len(dvi)
new=''
for l in range (0,dd,2):
    dvi[l],dvi[l+1]=dvi[l+1],dvi[l]
print(*dvi,sep='')
