"""
Written by Ameen Ahmed for the Shiptheory programming test.

"A string is ordered incorrectly. Write some code that returns the string reversed, with all occurrences of the most frequent character removed.
Do not use a function native to your selected language that directly reverses a string, such as PHP’s ​​strrev()​ ​function."


"""

# Dict for keeping track of letter freq.
letter_count = {}

# Take uppercase string
user_input_string = input("Please enter a string: \n").upper()

# Reverse letters using list indexing
reversed_string = user_input_string[::-1]

# If letter exists in letter_count dict, incrememnet its value. If not, start at 1.
for letter in reversed_string:
	if letter in letter_count:
		letter_count[letter] += 1
	else:
		letter_count[letter] = 1

# Replace most freq. occuring letter in reversed_string with an empty ""
reversed_most_freq_remvd = reversed_string.replace(max(letter_count, key=letter_count.get), "")

print("Your reversed string with the most frequent letter removed is: {} ".format(reversed_most_freq_remvd))