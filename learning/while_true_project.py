username = "Austine"
password = "1234"
count = 0
while True:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")


    if (input_username == username) and (input_password == password): #be using and instead of &
        print("Login Successful")
        break

    else:
        print("Invalid username or password")
        count = count + 1
        if count == 3:
            print("Try Again in 24hrs")
            break





