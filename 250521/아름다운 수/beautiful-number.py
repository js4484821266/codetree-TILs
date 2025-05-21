n = int(input())

# Please write your code here.
def f(k):
    if k<=2:return k
    s=0
    for i in range(min(4,k-1)):
        s+=f(k-(i+1))
    return s+1
print(f(n))