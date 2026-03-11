
# num_of_scores = int(input("How many scores do you want to enter: "))


# for i in range(num_of_scores):
#     enter_score = int(input(f"Enter score {i+1}: "))
#     scores.append(enter_score)



def find_min_max_avg_total(scores):
    highest = scores[0]
    lowest = scores[0]
    total = 0

    #highest
    for score in scores:
        if score > highest:
            highest = score
    #lowest
        if score < lowest:
            lowest = score
    #Average
        total += score 
    
        average = total/len(scores)
    
    

    return highest, lowest, average, total

Max_score, Min_score, average_score, total_score = find_min_max_avg_total([1,3,4,2])
print("The Max Score is", Max_score)
print("The Min Score is", Min_score)
print("The Average Score is", average_score)
print("The Total Score is", total_score)


#CORRECT VERSION
# def find_min_max_avg_total(scores):
#     highest = scores[0]
#     lowest = scores[0]
#     total = 0

#     for score in scores:
#         if score > highest:
#             highest = score

#         if score < lowest:
#             lowest = score

#         total += score

#     average = total / len(scores)

#     return highest, lowest, average, total

