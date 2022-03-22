#!/usr/bin/env python3
# 0xA / Zylideum
# 02/23/2022
# Project: Reviewing Python

print("The \'input()\' function is used to get information from the user in stdin.")
userInput = input("\nThe only parameter for \'input()\' is a string to communicate to the user. Input a number here:\n")

print("\'input()\' accepts user input as a string data type, which is important if integers need to be used.")
print("userInput + 5 would fail, as it's a string + int. To solve this, we have to typecast the input to an integer like so:")
print("\n\tuserInput = int(input(\"Enter a number:\"))")
userInputTwo = int(input("\nSo go ahead and enter a number that can actually be used this time:\n"))
print(userInputTwo, "+ 5 =", userInputTwo + 5)

input("Inputs can also be used to halt the CL from exiting, which is helpful for windows. This is an input function. \n\nPress anything to exit.")

# Future Challenge
# Take a large amount of user input and do some kind of processing.