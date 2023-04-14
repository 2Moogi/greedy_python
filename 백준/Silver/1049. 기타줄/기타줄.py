import sys,math
input=sys.stdin.readline

whole_list=[]
single_list=[]

n,m=map(int,input().split())
for i in range(m):
    whole,single=map(int,input().split())
    whole_list.append(whole)
    single_list.append(single)
whole_list.sort()
single_list.sort()

result = 0
cnt=0

if whole_list[0] > single_list[0] * 6:
    result +=single_list[0]*n
else:
    for i in range(n):
        result +=whole_list[0]
        cnt+=6
        if cnt > n:
            only_set = (i+1)*whole_list[0]
            result -= whole_list[0]
            cnt -= 6
            result = result + (n-cnt) * single_list[0]
            result = min(result,only_set)
            break
    
print(result)
