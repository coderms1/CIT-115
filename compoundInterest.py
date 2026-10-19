# compoundInterest.py

# FV = PV(1 + r/m) ** (m * t)

# INPUT (prompt user for data)
fPrincipal = float(input("Enter the s  arting principal: $"))
fRate = float(input("Enter the annual interest rate (%): "))
iFrequency = int(input("How many times per year is the interest compounded? "))
fYears = float(input("For how many years will the account earn interest? "))

# LOGIC (calculate the future value)
fRate = fRate / 100
fFutureValue = fPrincipal * (1 + fRate / iFrequency) ** (iFrequency * fYears)

# OUTPUT (display formatted results)
print(f"\nAt the end of {fYears} years you will have ${fFutureValue:,.2f}")
