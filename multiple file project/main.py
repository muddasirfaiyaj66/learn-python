import support
# from support import Test, var, add_2_numbers # import specific variable, function, class etc
from support import * #import everything
test = support.Test()
test.some_method()
print(support.var)

sum =support.add_2_numbers(5,6)
print(sum)