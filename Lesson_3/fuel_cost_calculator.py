distance = float(input("Please enter the distance of your trip in kilometers: "))
cost_per_liter = float(input("Please enter the cost per liter of fuel: "))

fuel_needed = (distance / 100) * 8

total_cost = fuel_needed * cost_per_liter

print(f"Your total fuel cost for the trip will be: ${total_cost:.2f}")