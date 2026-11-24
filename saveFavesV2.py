# saveFavsV2.py

# Create a program that saves a user's name and favorite game to a 
# text file, then reads the file and displays its contents.

sName = input("Enter your name: ")
sGame = input("Enter your favorite game: ")
sFood = input("Enter your favorite food: ")

while True:
    try:
        iHours = int(input("How many hours a week do you play it? "))
        break
    except ValueError:
        print("Please enter a whole number.")

with open("gameFoodFavs.txt", "a") as file:
    file.write(f"{sName} | {sGame} | {sFood} | {iHours} hrs\n")

print("Saved to gameFoodFavs.txt!")

iCount = 0

print("\nEveryone's favorites:")
with open("gameFoodFavs.txt", "r") as file:
    for sLine in file:
        iCount += 1
        print(f"{iCount}. {sLine.strip()}")

print(f"\nTotal entries: {iCount}")
