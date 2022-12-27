# Remove the i'th character from given string

test_str = 'Python Programming'

print(test_str.translate({ord(i): None for i in ' 1234'}))