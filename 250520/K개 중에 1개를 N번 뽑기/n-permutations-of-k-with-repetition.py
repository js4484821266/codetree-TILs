K, N = map(int, input().split())

# Please write your code here.
[print(*(i+1,j+1))for i in range(K)for j in range(N)]