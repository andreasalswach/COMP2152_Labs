# Question 4: Class Attendance (Sets - Uniqueness and Operations)

# creating sets
mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Eve", "Frank"}

# adding a new item to a set using .add() function
mondayClass.add("Grace")

print("Monday class attendance: ", mondayClass)
print("Wendesday class attendance: ", wednesdayClass)

# combining sets
bothClasses = mondayClass & wednesdayClass
print("Attended both classes: ", bothClasses)


# using union (|)
allStudents = mondayClass | wednesdayClass
print("Attended either class: ", allStudents)

# using difference (-)
onlyMonday =  mondayClass - wednesdayClass
print("Only Monday: ", onlyMonday)

# using aymmetric difference (^)
onlyOne = mondayClass ^ wednesdayClass
print("Only one class: ", onlyOne)

# subset (<=)
print("Is Monday subset of all students?", mondayClass <= allStudents)