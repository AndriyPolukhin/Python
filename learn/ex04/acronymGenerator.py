# Acronym Generator
# Random Access Memory : RAM

# HINT
# 1. Ask for a string
a_string = input("Enter a string to convert : ")
# 2. Convert the string to uppercase
a_string = a_string.upper()
# 3. Convert the string into a list
a_list = a_string.split()
# 4. Cycle through the list
for i in a_list:
    # 5. Get the 1st letter of the word and eliminate the newline
    print(i[0], end="")
# 6. Add a new line
print()

# CHECKING:
orig_string = input("Convert to acronym : ")
orig_string = orig_string.upper()
list_of_words = orig_string.split()
for word in list_of_words:
    print(word[0], end="")
print()
