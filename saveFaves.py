# saveFavs.py

# Create a program that saves a user's name and favorite game to a 
# text file, then reads the file and displays its contents.

sName = input("Enter your name: ")
sGame = input("Enter your favorite game: ")
sFood = input("Enter your favorite food: ")

with open("saveFavs.txt", "a") as file:
    file.write(f"{sName} | {sGame} | {sFood}\n")

print("Saved to saveFavs.txt!")

iCount = 0

print("\nEveryone's favorites:")
with open("saveFavs.txt", "r") as file:
    for sLine in file:
        iCount += 1
        print(f"{iCount}. {sLine.strip()}")

print(f"\nTotal entries: {iCount}")
