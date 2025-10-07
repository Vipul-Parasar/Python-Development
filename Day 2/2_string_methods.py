# Write you code below this line 👇

# 1. Case Conversion Methods

text = "heLLo wOrld"

print(text.upper()) # Converts all characters to uppercase, takes no parameters.
print("".upper()) # Calling any case conversion method on an empty string will return an empty string.
print(text.lower()) # Converts all characters to lowercase, takes no parameters.
print(text.title()) # Converts the first character of each word to uppercase and the rest to lowercase, takes no parameters.
print(text.capitalize()) # Converts the first character of the string to uppercase and the rest to lowercase, takes no parameters.
print(text.swapcase()) # Swaps the case of each character in the string, takes no parameters.

# 2. Whitespace(spaces, tabs, newlines) Removal Methods

text_1 = "      Hello World     \n"
text_2 = "\nn\\\\nHello World\\\\n\n"

print(text_1.strip()) # Removes leading and trailing whitespace characters (spaces, tabs, newlines), takes optional string of characters to remove as parameter.
print(text_1.strip(" Held\n")) # Will remove " ", "H", "e", "l","d" and "\n" from the start and end of the string until it encounters a character not in the set.
print(text_2.strip("\n")) # Will remove leading and trailing newlines from the string.
print(text_2.strip("\\n\n")) # will remove leading and trailing "\", "n" and "\n" from the string.
                             # Example: Difference between print("\\n") and print("\\\n")
                             # In a Python string:
                             # - "\\" represents a single literal backslash '\'
                             # - "\n" represents a real newline character
                             # - "\\n" → becomes backslash + letter n  → prints \n literally
                             # - "\\\n" → becomes backslash + real newline → prints '\' then moves to next line
print(text_1.lstrip()) # Removes leading whitespace characters(spaces, tabs, newlines), takes optional string of characters to remove as parameter.
print(text_1.rstrip()) # Removes trailing whitespace characters(spaces, tabs, newlines), takes optional string of characters to remove as parameter.

# 3. Searching, Counting and Replacing Methods

text = """
Python is powerful. Python is easy to learn.
Python is popular in data science, web development, and automation.
Many developers love python because of its simplicity and readability.
However, Python is case-sensitive when searching with .find() or .replace().
    Extra spaces and inconsistent casing make searching trickier.
"""
file_1="data_science.txt"
file_2="Data.csv"
file_3="presentation.pptx"

print(text.find("data")) # Returns the lowest index of the substring if found in the string. If not found, returns -1. Case-sensitive.
print(text.find("Data")) # Case-sensitive, so this will return -1 as "Data" is not found in the string.
print(text.find("Python")) # Will return the index of the first occurrence of "Python".
print(text.rfind("Python")) # Returns the highest index of the last occurrence of the "Python".
print(text.index("learn")) # Similar to find() but raises a ValueError if the substring is not found.

try:
    print(text.index("Learn")) # This will raise a ValueError as "Learn" is not found in the string.
except Exception as error:
    print(f"❌ Error: {error}")

# .startswith() and .endswith() do not ignore leading/trailing whitespace, so its better to use .strip() before using these methods if there are chances of leading/trailing whitespace.
print(file_1.endswith(".txt")) # Returns True if the string ends with the specified suffix, otherwise False. Case-sensitive.
print(file_2.endswith(".txt")) # Will return False as file_2 ends with ".csv"
print(file_3.startswith("Data")) # Checks if file_3 starts with "Data" (case-sensitive). Returns False here.
print(file_3.startswith("presentation")) # Will return True as file_3 starts with "presentation"
print(file_1.endswith((".txt", ".csv", ".pptx"))) # Can check for multiple suffixes by providing a tuple of suffixes.# print(file_1.endswith([".txt", ".csv"])) # ❌ TypeError, only tuple allowed
print(file_1.startswith(("data", "Data"))) # Can check for multiple prefixes by providing a tuple of prefixes.
print(file_1.startswith("data",0,4)) # startswith() and endswith() can also take optional start and end parameters to specify a substring within the string to check.
print(file_2.endswith(".csv",0,8)) # basically file.startswith(prefix, start, end) or file.endswith(suffix, start, end) is equivalent to file[start:end].startswith(prefix) or file[start:end].endswith(suffix) respectively.

print(text.count("Python")) # Returns the number of non-overlapping occurrences of the substring in the string. Case-sensitive.

print(text.replace("Python", "PYTHON")) # Returns a new string where all occurrences of the substring are replaced with another substring. Case-sensitive.
print(text.replace("Python", "PYTHON",2)) # Replaces only the first 2 occurrences of "python" with "PYTHON".
print(text.replace("Java", "JAVA")) # If the substring to be replaced is not found, the original string is returned unchanged.

# 4. String Splitting and Joining Methods

# General Syntax: string.split(sep=None, maxsplit=-1) , maxsplit -1 means no limit on the number of splits.
# string.split() # Splits the string at whitespace (spaces, tabs, newlines) if no separator is provided. and maxsplit is -1 by default.
# string.split(sep=None, maxsplit=-1) and string.split() are equivalent.
# .split method returns a list of substrings.

text_1 = "  one   two \t three\nfour  "
text_2 = "Python is powerful, Python is easy to learn."
text_3 = "line1\nline2\rline3\r\nline4\n\rline5" # \r is carriage return, it moves the cursor to the beginning of the line.Any text after \r will overwrite the existing text on that line.

