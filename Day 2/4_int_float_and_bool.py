# Write Code Below This Line 👇

# Integer and Float data types in Python.

num_1 = 123        # Integer
num_2 = -456       # Negative Integer
num_3 = 0          # Zero Integer
num_4 = 3.14       # Float
num_5 = -0.001     # Negative Float
num_6 = 2.0        # Float that is mathematically an integer
num_7 = 0.0        # Zero Float

print(f"Type of {num_1} is: {type(num_1)}")
print(f"Type of {num_2} is: {type(num_2)}")
print(f"Type of {num_3} is: {type(num_3)}")
print(f"Type of {num_4} is: {type(num_4)}")
print(f"Type of {num_5} is: {type(num_5)}")
print(f"Type of {num_6} is: {type(num_6)}")
print(f"Type of {num_7} is: {type(num_7)}")
 

# Converting between Int and Float

int_to_float = float(num_1)  # Convert integer to Float
float_to_int = int(num_4)    # Convert Float to integer (truncates decimal part)

print(f"Converting {num_1} to float gives: {int_to_float} of type: {type(int_to_float)}")
print(f"Converting {num_4} to int gives: {float_to_int} of type: {type(float_to_int)}")

# Arithmetic between Int and Float

int_1, int_2, int_3, int_4, int_5 = 10, 3, 2, 0, -4
float_1, float_2, float_3, float_4, float_5 = 2.5, 4.0, -1.5, 0.0, 2.0

# Addition(+)
print(f"{int_1} + {int_2} = {int_1 + int_2}, Type: {type(int_1 + int_2)}")
print(f"{int_1} + {int_4} = {int_1 + int_4}, Type: {type(int_1 + int_4)}") 
print(f"{int_1} + {float_1} = {int_1 + float_1}, Type: {type(int_1 + float_1)}")
print(f"{int_1} + {float_2} = {int_1 + float_2}, Type: {type(int_1 + float_2)}")
print(f"{float_1} + {float_2} = {float_1 + float_2}, Type: {type(float_1 + float_2)}")
print(f"{float_2} + {float_5} = {float_2 + float_5}, Type: {type(float_2 + float_5)}")
print(f"{float_1} + {float_4} = {float_1 + float_4}, Type: {type(float_1 + float_4)}")


# Subtraction(-)
print(f"{int_1} - {int_2} = {int_1 - int_2}, Type: {type(int_1 - int_2)}")
print(f"{int_1} - {float_1} = {int_1 - float_1}, Type: {type(int_1 - float_1)}")
print(f"{int_1} - {float_2} = {int_1 - float_2}, Type: {type(int_1 - float_2)}")
print(f"{int_4} - {float_1} = {int_4 - float_1}, Type: {type(int_4 - float_1)}")
print(f"{float_1} - {int_4} = {float_1 - int_4}, Type: {type(float_1 - int_4)}")
print(f"{float_1} - {float_2} = {float_1 - float_2}, Type: {type(float_1-float_2)}")
print(f"{float_2} - {float_5} = {float_2 - float_5}, Type: {type(float_2-float_5)}")


# Multiplication(*)
print(f"{int_1}*{int_2} = {int_1*int_2}, Type: {type(int_1*int_2)}")
print(f"{int_1}*{int_4} = {int_1*int_4}, Type: {type(int_1*int_4)}")
print(f"{int_2}*{float_1} = {int_2*float_1}, Type: {type(int_2*float_1)}")
print(f"{int_1}*{float_2} = {int_1*float_2}, Type: {type(int_1*float_2)}")
print(f"{int_4}*{float_1} = {int_4*float_1}, Type: {type(int_4*float_1)}")
print(f"{int_4}*{float_4} = {int_4*float_4}, Type: {type(int_4*float_4)}")
print(f"{float_1}*{float_3} = {float_1*float_3}, Type: {type(float_1*float_3)}")
print(f"{float_2}*{float_5} = {float_2*float_5}, Type: {type(float_2*float_5)}")
print(f"{float_2}*{float_4} = {float_2*float_4}, Type: {type(float_2*float_4)}")

# Division(/)
print(f"{int_1}/{int_2} = {int_1/int_2}, Type: {type(int_1/int_2)}")
print(f"{int_1}/{int_3} = {int_1/int_3}, Type: {type(int_1/int_3)}")
try:
    print(f"{int_1}/{int_4} = {int_1/int_4}, Type: {type(int_1/int_4)}")
except Exception as error:
    print(f"{int_1}/{int_4} = ❌ Error : {error}")
