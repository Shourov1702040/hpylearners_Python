class MyException1(Exception):
    pass
class MyException2(Exception):
    pass

list_one = input("list_one: ").split(",")
list_two = input("list_two: ").split(",")

sum_t = 0
try:
	if len(list_one)!=len(list_two):
		raise MyException1
	for i in range(len(list_one)):
		if not list_one[i].isdigit():
			raise MyException2
		elif not list_two[i].isdigit():
			raise MyException2
		else:
			sum_t += int(list_one[i])*int(list_two[i])
	print(sum_t)

except MyException1:
	print("Index out of bound")
except MyException2:
	print("The list has some non number values")
