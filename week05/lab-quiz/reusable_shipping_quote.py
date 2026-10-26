
def calculate_subtotal(prices):
    subtotal = sum(prices)
    return subtotal


def get_discount_rate(subtotal):
    if subtotal >= 1000:
        return 0.10
    else:
        return 0


def calculate_shipping_fee(subtotal):
    if subtotal >= 500:
        return 0
    else:
        return 50



def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    final_total = subtotal - discount + shipping_fee
    return final_total



# Sample order 1
order1 = [300, 250]
subtotal1 = calculate_subtotal(order1)
discount_rate1 = get_discount_rate(subtotal1)
shipping_fee1 = calculate_shipping_fee(subtotal1)
total1 = calculate_final_total(subtotal1, discount_rate1, shipping_fee1)

print("Order 1")
print("Subtotal:", subtotal1, "TRY")
print("Discount rate:", discount_rate1 * 100, "%")
print("Shipping fee:", shipping_fee1, "TRY")
print("Final total:", total1, "TRY")

print()

# Sample order 2
order2 = [600, 500]
subtotal2 = calculate_subtotal(order2)
discount_rate2 = get_discount_rate(subtotal2)
shipping_fee2 = calculate_shipping_fee(subtotal2)
total2 = calculate_final_total(subtotal2, discount_rate2, shipping_fee2)



print("Order 2")
print("Subtotal:", subtotal2, "TRY")
print("Discount rate:", discount_rate2 * 100, "%")
print("Shipping fee:", shipping_fee2, "TRY")
print("Final total:", total2, "TRY")



assert calculate_subtotal([100, 200]) == 300
assert get_discount_rate(1000) == 0.10
assert calculate_shipping_fee(500) == 0
assert calculate_shipping_fee(499) == 50

print("All tests passed!")
