while True:
    try: 
        a,b,c=map(int, input().split())
        left = c-b-1
        right = b-a-1
        print(max(left,right))
    except:
        break
