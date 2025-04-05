#functions 

# print('a value')
# print(input('ask for a value'))

#methods -> functions of datatypes

# print('value'.upper())
# print('VALUE'.lower())
# print('VALUE'.replace('E','e'))


#other new functions

# print(abs(-1))
# print(max(10,5))
# print(min(0,1))
# print(len('test'))


# pythagoras theorem

side_a = int(input('The width of the triangle'))

side_b = int(input('The height of the triangle'))
# print(type(side_a))
# print(int(side_a) + 5)
# print(side_b)

hypotenuse = (side_a ** 2 + pow(side_b,2)) ** (1/2)

print('the hypotenuse',round(hypotenuse,2))

