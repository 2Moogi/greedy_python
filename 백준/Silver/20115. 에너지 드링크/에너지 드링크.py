n=int(input())
data = list(map(int,input().split()))
data.sort(reverse=True)
huge=data[0]

for i in range(1,n):
    huge += data[i]/2
print(huge)
