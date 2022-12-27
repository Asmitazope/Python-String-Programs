# Find the length of string 

# 1 using build-in fuction len

str = 'python'
print(len(str))


# 2 using loop and in operator
def findlen(str):
    count = 0

    for i in str:
        count+=1
    return count

print(findlen(str))

# 3 using loop and slicing
def strlen(str):
    count = 0
    while str[count:]:
        count+=1
    return count
print(strlen(str))

# 4 using sum function
def findlen(str):
    return sum(1 for i in str)
print(findlen(str))