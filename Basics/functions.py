#create a function
# def print_5_times():
#     counter = 0;
#     while counter <= 5:
#         print('test')
#         counter += 1
# def print_nth_times(parameter, n = 5):
#     counter = 0;
#     while counter <= n:
#         print(counter, parameter)
#         counter += 1


# def sum ( a, b):
#     return a+b
## call 
# print('Print')
# print_5_times()
# print_nth_times("test",10)
# print_nth_times("test")


# total =  sum(5,5)
# print(total)


# def hypotenuseCalculator(a, b):
#     hypotenuse = (a ** 2 + pow(b,2)) ** (1/2)
#     return round(hypotenuse,2)


# print(hypotenuseCalculator(1,1))

def souter(text, n):
    for x in range(n):
        print(text.upper())


souter("Hi",5)
