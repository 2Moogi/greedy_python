import sys
input=sys.stdin.readline

n=int(input())
result=0
while n >= 0:
    if n % 5 ==0:
        result = result + n//5
        print(result)
        break
    n = n-2
    result +=1
else:
    print(-1)
    
        
    
