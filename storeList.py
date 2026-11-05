# storeList.py

lstPrices = []

for iCount in range(1, 4):
    while True:
        try:
            fPrice = float(input(f"Enter price for item {iCount}: $"))

            if fPrice < 0:
                print("Price cannot be negative.")
                continue

            lstPrices += [fPrice]
            break

        except ValueError:
            print("Please enter a valid number.")
