class MyException1(Exception):
    pass
class MyException2(Exception):
    pass

my_list = [10, 20, 30, 40, 60, 100, 2, 5]
n = input()
try:
	if not n.isdigit():
		raise MyException1
	elif int(n)>len(my_list) or int(n)<0:
		raise MyException2
	index = int(n)
	print(my_list[index])

except MyException1:
	print("For position, please enter an Integer value")
except MyException2:
	print("Index out of range")
finally:
  print("Program ended")