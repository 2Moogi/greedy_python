import sys
input = sys.stdin.readline

n,m=map(int,input().split())
my_list=[]
for i in range(n):
    p,l = map(int,input().split())
    m_list= list(map(int, input().split()))
    if l > p:
        my_list.append(1)
    else:
        m_list.sort()
        m_list.reverse()
        minim = m_list[l-1]
        my_list.append(minim)
        
my_list.sort()  
sum=0
for j in range(n):
    sum = sum + my_list[j]
    if sum == m :
        print(j+1)
        break
    elif sum > m :
        print(j)
        break
if sum < m :
    print(n)