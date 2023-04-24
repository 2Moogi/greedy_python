import sys
n=int(sys.stdin.readline())
tmp1=(list(map(int, sys.stdin.readline().split())))
jun=tmp1[0]
tmp1.pop(0)
tmp1.sort()
for i in tmp1:
  if i<jun :
    jun+=i
    ans="Yes"
  else:
    ans="No"
    break
if len (tmp1)!=0: print(ans)
else: print("Yes")
