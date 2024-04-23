from user import *
from cart import *
from inventory import *
from history import *


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory()
    history = OrderHistory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        print("4. Order Information")
        option = input("Enter your menu choice: ")
        print()

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")
        elif(option == "1"):
            user.viewAccountInformation()
        elif(option == "2"):
            print("1. View the Inventory")
            print("2. Search for item in the inventory ")
            print("3. Go back")
            opt = int(input("pick one: "))
            if(opt == 1):
                e1 =Inventory.viewInventory(user)
                print(e1)
            elif(opt == 2):
                e2 = Inventory.searchInventory(user)
                print(e2)
            elif(opt == 3):
                mainMenu(user, cart, inventory, history)
        elif(option == "3"):
            print("1. View your Cart")
            print("2. Add to your cart")
            print("3. Remove an item from your cart")   
            print("4. Checkout!!")  
            print("5. Go back")
            opt = int(input("pick one: "))
            if(opt == 1):
                F1 = Cart.viewCart(cart)
                print(F1)
            elif(opt == 2):
                F2 = Cart.addToCart(cart)
                print(F2)
            elif(opt == 3):
                F2 = Cart.removeFromCart(cart)
                print(F2)
            elif(opt == 4):
                Cart.checkOut(cart)
            elif(opt == 5):
                mainMenu(user, cart, inventory, history)
            else:
                print("this isn't a valid option")
        elif(option == 4):
            print("order Information")  
            print("create an order")
            print("add items to order")
            opt = int(input("pick one: "))
            if(opt == 1):
                F1 = OrderHistory.viewHistory(user)
                print(F1)
            elif(opt == 2):
                F2 = OrderHistory.viewOrder(user)
                print(F2)
            elif(opt == 3):
                F3 = OrderHistory.createOrder(user)
                print(F2)
            elif(opt == 4):
                F3 = OrderHistory.addOderItems(user)
                print(F3)
            elif(opt == 5):
                mainMenu()
            else:
                print("this isn't a valid option")
        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")
            print()

def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
