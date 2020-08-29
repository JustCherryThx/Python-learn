print('Simple Calculator!')

first_value = input('First number? ')

if first_value.isnumeric() == False:
    print('Please input a number.')
    exit()

second_value = input('Operation? ')

third_value = input('Second number: ')

if third_value.isnumeric() == False:
    print('Please input a number.')
    exit()

first_value = int(first_value)
third_value = int(third_value)

result = 0
if second_value == '+':
    label= 'sum'
    result = first_value + third_value
elif second_value == '-':
    label = 'difference'
    result = first_value - third_value
elif second_value == '*':
    label ='product'
    result = first_value * third_value
elif second_value == '/':
    label = 'quotient'
    result = first_value / third_value
elif second_value == '**':
    label = 'exponent'
    result = first_value ** third_value
elif second_value == '%':
    label = 'modulus'
    result = first_value % third_value

else:
    print('Operation not recognized.')
    exit()


print(label + ' of ' + str(first_value) + ' ' + second_value + ' ' + str(third_value) + ' equals ' + str(result))