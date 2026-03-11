correct_username = input("Enter your username: ")
correct_username = correct_username.lower()
correct_password = input("Enter your password: ")

input_username = input("Enter username: ")
if input_username.lower() != correct_username:
    print("Wrong Username")
else:
    input_password = input("Enter Password: ")
    if  input_password != correct_password:
        print("Wrong password")
    else:
        print("Login Successful 🎉")