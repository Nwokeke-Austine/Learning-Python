#Secret number = 7
#User keeps guessing until correct
#Count attempts
#Print attempts when user wins

secret_number = 7
attempt = 0

while True:
    number = int(input("Guess the secret number: ")) #it is int(input) and not input(int)
    attempt = attempt + 1
    
    if secret_number == number:
        print("You guessed right")
        print("You used", attempt, "attempts" )
        break

    else:
        print("You guessed wrong, Try again")
        attempt = attempt + 1
        