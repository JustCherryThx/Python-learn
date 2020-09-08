colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

#print(colors)
#print(type(colors))

sundry = ['John', 3.14, 7, False]
#print(sundry)
#print(type(sundry))

#my_list = []

# print(f'0-based indexing into the list ... second item: {colors[1]}')

# print(f'Last item of the list: {colors[-1]}')

# print(f'Next to last item in the list: {colors[-2]}')


# print'\nPrint a SLICE. starting at index 2 and excludng index 5:')
# print(colors[2:5])
# print(type(colors[2:5]))
#
# print('\nPrint a slice starting at index 0 to index 3:')
# print(colors[:3])
#
# print('\nPrint a slice, starting at index 4 to the end of the list:')
# print(colors[4:])
#
# print('\nPrint a slice, from the 4th from the end up until the last # item:')
# print(colors[-4:-1])
#
# print(colors)

color = colors.pop(0)
print('popped', color)

print(colors)

print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)

colors.remove('whatever')

new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(new_colors)

colors.clear()
print(colors)