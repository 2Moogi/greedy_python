# 곱셈은 작은 수를 곱해주는게 크기를 작게함에 있어서 중요하다
# 따라서 sort 사용후 첫 번째 인덱스부터 막대를 잘라주면 된다

import sys
input=sys.stdin.readline

n=int(input())
stick=list(map(int,input().split()))

stick.sort()
xy=[]

big=sum(stick) # 막대 전체
for i in range(n):
    big = big - stick[i] # 막대를 big과 small로 분리
    small=stick[i]
    xy.append(big * small) # 두 막대 곱한값을 xy리스트에 저장
print(sum(xy))
    
