# dailySales.py
print("Daily Sales Tracker 📊")
fTotalSales = 0.0

for iDay in range(1, 6):
    fSales = float(input(f"Enter sales for Day {iDay}: $"))
    fTotalSales += fSales
    if fSales >= 500:
        print("Great sales day!")
    elif fSales >= 100 and fSales < 500:
        print("Sales were in normal range.")
    else:
        print("Pay has been docked.")

fAverageSales = fTotalSales / 5

print("\n### SALES REPORT ###")
print(f"Total Sales: ${fTotalSales:.2f}")
print(f"Average Sales: ${fAverageSales:.2f}")
