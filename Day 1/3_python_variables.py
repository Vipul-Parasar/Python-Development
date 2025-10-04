# Write you code below this line 👇

# Variable Naming Best Practices and Rules:
# 1. Use descriptive names that reflect the variable's purpose (e.g., user_age, city_name).
# 2. Variable names must start with a letter (a-z, A-Z) or underscore (_), not a number.
# 3. Only letters, numbers, and underscores are allowed (no spaces or special characters).
# 4. Variable names are case-sensitive (user and User are different).
# 5. Avoid using Python reserved keywords (like 'for', 'if', 'class', etc.).
# 6. Use lowercase letters for variable names (snake_case is preferred: my_variable).
# 7. Do not use single letters except for temporary or loop variables.
# 8. Avoid starting variable names with underscores unless needed for special purposes.
# 9. Make variable names meaningful and easy to read.

# Examples:
# Good: user_name, total_amount, is_valid
# Bad: x, temp, 1stValue, my-variable, for

# 1. Create variables for your name age and city and print them in sentence.
name = input("What's your name? ")
age = input("How old are you? ")
city = input("Which city do you live in? ")

print("Hello, my name is " + name + ", I am " + age + " years old and I live in " + city +".")

# 2(a). Swap the values of two variables using tuple unpacking/multiple assignments.
glass1 = "Milk"
glass2 = "Water"
print(glass1,glass2)

glass1,glass2 = glass2,glass1
print(glass1,glass2)

# 2(b). Swap the values of two string variables with using a thrid variable

glass1 = "Milk"
glass2 = "Water"
print(glass1,glass2)

temp_var = glass1
glass1 = glass2
glass2 = temp_var
print(glass1,glass2)

# 2 (c). Swap the values of two string variables without using a third variable or tuple unpacking.

glass1 = "Milk"
glass2 = "Water"
print(glass1,glass2)

glass1 = glass1+glass2 # glass1 now contains "MilkWater"
glass2 = glass1[:len(glass1)-len(glass2)] # length of glass1 =len("MilkWater")=9, length of glass2=len("Water")=5, so glass2=glass1[:9-5]=glass1[:4]="Milk"
glass1 = glass1[len(glass2):] # glass1=glass1[4:]="Water"
print(glass1,glass2)

# 3(a). Swap the values of two integer variables without using a third variable or tuple unpacking.

int_1 = 10
int_2 = 20
print(int_1,int_2)

int_1 = int_1 + int_2 # int_1 now contains 30
int_2 = int_1 - int_2 # int_2 = 30 - 20 = 10
int_1 = int_1 - int_2 # int_1 = 30 - 10 = 20
print(int_1,int_2)

# 3(b). Swap the values of two integer variables using bitwise XOR operator.
int_1 = 10
int_2 = 20
print(int_1,int_2)

# XOR operator properties: a^a=0, a^0=a, a^b^a=b
int_1 = int_1 ^ int_2 # int_1 now contains XOR of int_1 and int_2
int_2 = int_1 ^ int_2 # int_2 becomes original int_1
int_1 = int_1 ^ int_2 # int_1 becomes original int_2
print(int_1,int_2)