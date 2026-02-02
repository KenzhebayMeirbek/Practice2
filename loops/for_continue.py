#example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#example 2
for x in range(10):
    if x % 2 != 0:
        continue
    print(x)

#example 3
for x in range(6):
    if x == 3:
        continue
    print(x)

#example 4
for x in range(10):
    if x == 2 or x == 5 or x == 8:
        continue
    print(x)

#example 5
for x in range(5):
    if x == 2:
        continue
    print(x)
else:
    print("Loop finished!")