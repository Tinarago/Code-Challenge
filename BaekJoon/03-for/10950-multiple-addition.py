t = int(input())
a = []
for i in range(t):
    a.append(input())

for j in range(t):
    x, y = map(int, a[j].split())
    print(x + y)

# for i in range(t):
#     a, b  = map(int, input().split())
#     print(a + b)