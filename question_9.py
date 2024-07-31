# Given string
s: str = "apple,banana,cherry,dates"

# Split the string into a list of substrings based on the delimiter ','
substrings = s.split(',')

# Join the list of substrings back into a single string, with each element separated by a space
joined_string = ' '.join(substrings)

# Print the results
print(substrings)
print(joined_string)
