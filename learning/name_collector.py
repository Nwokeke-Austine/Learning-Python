#Student name collector
stundets = []

print("Enter the name of 5 students")
for i in range(1,6):
    name = input(f"Student {i}: ")
    stundets.append(name)

print("Student List: ", stundets)

# .append to add item to a list
#. remove to remove an item from a list