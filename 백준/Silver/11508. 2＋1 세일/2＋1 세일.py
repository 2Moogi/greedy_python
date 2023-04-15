import sys,math
input=sys.stdin.readline

drink=[]
bonus=[]

n=int(input())
for i in range(n):
    yogurt=int(input())
    drink.append(yogurt)
drink.sort(reverse=True)

result= sum(drink)

for i in range(n):
    if i%3 == 2:
        result -= drink[i]
print(result)
