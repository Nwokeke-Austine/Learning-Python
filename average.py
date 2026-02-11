#average
scores = [70, 80, 90, 60]
total = 0

for score in scores:
    total = total + score

average = total/len(scores)

print("The average of the 5 students is", average)