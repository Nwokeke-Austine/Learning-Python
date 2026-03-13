while True:
    print("\nMenu")
    print("1. Print Hello")
    print("2. Print my name")
    print("3. Exit")

    option = int(input("Select an option: "))
    if option == 1:
        print("\nHello")
    elif option == 2:
        print("\nMy name is Austine")
    elif option == 3:
        exit = input("Are you sure you want to exit(Y/N): ").upper()
        if exit == "Y":
            break
        
        

    else:
        print("\nInvalid Option, Try again(1-3)")
