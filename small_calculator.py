#!/usr/bin/env python3
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
print("Enter 1 for + \nEnter 2 for - \nEnter 3 for * \nEnter 4 for /")
choice = int(input("Enter your choice:"))

if choice == 1:
    answer = number_1 + number_2
elif choice == 2:
    answer = number_1 - number_2
elif choice == 3:
    answer = number_1 * number_2
elif choice == 4:
    answer = number_1 / number_2
else:
    print("Wrong choice")

print("Your answer is : %.4f" % answer)

