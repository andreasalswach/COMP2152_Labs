# Question 2: Shopping Cart (Lists - Searching and Removal)

# Counting Apples
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("We have", apple_count, "apples")

# Searching for item in list
print("Position of milk in list:", cart.index("milk"))

# Removal
# .remove function - remove first occurrence of item
cart.remove("apple")

# pop function - remove last item of the list
print("Removed item using pop:", cart.pop())

# Check if we have something in the list
print("Is banana in the cart?", "banana" in cart)

print("Final shopping cart:", cart)