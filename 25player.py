n7=int(input())        
words=input().split()  
words.sort(key=len)
print(" ".join(words))  
