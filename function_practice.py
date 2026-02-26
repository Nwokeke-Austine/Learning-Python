def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def determine_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"
    
scores = [70, 80, 65, 90]

average = calculate_average(scores)
grade = determine_grade(average)