print(text_1.split()) # Splits at whitespace, ignores leading/trailing whitespace, collapses multiple spaces/tabs/newlines into one separator.
print(text_1.split(None, 2)) # Splits at whitespace, but only does a maximum of 2 splits, resulting in 3 substrings.
print(text_1.rsplit(None,2)) # Splits at whitespace, but only does a maximum of 2 splits from the right, resulting in 3 substrings.
print(text_2.split(",")) # Splits at each comma, resulting in 2 substrings.

# if we have to split at "," and " " (comma and space) then first we can replace all commas with spaces and then split at spaces.
print(text_2.replace(","," ").split()) # first replaces all commas with spaces and then splits at spaces.

print("".split()) # Splitting a completely empty string with no separator returns an empty list.
print(" ".split()) # Splitting a string with only whitespace returns an empty list, as there are no non-whitespace substrings.
print("".split(" ")) # Splitting a completely empty string with any separator returns a list with one element, the empty string itself.
print(" ".split(" ")) # Splitting a string with only whitespace with space as separator returns a list with two elements, both empty strings (one before the space and one after).

# 📌 Important: str.split() behaves differently depending on whether a separator is provided or not.
#
# 1️⃣ When called with NO arguments (sep=None):
#     - Splits on any whitespace (spaces, tabs, newlines, etc.)
#     - Collapses consecutive whitespace into a single separator
#     - Ignores leading and trailing whitespace
#     - Returns [] if the string is empty or contains only whitespace
#
# 2️⃣ When called WITH an explicit separator (e.g., " "):
#     - Splits exactly on that separator
#     - Does NOT collapse consecutive separators
#     - Leading and trailing separators produce empty strings in the result
#     - Even an empty string returns [''] because the separator is explicitly defined
#
# 👉 This is why:
# " ".split()       → []       (whitespace collapsed & ignored)
# " ".split(" ")    → ['', ''] (explicit literal split, preserves empty fields)
#
# Another example:
# s = "  a  b  "
# s.split()       → ['a', 'b']                        # collapses and trims whitespace
# s.split(" ")    → ['', '', 'a', '', 'b', '', '']    # literal split on ' ', empty strings preserved


# Multiline string splitting
# splitlines() splits on line breaks (\n, \r, \r\n,\n\r)

print(text_3.splitlines()) # Splits the string at line breaks, returning a list of lines without the line break characters.
print(text_3.splitlines(True)) # If True, line break characters are included in the resulting substrings.

# 📌 How .splitlines() handles different line break sequences:
#
# - \n  → Line Feed (LF), Unix/Linux
# - \r  → Carriage Return (CR), old Mac
# - \r\n → CR+LF (Windows) → treated as ONE single line break
# - \n\r → LF+CR (non-standard) → treated as TWO separate breaks
#
# Why?
# \r\n is a well-defined standard newline sequence (Windows). Python's .splitlines() recognizes this
# pair and treats it as a single break to avoid creating empty strings unnecessarily.
#
# \n\r has no special meaning — it's just a line feed followed by a carriage return.
# So .splitlines() first splits on \n, then immediately splits again on \r,
# producing an extra empty string between the two splits.
#
# Example:
# "line3\r\n" → "line3"       (single break)
# "line4\n\r" → "line4", ""   (two breaks: one for \n, another for \r)


# Joining a list of strings into a single string using a specified separator
# Syntax: separator.join(iterable)

words =["Python","is","fun"]
date = [ "2025", "10", "05"]
tuple_words = ("Join","these","words")

print("".join(words)) # Joins the list of words into a single string with no spaces.
print(" ".join(words)) # Joins the list of words into a single string with spaces as separators.
print("-".join(date)) # Joins the list of date components into a single string with hyphens as separators.
print(" ".join(tuple_words)) # Joins the tuple of words into a single string with spaces as separators.
print(" ".join(word for word in words)) # works with any iterable, not just lists or tuples.
try:
    print(" ".join(["Hello", 123, "World"])) # This will raise a TypeError as all elements must be strings.
except Exception as error:
    print(f"❌ Error : {error}")
# Note: The join() method requires all elements in the iterable to be strings. If any element is not a string, it will raise a TypeError.

# 5. String Character Check Methods

print(f"1. {'Hello123'.isalpha()}") # Returns True if all characters in the string are alphabetic and there is at least one character. Here it will return False as there are digits in the string.
print(f"2. {'Hello'.isalpha()}") # Returns True as all characters are alphabetic.
print(f"3. {'hello123'.isalnum()}") # Returns True if all characters in the string are alphanumeric (letters or numbers) and there is at least one character. Here it will return True.
print(f"4. {'Hello@123'.isalnum()}") # Returns False as there is a special character "@" in the string.
print(f"5. {'123.4'.isdigit()}") # Returns False as "." is not a digit.
print(f"6. {'1234'.isdigit()}") # Returns True as all characters are digits.
print(f"7. {'   \n  \t  \r  \n  '.isspace()}") # Returns True if all characters in the string are whitespace and there is at least one character.
print(f"8. {'HELLO'.isupper()}") # Returns True if all characters in the string are uppercase and there is at least one character.
print(f"9. {'hello'.islower()}") # Returns True if all characters in the string are lowercase and there is at least one character.
print(f"10. {'Hello World'.istitle()}") # Returns True if the string is in title case (first letter of each word is uppercase and the rest are lowercase) and there is at least one character.
print(f"11. {'This is Line1.\nThis is Line2.'.isprintable()}") # Returns False if the string contains any non-printable characters (like \n, \t, etc.), spaces are considered printable.
print(f"12. {'Hello World!'.isprintable()}") # Returns True as all characters are printable.
print(f"13. {''.isprintable()}") # An empty string is considered printable, so this will return True.
