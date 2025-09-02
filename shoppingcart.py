Food = {"Pizza":15,"Burger":4,"Water:":2,"Soda": 4,"Tacos": 7}
Electronics = {"TV": 500,"Computers": 1000,"Phone": 700}
Toys = {"Balls": 15,"Squishy Toys": 5,"Toy Cars": 5}
cart = []
#---------------------------------------------------------------------------
def add():
    add = input("What would you like to add?: ")
    if add in Food:
        cart.append((add, Food[add]))
        print("The item", add, "was added to the cart")
    elif add in Electronics:
        cart.append((add, Electronics[add]))
        print("The item", add, "was added to the cart")
    elif add in Toys:
        cart.append((add, Toys[add]))
        print("The item", add, "was added to the cart")
    else: 
        print("Item not found in any categories. Please pick a valid item")

    
def remove():
    item = input("What would you like to remove? ")
    for cart_item in cart:
        if cart_item[0] == item:
            cart.remove(cart_item)
            print("The item", cart_item, "is removed from the cart")
            return  
    print("The item,", item, "is not in the cart.")
    
def view():
    if cart:
        print('Your cart contains:')
        for item,price in cart:
            print("The", item, "is", "$",price)
    else:
        print("Your cart is empty")

    
#---------------------------------------------------------------------------\
print("The products you can buy:")
print("Food:",Food)
print("Electronics:",Electronics)
print("Toys:",Toys)


while True:
    action = input("Would you like to add items, remove items, view items or quit the cart? ").lower()

    if action == "add":
        add()
    elif action == "remove":
        remove()
    elif action == "view":
        view()
    elif action == "quit":
        view()
        total = sum(price for item,price in cart)
        print("Your total is","$",total)
        print("Thanks for shopping with us!")
        break
    else: 
        print("Invalid action, choose either 'add', 'remove', 'view', or 'quit'")


    




    
   
