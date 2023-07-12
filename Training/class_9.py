lst1 = ['C', 'C++', 'Java', 'Python', 'Ruby', 'C++', 'Java']
lst2 = [2,3,68,9,34,2]
lst3 = [True, False, False, True]
lst4 = ['C++', 101, True, 3.1416]

tpl = ('Apple', 'Banana', 'Lichi', 'Mango')

# lst5 = list(tpl) 
# # C++ is a String type data
# # 101 is a int type data 

# print(tpl)
# print(lst5)
# print(len(lst1))

# print(lst1[-2])

# print(lst1[-1::-1]) 

# lst1[-2] = 'JavaScript'
# lst1.append('JavaScript')
# lst1.insert(-2, 'JavaScript')
# print(lst1)

lst2.extend(tpl)
print(lst2)
