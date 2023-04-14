import sys,math
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
result=[]
for i in range(n):
    day = (i+1) + data[i] +1
    result.append(day)

print(max(result))
