n=int(input())
fact=1
cnt=0
for i in range(1,n+1):
    fact *=i
str_fact=str(fact)
list_fact=list(str_fact)
list_fact.reverse()
for i in list_fact:
    if i =='0':
        cnt+=1
    else :
        print(cnt)
        break
    
