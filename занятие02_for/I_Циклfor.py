n, b = map(int,input().split())

for i in range(n+1,b):
    print(i, end=' ')
print()

for i in range(b-1, n, -1):
    print(i, end=" ")
print()

for i in range(n+1, b):
    if i%2==0:
        print(i, end=" ")
print()

for i in range(0, b):
    if n < i**2 < b:
        print(i**2, end=" ")