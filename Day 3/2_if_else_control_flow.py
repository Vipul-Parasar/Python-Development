# Write Code Below This Line 👇

# 🧠 IF-ELSE CONTROL FLOW IN PYTHON


# Control flow determines *which part* of the code executes
# depending on whether a condition is True or False.
#
# Python uses indentation (spaces) to define code blocks.
# The syntax is:
#
#   if condition:
#       # code block (executes if condition is True)
#   else:
#       # executes when condition is False

# 1️⃣ BASIC IF STATEMENT

if True:
    print("This always runs")
else:
    print("This never runs")

if False:
    print("This never runs")
else:
    print("This always runs")

if True:
    print("This does not have any else.")  # We can have if by itself


age = int(input("What's your current age in years?\n"))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")


# MULTIPLE IF STATEMENTS

temper = int(input("🌡️ What's the temperature today (°C)? [Range: -15 to 50]\n"))

# WEATHER DESCRIPTION
if temper < 0:
    print("❄️ Freezing cold — heavy snow or frost expected.")
if 0 <= temper < 10:
    print("🥶 Cold and chilly — you'll need to bundle up.")
if 10 <= temper < 20:
    print("🌤️ Mild and pleasant weather.")
if 20 <= temper < 30:
    print("☀️ Warm and comfortable day.")
if temper >= 30:
    print("🥵 Hot and sunny — could feel humid or dry depending on region.")

# CLOTHING RECOMMENDATION
if temper < 0:
    print("🧣 Wear thermal layers, heavy coat, gloves, and boots.")
if 0 <= temper < 5:
    print("🧥 Thick jacket and warm cap recommended.")
if 5 <= temper < 15:
    print("🧶 Sweater or light winter wear should be fine.")
if 15 <= temper < 25:
    print("👕 Light clothes or full sleeves for comfort.")
if 25 <= temper < 35:
    print("🩳 Summer wear — T-shirts, cotton shirts, stay hydrated.")
if temper >= 35:
    print("🕶️ Loose, breathable clothes, hat, and sunglasses — avoid heat exposure.")

# SUGGESTED ACTIVITY
if temper < 0:
    print("🏠 Stay indoors, enjoy a hot drink, and keep warm.")
if 0 <= temper < 5:
    print("☕ Cozy day for reading indoors or light indoor workouts.")
if 5 <= temper < 10:
    print("🚶 Short morning walk or quick errand outside.")
if 10 <= temper < 20:
    print("🚴 Perfect for outdoor sports, biking, or sightseeing.")
if 20 <= temper < 30:
    print("🏖️ Ideal for picnics, park walks, or light activities.")
if 30 <= temper < 35:
    print("🏊 Swimming or staying near water would be refreshing.")
if temper >= 35:
    print("🧊 Stay home in AC, hydrate, and avoid outdoor work.")

# Each 'if' section (weather, clothing, activity) is independent.
# That means:
#   - Weather message prints based on temperature range
#   - Clothing message prints based on temperature range
#   - Activity message prints based on temperature range

# All 3 sections run independently — this is the essence of
# MULTIPLE IF statements: several unrelated decisions happening in parallel.


# 🌦️ IF-ELIF-ELSE STATEMENTS

temper = int(input("🌡️ What's the temperature today (°C)? [Range: -15 to 50]\n"))

if temper < 0:
    print("❄️ Weather: Freezing cold — expect snow or frost.")
    print("👕 Clothing: Heavy jacket, gloves, scarf, boots.")
    print("🎯 Activity: Stay indoors, have soup, and keep warm.")

elif temper < 10:
    print("🥶 Weather: Cold and frosty morning.")
    print("👕 Clothing: Thick sweater or jacket.")
    print("🎯 Activity: Short walk or cozy indoor reading day.")

elif temper < 20:
    print("🌤️ Weather: Mild and pleasant.")
    print("👕 Clothing: Light jacket or long sleeves.")
    print("🎯 Activity: Great for jogging or light outdoor fun.")

elif temper < 30:
    print("☀️ Weather: Warm and comfortable.")
    print("👕 Clothing: T-shirt and breathable cotton wear.")
    print("🎯 Activity: Perfect picnic or park day!")

elif temper < 40:
    print("🔥 Weather: Hot and sunny day ahead.")
    print("👕 Clothing: Light cotton clothes, sunglasses, cap.")
    print("🎯 Activity: Stay hydrated — ideal for swimming or relaxing indoors.")

else:
    print("🥵  Weather: Scorching heat — extreme temperatures!")
    print("👕 Clothing: Very light clothes, hat, sunscreen, and lots of water.")
    print("🎯 Activity: Avoid going out — stay in AC and hydrate frequently.")

# In if-elif-else chain, Python checks conditions from top to bottom.
# As soon as one condition is True, it executes that block
# and SKIPS all remaining conditions.
# This ensures only ONE block of code is printed persection.

# Compare this with “multiple if”:
#    - There, all conditions were checked independently.
#    - Here, Python stops after the first True condition.


# Nested If Statements:

print("-- Welcome to INOX Cinemas --")

