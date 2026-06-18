import random



difficultylevel = int(input("Select Difficulty: \n1. Easy\n2. Medium\n3. Hard\nDifficulty Level: "))
if difficultylevel == 1:
    secretNumber = random.randint(1, 10)
    totalattempt = 10
    attempt = 10

elif difficultylevel == 2:
    secretNumber = random.randint(1, 50)
    totalattempt = 5
    attempt = 5

elif difficultylevel == 3:
    secretNumber = random.randint(1, 100)
    totalattempt = 3
    attempt = 3




while attempt > 0:
    guess = int(input(f"Guess the secret number:"))

    if guess == secretNumber:
        print("--------------------")
        print("You are coorrect")
        print("--------------------")       

        break

    attempt -= 1

    if guess > secretNumber:
        print("Too High")
        print(f"You have {attempt} Attempt left")
        print("--------------------")

    elif guess < secretNumber:
        print("Too Low")
        print(f"You have {attempt} Attempt left")
        print("--------------------")

    if attempt == 0:
        print("Game Over")
        print("--------------------")


score = attempt / totalattempt * 100
print(f"Score: {score}")



    # correct version
# secretNumber = int(input("Enter Secret Number: "))
# attempt = 5

# while attempt > 0:

#     guess = int(input("Guess the secret number: "))

#     if guess == secretNumber:
#         print("You are correct")
#         break

#     attempt -= 1

#     if guess > secretNumber:
#         print("Too High")

#     elif guess < secretNumber:
#         print("Too Low")

#     print(f"You have {attempt} attempts left")
#     print("--------------------")

#     if attempt == 0:
#         print("Game Over")