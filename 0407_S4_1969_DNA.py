from collections import Counter

n,m = map(int,input().split())

dna_list=[]
low_dna=[]

for i in range(n):
    dna = input()
    dna_list.append(dna)

for j in range(m):
    middle_dna=[]
    for k in range(n):
        letter = dna_list[k][j]
        middle_dna.append(letter)
        middle_dna.sort()

        cnt = Counter(middle_dna).most_common(1)
        if k == n-1:
            low_dna.append(cnt[0][0])
            
result = ''.join(low_dna)            

hd=0
for x in range(m):
    for y in range(n):
        letter = dna_list[y][x]
        if result[j] != letter:
            hd+=1
            
print(result,hd, sep='\n')
