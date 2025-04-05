# print(5 == 5 )
# if statements
# if 0 > 4:
#     print("Correct Result")
# elif 0 > 1:
#     print("Some other result")
# elif 1 == 1 and 5 > 1:
#     print("Some other result")
#     if len([1,2,3]) > 2:
#         print("list is long enough")
# else:
#     print("Incorrect result")


#  while loop

# counter = 0;
# while counter <= 10:
#     print(counter)
#     counter += 1
#     if (counter == 5):
#         print("Counter is 5")
# print('while loop is finished')


# for loop

# test_list = [1,2,3,4,5]
# test_list = {1,2,3,4,5}
# test_list = (1,2,3,4,5)
# test_list = {1:2,3:4}


# for x in test_list:
#     print(x)
# for x in test_list.keys():
#     print(x)
# for x in test_list.values():
#     print(x)
# for x in test_list.items():
#     print(x)
# for x in test_list.items():
#     print(x[0])

# for k,v in test_list.items():
#     print(k)
#     print(v)




# truthy and falsy
## Empty container, string without letters and 0 are False 
# Everything else is Truthy

# if 1: 
#     print('truthy')
# else:
#     print('falsy')
# if 0: 
#     print('truthy')
# else:
#     print('falsy')
# if [1]: 
#     print('truthy')
# else:
#     print('falsy')
# if []: 
#     print('truthy')
# else:
#     print('falsy')
# if '': 
#     print('truthy')
# else:
#     print('falsy')


list = [1,2,3,4,5]
listCounter = 0

for i in list:
    if i == 2:
        print('The Value is 2')
    else:
       print('The value is not 2')
while listCounter <= 6:
    print(i)
    listCounter +=1