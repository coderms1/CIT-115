# shopList.py

lstPrices = [5.00, 12.50, 3.25]

# Access an item using its index.
print(f"Original first price: ${lstPrices[0]:.2f}")

# Change the first item.
lstPrices[0] = 6.00

fTotal = 0.0
iCount = 0

print("\nShopping prices:")

for fPrice in lstPrices:
    iCount += 1
    print(f"Item {iCount}: ${fPrice:.2f}")
    fTotal += fPrice

print(f"\nItems purchased: {iCount}")
print(f"Total cost: ${fTotal:.2f}") 
