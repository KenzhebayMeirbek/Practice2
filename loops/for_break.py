#example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#example 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#example 3
for x in range(10):
    if x == 5:
        print("Found 5!")
        break
    print(x)

#example 4
numbers = [1, 3, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

#example 5
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print("Loop completed")