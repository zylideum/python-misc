# 0xA / Zylideum
# 02/24/2022
# Project: Reviewing Python

def defaultParam(string, number = 1):
	print("Your string is", string, "and your default number is", number)

print("You can specify default parameters in a function by assigning the parameter to a value.")
print("\nIn Python, you must have default parameters after non-default parameters to not throw an error.")
print("\nCorrect:\n")
print("def defaultParam(letter, number = 1):")
print("\n\nIncorrect:\n")
print("def defaultParam(letter = \'a\', number):")

userString = input("\n\nTo show default parameters, enter a string for passing into the function: ")
defaultParam(userString)

userNumber = input("Now enter a number to replace the default: ")
defaultParam(userString, userNumber)

input("Press any key to exit.")

# Future Challenge
# Allow a user to create a 'profile' with defaults
# Call functions to change each aspect of the profile