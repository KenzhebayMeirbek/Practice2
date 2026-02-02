#example 1
i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1

#example 2
count = 0
while True:
    count += 1
    print(count)
    if count == 5:
        break

#example 3
number = 1
while number < 100:
    if number == 50:
        print("Found 50!")
        break
    number += 1

#example 4
attempts = 0
while attempts < 5:
    password = "secret"  # Simulating input
    if password == "secret":
        print("Access granted!")
        break
    attempts += 1

#example 5
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("Loop completed")