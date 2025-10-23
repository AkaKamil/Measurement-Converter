from time import sleep

def cmtoinches():
    try:    
        cm = float(input("Enter the amount of centimeters you would like to convert to inches:"))
        inchfromcm = cm/2.54
        print(f"{cm}cm in inches is {inchfromcm:.2f} inches")
    except ValueError:
        print("Invalid input. Please enter a number.")

def inchestocm():
    try:
        inches = float(input("Enter the amount of inches you would like to convert to centimeters:"))
        cmfrominches = inches * 2.54
        print(f"{inches} inches in centimeters is {cmfrominches:.2f} cm")
    except ValueError:
        print("Invalid input. Please enter a number.")

def feettocm():
    try:    
        feet = float(input("Enter the amount of feet you would like to convert to centimeters:"))
        cmfromfeet = feet * 30.48
        print(f"{feet} feet in centimeters is {cmfromfeet:.2f} cm")
    except ValueError:
        print("Invalid input. Please enter a number.")

def cmtofeet():
    try:
        cm = float(input("Enter the amount of centimeters you would like to convert to feet:"))
        feetfromcm = cm / 30.48
        print(f"{cm} cm in feet is {feetfromcm:.2f} feet")
    except ValueError:
        print("Invalid input. Please enter a number.")

def yardstometres():
    try:    
        yards = float(input("Enter the amount of yards you would like to convert to metres:"))
        metresfromyards = yards * 0.9144
        print(f"{yards} yards in metres is {metresfromyards:.2f} metres")
    except ValueError:
        print("Invalid input. Please enter a number.")

def metrestoyards():
    try:    
        metres = float(input("Enter the amount of metres you would like to convert to yards:"))
        yardsfrommetres = metres / 0.9144
        print(f"{metres} metres in yards is {yardsfrommetres:.2f} yards")
    except ValueError:
        print("Invalid input. Please enter a number.")

def welcome():
    print("Welcome to Kamil's measurement converter!")
    sleep(1)
    name=input("Please enter your name:")
    sleep(1)
    print("Hello", name)
    sleep(1)
    
    while True:    
        measuredecision= input(
        "Which would you like to do today:?\n"
        "1. CM to Inches\n"
        "2. Inches to CM\n"
        "3. Feet to CM\n"
        "4. CM to feet\n"
        "5. Yards to Metres\n"
        "6. Metres to Yards\n"
        "7. Exit\n"
        "Please enter option here:")
    
    
        if measuredecision == "1":
            sleep(1)
            cmtoinches()
        elif measuredecision == "2":
            sleep(1)
            inchestocm()
        elif measuredecision == "3":
            sleep(1)
            feettocm()
        elif measuredecision == "4":
            sleep(1)
            cmtofeet()
        elif measuredecision == "5":
            sleep(1)
            yardstometres()
        elif measuredecision == "6":
            sleep(1)
            metrestoyards()
        elif measuredecision == "7":
            sleep(1)
            print("Goodbye", name)
            break 
        else:
            print("Please choose from options above")

welcome()