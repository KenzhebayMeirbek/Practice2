n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i % 3 == 0 and i % 2 == 0:
        print(i)