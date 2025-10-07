# Write your code below this line 👇

# String Membership Operators

text = "Python is fun and Python is easy to learn. Programming is also fun."

print("Python" in text) # True, because "Python" is present in the text.
print("Java" in text)  # False, because "Java" is not present in the text.
print("fun" not in text) # False, because "fun" is present in the text.
print("difficult" not in text) # True, because "difficult" is not present in the text.
print("Program" in text) # True, because "Program" is part of "Programming" in the text. Substring match.
print("program" in text) # False, because "program" (lowercase 'p') is not present in the text. Case-sensitive match.

# String Escaping Sequences

# Escape sequences are used to represent characters that are difficult or impossible to type directly.
# Common escape sequences:
# \n → Newline
# \t → Horizontal Tab
# \\ → Literal backslash
# \' → Single quote
# \" → Double quote
# \r → Carriage return (moves cursor to beginning of the line) and overwrites the line.
# \b → Backspace
# \r\n → Carriage return + Newline (Historically used in Windows for new lines)

print("hello\nworld") # Newline
print("hello\tworld") # Tab
print("This is backslash: \\") # Backslash
print("it\'s a sunny day") # Single quote
print("He said \"Hello!\"") # Double quote
print("Hello\rWorld") # Carriage return, Cursor moves to start of line, "World" overwrites "Hello"
print("Hello\r\nWorld") # Carriage return + Newline, moves to new line
print("Hello\bWorld") # Backspace, removes the character before it, so "o" is removed.

# Raw Strings

# Raw strings treat backslashes as literal characters and do not interpret them as escape sequences.
# This is useful for file paths, regular expressions, and other scenarios where backslashes are common.

print(r"C:\Users\Vipul\Desktop\Projects") # Raw string, backslashes are treated literally.

# These are common wrong ways to use raw strings:
# print(r"C:\Users\Vipul\Desktop\Projects\") # Cant end with a single backslash
# print(r"This is "raw" string") # Cant have double quotes inside double quotes without escaping them.
# print(r'This is 'raw' string') # Cant have quotes inside quotes without escaping them.

print(r"This is a 'raw' string") # Correct way to have single quotes inside raw string.
print(r'This is a "raw" string') # Correct way to have double quotes inside raw string.
print(r"This is a \"raw\" string") # Correct way to have double quotes inside raw string by escaping them.
print(r'This is a \'raw\' string') # Correct way to have single quotes inside raw string by escaping them.

# 1️⃣ PARSING ALGORITHM
# - When Python sees r"..." or r'...', it still performs **lexical analysis**:
#   • It looks for a matching closing quote to end the string.
#   • It still recognizes backslash–quote sequences (\" or \') at the syntax level
#     so the string isn't accidentally closed too early.
#
# - After parsing, **escape sequence processing is skipped**. So sequences like
#   \n, \t, \", \\, etc. remain exactly as typed in the final string value.
#
# 2️⃣ QUOTES INSIDE RAW STRINGS
# - You cannot include an unescaped quote of the same type inside the raw string.
#       r"This is a "test""    ❌ SyntaxError (second " ends the string)
#       r'This is a 'test''    ❌ SyntaxError
#
# - You also cannot use \" or \' to "escape" quotes in a raw string — backslashes
#   are stored literally. But syntactically, \" and \' prevent the parser from
#   prematurely closing the string:
#       r"This is a \"test\""  ✅ Valid syntax, final string contains backslashes.
#       output: This is a \"test\"
#       Actually stored as: This is a \\"test\\"
#       r'This is a \'test\''  ✅ Valid syntax, final string contains backslashes.
#       output: This is a \'test\'
#       Actually stored as: This is a \\'test\\'
# 3️⃣ TRAILING BACKSLASH
# - A raw string **cannot end with a single backslash** because it recognises the \" at syntax level and do not consider it as ending the string.
#
#       r"C:\path\to\folder\"   ❌ invalid
#
# - ✅ Fix by doubling the backslash or concatenating:
#       r"C:\path\to\folder\\"
#       r"C:\path\to\folder" + "\\"
# 4️⃣ ESCAPE SEQUENCES (\n, \t, etc.)
# - In normal strings, these are interpreted:
#       "\n" → newline, "\t" → tab, "\\" → one backslash
#
# - In raw strings, these remain literal:
#       r"\n" → '\' + 'n'   (2 characters)
#       r"\t" → '\' + 't'
#       r"\\" → '\' + '\'
#
# - The parser does not throw an error on \n or \t inside raw strings,
#   but they are **not converted** to newline or tab characters.
# 5️⃣ NEWLINES IN RAW STRINGS
# - You CANNOT use \n inside a raw string to make a real newline.
#       r"Line1\nLine2"  → prints literally with \n
#
# - ✅ To include real newlines:
#   • Use triple-quoted raw strings:
#         s = r"""Line 1
#         Line 2"""
#
#   • Or concatenate with a normal string containing "\n":
#         s = r"Line 1" + "\n" + r"Line 2"

print(r"Line1\nLine2") # \n is treated literally
print(r"""Line1
Line2""") # Triple quotes allow real newlines
print(r"Line1" + "\t" + r"Line2") # Concatenation with normal string for tab

# 📌 repr(x) returns the “official” string representation of an object.
# For strings, it shows escape sequences explicitly, so you can see what’s
# actually stored in memory (e.g., \n, \t, backslashes, quotes).

print(repr(r"Hello\nWorld")) # Shows the \n escape sequence
print(repr(r"this is a \"raw\" string")) # Shows the backslashes before quotes