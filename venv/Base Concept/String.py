name = "Azzaz Khan"
# Multiline strings, enclosed either in 6 single/double quotes or 6 backticks
address = """House D-10
Muslim City colony, Tarnab Farm
Peshawar, Pakistan - 25000"""

# Strings are treated as arrays
test = "Hello world"
print(test[0]) # Get first character
# Get the characters from position 2 to position 5 (not included)
print(test[2:5]) # Slicing
# Get the characters from position 5 to position 1 (not included), starting the count from the end of the string
print(test[-5:-2])
print(len(test)) # Get length of the string

text = " Hello, Python! "
print(text.strip()) # Removes leading and trailing white spaces
print(text.lower()) # Transforms the text into lowercase
print(text.upper()) # Transforms the text into uppercase
print(text.replace("H", "J")) # Replaces a string with another
# Splits the string into substrings if it finds instances of seperator
print(text.split(",")) # Returns ["Hello", " Python!"]

sentence = "The rain in Spain stays mainly in the plain"
print("ain" in sentence) # Checks if the phrase is present in string
print("ain" not in sentence) # Checks if the phrase is NOT present in string
print("Hello" + " World!") # Concat strings using the (+) operator


