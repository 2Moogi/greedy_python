topping_kcal=[]
effi=[]
n=int(input())
a,b=map(int,input().split())
dough_kcal=int(input())
for i in range(n):
    topping = int(input())
    topping_kcal.append(topping)

topping_kcal.sort(reverse=True)
pizza_price = a
pizza_kcal = dough_kcal
pizza_doughonly = int(pizza_kcal / pizza_price)

for j in range(n):
    pizza_price +=b
    pizza_kcal += topping_kcal[j]
    pizza_effi = int (pizza_kcal / pizza_price)

    effi.append(max(pizza_doughonly,pizza_effi))
effi.sort(reverse=True)
print(effi[0])
