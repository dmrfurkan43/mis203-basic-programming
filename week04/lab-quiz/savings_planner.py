while True:
    starting_balance = float(input("Enter starting balance: "))
    if starting_balance >= 0:
        break
    print("Starting balance cannot be negative. Try again.")

while True:
    monthly_deposit = float(input("Enter monthly deposit: "))
    if monthly_deposit > 0:
        break
    print("Monthly deposit must be positive. Try again.")

while True:
    interest_rate = float(input("Enter monthly interest rate (%): "))

    if interest_rate >= 0:
        break
    print("Interest rate cannot be negative. Try again.")
while True:
    savings_goal = float(input("Enter savings goal: "))

    if savings_goal > 0:
        break
    print("Savings goal must be positive. Try again.")

balance = starting_balance
total_interest = 0.0
months = 0

print("\nSavings Goal Planner")
print("-" * 50)

if balance >= savings_goal:
    print("Goal already reached!")
else:
    print(f"{'Month':<10}{'Interest':<15}{'New Balance':<15}")
    print("-" * 40)

    while months < 60:
        months += 1

        interest = balance * interest_rate / 100
        balance += interest
        total_interest += interest

        balance += monthly_deposit

        print(f"{months:<10}{interest:<15.2f}{balance:<15.2f}")

        if balance >= savings_goal:
            break

    print("-" * 40)

    if balance >= savings_goal:
        print(f"Goal reached in {months} months!")
    else:
        print("Goal not reached within 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")