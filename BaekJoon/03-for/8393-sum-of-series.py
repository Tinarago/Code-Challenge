n = int(input())

# print(int(n*(1 + n)/2))

x = 0
for i in range(0, n):
    x += (n - i)
print(x)