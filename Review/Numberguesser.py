
secretNumber = int(input("Enter Secret Number: "))
attempt = 5

while True:
    guess = int(input(f"Guess the secret number:"))

    if guess == secretNumber:
        attempt -= 1
        print("You are coorrect")
        print("--------------------")       

        break

    elif guess > secretNumber:
        print("Too High")
        attempt -= 1
        print(f"You have {attempt} Attempt left")
        print("--------------------")

    elif guess < secretNumber:
        print("Too Low")
        attempt -= 1
        print(f"You have {attempt} Attempt left")
        print("--------------------")

    if attempt == 0:
        print("Game Over")
        print("--------------------")
        break

    # correct version
# secretNumber = int(input("Enter Secret Number: "))
# attempt = 5

# while True:
#     guess = int(input(f"Guess the secret number:"))

#     if guess == secretNumber:
#         attempt -= 1
#         print("You are coorrect")
#         print("--------------------")       

#         break

#     elif guess > secretNumber:
#         print("Too High")
#         attempt -= 1
#         print(f"You have {attempt} Attempt left")
#         print("--------------------")

#     elif guess < secretNumber:
#         print("Too Low")
#         attempt -= 1
#         print(f"You have {attempt} Attempt left")
#         print("--------------------")

#     if attempt == 0:
#         print("Game Over")
#         print("--------------------")
#         break