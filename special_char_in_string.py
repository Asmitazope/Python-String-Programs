# check if the string contains any special characters
string = ' asmita@!@$#%$^&^*&(*)(*) '

string.split()

count = 0

special_char='[!@#$%^&*()<>?/\|}{`:}]'

for i in range(len(string)):
    if string[i] in special_char:
        count+=1


if count:
    print(' string contains special characters')
else:
    print('string doesnt contain special characters')