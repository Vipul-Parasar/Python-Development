# Write Code Below This Line 👇

# Logical Operators in Python

# There are 3 logical operators in Python:
#   and → True if both operands are True
#   or  → True if at least one operand is True
#   not → Inverts the boolean value (True ↔ False)

print(f"True and True gives: {True and True}")
print(f"True and False gives: {True and False}")
print(f"False and True gives: {False and True}")
print(f"False and False gives: {False and False}")

print(f"True or True gives: {True or True}")
print(f"True or False gives: {True or False}")
print(f"False or True gives: {False or True}")
print(f"False or False gives: {False or False}")

print(f"not True gives: {not True}")
print(f"not False gives: {not False}")

# Operator Precedence
# not has highest precedence, then and, then or
# Parentheses can override the natural precedence

print(f"Expression \"True or False and False\" gives: {True or False and False}")
print(f"Expression \"not True or False\" gives: {not True or False}")
print(f"Expression \"not (True or False)\" gives: {not (True or False)}")
print(f"Expression \"(True and False) or True\" gives: {(True and False) or True}")
print(f"Expression \"True or False and False\" gives: {True or False and False}")
print(f"Expression \"(True or False) and False\" gives: {(True or False) and False}")

# Truthy / Falsy Values with Logical Operators
# In Python:
#   Falsy values include → 0, 0.0, "", [], {}, None, False
#   Everything else is considered Truthy.
# and → returns first falsy or last truthy
# or  → returns first truthy or last falsy

print(f"10 and 20       → {10 and 20}")                 # both truthy → returns last
print(f"0 and 5         → {0 and 5}")                   # first falsy → returns 0
print(f"'' or 'Hello'   → {'' or 'Hello'}")             # '' falsy, so returns 'Hello'
print(f"None or 100     → {None or 100}")               # None falsy, returns 100
print(f"[] and 'Hi'     → {[] and 'Hi'}")               # [] falsy, returns []
print(f"'Hi' and []     → {'Hi' and []}")               # 'Hi' truthy, [] falsy → returns []
print(f"[] or 'Fallback'     → {[] or 'Fallback'}")     # Fallback
print(f"0 or 'Number'        → {0 or 'Number'}")        # 'Number'
print(f"None and 'Ignored'   → {None and 'Ignored'}")   # None
print(f"'' and 123           → {'' and 123}")           # ''
print(f"True and 0 and 'Hi'  → {True and 0 and 'Hi'}")  # 0


# Relational (or Comparison) operators are used to compare two values.
# They always return a Boolean value: True or False.
# Operators:
# ==   → Equal to
# !=   → Not equal to
# >    → Greater than
# <    → Less than
# >=   → Greater than or equal to
# <=   → Less than or equal to

num_1, num_2, num_3 = 10, 20, 10


print(f"{num_1} == {num_2} gives: {num_1 == num_2}")
print(f"{num_1} == {num_3} gives: {num_1 == num_3}")
print(f"{num_1} != {num_2} gives: {num_1 != num_2}")
print(f"{num_1} != {num_3} gives :{num_1 != num_3}")
print(f"{num_1} < {num_2} gives :{num_1 < num_2}")
print(f"{num_1} > {num_2} gives :{num_1 > num_2}")
print(f"{num_1} < {num_3} gives :{num_1 < num_3}")
print(f"{num_1} > {num_3} gives :{num_1 > num_3}")
print(f"{num_1} <= {num_2} gives :{num_1 <= num_2}")
print(f"{num_1} >= {num_2} gives :{num_1 >= num_2}")
print(f"{num_1} <= {num_3} gives :{num_1 <= num_3}")
print(f"{num_1} >= {num_3} gives :{num_1 >= num_3}")

# Comparison Between Different Data Types

# Int vs Float
# While comparing int is promoted to float internally

print(f"\"10 == 10.0\" gives: {10 == 10.0}")
print(f"\"10 != 10.0\" gives: {10 != 10.0}")
print(f"\"10 > 10.0\" gives: {10 > 10.0}")
print(f"\"10 < 10.0\" gives: {10 < 10.0}")
print(f"\"10 >= 10.0\" gives: {10 >= 10.0}")
print(f"\"10 <= 10.0\" gives: {10 <= 10.0}")
print(f"\"10 == 10.5\" gives: {10 == 10.5}")
print(f"\"10 != 10.5\" gives: {10 != 10.5}")
print(f"\"10 > 10.5\" gives: {10 > 10.5}")
print(f"\"10 < 10.5\" gives: {10 < 10.5}")
print(f"\"10 >= 10.5\" gives: {10 >= 10.5}")
print(f"\"10 <= 10.5\" gives: {10 <= 10.5}")

