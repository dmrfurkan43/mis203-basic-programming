item1 = input("item name: ")
quantity1 = int(input("quantity: "))
price1 = float(input("price: "))

item2 = input("second item name: ")
quantity2 = int(input("second quantity: "))
price2 = float (input("second price: "))

delivery_fee = float(input("delivery fee: "))
tax_percentage = float(input("tax percentage: "))

cal1 = quantity1 * price1
cal2 = quantity2 * price2

subtotal = cal1 + cal2
tax = subtotal * (tax_percentage / 100)
final_total = subtotal + tax + delivery_fee

print()
print("purchase quote")
print(f"{item1}: {quantity1} x {price1:.2f} = {cal1:.2f}")
print(f"{item2}: {quantity2} x {price2:.2f} = {cal2:.2f}")
print(f"subtotal: {subtotal:.2f}")
print(f"delivery: {delivery_fee:.2f}")
print(f"final total: {final_total:.2f}")
