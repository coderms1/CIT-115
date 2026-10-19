# movieAge.py

# INPUT (prompt user)

## Error Handling (try)
try:
    iAge = int(input("How old are you?: "))

# LOGIC / OUTPUT
    if(iAge >= 18 and iAge < 85):
        print("Enjoy the movie! 🍿🥤")
    elif(iAge >= 85):
        sDocNote = input("Do you have doc note? (Y/N): ")
        if(sDocNote == 'Y' or sDocNote == 'y'):
            print("Enjoy the movie! 🍿🥤")
        else:
            print("So sorry, must have doc note.")
    else:
        print("NO ENTRY! 🚫")
      
## Error Handling (except)
except ValueError:
    print("Please enter your age as a whole number.")
