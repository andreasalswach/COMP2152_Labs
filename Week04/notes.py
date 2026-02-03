# Loops
# for loops
numbers = [0, 1, 2, 3, 4]

for i in numbers:
    print(i)

# How to define function: def functionName():
def my_function():
    pass # pass does nothing, a placeholder

my_function()

# print is only for the console
def my_print_function():
    print("\nHi!")
my_print_function()

# calling my_function again? --> to see the effect of the function
my_function()

def sum_a_b(a, b):
    return a + b

sum_a_b(2, 4) # This will return 6 but not print it
print("\nsum a + b: ", sum_a_b(2, 4)) # This will print 6

