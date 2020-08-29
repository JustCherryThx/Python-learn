#numeric_value = '7'
#print(numeric_value.isnumeric())
#
#string_value = 'Bob'
#print(string_value.isnumeric())

first_value = input('First Number: ')
second_value = input('Second Number: ')

if second_value.isnumeric() == False or first_value.isnumeric() == False:
    print('Please enter numbers only.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))

