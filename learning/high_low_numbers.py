numbers = [5,10,50,30,70,29,80]

def find_highest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number

        else:
            continue
    return highest

def find_lowest(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number

        else:
            continue

    return lowest

highest_number = find_highest(numbers)
lowest_number = find_lowest(numbers)


print("The highest number is", highest_number)
print("The lowest number is", lowest_number)