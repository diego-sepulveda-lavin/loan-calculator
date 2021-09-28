import math


# your code here
def dont_cheat(_):
    print("Don't cheat!")


math.factorial = dont_cheat

num = 23
# don't delete this line, please
math.factorial(num)
