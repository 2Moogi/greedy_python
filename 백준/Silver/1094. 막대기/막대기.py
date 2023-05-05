stick=[64,32,16,8,4,2,1]
cnt=0
n=int(input())
for i in stick:
    if n - i < 0:
        continue
    elif n == i:
        print(cnt+1)
        break
    else:
        n -=i
        cnt +=1
