#example 1
i = 1
while i < 6:
    print(i)
    i += 1

#example 2
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

#example 3
i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1

#example 4
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#example 5
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Loop finished!")