import sys,math
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))


result=1000000
ablity_st=sorted(data)
ablity_re=sorted(data,reverse=True)

for i in range(n):
    teammates = ablity_st[i] + ablity_re[i]
    result = min(teammates,result)
print(result)
