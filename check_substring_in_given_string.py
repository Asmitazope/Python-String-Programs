# check if a substring is present in a given string

# 1
string = ' abcd efgh ijkl mnop'

if 'adb' in string:
    print('Yes! sub-string present in string')
else:
    print('No! sub-string is not present in string')


# 2 

def check(string,sub_string):
    if(string.find(sub_string) == -1 ):
        print('No!')
    else:
        print('Yes!')
    
string = 'geeks for geeks'
sub_string = ' geek'
check(string, sub_string)
