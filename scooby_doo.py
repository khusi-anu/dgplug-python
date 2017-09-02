#!/usr/bin/env python3

for i in range(1,101):
    if i%3 == 0 and i%7==0:
        print("Scooby Doo")
    elif i%3 == 0:
        print("Scooby")
    elif i%7 == 0:
        print("Doo")
    else:
        print(i)