print(f"{int_1}/{float_1} = {int_1/float_1}, Type: {type(int_1/float_1)}")
print(f"{int_4}/{float_1} = {int_4/float_1}, Type: {type(int_4/float_1)}")
print(f"{int_1}/{float_5} = {int_1/float_5}, Type: {type(int_1/float_5)}")
print(f"{int_5}/{float_1} = {int_5/float_1}, Type: {type(int_5/float_1)}")
try:
    print(f"{int_4}/{float_4} = {int_4/float_4}, Type: {type(int_4/float_4)}")
except Exception as error:
    print(f"{int_4}/{float_4} = ❌ Error : {error}")
print(f"{float_1}/{float_2} = {float_1/float_2}, Type: {type(float_1/float_2)}")
print(f"{float_2}/{float_5} = {float_2/float_5}, Type: {type(float_2/float_5)}")
print(f"{float_4}/{float_1} = {float_4/float_1}, Type: {type(float_4/float_1)}")
try:
    print(f"{float_1}/{float_4} = {float_1/float_4}, Type: {type(float_1/float_4)}")
except Exception as error:
    print(f"{float_1}/{float_4} = ❌ Error : {error}")

# Floor Division(//)
print(f"{int_1}//{int_2} = {int_1//int_2}, Type: {type(int_1//int_2)}")
print(f"{int_1}//{int_3} = {int_1//int_3}, Type: {type(int_1//int_3)}")
try:
    print(f"{int_1}//{int_4} = {int_1//int_4}, Type: {type(int_1//int_4)}")
except Exception as error:
    print(f"{int_1}//{int_4} = ❌ Error : {error}")
print(f"{int_1}//{float_1} = {int_1//float_1}, Type: {type(int_1//float_1)}")
print(f"{int_4}//{float_1} = {int_4//float_1}, Type: {type(int_4//float_1)}")
print(f"{int_1}//{float_5} = {int_1//float_5}, Type: {type(int_1//float_5)}")
print(f"{int_5}//{float_1} = {int_5//float_1}, Type: {type(int_5//float_1)}")
try:
    print(f"{int_4}//{float_4} = {int_4//float_4}, Type: {type(int_4//float_4)}")
except Exception as error:
    print(f"{int_4}//{float_4} = ❌ Error : {error}")
print(f"{float_1}//{float_2} = {float_1//float_2}, Type: {type(float_1//float_2)}")
print(f"{float_2}//{float_5} = {float_2//float_5}, Type: {type(float_2//float_5)}")
print(f"{float_4}//{float_1} = {float_4//float_1}, Type: {type(float_4//float_1)}")
try:
    print(f"{float_1}//{float_4} = {float_1//float_4}, Type: {type(float_1//float_4)}")
except Exception as error:
    print(f"{float_1}//{float_4} = ❌ Error : {error}")

# Modulus ( % )
# 📌 NOTE: In Python, the remainder **always takes the sign of the divisor**, not the dividend.
# For any a % b → the result r satisfies:  a = b*q + r   and  sign(r) == sign(b)
print(f"{int_1}%{int_2} = {int_1%int_2}, Type: {type(int_1%int_2)}")
print(f"{int_1}%{int_3} = {int_1%int_3}, Type: {type(int_1%int_3)}")
try:
    print(f"{int_1}%{int_4} = {int_1%int_4}, Type: {type(int_1%int_4)}")
except Exception as error:
    print(f"{int_1}%{int_4 } = ❌ Error : {error}")
print(f"{int_1}%{float_1} = {int_1%float_1}, Type: {type(int_1%float_1)}")
print(f"{int_4}%{float_1} = {int_4%float_1}, Type: {type(int_4%float_1)}")
print(f"{int_1}%{float_5} = {int_1%float_5}, Type: {type(int_1%float_5)}")
print(f"{int_5}%{float_1} = {int_5%float_1}, Type: {type(int_5%float_1)}")
try:
    print(f"{int_4}%{float_4} = {int_4%float_4}, Type: {type(int_4%float_4)}")
except Exception as error:
    print(f"{int_4}%{float_4} = ❌ Error : {error}")
print(f"{float_1}%{float_2} = {float_1%float_2}, Type: {type(float_1%float_2)}")
print(f"{float_2}%{float_5} = {float_2%float_5}, Type: {type(float_2%float_5)}")
print(f"{float_4}%{float_1} = {float_4%float_1}, Type: {type(float_4%float_1)}")
try:
    print(f"{float_1}%{float_4} = {float_1%float_4}, Type: {type(float_1%float_4)}")
except Exception as error:
    print(f"{float_1}%{float_4} = ❌ Error : {error}")
# Modulo with Different Signs (Divisor vs Dividend)
print(f"{int_5}%{int_1} = {int_5%int_1}, Type: {type(int_5%int_1)}")
print(f"{int_1}%{int_5} = {int_1%int_5}, Type: {type(int_1%int_5)}")

