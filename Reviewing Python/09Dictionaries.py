# 0xA / Zylideum
# 02/25/2022
# Project: Reviewing Python


fruitInventory = {"Apple":23, "Pear":12, "Avocado":2}
selection = False

print("Dictionaries are used as associative arrays where values are indexed with keys.")
print("Use brackets to set them up: {}")
lookup = input("What item would you like to look up? (Apple, Pear, Avocado): ")

while(selection == False):
	if lookup.lower() == 'apple':
		print(fruitInventory['Apple'], "apples in stock.")
		selection = True
	elif lookup.lower() == 'pear':
		print(fruitInventory['Pear'], "pears in stock.")
		selection = True
	elif lookup.lower() == 'avocado':
		print(fruitInventory['Avocado', "avocados in stock."])
		selection = True
	else:
		print("Not a valid item.")
		break
input("Press anything to exit.")

# Future Challenge
# Create a full-fledged shop inventory using dictionaries
# Allow user to buy things with a given balance and allow the store to restock
# Do this with a menu loop to keep the customer able to purchase while money > 0.