# numberMultiplier2.py

while True:
    try:
        iNum = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue
    iTotal = 0
    for iCount in range(1, 6):
        iResult = iNum * iCount
        print(iResult)
        iTotal += iResult
    print(f"\nFinal Total: {iTotal}")
    sRedo = input("\nTry another number? (Y/N): ")
    # sRedo = input("\nTry another number? (Y/N): ").upper() 
    if sRedo == 'N' or sRedo == 'n':
    # if sRedo == 'N':
        print("Later dude! 👋")
        break
    else:
        continue
