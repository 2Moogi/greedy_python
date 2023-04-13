import sys
input=sys.stdin.readline

n=int(input())
rank=[]
dataset=[]
real_rank=[]
for i in range(n):
    fore_rank=int(input())
    rank.append(fore_rank)
    dataset.append(i+1)
rank.sort()
for j in range(n):
    onlyfire = abs(dataset[j]-rank[j])
    real_rank.append(onlyfire)
print(sum(real_rank))