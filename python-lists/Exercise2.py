#TEST VALUE FOR INCLUSION IN A LIST

#numbers = [1, 3, 5]
#
# print(5 in numbers)
# print(8 in numbers)
#
# print(5 not in numbers)
# print(8 not in numbers)



# USE AN 'ELSE' STATEMENT

# import random
# numbers = []

# while len(numbers) < 5:
#   numbers.append(random.randint(1, 100))
#
# for number in numbers:
#   print(number)
#   if number >= 90:
#     print('Found at least one number greater than 90')
#     break
# else:
#   print('No numbers greater than 90')
#
# print('Complete')



# USE A 'CONTINUE' STATEMENT

# values = ["laptop", 7, "phone", 3, "dslr", 5]
# equipment = []
#
# for value in values:
#   if isinstance(value, str) == False:
#     continue
#   equipment.append(value)
#
# print(equipment)




# CREATE NESTED 'FOR' LOOPS

# suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", # "King", "Ace"]
#
# for  suit in suits:
#   for rank in ranks:
#     print(f'{rank} of {suit}')



# BREAKOUT OF A "FOR" LOOP

# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# numbers.sort()
#
# for number in numbers:
#   if number > 42:
#     break
#   print(number)



# USE AN 'ELSE' STATEMENT

# import random
# numbers = []
#
# while len(numbers) < 5:
#   numbers.append(random.randint(1, 100))
#
# for number in numbers:
#   print(number)
#   if number >= 90:
#     print('Found at least one number greater than 90')
#     break
# else:
#   print('No numbers greater than 90')
#
# print('Complete')


# USE A 'CONTINUE' STATEMENT

values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
  if isinstance(value, str) == False:
    continue
  equipment.append(value)

print(equipment)




#CHOOSE RANDOMLY FROM A LIST

#import random

# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# selected_number = random.choice(numbers)
# print(selected_number)
#
# selected_numbers = random.choices(numbers, k=3)
# print(selected_numbers)