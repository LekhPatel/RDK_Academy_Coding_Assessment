MAX_FAVOURITES = 3
favourites = []

while True:
    choice = input("Select an option: ").strip()
    if choice == "2":
        city = input("Enter city name to add: ").strip()

        if city in favourites:
            print("City already in favourites\n")
            continue
        if len(favourites) >= MAX_FAVOURITES:
            print("Favourites list is full (max 3). Remove one first.\n")
            continue

        favourites.append(city)
        print(f"{city} added to favourites\n")