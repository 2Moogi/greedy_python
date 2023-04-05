n=int(input())
data = list(map(int, input().split()))

data.sort()
del data[-1]
print(sum(data))

