import sys
input=sys.stdin.readline

n=int(input())
tips=[]
sum=0

for i in range(n):
    tip = int(input())
    tips.append(tip)

tips.sort(reverse=True)

for j in range(n):
    real_tip= tips[j] - ( j+1 -1)
    if real_tip < 0 :
        real_tip = 0
    sum = sum + real_tip

print(sum)
