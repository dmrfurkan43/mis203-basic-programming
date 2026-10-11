import datetime
import random

print("==========Restaurant Order System==========")
print()
total = 0
order_count = 0

order_number = random.randint(1000, 9999)

while True:
    print("\n -------MENU-------")
    print("1. Pizza - 300 TRY")
    print("2. Burger - 270 TRY")
    print("3. Pasta - 180 TRY")
    print("4. Salad - 140 TRY")
    print("5. Cola - 70 TRY")
    print("6. Finish order")
    print("------------------")

    choice = input("Please select an item (1-6): ")

    if choice == "6":
        break

    if choice == "1":
        product = "Pizza"
        price = 300
    elif choice == "2":
        product = "Burger"
        price = 270
    elif choice == "3":
        product = "Pasta"
        price = 180
    elif choice == "4":
        product = "Salad"
        price = 140
    elif choice == "5":
        product = "Cola"
        price = 70
    else:
        print("Invalid selection. Please choose a valid item.")
        continue
    quantity = int(input("enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity. Please enter a positive number.")
        continue

    item_total = price * quantity
    total += item_total
    order_count += quantity

    print(f"Added {quantity} x {product} = {item_total:.2f} TRY")

print("\nOrder Summary:")

print("Order Number:", order_number)
print("Order Date:", datetime.datetime.now())

if order_count == 0:
    print("No items ordered.")
else:
    print(f"Total items: {order_count}")
    print(f"Subtotal: {total:.2f} TRY")

    if total >= 1000:
        discount = total * 0.10
        print("Discount: 10%")
    else:
        discount = 0
        print("Discount: 0%")

    final_total = total - discount
    print(f"discount amount: {discount:.2f} TRY")
    print(f"Final total: {final_total:.2f} TRY")
print("Thank You for your order!")