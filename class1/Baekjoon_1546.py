N = int(input())
a = list(map(int, input().split()))
smax = max(a)
for i in range(N):
    a[i] = a[i] / smax * 100
print(sum(a)/N)