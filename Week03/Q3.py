# Question 3: Coordinate System (Tuples - Creation and Unpacking)

# creating tuples
point1 = (3,5)
point2 = (7,2)
print(f"Point 1: {point1}\nPoint 2: {point2}\n")

# unpacking tuples into variables x and y
x1, y1 = point1
x2, y2 = point2
print(f"x1: {x1}, y1: {y1}\nx2: {x2}, y2: {y2}\n") # formatted string

# calculating distance between two points
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f"Distance between points: {distance}\n")

# creating a tuple from a string using tuple() function
word = "hello"
word_tuple = tuple(word)
print(f"Tuple from string: {word_tuple}")

# printing each character from the tuple using a for loop