K, N = map(int, input().split())

# Please write your code here.
def f(following, followed):
    if len(following)<=1:
        for i in range(following[0]):
            print(*followed,i+1)
    else:
        l=following[1:]
        for i in range(following[0]):
            f(l,followed+[i+1])
f([K for i in range(N)],[])