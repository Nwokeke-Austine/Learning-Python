students = [
    {"Name": "Austine", "Score": 80},
    {"Name": "John", "Score": 55},
    {"Name": "Mary", "Score": 92},
    {"Name": "David", "Score": 48},
    {"Name": "Grace", "Score": 76}
]

highest_student = students[0]
lowest_student = students[0]
total_score = 0
pass_count = 0
fail_count = 0

for student in students:
    if student["Score"] >= highest_student["Score"]:
        highest_student = student

    if student["Score"] <= lowest_student["Score"]:
        lowest_student = student

    if student["Score"] >= 50:
        pass_count += 1
    
    else:
        fail_count += 1

    total_score += student["Score"]

average = total_score/len(students)

print("Highest Scoring student:", highest_student["Name"])
print("Score:", highest_student["Score"])


print("Lowest Scoring student:", lowest_student["Name"])
print("Score:", lowest_student["Score"])

print("Average Score:", average)

print("Number of Students who passed:", pass_count)
print("Number of Students who failed:", fail_count)


