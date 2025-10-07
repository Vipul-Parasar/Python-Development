# Write you code below this line 👇

# 1. STRING OPERATIONS


# Example: Substring using indexing
print("Hello"[0] + "," + "Hello"[1] + "," + "Hello"[2] + "," + "Hello"[3] + "," + "Hello"[4])

# Example: positive and negative indexing
text = "Python"
print(text[0]) # will print first letter from the beginning of the string
print(text[-1]) # will print first letter from the end of the string

print(text[0] + text[1] + text[2] + text[3] + text[4] + text[5]) # will print the whole string
print(text[-1] + text[-2] + text[-3] + text[-4] + text[-5] + text[-6]) # will print the whole string in reverse order

# Example: String Slicing and Substring Stepping

print(text[0:3]) # will print text from index 0 to index 2 (3 is excluded)
print(text[3:6]) # will print text from index 3 to index 5 (6 is excluded)
print(text[:3]) # will print text from index 0 to index 2 (3 is excluded)
print(text[3:]) # will print text from index 3 to the end of the string
print(text[0:6]) # to get the whole string we have to specify the length of the string as the end index
print(text[:]) # this will also print the whole string
print(text[2:1]) # this will print an empty string as the start index is greater than the end index
print(text[0:6:2]) # will print every second letter from index 0 to index 5

print(text[-6:-3]) # will print text from index -6 to index -4 (-3 is excluded)
print(text[-3:-1]) # will print text from index -3 to index -2 (-1 is excluded)
print(text[-3:]) # will print text from index -3 to the end of the string
print(text[:-3]) # will print text from index 0 to index -4 (-3 is excluded)
print(text[-3:0]) # even this wont include -1 as 0 is a considered part of positive indexing and this will print an empty string because start index is greater than end index.
print(text[-3:6]) # this will include the last letter as this string will go from index -3 to index 5
print(text[-6:500]) # this will also include the last letter as python will consider the length of the string as the end index if the specified end index is greater than the length of the string

# while negative indexing, python just maps the negative index to positive index and then extracts the substring 
# start = len(s) + start (if starting index is negative)
# end   = len(s) + end (if ending index is negative)
# index:  0  1  2  3  4  5   (positive indexing)
# letter: p  y  t  h  o  n
# index: -6 -5 -4 -3 -2 -1   (negative indexing)
# thats why print(text[-3:0]) prints an empty string as -3 is mapped to 3 and 0 is mapped to 0 and start index is greater than end index
# but print(text[-3:6]) prints "hon" as -3 is mapped to 3 and 6 is mapped to 6 and start index is less than end index

print(text[::-1]) # this will print the whole string in reverse order
print(text[-1:-7:-1]) # this will also print the whole string in reverse order
print(text[5:0:-1]) # this will print the string from index 5 to index 1 in reverse order (0 is excluded)
print(text[5:-7:-1]) # this will also print the whole string in reverse order, it will start with index 5 and go to index 0 which corresponds to -6 in negative indexing and it will stop there as -7 is excluded. 
                     # even if we take a number lesser than -7 like -100, it will still stop at index 0 as python will consider the length of the string as the end index.
                     # so while slicing if we are going in reverse order then the default end index is -len(s)-1
print(text[-1:-(len(text)+1):-1]) # this will also print the whole string in reverse order, here we are calculating the default end index using len() function.
print(text[5::-1])  # this will also print the whole string in reverse order.
print(text[-1:-7:-2]) # this will print every second letter in reverse order

# Slicing rule for s[start:end:step]:
#
# 1. If step > 0 (forward):
#       - Works only if start < end
#       - Traverses left → right
#       - If start >= end → result is empty
#
# 2. If step < 0 (backward):
#       - Works only if start > end
#       - Traverses right → left
#       - If start <= end → result is empty
#
# Note:
# - Negative indices are first converted to their positive equivalent
#   (e.g., -1 → len(s)-1).
# - End index is always exclusive (not included in the result).

# Example: String Concatination and Repetition

print("Hi" + " there!") # concatenation
print("ha" * 4) # repetition

# Example: String Immutability

original = "Hello"

try:
    original[0] = "h" # This will raise an error
except Exception as error:
    print(f"❌ Error: {error}") # Strings are immutable, so we cannot change a character directly

modified = "h" + original[1:] # Correct way to modify a string
print(modified) # prints "hello"


