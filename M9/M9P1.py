# Problem 1 - Extended price with a function (pass by value)

def compute_ext_price(qty, price):
    total = qty * price
    if total > 10000.00:
        total = total * 0.90   # 10% discount on totals over $10,000
    return total


total_ext_price = 0.0
response = "Y"

while response.upper() == "Y":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    ext_price = compute_ext_price(qty, price)
    total_ext_price += ext_price

    print(f"Quantity: {qty}  Price: ${price:,.2f}  Extended Price: ${ext_price:,.2f}")

    response = input("Enter another item? (Y/N): ")

print(f"\nTotal extended price for all items: ${total_ext_price:,.2f}")