# Floating-point numbers are represented in binary (base-2),
# not decimal (base-10). Many decimal fractions cannot be represented
# exactly in binary, leading to tiny rounding errors.
# You should avoid comparing the results of floating-point arithmetic.


# Example: Let's test some float addition results that *look* like
# they should be exact, but often are not.

print(f"\"0.1 + 0.2 == 0.3\" gives: {0.1 + 0.2 == 0.3}")
print(f"\"0.2 + 0.3 == 0.5\" gives: {0.2 + 0.3 == 0.5}")
print(f"\"0.4 + 0.1 == 0.5\" gives: {0.4 + 0.1 == 0.5}")
print(f"\"0.7 + 0.1 == 0.8\" gives: {0.7 + 0.1 == 0.8}")

# Let's also print the *actual stored values* (full precision)
print(f"repr(0.1 + 0.2) → {repr(0.1 + 0.2)}")
print(f"repr(0.3 + 0.2) → {repr(0.3 + 0.2)}")
print(f"repr(0.4 + 0.1) → {repr(0.4 + 0.1)}")
print(f"repr(0.7 + 0.1) → {repr(0.7 + 0.1)}")

# ⚠️ Notice that some of these are slightly off:
# 0.1 + 0.2 → 0.30000000000000004
# 0.7 + 0.1 → 0.7999999999999999
# while others, like 0.3 + 0.2, happen to land exactly on 0.5
# because 0.5 is representable precisely in binary.

# In binary:
#   0.1 (decimal) = 0.0001100110011... (repeating)
#   0.2 (decimal) = 0.0011001100110... (repeating)
# These numbers have no finite binary representation, so Python stores
# an approximation. When you add them, you get a small rounding error.
# Thus, direct comparison using == can fail even when mathematically equal.


# ⚖️ Comparisons Between Numbers (int/float) and Strings

# 🧠 Implicit Coercion:
# When Python performs an operation between two different types,
# it sometimes converts one type into another automatically
# (e.g., int → float) so the operation makes sense.

# Example:
#   10 + 2.5 → int is converted to float → 10.0 + 2.5 = 12.5

# ⚠️ BUT Python never does implicit coercion between
# numbers (int/float) and strings (str).
# Because "10" (text) and 10 (number) are fundamentally different kinds of data.

# Equality (==, !=)

# Equality (==) only returns True if both value and type are same or coercible.
# Since int/float and str are different and non-coercible → always False.
print(f"10 == '10'     → {10 == '10'}")       # False
print(f"10 != '10'     → {10 != '10'}")       # True
print(f"10.0 == '10'   → {10.0 == '10'}")     # False
print(f"10.0 == '10.0' → {10.0 == '10.0'}")   # False

# Ordering (<, >, <=, >=)
# Python 3 does NOT allow ordering between numbers and strings.
# Such operations are meaningless → raise TypeError.
try:
    print(10 < "11")
except Exception as error:
    print(f"10 < '11' → ❌ Error: {error}")

try:
    print("9" > 8)
except Exception as error:
    print(f"'9' > 8 → ❌ Error: {error}")

try:
    print(10.5 < "11.2")
except Exception as error:
    print(f"10.5 < '11.2' → ❌ Error: {error}")

# Bool vs Int / Float / String

# Bool is subclass of int → True == 1, False == 0
print(f"True == 1   → {True == 1}")       # True
print(f"False == 0  → {False == 0}")      # True
print(f"True != 1   → {True != 1}")       # False
print(f"False != 0  → {False != 0}")      # False

# Arithmetic ordering also works (True = 1, False = 0)
print(f"True < 2  → {True < 2}")         # True (1 < 2)
print(f"False > -1 → {False > -1}")      # True (0 > -1)

# Bool vs String → always False for equality, ordering not allowed
print(f"True == 'True'  → {True == 'True'}")   # False
print(f"False == '0'    → {False == '0'}")     # False
try:
    print(True < "1")
except Exception as error:
    print(f"True < '1' → ❌ Error: {error}")

# 5. String vs String (Lexicographical Order)
# Python compares strings **character by character** using their
# ASCII Character Order (in increasing numeric code):
# 0–31   → Control characters (non-printable)
# 32–47  → Punctuation & symbols
# 48–57  → Digits 0–9
# 58–64  → More punctuation
# 65–90  → Uppercase letters A–Z
# 91–96  → More punctuation
# 97–122 → Lowercase letters a–z

print(f"'10' == '10'   → {'10' == '10'}")   # True (same string)
print(f"'10' == '010'  → {'10' == '010'}")  # False (leading zeros matter)
print(f"'10' != '10.0' → {'10' != '10.0'}") # True

