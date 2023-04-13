import sys
input= sys.stdin.readline

n=int(input())
data=[]
list=[]
for i in range(n):
    k=int(input())
    data.append(k)
data.sort()
for i in range(1,n+1):
    list.append(i)
result=0
for i in range(n):
    result = result + abs(list[i]-data[i])
print(result)