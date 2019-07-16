A8=int(input())
B8=str(input())
B8=list(B8)
for i in B8:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		B8.remove(i)
C5=B8[::-1]
print("".join(C5))
