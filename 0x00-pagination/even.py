#!/usr/bin/env python3

# number = int(input("enter any number"))

for i in range(11):
    try:
        number = input("enter any number")

        if isinstance(float(number), float):
            print("This is a float number")
        if int(number) & 1 == 0:
            print("Even Number")
        else:
            print("Odd")
    except Exception as e:
        print("The error is {}".format(e))