# Exponent(**)
print(f"{int_2}**{int_3} = {int_2**int_3}, Type: {type(int_2**int_3)}")
print(f"{int_2}**{int_5} = {int_2**int_5}, Type: {type(int_2**int_5)}")
print(f"{int_5}**{int_3} = {int_5**int_3}, Type: {type(int_5**int_3)}")
print(f"{int_5}**{int_5} = {int_5**int_5}, Type: {type(int_5**int_5)}")
print(f"{int_4}**{int_3} = {int_4**int_3}, Type: {type(int_4**int_3)}")
try:
    print(f"{int_4}**{int_5} = {int_4**int_5}, Type: {type(int_4**int_5)}")
except Exception as error:
    print(f"{int_4}**{int_5} = ❌ Error : {error}")
print(f"{int_2}**{int_4} = {int_2**int_4}, Type: {type(int_2**int_4)}")
print(f"{int_5}**{int_4} = {int_5**int_4}, Type: {type(int_5**int_4)}")
print(f"{int_4}**{int_4} = {int_4**int_4}, Type: {type(int_4**int_4)}")
print(f"{int_2}**{float_1} = {int_2**float_1}, Type: {type(int_2**float_1)}")
print(f"{int_2}**{float_3} = {int_2**float_3}, Type: {type(int_2**float_3)}")
try:
    print(f"{int_5}**{float_3} = {int_5**float_3}, Type: {type(int_5**float_3)}")
except Exception as error:
    print(f"{int_5}**{float_3} = ❌ Error : {error}")
try:
    print(f"{int_5}**{float_1} = {int_5**float_1}, Type: {type(int_5**float_1)}")
except Exception as error:
    print(f"{int_5}**{float_1} = ❌ Error : {error}")
print(f"{int_4}**{float_1} = {int_4**float_1}, Type: {type(int_4**float_1)}")
try:
    print(f"{int_4}**{float_3} = {int_4**float_3}, Type: {type(int_4**float_3)}")
except Exception as error:
    print(f"{int_4}**{float_3} = ❌ Error : {error}")
try:
    print(f"{float_4}**{int_5} = {float_4**int_5}, Type: {type(float_4**int_5)}")
except Exception as error:
    print(f"{float_4}**{int_5} = ❌ Error : {error}")
print(f"{float_4}**{int_3} = {float_4**int_3}, Type: {type(float_4**int_3)}")
print(f"{int_2}**{float_4} = {int_2**float_4}, Type: {type(int_2**float_4)}")
print(f"{int_5}**{float_4} = {int_5**float_4}, Type: {type(int_5**float_4)}")
print(f"{float_1}**{int_4} = {float_1**int_4}, Type: {type(float_1**int_4)}")
print(f"{float_3}**{int_4} = {float_3**int_4}, Type: {type(float_3**int_4)}")
print(f"{int_4}**{float_4} = {int_4**float_4}, Type: {type(int_4**float_4)}")
print(f"{float_1}**{float_1} = {float_1**float_1}, Type: {type(float_1**float_1)}")
try:
    print(f"{float_3}**{float_1} = {float_3**float_1}, Type: {type(float_3**float_1)}")
except Exception as error:
    print(f"{float_3}**{float_1} = ❌ Error : {error}")
try:
    print(f"{float_3}**{float_3} = {float_3**float_3}, Type: {type(float_3**float_3)}")
except Exception as error:
    print(f"{float_3}**{float_3} = ❌ Error : {error}")
print(f"{float_1}**{float_3} = {float_1**float_3}, Type: {type(float_1**float_3)}")
print(f"{float_4}**{float_1} = {float_4**float_1}, Type: {type(float_4**float_1)}")
try:
    print(f"{float_4}**{float_3} = {float_4**float_3}, Type: {type(float_4**float_3)}")
except Exception as error:
    print(f"{float_4}**{float_3} = ❌ Error : {error}")
print(f"{float_1}**{float_4} = {float_1**float_4}, Type: {type(float_1**float_4)}")
try:
    print(f"{float_3}**{float_4} = {float_3**float_4}, Type: {type(float_3**float_4)}")
except Exception as error:
    print(f"{float_3}**{float_4} = ❌ Error : {error}")
print(f"{float_4}**{float_4} = {float_4**float_4}, Type: {type(float_4**float_4)}")


# 🧠 Operator Precedence in Python (PEMDASLR)
#
# P → Parentheses (...)
# E → Exponentiation (**)                  → Right-to-Left ⚠️
# M/D → Multiplication (*), Division (/), Floor Division (//), Modulo (%)
#        → Same precedence, evaluated Left-to-Right
# A → Addition (+)
# S → Subtraction (-)
#
# ✅ All operators except exponentiation are evaluated Left-to-Right.
# ✅ Use parentheses to make the intended order explicit when in doubt.

