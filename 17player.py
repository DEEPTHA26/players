A5,A8=map(int,input().split())
num=1
while num>0:
	if num%A5==0 and num%A8==0:
		print(num)
		num=0
	else:
		num+=1
