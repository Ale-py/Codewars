# 1. Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    newst = ""
    for x in n:
        newst += str(x)


    return f"({newst[0:3]}) {newst[3:6]}-{newst[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# 2. Your task is to make a function that can take any non-negative integer as an argument and
# return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    lis = []
    newst = ""
    if num == None:
        return 0
    elif int(num) > 0:
        for x in str(num):
            lis.append(x)
        lis.sort()
        lis.reverse()
    elif type(num) == str:
        for i in num:
            lis.append(i)
        lis.sort()
        lis.reverse()
    else:
        return 0
    for y in lis:
        newst += y
    return newst
print(descending_order(4654971))