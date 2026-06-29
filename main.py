customer_name = input("Enter Customer Name: ")
customer_name = customer_name.title()

product_name = input("Enter Product Name: ")
product_name = product_name.title()

quantity = int(input("Enter Quatity: "))
price = float(input("Enter Price Per Item: "))
total = quantity * price


print("=" * 30)
print("      BILL SUMMARY")
print("=" * 30)

print("Customer :", customer_name)
print("Product  :", product_name)
print("Quantity :", quantity)
print("Price    :₹", format(price, ".2f"))

print("-" * 30)
print("Total    :₹", format(total, ".2f"))
print("Thank you for shopping with us!")

print("=" * 30)