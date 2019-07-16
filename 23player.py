n8,k8=list(map(int,input().split()))
waste=input()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
final=[]
for i in range(len(arr2)):
    arr1.append(arr2[i])
    final.append(str(max(arr1)))
print(" ".join(final))
