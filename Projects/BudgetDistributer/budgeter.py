#last thing is to try to get float values to show 2 digits for values like .5 or .0
import os

def loadWants():
    with open('D:/Programming/Wants/test.txt', 'r') as f:
        final = []
        for line in f:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            final.append(line_list)
    try:
        for want in final:
            want[1] = float(want[1])
            want[2] = float(want[2])
    except:
        return 0
    print("List loaded successfully.")
    return final

def saveWants():
    with open('D:/Programming/Wants/test.txt', 'w') as f:
        try:
            for want in wants:
                item = want[0]
                cost = want[1]
                saved = want[2]
                f.write(item + ',' + str(cost) + ',' + str(saved) + '\n')
        except:
            print("Error saving file. Ask Ashton nicely to look at it.")

def printWants(clearScreen):
    if (clearScreen):
        os.system('cls')

    if (wants):
        for want in wants:
            item = want[0]
            cost = want[1]
            saved = want[2]
            percentage = round(saved/cost,1)
            print(str(wants.index(want) + 1) + '.', item, '- $' + str(saved) + ' / $' + str(cost) + ' (' + str(round(((saved/cost) * 100), 2)) + ' % saved) ', end="")
            printProgressBar(percentage)
        if (clearScreen):
            os.system('pause')
            menu()
            return
    else:
        print("No wants! Try adding some.")
        if (clearScreen):
            os.system('pause')
            menu()
            return

def printProgressBar(percent):
    print('[', end="")
    for percent in range(0,int(percent*10)):
        print('█', end="")
    for percent in range(int(percent),9):
        print("░", end="")
    print("]")

def printSaved():
    for want in savedComplete:
        print("You can now buy", want[0] + "!")

def firstDistribution():
    initial = .50
    for want in wants:
        if (wants.index(want) == len(wants) - 1):
            want.append(initial * 2)
        else:
            want.append(initial)
            initial /= 2

def reDistribution():
    initial = .50
    for want in wants:
        if (wants.index(want) == len(wants) - 1):
            want.insert(3, initial * 2)
            del want[4]
        else:
            want.insert(3, initial)
            del want[4]
            initial /= 2
    
def printDistribution():
    for want in wants:
        item = want[0]
        percentage = (want[3] * 100)
        print(item, '- ' + str(percentage) + '%')

def getSavings():
    os.system('cls')
    base = input("Enter the amount you have to save: ")
    return int(base)

def saveForWants(monthlySavings):
    overflow = 0
    for want in wants:
        cost = want[1]
        saved = want[2]
        percentage = want[3]

        want[2] = saved + (monthlySavings * percentage)
        saved = want[2]

        if (saved >= cost):
            overflow += saved - cost
            want[2] = want[1]
    
    if (overflow > 0):
        removeSaved()
        reDistribution()
        saveForWants(overflow)

def removeSaved():
    for want in wants:
        cost = want[1]
        saved = want[2]
        if (cost == saved):
            savedComplete.append(want)
            wants.remove(want)

def roundWants():
    for want in wants:
        want[2] = round(want[2], 2)

def runDistribution():
    firstDistribution()
    savings = getSavings()
    saveForWants(savings)
    roundWants()
    saveWants()
    printWants(False)
    printSaved()
    os.system('pause')
    menu()
    return

def getWantAttributes():
    os.system('cls')
    print("Here are the current wants:\n")
    printWants(False)
    print("\nEnter 'q' to cancel adding a want at any time.")

    newWantPrio = input("Enter the priority of the new want: ")
    if (newWantPrio == 'q'):
        menu()
        return
    elif (int(newWantPrio) <= 0 or int(newWantPrio) > len(wants) + 1):
        print("Error: cannot add a priority below 1 or above", str(len(wants) + 1) + '.')
        os.system('pause')
        getWantAttributes()
        return

    newWantName = input("Enter the name of the new want: ")
    if (newWantName == 'q'):
        menu()
        return

    newWantCost = input("Enter the price of the new want: ")
    if (newWantCost == 'q'):
        menu()
        return
    elif (int(newWantCost) <= 0):
        print("Error: cannot enter a cost less than $0.")
        os.system('pause')
        getWantAttributes()
        return

    insertWant(newWantPrio, newWantName, newWantCost)

    menu()
    return

