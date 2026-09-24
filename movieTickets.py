# movieTickets.py
# Due: 9/29/26

# IF / ELSE Statements

## STRING -  Text
## INT -  Whole Number
## FLOAT  -  DECIMALS
## BOOLEAN  -  True / False

## EQUAL SIGN: 
#### Comparison Operator-> ==
#### Assignment Operator-> = 
## >   //  >=
## <   //  <=

iAge = int(input("How old are you?: "))

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
