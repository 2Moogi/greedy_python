import sys
input=sys.stdin.readline

n,m=map(int,input().split())
books=list(map(int,input().split()))

cnt=0
box=0

for book in books:
    box += book
    if box < m:
        continue
    elif box == m:
        cnt+=1
        box=0
    elif box > m:
        cnt+=1
        box=book
if box > 0:
    cnt +=1
print(cnt)
