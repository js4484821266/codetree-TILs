n = int(input())

# Please write your code here.
def f(k):
    if k<=1:return k
    s=0
    for i in range(1,k):
        s+=f(i)
    return s+1
print(f(n))