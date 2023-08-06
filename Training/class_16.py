# def maximum(a,b,c):
#     if a>b and a>c:
#         return a 
#     elif b>a and b>c:
#         return b 
#     else: 
#         return c 
# max = maximum(7,9,1)
# print(max)

# Keyword arguments
# def my_function(name2, name1):
#     print(name1 + " & " + name2+" are taking Python programming class")

# my_function(name1="Toufiq", name2="Shuvo")


# Arbaitary keywords

# def maximum2(*arg):
#     max = arg[0]
#     for i in arg:
#         if i>max:
#             max= i
#     return max

# print("Maximum number= ",maximum2(1,5,7,3))


# def my_function(**names):
#     print("Attendence: ")
#     for i in names.values():
#         print(i)

#     # print(names['name1'])

# my_function(name1="Toufiq", name2="Shuvo", name3 = "Rakib", name4="Sumon")

# default argument
# def myfunction(n=4):
#     for i in range(1,n+1):
#         print(i**2)

# myfunction()


def maximum2(n):
    max = n[0]
    for i in n:
        if i>max:
            max= i
    return max
numbers = [1,5,7,3] 
print("Maximum number= ",maximum2(numbers))
