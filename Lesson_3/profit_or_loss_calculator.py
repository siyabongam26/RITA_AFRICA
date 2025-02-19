# Ask the user to input the buying price of a product
buying_price = float(input("Enter the buying price of the product: "))

# Ask the user to input the selling price of the product
selling_price = float(input("Enter the selling price of the product: "))

# Calculate profit or loss
if selling_price > buying_price:
    profit = selling_price - buying_price
    print(f"You made a profit of ${profit:.2f}")
elif selling_price < buying_price:
    loss = buying_price - selling_price
    print(f"You made a loss of ${loss:.2f}")
else:
    print("No profit, no loss. The selling price is the same as the buying price.")