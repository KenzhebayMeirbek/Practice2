#example 1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#example 2
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)

#example 3
i = -5
while i < 5:
    i += 1
    if i < 0:
        continue
    print(i)

#example 4
count = 0
while count < 10:
    count += 1
    if count == 3 or count == 7:
        continue
    print(count)

#example 5
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("Loop completed!")