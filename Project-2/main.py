#Profit or Loss Calculator
actual_cost = float(input("Enter the actual cost of the product: "))
selling_price = float(input("Enter the selling price of the product: "))

if selling_price > actual_cost:
    profit = selling_price - actual_cost
    print(f"Profit: {profit}")
elif selling_price < actual_cost:
    loss = actual_cost - selling_price
    print(f"Loss: {loss}")