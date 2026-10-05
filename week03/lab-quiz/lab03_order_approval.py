order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
member = input("Is the customer a member? (yes/no): ")


if requested_quantity <= 0:
    print("Order rejected: Invalid quantity.")
elif requested_quantity > available_stock:
    print("Order rejected: Insufficient stock.")
elif member.lower() != "yes" and member.lower() != "no":
    print("Order rejected: Please answer yes or no.")
else:
    print("Order approved.")
    if member.lower() == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Reason: Member discount applied.") 
    else:
        final_price = order_amount
        print("Reason: No discount applied.")
    print(f"Final price: {final_price:.2f} TRY")
