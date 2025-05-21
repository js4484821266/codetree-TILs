n = int(input())

# Please write your code here.
def f(k):
    if k<=1:return 1
    s=0
    for i in range(min(4,k)):
        s+=f(k-(i+1))
    return s
print(f(n))