def insertWant(priority, itemName, cost):
    wants.insert(int(priority) - 1, [itemName, int(cost), 0])
    os.system('cls')
    print("Successfully added", itemName, "to list!")
    os.system('pause')

def getRemoveTarget():
    os.system('cls')
    print("Here are the current wants:\n")
    printWants(False)
    print("\nEnter 'q' to cancel removing a want at any time.")
    wantTarget = input("Enter a priority number to remove the want: ")
    if (wantTarget == 'q'):
        menu()
        return
    elif (int(wantTarget) <= 0 or int(wantTarget) > len(wants)):
        print("Error: cannot remove that item, it does not exist.")
        os.system('pause')
        getRemoveTarget()
        return

    wantTarget = int(wantTarget)
    wantTarget -= 1

    removeWant(wantTarget)

    menu()
    return

def removeWant(item):
    del wants[item]
    os.system('cls')
    print("Successfully removed item.")
    os.system('pause')

def getMoveTarDest():
    os.system('cls')
    print("Here are the current wants:\n")
    printWants(False)
    print("\nEnter 'q' to cancel changing wants at any time.")
    moveTarget = input("Enter a priority number you want to move: ")
    if (moveTarget == 'q'):
        menu()
        return
    elif (int(moveTarget) <= 0 or int(moveTarget) > len(wants)):
        print("Error: cannot move an item that does not exist.")
        os.system('pause')
        getMoveTarDest()
        return
    
    moveDestination = input("Enter a priority number you want to move this item to: ")
    if (moveDestination == 'q'):
        menu()
        return
    elif (int(moveDestination) <= 0 or int(moveDestination) > len(wants)):
        print("Error: cannot move to a destination that does not exist.")
        os.system('pause')
        getMoveTarDest()
        return

    moveTarget = int(moveTarget)
    moveDestination = int(moveDestination)
    moveTarget -= 1
    moveDestination -= 1

    moveWant(moveTarget, moveDestination)

    menu()
    return

def moveWant(oldPrio, newPrio):
    wants.insert(newPrio, wants.pop(oldPrio))
    os.system('cls')
    print("Successfully moved item.")
    os.system('pause')

def getPriceTarget():
    os.system('cls')
    print("Here are the current wants:\n")
    printWants(False)
    print("\nEnter 'q' to cancel changing wants at any time.")
    priceTarget = input("Enter a priority number you want to change the price of: ")
    if (priceTarget == 'q'):
        menu()
        return
    elif (int(priceTarget) <= 0 or int(priceTarget) > len(wants)):
        print("Error: cannot move an item that does not exist.")
        os.system('pause')
        getPriceTarget()
        return
    
    priceTarget = int(priceTarget)
    priceTarget -= 1

    newPrice = input("Enter the new price of a the item: ")
    if (newPrice == 'q'):
        menu()
        return
    elif (int(newPrice) <= 0):
        print("Error: cannot change the price to $0 or lower.")
        os.system('pause')
        getPriceTarget()
        return
    elif (int(newPrice) <= wants[priceTarget][2]):
        print("Add", wants[priceTarget][2] - int(newPrice), "to your next monthly savings and buy the item.")
        os.system('pause')
        menu()
        return

    newPrice = int(newPrice)
    changePrice(priceTarget, newPrice)

    menu()
    return

def changePrice(priceTarget, newPrice):
    wants[priceTarget][1] = newPrice
    os.system('cls')
    print("Successfully changed price.")
    os.system('pause')

wants = loadWants()
if (wants == 0):
    print("Error with file format. Ask Ashton nicely to look at it.")
    os.system('pause')

savedComplete = []

def menu():
    os.system('cls')
    print("Hello. Type the number to select an option:")
    print("1. See Wants")
    print("2. Add to Wants")
    print("3. Remove from Wants")
    print("4. Move Wants around")
    print("5. Change the price of a Want")
    print("6. Calculate Savings (End of Month)")
    print("7. Save and quit")
    selection = input("> ")

    if (selection == '1'):
        printWants(True)
    elif (selection == '2'):
        getWantAttributes()
    elif (selection == '3'):
        getRemoveTarget()
    elif (selection == '4'):
        getMoveTarDest()
    elif (selection == '5'):
        getPriceTarget()
    elif (selection == '6'):
        runDistribution()
    elif (selection == '7'):
        saveWants()
    else:
        menu()
        return
menu()
