B,A=map(int,input().split())
C=list(map(int,input().split()[:B]))
for i in range (0,A):
	C=[C[-1]]+C[:-1]
for j in C:
	print(j,end=" ")
