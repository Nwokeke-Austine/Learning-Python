number = int(input("Enter a number to produce its multiplicationn table: "))
multiple_array=[]

multiple = int(input("Enter how many multiples: "))
for i in range(multiple):
    multiple_array.append(i+1)


for digit in multiple_array:
    print(number * digit)