# Python follows standard precedence rules when evaluating expressions.

expr_1 = 10 + 5 * 2       # Multiplication before Addition
expr_2 = (10 + 5) * 2     # Parentheses change the order
expr_3 = 2 ** 3 * 4       # Exponent before Multiplication
expr_4 = 2 ** (3 * 4)     # Parentheses change the order again
expr_5 = 10 - 4 + 2       # Left to right for operators of the same precedence

print(expr_1)  # 20  (5*2=10, then 10+10)
print(expr_2)  # 30  (10+5=15, then 15*2)
print(expr_3)  # 32  (2**3=8, 8*4=32)
print(expr_4)  # 4096  (3*4=12, 2**12=4096)
print(expr_5)  # 8  (10-4=6, 6+2=8)

expr_6 = 10 + 4 // 2 * 3 % 5
# Step by step:
# 4 // 2 = 2
# 2 * 3 = 6
# 6 % 5 = 1
# 10 + 1 = 11
print(expr_6)  # 11


# # Big Numbers in Python (Arbitrary-Precision Integers)
big_num = 10**50
large_num = 123_234_147_247
print(f"Type of big number \"{big_num}\" is: {type(big_num)}")  # Same as a small integer (Python uses arbitrary-precision integers)
print(f"Type of large number \"{large_num}\" is: {type(large_num)}")  # Underscores improve readability; Python interprets it as a normal number

# Introduction to Boolean

bool_1 = True
bool_2 = False

print(f"Type of {bool_1} is: {type(bool_1)}")
print(f"Type of {bool_2} is: {type(bool_2)}")

print(isinstance(bool_1,int)) # Bool is a subclass of int

# Bool to Int & Float
print(int(True))    # 1
print(int(False))   # 0
print(float(True))  # 1.0
print(float(False)) # 0.0

# Int/Float to Bool
print(bool(0))       # False
print(bool(5))       # True
print(bool(-5))      # True
print(bool(0.0))     # False
print(bool(-2.5))    # True
print(bool(5.6))     # True

# Truthy/Falsy Values
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False
print(bool([1]))     # True
print(bool("Hi"))    # True

# Arithmetic with Boolean values
# Remember: Bool is a subclass of Int
# True  → 1
# False → 0

# ✅ Bool with Bool
print(True + True)      # 2
print(True + False)     # 1
print(False + False)    # 0

print(True - True)      # 0
print(True - False)     # 1
print(False - True)     # -1

print(True * True)      # 1
print(True * False)     # 0
print(False * False)    # 0

# Division between Bools → gives Float result
print(True / True)      # 1.0
# print(True / False)   # ❌ ZeroDivisionError (1/0)
# print(False / False)  # ❌ ZeroDivisionError (0/0)

# Floor division & modulo with Bool
print(True // True)     # 1
# print(True // False)  # ❌ ZeroDivisionError
print(False // True)    # 0

print(True % True)      # 0
print(False % True)     # 0
# print(True % False)   # ❌ ZeroDivisionError

print(True ** True)     # 1
print(True ** False)    # 1  (1^0 = 1)
print(False ** True)    # 0  (0^1 = 0)
print(False ** False)   # 1  (0^0 = 1 — Python defines it this way)

# ✅ Bool with Int
print(True + 5)         # 6
print(False + 5)        # 5
print(True * 10)        # 10
print(False * 10)       # 0
print(10 - True)        # 9
print(10 - False)       # 10
print(10 / True)        # 10.0
# print(10 / False)     # ❌ ZeroDivisionError

print(10 // True)       # 10
# print(10 // False)    # ❌ ZeroDivisionError
print(10 % True)        # 0
# print(10 % False)     # ❌ ZeroDivisionError
print(2 ** True)        # 2
print(2 ** False)       # 1

# ✅ Bool with Float
print(True + 2.5)       # 3.5
print(False + 2.5)      # 2.5
print(True * 2.5)       # 2.5
print(False * 2.5)      # 0.0
print(2.5 - True)       # 1.5
print(2.5 - False)      # 2.5
print(2.5 / True)       # 2.5
# print(2.5 / False)    # ❌ ZeroDivisionError

print(2.5 // True)      # 2.0
# print(2.5 // False)   # ❌ ZeroDivisionError
print(2.5 % True)       # 0.5
# print(2.5 % False)    # ❌ ZeroDivisionError
print(2.5 ** True)      # 2.5
print(2.5 ** False)     # 1.0

# Checking Object Types Using isinstance()
print(isinstance(3.14, float))
print(isinstance(10, int))
print(isinstance("abc",int))
print(isinstance('abc',(int,float,str)))
print(isinstance(True, bool))
print(isinstance(True, int))
