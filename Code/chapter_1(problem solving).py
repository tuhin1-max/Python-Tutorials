product_name = input("Product Name: ")
product_price = float(input("Product Price: "))
quantity = int(input("Quantity: "))

total_price = product_price*quantity

print("--- Shopping Information ---")
print("Product:", product_name)
print("Price:", product_price)
print("Quantity:", quantity)
print("Total Price:", total_price)
print("Final Price (Integer):", int(total_price))



