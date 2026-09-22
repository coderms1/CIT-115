# Project: Snack Calculator
# Author: (Your name here)
# Class: Python 1
# Due: 9/24/26

TAX = 0.0625
# INPUT (Prompt user)
sSnack = input("Name of snack: ")
fPrice = float(input("Price of 1 snack: "))
iNumSnacks = int(input("Number of snacks: "))
# LOGIC (Calculations)
fSubTotal = (fPrice * iNumSnacks)
fSalesTax = (fSubTotal * TAX)
fTotalCost = (fSubTotal + fSalesTax)
# OUTPUT (Display results)
print(" --- RECEIPT ---")
print(f"Subtotal: {fSubTotal:,.2f}")
print(f"Tax: {fSalesTax:,.2f}")
print(f"Total: {fTotalCost:,.2f}")
print(" -------------- ")
