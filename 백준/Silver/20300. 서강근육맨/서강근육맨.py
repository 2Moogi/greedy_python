import sys
input=sys.stdin.readline

n=int(input())
loss=list(map(int,input().split()))
loss_st=sorted(loss)
loss_rev=sorted(loss,reverse=True)
loss_av=[]
if n % 2 == 0:
    for i in range(n//2):
        av=loss_st[i]+loss_rev[i]
        loss_av.append(av)
    print(max(loss_av))
elif n % 2 == 1:
    loss_av.append(loss_rev[0]) # 근손실 평균 리스트에 max값 추가
    del loss_st[-1]  #max값 삭제시켜 짝수와 동일하게 사용가
    del loss_rev[0]
    for i in range((n-1)//2):
        av=loss_st[i]+loss_rev[i]
        loss_av.append(av)
    print(max(loss_av))
