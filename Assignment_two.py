budget = float(input("Enter your monthly budget: "))

expenses = float(input("Enter your total monthly expenses: "))

if expenses > budget:
    print(f"You are over budget by ${expenses - budget:.2f}.")
elif expenses < budget:
    print(f"You are within budget with ${budget - expenses:.2f} remaining.")
else:
    print("You have spent exactly your budget.")

if expenses > budget:
    penalty = 0.05 * (expenses - budget)  # 5% penalty on exceeded amount
    budget -= penalty
    print(f"A penalty of ${penalty:.2f} has been applied. Your new budget is ${budget:.2f}.")
