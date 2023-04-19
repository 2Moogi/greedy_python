import sys
input=sys.stdin.readline

n,m = map(int,input().split())
point = list(map(int,input().split()))
point.sort()
for i in range(m):
    least = point[0] + point[1]
    point[0],point[1] = least,least
    point.sort()
print(sum(point))
