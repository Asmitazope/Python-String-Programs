# python program to accept the string which contains all the vowels

def check(string):
    string = string.lower()

    #set function convert the string into set of characters

    vowels = set('aeiou')

    s = set({})

    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass

    
    if len(s) == len(vowels):
        print('Accepted')
    else:
        print('Not Accepted')

string = 'as it was eqaul our '
print(check(string)) 

