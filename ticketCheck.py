# ticketCheck.py

# INPUT (prompt user)
while True:
  # Error validation
    try:
        fMoney = float(input("How much money do you have? $"))
        break
    except ValueError:
        print("Please enter a number.")

bCanAfford = fMoney >= 10

# LOGIC & OUTPUT (display results)
if bCanAfford:
    print("You can afford a ticket!")
else:
    print("You need more money.")
