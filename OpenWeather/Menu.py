
while True:
    print("1. Search weather by city")
    print("2. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        #city = input("Enter city name: ").strip()
        #data = get_weather(city)
        #print_weather(data)
        print("Choice 1 selected")
    elif choice == "2":
        break
    else:
        print("Invalid option\n")