# Lexicographical ordering (like dictionary order)
print(f"'2' < '10' → {'2' < '10'}")        # False (compares char by char: '2' > '1')
print(f"'abc' < 'abd' → {'abc' < 'abd'}")  # True
print(f"'Z' < 'a' → {'Z' < 'a'}")          # True (uppercase has lower ASCII code)
print(f"'1' < 'A' → {'1' < 'A'}")          # True (numbers have even lower ASCII code)
print(f"'.' < '1' → {'.' < '1'}")          # True (check ASCII code)
print(f"'' < chr(0) → {'' < chr(0)}")      # True, Empty string comes even before 1st ASCII character..
print(f"'' == '' → {'' == ''}")            # True, Empty string is equal to empty string


# 6. None Comparisons
print(f"None == None   → {None == None}")   # True
print(f"None != 0      → {None != 0}")      # True
print(f"None == False  → {None == False}")  # False
print(f"None == ''     → {None == ''}")     # False
print(f"None == []     → {None == []}")     # False

# Ordering comparisons with None are not allowed
try:
    print(None < 1)
except Exception as error:
    print(f"None < 1 → ❌ Error: {error}")

try:
    print(None > "a")
except Exception as error:
    print(f"None > 'a' → ❌ Error: {error}")

# Special Float values: NaN, Inf.

nan_val = float("nan") # Not a number , it literally means value that is not avaliable
inf_val = float("inf") # infinity
neg_inf_val = float("-inf") # negative infinity

# NaN compared with anything is always False
print(f"nan_val == nan_val → {nan_val == nan_val}")   # False
print(f"nan_val == 100  → {nan_val == 100}")          # False
print(f"nan_val != 100  → {nan_val != 100}")          # True

# Infinity comparisons
print(f"inf_val > 1e308   → {inf_val > 1e308}")       # True
print(f"neg_inf < -1e308  → {neg_inf_val < -1e308}")  # True


# Assignment Operators (+=, -=, *=, /=, //=, %=, **=)

num = 10
print(f"Initial number = {num}") # num = 10
num += 5
print(f"number += 5  → {num}")   # num = num + 5, num = 15 
num -= 3
print(f"number -= 3  → {num}")   # num = num - 3, num = 12 
num *= 2
print(f"number *= 2  → {num}")   # num = num * 2, num = 24 
num /= 4
print(f"number /= 4  → {num}")   # num = num / 4, num = 6 
num //= 2
print(f"number //= 2 → {num}")   # num = num // 2, num = 3 
num %= 3
print(f"number %= 3  → {num}")   # num = num % 3, num = 0 
num **= 4
print(f"number **= 4 → {num}")   # num = num ** 4, num = 0

str_1 = 'Hello'
str_1 += ' World'
print(f"Concated string: {str_1}")


# 🔗 Chained Comparisons in Python
# Python allows you to chain multiple comparisons in one line,
# making expressions more natural and mathematical.
#
#   a < b < c  →  (a < b) and (b < c)
#
# ✅ All chained comparisons are logically connected with **AND**.
#    There is no implicit OR in chaining.
#
# ✅ You can chain more than 3 comparisons — any number.
#    1 < 2 < 3 < 4 < 5 → True
#
# ✅ Each middle operand (like b in a<b<c) is evaluated only once.
#
# ✅ The chain short-circuits like 'and' — stops if any test fails.

num_1, num_2, num_3 = 5, 10, 20
print(f"num_1 < num_2 < num_3 → {num_1 < num_2 < num_3}")        # True → 5 < 10 and 10 < 20
print(f"num_1 < num_2 > num_3 → {num_1 < num_2 > num_3}")        # False → 5 < 10 but 10 > 20 is False
print(f"num_1 == num_2 == num_3 → {num_1 == num_2 == num_3}")    # False → (5 == 10) and (10 == 20)

# Mixed operators
print(f"num_1 < num_2 <= num_3 → {num_1 < num_2 <= num_3}")      # True
print(f"num_1 < num_2 != num_3 → {num_1 < num_2 != num_3}")      # True
print(f"num_1 == num_2 != num_3 → {num_1 == num_2 != num_3}")    # False

# More than 3 comparisons
num = 5
print(f"1 < num < 10 < 100 → {1 < num < 10 < 100}")       # True (1<5 and 5<10 and 10<100)
print(f"1 < num < 5 < 10 → {1 < num < 5 < 10}")           # False (5<5 is False)

# Mixed-type chaining (allowed if types are comparable)
print(f"0 < num < 10.5 → {0 < num < 10.5}")               # True (int/float mix OK)
print(f"True < num < 6 → {True < num < 6}")               # True (True→1; 1<5<6)

# Invalid chaining (str vs int not comparable)
try:
    print(5 < "10" < 20)
except Exception as error:
    print(f"5 < '10' < 20 → ❌ Error: {error}")
