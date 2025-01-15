
item= ['milk','bread', 'chips' ]
price=[12.50 , 30.20 , 15.60]
choice= '0'

for item in item:
     print(item)

print("Welcome to the shopping program")
print()

while choice != '5' :
    print ("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = input("Please enter an action: ")
    if choice  == '1' :
        add_item = input("What item would you like to add? ")
        add_price = float(input(f" What is the cost of the {add_item} ? "))
        print(add_item , "has been added to the cart")
    elif choice == '2':
        print("The contents of the shopping cart are:")
        for i in range(len(item)):
            items = item[i]
        for i in range (len(price)):
            prices = price[i]   
            print(f"{items}  : $ ({price[i]})" )
    if choice == '3' :
        removed= input("Which item you would like to to remove? ")
        print(removed , "removed")
    elif choice == '4':
        total = sum(price)
        print("The total price of the items in the shopping cart is $" , total)
    if choice == '5':
     print("Thank you. Goodbye.")

      