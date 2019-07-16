dee1=int(input())
Sum=0
dig=0
while(dee1>0):
	dig=dee1%10
	Sum+=dig*dig
	dee1=dee1//10
print(Sum)	
