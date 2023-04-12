rope=[]
arr=[]
n=int(input())
for i in range(n):
    max_kg = int(input())
    rope.append(max_kg)
rope.sort()
for i in range(n):
    k = rope[i] * (n-i)
    arr.append(k)
arr.sort()
print(arr[-1])