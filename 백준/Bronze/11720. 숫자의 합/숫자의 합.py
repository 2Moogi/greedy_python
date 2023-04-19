import sys
input=sys.stdin.readline
numbers=[]
n=int(input())
data=input()
result = 0
for i in range(n):
    result += int(data[i])

print(result)

