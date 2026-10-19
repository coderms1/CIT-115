# savingsGoal.py

#INPUT (prompt user for data)
sGoalName = input("Account Name: ")
fGoal = float(input("Goal amount: $"))
iTime = int(input("Months planned to save: "))

fSaved = 0.0
iMonths = 0

# LOGIC (calculations)
while iMonths < iTime:
    iMonths += 1
    fDeposit = float(input(f"month {iMonths} of {iTime} - deposit: $"))
    if fDeposit < 0:
        fDeposit = 0
    fSaved += fDeposit

fAverage = 0.0
if iMonths > 0:
    fAverage = fSaved / iMonths

#OUTPUT (display results)
print("\nSavings Summary:\n")
print("-" * 20)
print(f"\nAccount Name: {sGoalName}")
print(f"Time period: {iTime} months")
print(f"Saved: ${fSaved:.2f} of ${fGoal:.2f}")
print(f"Average per month: ${fAverage:.2f}")

if fSaved >= fGoal:
    print(f"Goal reached! Extra saved: ${fSaved - fGoal:.2f}")
    print()
else:
    print(f"Missed your goal. Still needed: ${fGoal - fSaved:.2f}")
    print()
