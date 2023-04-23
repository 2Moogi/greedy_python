import sys
input=sys.stdin.readline

p,n=map(int,input().split())
acc=list(map(int,input().split()))
acc.sort()

result=0
if p >= 200:
    print(0)
else:
    for i in range(n):
        p += acc[i]
        result +=1
        if p <200: # 피로도가 200 미만이면 장신구 하나 더 제작
            continue
        elif p >= 200: # 피로도가 200이상이면 반복문 탈출
            break
    print(result)

    
