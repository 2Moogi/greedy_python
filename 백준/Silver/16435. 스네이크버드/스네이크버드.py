import sys,math
input=sys.stdin.readline

n,l = map(int,input().split())
data=list(map(int,input().split()))
data.sort()

for i in range(n):
    if data[i] <= l:
        l += 1
        if i ==n-1:
            print(l)
    else:
        print(l)
        break
