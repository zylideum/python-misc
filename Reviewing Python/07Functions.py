# 0xA / Zylideum
# 02/24/2022
# Project: Reviewing Python

def callFunction():
	print("Function successfully called!")
	input("Press anything to exit.")

print("Functions are defined with \'def funcName(param):\'")
print("They act as reusable code that can be called later.")
userCheck = input("To call the function in this code, enter a \'1\': ")

if userCheck == '1':
	callFunction()
else:
	print("That was not a 1, so we'll assume you want to exit.")
	input("Press any key to exit.")

# Future Challenge
# Write functions that call each other for various tasks in data processing
# Depending on input, use certain functions.
# Eg. if an even number is entered, do x, y, z.
# If an odd number is entered, do x, z.
# If 12 is entered, do y, z.