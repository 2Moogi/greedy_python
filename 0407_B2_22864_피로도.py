a,b,c,m=map(int,input().split())
p,t,work = 0,0,0

while t < 24:
    if a > m:
        break
    elif p +a <= m :
        p = p + a
        work = work + b
        t = t + 1
    elif p + a > m:
        p = p - c
        if p<0:
            p=0
        t = t + 1
print(work)

#for문으로 푸는게 왜 막힌거지?
#왜 계속 while문과 for문을 고민했을까 --> 숙련도 이슈 ..많이풀자
#for문으로 썻으면 t변수 자체를 없앨수 있었으므로 더 좋은코드가 나올수 있었을 것 같다
