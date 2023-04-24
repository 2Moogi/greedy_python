import sys
input=sys.stdin.readline

n=int(input())
acc=list(map(int,input().split()))
x=acc[0]
del acc[0]
acc.sort()

for i in range(n-1):
    y=acc[i]
    if x <= y :
        print('No')
        break
    else:
        x += y
else:
    print('Yes')
        
