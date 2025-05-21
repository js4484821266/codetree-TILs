n = int(input())

# Please write your code here.
l=[0 for i in range(n+1)]
l[1]=1
def f(k):
    if k==0:return 0
    elif l[k]>0:return l[k]
    else:
        s=0
        for i in range(1,min(k+1,10)):
            s+=f(k-i)
        l[k]=s+1
        return l[k]
print(f(n))