import sys,math
input=sys.stdin.readline

a,b=map(int,input().split())
n=int(input())
button_list=[]
data=[]
for i in range(n):
    button=int(input())
    button_list.append(button)
for i in range(n):
    result = min(abs(a-b),abs(button_list[i]-b))
    if abs(button_list[i]-b) < abs(a-b):
        result +=1
    data.append(result)

if a == b:
    print(0)
elif b in button_list:
    print(1)
else:
    print(min(data))
