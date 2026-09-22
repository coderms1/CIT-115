# Project: Roadtrip Calculator
# Author: (Your name here)
# Class: Python 1
# Due: 9/24/26

# Get trip information from the user
sDestination = input("Where are you traveling to? ")
fDistance = float(input("How many miles away is it? "))
fGasPrice = float(input("What is the current price of gas? "))
fMilesPerGallon = float(input("How many miles per gallon does your car get? "))

# Calculate the trip
fGallonsNeeded = fDistance / fMilesPerGallon
fGasCost = fGallonsNeeded * fGasPrice

# Display the results
print("\n--- Road Trip Calculator ---")
print("Destination:", sDestination)
print("Distance:", fDistance, "miles")
print(f"Gallons Needed: {fGallonsNeeded:.2f}")
print(f"Estimated Gas Cost: ${fGasCost:.2f}")
