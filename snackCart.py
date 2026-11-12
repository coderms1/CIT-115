# snackCart.py

lstPrices = [1.50, 2.00, 1.25]
fTotal = 0.0
iCount = 0

while True:
    print("\nSnack Menu")
    print("1. Chips - $1.50")
    print("2. Cookie - $2.00")
    print("3. Apple - $1.25")
    print("4. Checkout")

    try:
        iChoice = int(input("Choose an option (1–4): "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    match iChoice:
        case 1:
            fPrice = lstPrices[0]
            sSnack = "Chips"

        case 2:
            fPrice = lstPrices[1]
            sSnack = "Cookie"

        case 3:
            fPrice = lstPrices[2]
            sSnack = "Apple"

        case 4:
            break

        case _:
            print("Please choose 1, 2, 3, or 4.")
            continue

    fTotal += fPrice
    iCount += 1
    print(f"{sSnack} added! Current total: ${fTotal:.2f}")

if iCount == 0:
    print("\nYou did not buy any snacks.")
else:
    print(f"\nNumber of snacks: {iCount}")
    print(f"Total cost: ${fTotal:.2f}")
    print("Enjoy your snacks!")
