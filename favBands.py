# favBands.py

lstBands = []

while True:
    print("\nFavorite Bands Menu")
    print("1. Add a band")
    print("2. View your bands")
    print("3. Exit")

    try:
        iChoice = int(input("Choose an option (1–3): "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    match iChoice:
        case 1:
            sBand = input("Enter a band name: ").strip()
            if sBand == "":
                print("Band name cannot be blank.")
            else:
                lstBands.append(sBand)
                print(f"{sBand} added!")

        case 2:
            if len(lstBands) == 0:
                print("Your list is empty.")
            else:
                print("\nYour favorite bands:")

                for sBand in lstBands:
                    print(f"- {sBand}")

        case 3:
            print("Thanks for sharing your favorite bands!")
            break

        case _:
            print("Please choose 1, 2, or 3.")
