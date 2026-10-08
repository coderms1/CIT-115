# gradeChecker.py

# INPUT (prompt user for data)
## Get student's name
sName = input("Enter the student's name: ")
 
## Get three grades
iGrade1 = int(input("Enter Grade #1: "))
iGrade2 = int(input("Enter Grade #2: "))
iGrade3 = int(input("Enter Grade #3: "))

# LOGIC (Calculations/Conditions)
## Calculate the average
fAverage = (iGrade1 + iGrade2 + iGrade3) / 3

## Determine the letter grade
if fAverage >= 90:
    sLetterGrade = "A"
elif fAverage >= 80:
    sLetterGrade = "B"
elif fAverage >= 70:
    sLetterGrade = "C"
elif fAverage >= 60:
    sLetterGrade = "D"
else:
    sLetterGrade = "F"

# OUTPUT (display results)
## Display results
print("\n--- Grade Results ---")
print("Student:", sName)
print(f"Average: {fAverage:.2f}")
print("Letter Grade:", sLetterGrade)
