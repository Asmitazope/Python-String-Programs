# Reverse a given string and check if its Pallindrome

# 1 
def reverse(s):
    return s[: : -1]

str='Hello'

ans=reverse(str)

if str == ans:
    print('is Pallindrome')
else:
    print('not Pallindrome')