# What specific meal is prepared for child and adult
print("child_meal:spaghetti")
print("adult_meal:steak")
child=float(input("What is the price of a child's meal? "))
adult=float(input("What is the price of an adult's meal? "))
num_children=int(input("How many children are there? "))
num_adults=int(input("How many adults are there? "))
child_cost=child*num_children
adult_cost=adult*num_adults
print(child_cost)
print(adult_cost)
subtotal=(child_cost + adult_cost)
print()
print("Subtotal:$"+ str(subtotal))
print()
sales_tax_rate=float(input("What is the sales tax rate? "))
sales_tax=subtotal/100
print("Sales_tax:$"+ str(sales_tax))
total=subtotal+sales_tax
print("Total:$"+ str(total))
print()
payment_amount=float(input("What is the payment amount? "))
change=payment_amount-total
print("Change:$"+ str(change))



