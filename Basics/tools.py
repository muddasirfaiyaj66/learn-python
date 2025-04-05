# f strings

# user_name = "Ena"
# user_age= 10
# user_information = f'{user_name} is {user_age} years old'

# bad_approach = user_name + ' is ' + str(user_age) + ' years old' #bad approach

# print(user_information)

#single line if statement 

# user_name ='Ena'
# user_age = 18
# user_information = f'{user_name} is {user_age} years old'
# user_status = 'Adult' if user_age >= 18 else 'Child'
# # if user_age < 18:
# #     user_status='Child'
# # else:
# #     user_status="Adult"

# print(f'{user_information}.The person is a {user_status}')

#list comprehension

# simple_list =[]
# for i in range(0,11,1):
#     simple_list.append(i)
# print(simple_list)

# simple_list = [i for i in range(0,11,1)]
# simple_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a','b','c') if j=='a' or j=='b']
# print(simple_list)

#lambda functions

# def double_value(num):
#     return num*2

# double_value = lambda num: num*2
# print(double_value(10))

## Some functions want a function as an argument

# random_list = [2,5,8,6,96,110,6988,888,75,8]
# sorted_list = sorted(random_list)
# print(sorted_list)
# random_list = [('Anna',25),('Paul',40), ('Lisa',10)]
# sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])
# print(sorted_list)

##exercise
battle_board = [f'{letter}{num}' for letter in {'A','B','C','D','E'} for num in range(1,6) if f'{letter}{num}' != 'C3']

print(battle_board)