ticket = int(input("""
Which Ticket do you want?
Type 1 → Regular  (₹200)
Type 2 → Premium  (₹350)
Type 3 → VIP      (₹700)
Enter ticket type (1/2/3): 
""").strip())

age = int(input("What's your age in years? (0-100): ").strip())
popcorn = input("Do you want popcorn for ₹300? (yes/no): ").strip().lower()

total_bill = 0
error = 0

if ticket == 1:
    total_bill = 200
    print("\n🎫 Regular Ticket Selected — ₹200")

    if 0 <= age < 12:
        print("👦 Child discount applied (20% off).")
        total_bill *= 0.8
    elif age < 60:
        print("🧍 Standard adult rate applies.")
    elif 60 <= age <= 100:
        print("👴 Senior citizen discount applied (10% off).")
        total_bill *= 0.9
    else:
        print("❌ Please enter a valid age (0-100).")
        error += 1

    if popcorn == "yes":
        print("🍿 Popcorn added (+₹300).")
        total_bill += 300
    elif popcorn == "no":
        print("🚫 No popcorn selected.")
    else:
        print("⚠️ Please reply 'yes' or 'no' for popcorn.")
        error += 1
elif ticket == 2:
    total_bill = 350
    print("\n🎫 Premium Ticket Selected — ₹350")

    if 0 <= age < 12:
        print("👦 Child discount applied (20% off).")
        total_bill *= 0.8
    elif age < 60:
        print("🧍 Standard adult rate applies.")
    elif 60 <= age <= 100:
        print("👴 Senior citizen discount applied (10% off).")
        total_bill *= 0.9
    else:
        print("❌ Please enter a valid age (0-100).")
        error += 1

    if popcorn == "yes":
        print("🍿 Popcorn added (+₹300).")
        total_bill += 300
    elif popcorn == "no":
        print("🚫 No popcorn selected.")
    else:
        print("⚠️ Please reply 'yes' or 'no' for popcorn.")
        error += 1
elif ticket == 3:
    total_bill = 700
    print("\n🎫 VIP Ticket Selected — ₹700")

    if 0 <= age < 12:
        print("👦 Child discount applied (20% off).")
        total_bill *= 0.8
    elif age < 60:
        print("🧍 Standard adult rate applies.")
    elif 60 <= age <= 100:
        print("👴 Senior citizen discount applied (10% off).")
        total_bill *= 0.9
    else:
        print("❌ Please enter a valid age (0-100).")
        error += 1

    if popcorn == "yes":
        print("🍿 Popcorn added (+₹300).")
        total_bill += 300
    elif popcorn == "no":
        print("🚫 No popcorn selected.")
    else:
        print("⚠️ Please reply 'yes' or 'no' for popcorn.")
        error += 1
else:
    print("\n❌ Invalid ticket type selected.")
    error += 1


if error == 0:
    print(f"\n✅ Enjoy your movie! Your total bill is ₹{total_bill:.2f}") # .2f to print exactly two digits after the deco=imal point.
else:
    print("\n🚫 Transaction failed.")

# 🧠 Truthy & Falsy Values in conditions.

# In Python, conditions don’t always have to be strictly True or False.
# Any value can be evaluated in a Boolean context.
# Values considered "Falsy" behave like False in conditions.
# Everything else is considered "Truthy".

# ⚫ Falsy values → 0, 0.0, "", [], {}, set(), None, False
# ⚪ Truthy values → All non-empty / non-zero values

user_input = ""
if user_input:
    print("You entered something!")
else:
    print("You entered nothing!")

num = 10
if num:
    print("✅ Non-zero numbers are truthy.")
else:
    print("❌ Zero is falsy.")

num = 0
if num:
    print("✅ Non-zero numbers are truthy.")
else:
    print("❌ Zero is falsy.")

value = None
if value:
    print("✅ None is truthy.")
else:
    print("❌ None is falsy.")

print("\n=== Combining Conditions with and / or / not ===")


# Logical operators allow combining multiple comparisons.

temperature = 25
is_raining = False
is_weekend = True

# AND → All conditions must be True
if temperature > 20 and not is_raining:
    print("🌤️ Great day for a walk!")

# OR → At least one condition must be True
if is_raining or temperature < 10:
    print("☔ Stay indoors or carry an umbrella.")
else:
    print("🌞 No rain expected today.")

# NOT → Negates the condition
if not is_weekend:
    print("🏢 Time to work!")
else:
    print("🎉 It's the weekend, enjoy your movie!")

# Combining multiple in one line
if (temperature > 15 and temperature < 35) or is_weekend:
    print("🌈 Perfect time for an outing!")


# Use of Pass
# `pass` is a no-operation statement — it does nothing.
# It’s used as a placeholder to keep code syntactically valid.

is_admin = False

if is_admin:
    pass  # Reserved for future code (prevents syntax error)
else:
    print("Access Denied — Admin Only Section.")


#Ternary Conditional Expressions

# Syntax:
# variable = value_if_true if condition else value_if_false

age = 24
status = "Adult" if age >=18 else "Minor"

print(f"Status: {status}")

num = 7
category = "Even" if num > 0 and num % 2 == 0 else ("Odd" if num > 0 and num % 2 != 0 else "Negative")

print(f"{category}")
