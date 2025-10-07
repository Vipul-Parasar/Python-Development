# Write Code Below This Line 👇

total_bill = float(input("What was the total Bill?\n"))
percentage_tip = float(input("How much Tip would you like to give in %?\n"))
number_of_person = int(input("How many people to split the bill?\n"))

each_split = round(((total_bill*(1+(percentage_tip/100)))/(number_of_person)),2)

print(f"Each one has to pay = {each_split}")