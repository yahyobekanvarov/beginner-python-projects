#Shopping cart
item = input("What item would you like to buy ?:")
price = float(input("What is the price ?:"))
quantity = float(input("How many would you like to buy ?:"))

total = price*quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is :${round(total, 2)}")












