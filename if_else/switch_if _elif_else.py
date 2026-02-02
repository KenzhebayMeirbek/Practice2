#example 1
day = int(input()) % 7
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")  # This will print
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Weekend")

#example 2
month = int(input()) % 12
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 12:
    print("December")  # This will print
else:
    print("Invalid month")

#example 3
choice = "B"
if choice == "A":
    print("You selected Option A")
elif choice == "B":
    print("You selected Option B")  # This will print
elif choice == "C":
    print("You selected Option C")
else:
    print("Invalid choice")

#example 4
operator = "+"
a = 10
b = 5

if operator == "+":
    print(a + b)  # Prints 15
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")

#example 5
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")  # This will print
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")