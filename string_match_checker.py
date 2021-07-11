# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.



def string_checker(a, b):
    if set(a) == set(b):
        return True
    else:
        return False

a = "abcde"
b = "bcdae"
print(string_checker(a,b))