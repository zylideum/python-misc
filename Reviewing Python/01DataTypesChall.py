# 0xA / Zylideum
# 03/21/2022
# Project: Reviewing Python, Challenge

# Challenge
# Remove the spaces between the apostrophes and the values from the original.
# Concatenation works, but is it better? 
# Evaluate performance benefit of , vs. +

a = 3
b = 4.5
c = True
d = 'Hello'
e = 'a'

print("Using commas in the print function is essentially passing an additional parameter that separates based on the default sep. Concatenation creates a larger string by using temporary memory, which is more efficient for smaller strings but is eclipsed by the multiple parameter method for much larger data. There doesn't seem to be consensus on using concatenation vs. parameters vs. substitution/f-strings in style guides, so I'll stick to concatenation when using raw strings and \'parameterization\' when using variables.")
print("For encapsulating these variables within quotes while maintaining my personal preference to use parameters when dealing with variables, I'll use f-strings to format it.")
print("Then comes the argument about .format() method and f-strings, and in this case I find better consensus about f-strings being easier to read and will use them over the .format() method from now on.")
print("Another small detail to note is using double quotations for strings and single quotes for characters. Haven't found anything in a style guide for this, but this is my preference.\n")
print(f'\'{a}\'', "is an integer.")
print(f'\'{b}\'', "is a float.")
print(f'"{c}"', "is a boolean.")
print(f'"{d}"', "is a string.")
print(f'\'{e}\'', "is a character.")

# Challenge Conclusion
# Spaces removed using f-string formatting to maintain preference of using , for variables
# Concatentation is faster for small strings, becomes worse with large data