b,c,d=map(int,input().split())
burger=list(map(int,input().split()))
burger.sort(reverse=True)
side=list(map(int,input().split()))
side.sort(reverse=True)
drink=list(map(int,input().split()))
drink.sort(reverse=True)
nosale = sum(burger)+sum(side)+sum(drink)
sum=0
for i in range(min(b,c,d)):
    sum += (burger[i]+side[i]+drink[i]) * 0.1

print(nosale)
print(int(nosale-sum))
