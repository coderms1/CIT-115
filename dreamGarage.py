# dreamGarage.py

lstCars = []
lstPrices = []

while True:
    sCar = input("Enter a car you would like to own: ")

    while True:
        try:
            fPrice = float(input("Enter its price: $"))

            if fPrice <= 0:
                print("Please enter a price greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a number without $ or commas.")

    lstCars += [sCar]
    lstPrices += [fPrice]

    while True:
        sMore = input("\nAdd another car? (Y/N): ")
        sMore = input("\nAdd another car? (Y/N): ").strip().upper()
        if sMore == "Y" or sMore == "y":
            break
        elif sMore == "N" or sMore == "n":
            break
        else:
            print("Please enter Y or N.")

    if sMore == "N" or sMore == "n":
        break
    else:
        print()

# Display the cars and calculate the total.
print("\nYour Dream Garage:")

iCount = 0
fTotal = 0.0

for sCar in lstCars:
    fPrice = lstPrices[iCount]
    print(f"{sCar:25}${fPrice:,.2f}")
    fTotal += fPrice
    iCount += 1

print(f"\nCars in your garage: {iCount}")
print(f"{'Total cost:':25}${fTotal:,.2f}")
