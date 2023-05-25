def dfs(x):
    if x == 1:
        print(1, end='')
    elif x % 2 ==0:
        x = x//2
        dfs(x)
        print(0, end='')
    else:
        x = x//2
        dfs(x)
        print(1, end='')
    



if __name__=="__main__":
    n=int(input())
    dfs(n)
