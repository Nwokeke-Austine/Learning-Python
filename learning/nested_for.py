# def multiplication_table(size):
#     for i in range(1, size + 1):
#         for j in range(1, size + 1):
#             print(f"{i * j:4}", end="")
#         print()  # Newline after each row

# table_size = int(input("Enter the size of the multiplication table: "))
# multiplication_table(table_size)

student = [
    [85, 90, 78],
    [92, 88, 95],
    [80, 85, 82]
]

for i in range(len(student)):
    total = 0
    for j in range(len(student[i])):
        total += student[i][j]
    average = total / len(student[i])
    print(f"Student {i + 1} - Total: {total}, Average: {average:.2f}")