# numberMultiplier.py

try:
    iNum = int(input("Enter a whole number: "))
    iTotal = 0
    # For loop iterates 5 times
    for iCount in range(1, 6):
        iResult = iNum * iCount
        print(f"{iNum} x {iCount} = {iResult}")
        iTotal += iResult
    print(f"\nFinal Total: {iTotal}")
except ValueError:
    print("Invalid input! Please enter a whole number.")
