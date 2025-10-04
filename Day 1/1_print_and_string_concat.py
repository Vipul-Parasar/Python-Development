# Write you code below this line 👇

print("Hello World!")

# Printing Exercise

# Method 1: Using \n escape sequence to print each step on a new line.
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

# Method 2: Using triple quotes (''' or """) to create a multi-line string.
print('''1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.''')

# Method 3: Using multiple print statements for each line.
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Concatination Exercise

# 1. Concatenate two strings
string1 = "Python"
string2 = "Rocks"
print(string1+" "+string2)

# 2. Concatenate a string and a number
age = 28
print("I am "+str(age)+" years old.")

# 3. Concatenate with special characters
greeting = "Hello!"
name = "Alice"
print(greeting+" "+name+"."+"\n"+"How are you?")

# 4. Concatenate using += operator
message = "Learning"
message += " Python"
message += " is fun!"
print(message)

# 5. Concatenate empty strings and check results
empty = ""
word = "Hi!"
print(empty + word)

# 6. Concatenate using Parentheses for long strings
long_string= ("This is a very long string that "
              "spans multiple lines and "
              "is concatenated automatically.")
print(long_string)

