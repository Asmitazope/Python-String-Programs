# check if string is Symmetrical
string = ' amaama '
half =  int(len(string)/2)

# check if legth of string is even
if len(string) % 2 == 0:
    first_str = string[: half]
    second_str = string[half :]
    
# check if length of string is odd
else:
    first_str = string[: half]
    second_str = string[half+1 :]

# check if string is symmetrical

if first_str == second_str:
    print('string is symmetrical')
    
else:
    print('not symmetrical')