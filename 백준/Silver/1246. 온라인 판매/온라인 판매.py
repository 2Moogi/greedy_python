import sys,math
input=sys.stdin.readline

n,m=map(int,input().split())
price_per=[]
price_result=[]
for i in range(m):
    egg = int(input())
    price_per.append(egg)
price_per.sort(reverse=True)

for i in range(m):
    n-=1
    revenue = price_per[i] * (i+1)
    price_result.append(revenue)
    if n ==0:
        break
    
for i in range(m):
    if max(price_result) == price_per[i] * (i+1):
        print(price_per[i],max(price_result))

