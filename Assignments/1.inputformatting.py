# Nykaa Product Information System using basic Python and formatting

# Collecting product details
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
categories = list(map(str.strip, input("Enter Categories (comma-separated): ").split(',')))
stock_details = tuple(map(int, input("Enter Available Stock and Sold Stock (separated by space): ").split()))
discount = float(input("Enter Discount Percentage: "))
product_features = set(map(str.strip, input("Enter Product Features (comma-separated): ").split(',')))
supplier_name, supplier_contact, supplier_location = input("Enter Supplier Name, Contact Number, and Location (comma-separated): ").split(',')

# Display using comma separation
print("Product ID, Name, Price:", product_id, product_name, price, sep=', ')

# Percentage formatting
print("Product Discount: %.2f%%" % discount)

# f-strings
print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Stock Available: {stock_details[0]} units")

# .format() method
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(supplier_name.strip(), supplier_contact.strip(), supplier_location.strip()))
