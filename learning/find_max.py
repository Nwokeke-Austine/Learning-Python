#Find the highest number in the list using a for loop.
numbers = [4, 7, 1, 9, 2]
max_number = 0

for number in numbers:
    if number > max_number:
        max_number = number

print("max number is", max_number)
