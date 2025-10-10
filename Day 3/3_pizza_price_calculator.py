# Write Code Below This Line 👇

print("--Welcome To Pizza Mania--")

size = str(input("What Size of Pizza do you want? S, M or L\n").strip().upper())
pepperoni = str(input("Do you want pepperoni on your pizza? Y or N").strip().upper())
cheese = str(input("Do you want extra cheese? Y or N:").strip().upper())

total_bill=0
error = 0

if size != "L" and size != "M" and size != "S":
    print("Please Enter a Valid Size.")
    error += 1
elif size == "L":
    total_bill += 25
    print("Large Size Pizza Selected")
    
    if pepperoni == "Y":
        print("Extra Pepperoni Added")
        total_bill += 3
    elif pepperoni == "N":
        pass
    else:
        print("Select a Valid Pepperoni Option.")
        error += 1
    
    if error == 0:
        if cheese == "Y":
            print("Extra Cheese Added")
            total_bill += 2
        elif cheese == "N":
            pass
        else:
            print("Select a Valid Cheese Option.")
            error += 1
elif size == "M":
    total_bill += 20
    print("Medium Size Pizza Selected")
    
    if pepperoni == "Y":
        print("Extra Pepperoni Added")
        total_bill += 3
    elif pepperoni == "N":
        pass
    else:
        print("Select a Valid Pepperoni Option.")
        error += 1
    
    if error == 0:
        if cheese == "Y":
            print("Extra Cheese Added")
            total_bill += 2
        elif cheese == "N":
            pass
        else:
            print("Select a Valid Cheese Option.")
            error += 1
elif size == "S":
    total_bill += 15
    print("Small Size Pizza Selected")
    
    if pepperoni == "Y":
        print("Extra Pepperoni Added")
        total_bill += 2
    elif pepperoni == "N":
        pass
    else:
        print("Select a Valid Pepperoni Option.")
        error += 1
    
    if error == 0:
        if cheese == "Y":
            print("Extra Cheese Added")
            total_bill += 2
        elif cheese == "N":
            pass
        else:
            print("Select a Valid Cheese Option.")
            error += 1
    
if error == 0:
    print(f"Your total bill is: ${total_bill}")
else:
    print("Transaction Error")
        