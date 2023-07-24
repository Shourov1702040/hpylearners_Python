# x = input("Enter number saperated by space: ").split(' ')
# s = []
# for i in range(5):
#     x = int(input(f"Enter number {i+1}: "))
#     s.append(x)
# s = [1,2,7,6,5]
# print(s)
# max1 = 0
# min1 = s[1]

# for j in s:
#     if j>max:
#         max = j

#     if j<min:
#         min = j

# min1 = min(s)
# max1 = max(s)

# print(f"Maximum = {max1} \nMinimum = {min1}")
# sum=0
# for i in x:
#     i = int(i)
#     sum +=i

# print(type(sum))



# ---------------------------------------------------------------------

s = [1,2,7,6,5]
s[2] = 9
# print(s)

# print(s[2])

# {key:value} 

dct = {1:3, 3:5, 2:7}
# print(dct[3])

dct2 = {'name': "Mr. X", 'age':17, 'class':'XI'}
# print(dct2['age'])

# print(type(dct2))
# print(len(dct2))

# key = dct2.keys()
# print(key)

# print(dct2.values())

# dct2['name'] = 'Mr. Y'
# print(dct2)

print('Mr. X' in dct2)
print('age' in dct2)